#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_jetstream
----------------------------------

Tests for `jetstream` package.
"""

import unittest, yaml, sys, os
import jetstream.util as util
import jetstream.core as core
import jetstream.base as base
from jetstream.core.instrumentation import INJECT_BEFORE, INJECT_AFTER
from tests.data import tabledata

HERE = os.path.abspath(os.path.dirname(__file__))

PIPE = "dummy pipe"
CFG_FILE = HERE + os.sep + "test.yaml"


class TestStreamer(unittest.TestCase):
   "test the Streamer"

   def setUp(self):
      config = util.yamlcfg(CFG_FILE)
      self.streamer = core.Streamer(pipename="dummy pipe", config=config)

   def test_passthru_injection(self):
      "streaming should work with simple pass-thru instrument"

      def dummy(stream):
         "a dummy pass-thru component"
         for record in stream:
            yield record

      self.streamer.inject(dummy, INJECT_AFTER, types=(base.InputComponent,))

      result = []
      for record in self.streamer:
         result.append(record)
      self.assertEqual(tabledata, tuple(result))
