
class Transformer:
   "a dummy transformer that just lets things pass"

   def __init__(self, stream):
      ""
      self._stream = stream

   def __iter__(self):
      ""
      for r in self._stream:
         yield r

