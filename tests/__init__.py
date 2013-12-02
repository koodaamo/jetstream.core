import unittest

def test_suite():
    suite = unittest.TestLoader().discover(start_dir=".")
    return suite
