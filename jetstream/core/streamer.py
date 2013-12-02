"""Jetstream core functionality."""

import logging
from collections import OrderedDict

from ..import util, base
from .instrumentation import INJECT_BEFORE, INJECT_AFTER

logging.basicConfig()

logger = logging.getLogger("streamer")
logger.setLevel(logging.ERROR)

class Streamer(list):
   "the Jetstream pipe runner"

   def __init__(self, pipename=None, config=None):
      "initialize the streamer"
      self.instruments = []
      self.components = []

      if pipename and config:
         self.load(pipename, config)

   def inject(self, instrument, order, types=()):
      "add instruments before or after particular types of components"
      self.instruments.append((instrument, types, order))
      self._build()

   def load(self, pipename, config):
      "load pipe from configuration"
      self.components = util.load_pipe(pipename, config)
      self._build()

   def _build(self):
      "build the pipe"
      parts = []
      logger.debug("BUILDING PIPE")
      for idx, (component, conf) in enumerate(self.components):
         klass = component.__class__.__name__
         parts.append(component)

         # instrument the component if so told
         for instrument, itypes, iorder in self.instruments:
            if util.subclasses_any(component, itypes):
               logger.debug(" -> instrumenting %s" % klass)
               if iorder == INJECT_BEFORE:
                  parts.insert(len(parts)-1, instrument)
               elif iorder == INJECT_AFTER:
                  parts.append(instrument)
               else:
                  raise Exception("cannot inject instrument: invalid ordering")

      self.pipe = util.piped(parts)

   def __iter__(self):
      "run the pipe"
      for record in self.pipe:
         yield record

