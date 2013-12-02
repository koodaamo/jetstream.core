import traceback, sys
from contextlib import contextmanager
from importlib import import_module
from types import SimpleNamespace
import yaml

from colorama import init, Fore
init(autoreset=True)


def red(txt):
   return Fore.RED + txt + Fore.RESET

def green(txt):
   return Fore.GREEN + txt+ Fore.RESET


class ComponentLoadingError(Exception):
   "notify user of component loading problem"

   def __init__(self, module, name, package=""):
      if package:
         package = "(%s)" % package
      self.fullname = "%s%s.%s" % (package, module, name)

   def __str__(self):
      return red("There is no component '%s' installed." % self.fullname)


def err(exc, msg):
   "add a message to exception"
   args = exc.args
   if not args:
      arg0 = ''
   else:
      arg0 = args[0]
   arg0 += "\n\n%s" % msg
   exc.args = (arg0,) + args[1:]
   raise


def yamlcfg(filename):
   with open(filename) as cfgfile:
      config = yaml.load(cfgfile)
   return config


def subclasses_any(klass, abcs):
   "test wheter a class subclasses one of given abcs"
   for base in abcs:
      if issubclass(klass, base):
         return True
   return False


def import_name(fqn, package=None):
   "import a name"
   dotted = fqn.split(".")
   name = dotted.pop()
   # klass part was removed from dotted by pop
   # relative imports need the package argument

   modulename = ".".join(dotted)

   try:
      module = import_module(modulename, package=package)
   except ImportError as exc:
      raise ComponentLoadingError(exc.name, name, package=package)

   result = getattr(module, name, None)
   if not result:
      raise ComponentLoadingError(modulename, name, package=package)

   return result


def load_pipe(pipename, config, package=None):
   "import pipe parts; return klass & cfg; no component name though"
   parts = []
   pipeconfig = config["pipes"][pipename]
   for partcfg in pipeconfig:
      klass = import_name(partcfg["use"], package=package)
      del partcfg["use"]
      parts.append((klass, partcfg))
   return parts


def piped(parts):
   "construct a piped generator"

   # it is convenient that parts can be given in logical order, but
   # here it's more convenient reversing it
   parts.reverse()
   pipe = parts.pop()([]) # instantiate first generator, with empty stream
   innermost = parts.pop() # but not its wrapper just yet
   while parts:
      pipe = innermost(pipe)
      innermost = parts.pop()
   return innermost(pipe)


class FieldMapper:
   ""

   def __init__(self, stream):
      self.stream = stream

   def __iter__(self):
      for record in self.stream:
         yield record


class KlassConstructor:
   "copy (dict) record data to the object attributes"

   def __init__(self, stream, klass=SimpleNamespace):
      self.stream = stream
      self.klass = klass

   def __iter__(self):
      for record in self.stream():
         obj = self.klass()
         obj.__dict__.extend(record)
         yield obj
