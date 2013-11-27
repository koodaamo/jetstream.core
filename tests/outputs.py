
class Subscriber:
   "a dummy output that merely prints the data out"

   def __init__(self):
      ""

   def __call__(self, item):
      print(item)
