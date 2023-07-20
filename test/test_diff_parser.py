import os
from unittest import TestCase

from diff_parser import DiffParser


class TestDiffParser(TestCase):
    def test_validate_data(self) -> None:
        parser = DiffParser("      ")
        self.assertFalse(parser.validate_data())

        with open(os.path.join(os.path.dirname(__file__), "resources", "diff.txt"), "r") as file:
            data = file.read()

        parser2 = DiffParser(data)
        self.assertTrue(parser2.validate_data())

    def test_parse_empty(self) -> None:
        self.assertFalse(DiffParser("      ").parse())

    def test_parse(self) -> None:
        with open(os.path.join(os.path.dirname(__file__), "resources", "diff.txt"), "r") as file:
            data = file.read()
        self.assertTrue(DiffParser(data))
