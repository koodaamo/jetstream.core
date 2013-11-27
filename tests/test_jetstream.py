#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_jetstream
----------------------------------

Tests for `jetstream` package.
"""

import unittest, yaml, sys
from jetstream.util import yamlcfg, import_name, piped

from .data import tabledata


class TestUtils(unittest.TestCase):

   def setUp(self):
      ""

   def test_import_normal(self):
      ""
      func = import_name("os.path.exists")
      self.assertEqual(func.__name__, "exists")

   def test_import_relative(self):
      ""

   def tearDown(self):
      ""


class TestJetstream(unittest.TestCase):

   def setUp(self, filename="tests/config.yaml"):
      with open(filename) as cfgfile:
         self.cfg = yaml.load(cfgfile)

   def test_loading(self):
      "parse and import everything"
      things = ["inputs", "transformers", "introspectors", "outputs"]
      print("("+", ".join(things) + ")");

      for thing in things:
         configs = self.cfg[thing]
         for name, cfg in configs.items():
            klass = import_name(cfg["use"], package="tests")
            title = cfg["description"]

   def test_piping(self):
      "build and run a basic pipe"
      configs = self.cfg["pipes"]
      parts = []
      for name, cfg in configs.items():
         for part in cfg:
            klass = import_name(part["use"], package="tests")
            parts.append(klass)
         pipe = piped(parts)
         result = []
         for r in pipe:
            result.append(r)
         self.assertEqual(tabledata, tuple(result))

   def tearDown(self):
       pass


if __name__ == '__main__':
   unittest.main()

