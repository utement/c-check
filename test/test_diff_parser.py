import os
from unittest import TestCase

from diff_parser import DiffParser


class TestDiffParser(TestCase):
    def test_parse(self):
        with open(os.path.join(os.path.dirname(__file__), "resources", "diff.txt"), "r") as file:
            data = file.read()
        self.assertTrue(DiffParser(data))
