from contextlib import contextmanager
from importlib import import_module
from types import SimpleNamespace
import yaml

@contextmanager
def yamlcfg(filename):
   with open(filename) as cfgfile:
      return yaml.load(cfgfile)


def import_name(fqn, package=None):
   "import a name"
   dotted = fqn.split(".")
   klassname = dotted.pop()
   # klass part was removed from dotted by pop
   # relative imports need the package argument
   module = import_module(".".join(dotted), package=package)
   return getattr(module, klassname)


def import_pipe(pipeconf, package="jetstream"):
   "import pipe parts"
   parts = []
   for name, cfg in configs.items():
      for part in cfg:
         klass = import_klass(part["use"], package=package)
         parts.append(klass)
   return parts


def piped(parts):
   "construct a piped generator"

   # it is convenient that parts can be given in logical order, but
   # here it's more convenient reversing it
   parts.reverse()
   pipe = parts.pop()() # instantiate first generator
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
      for record in self.stream():
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
