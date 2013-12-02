#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_utils
---------------------

Tests for `jetstream.utils` package.
"""

import unittest, yaml, sys, os
import jetstream.util as util
import jetstream.core as core
import jetstream.base as base
from jetstream.core.instrumentation import INJECT_BEFORE, INJECT_AFTER
from tests.data import tabledata

from jetstream.util import ConfigurationError, ComponentLoadingError

HERE = os.path.abspath(os.path.dirname(__file__))

PIPE = "dummy pipe"
BAD_PIPENAME = "me bad"
CASE_BAD_MODULE = "nothing.here"
CASE_BAD_NAME = "sys.NO_NAME_LIKE_THIS"

CFG_FILE = HERE + os.sep + "test.yaml"

COMPONENTLOADING_MSG = ""
CONFIGURATION_COMPONENT_MSG = "There is no component"
CONFIGURATION_PIPE_MSG = "There is no pipe"

class TestImporting(unittest.TestCase):
   "test the utils"

   def setUp(self):
      self.cfg = util.yamlcfg(CFG_FILE)

   def test_import_nonrelative(self):
      "import a fqn without leading dot"
      func = util.import_name("os.path.exists")
      self.assertEqual(func.__name__, "exists")

   def test_import_nonrelative_failure(self):
      "import a BAD (module/name) fqn without leading dot"
      fail = lambda: util.import_name(CASE_BAD_MODULE)
      self.assertRaises(ComponentLoadingError, fail)
      fail2 = lambda: util.import_name(CASE_BAD_NAME)
      self.assertRaisesRegex(ComponentLoadingError, CONFIGURATION_COMPONENT_MSG, fail2)

   def test_import_relative(self):
      "import a relative name with leading dot"
      klass = util.import_name(".components.Input", package="tests")
      self.assertEqual(klass.__name__, "Input")

   def test_import_relative_failure(self):
      "import a relative bad name with leading dot"
      fail = lambda: util.import_name(".components.NOTEXISTING", package="jjaj")
      self.assertRaises(ComponentLoadingError, fail)

   def test_config_loading(self):
      "parse and import everything in config"
      things = ["inputs", "transformers", "inspectors", "outputs"]
      for thing in things:
         configs = self.cfg[thing]
         for name, cfg in configs.items():
            klass = util.import_name(cfg["use"], package="tests")
            title = cfg["description"]


class TestPiping(unittest.TestCase):

   def setUp(self):
      self.cfg = util.yamlcfg(CFG_FILE)

   def test_pipe_loading(self):
      components = util.load_pipe(PIPE, self.cfg)
      fail = lambda: util.load_pipe(BAD_PIPENAME, self.cfg)
      self.assertRaisesRegex(ConfigurationError, CONFIGURATION_PIPE_MSG, fail)

   def test_pipe_running(self):
      "build and run a pipe with a dummy data source"
      configs = self.cfg["pipes"]
      parts = []
      for name, cfg in configs.items():
         for part in cfg:
            klass = util.import_name(part["use"], package="tests")
            parts.append(klass)
         pipe = util.piped(parts)
         result = []
         for r in pipe:
            result.append(r)
         self.assertEqual(tabledata, tuple(result))
