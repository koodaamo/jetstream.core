from .data import tabledata

class Source:
   "a dummy source with some data records"

   def __call__(self):
      return self

   def __iter__(self):
      for row in tabledata:
         # we are a generator
         yield row


