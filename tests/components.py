from jetstream.base import *
from .data import tabledata
from types import SimpleNamespace


class Input(InputComponent):
   "a dummy source with some data records"

   def __iter__(self):
      for row in tabledata:
         # we are a generator
         yield row

class Validator(InspectorComponent):
   "a dummy validator that just lets things pass"

class Transformer(TransformerComponent):
   "a dummy transformer that just lets things pass"

class Subscriber(OutputComponent):
   "a dummy output that merely prints the data out"

   def __call__(self):
      for record in self._stream:
         print(record)


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
