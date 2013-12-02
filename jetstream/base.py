"""Jetstream (abstract) base classes."""

from abc import ABCMeta

class Component(metaclass=ABCMeta):
   "base component implementation"

   def __init__(self, stream):
      self._stream = stream

   def __iter__(self):
      for record in self._stream:
         yield record


class InputComponent(Component):
   "Input component meant to be subclassed"

class InspectorComponent(Component):
   "Inspector component meant to be subclassed"

class TransformerComponent(Component):
   "Transformer component meant to be subclassed"

class OutputComponent(Component):
   "Output component meant to be subclassed"


