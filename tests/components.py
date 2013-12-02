from jetstream.base import *
from .data import tabledata


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
