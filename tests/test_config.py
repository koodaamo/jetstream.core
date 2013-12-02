#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_config
----------------------------------

Tests for `jetstream` package configuration
"""

import unittest, os
import jetstream.config as config

HERE = os.path.abspath(os.path.dirname(__file__))

CFG_FILE = HERE + os.sep + "test.yaml"
CFG_URL = "file://" + CFG_FILE

SECTIONS = ["inputs", "inspectors", "transformers", "outputs", "pipes"]

class TestConfiguring(unittest.TestCase):
   "test the utils"

   def test_load_path(self):
      mapping = config.from_yaml(CFG_FILE)
      self.assertEqual(sorted(SECTIONS), sorted(list(mapping.keys())))

   def test_load_url(self):
      mapping = config.from_yaml(CFG_URL)
      self.assertEqual(sorted(SECTIONS), sorted(list(mapping.keys())))

   def test_mapping_config(self):
      konfig = config.MappingConfig(config.from_yaml(CFG_FILE))
