import traceback, sys
from contextlib import contextmanager
from importlib import import_module
from types import SimpleNamespace
import yaml

from .exceptions import ConfigurationError, ComponentLoadingError


def yamlcfg(filepath):
   "parse YAML configuration instance from file at path"
   with open(filepath) as cfgfile:
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
   except (ImportError, SystemError) as exc:
      modulename = getattr(exc, "name", "")
      raise ComponentLoadingError(modulename, name, package=package)

   result = getattr(module, name, None)
   if not result:
      raise ComponentLoadingError(modulename, name, package=package)

   return result


def load_pipe(pipename, config, package=None):
   "import pipe parts; return klass & cfg; no component name though"
   parts = []
   try:
      pipeconfig = config["pipes"][pipename]
   except:
      raise ConfigurationError("pipe", pipename)

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

