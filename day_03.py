import enum
import unittest
from typing import List, Tuple


class Solution:

    @staticmethod
    def binary_diagnostic(diagnostic_report: List[str]):
        pass


class Tests(unittest.TestCase):
    @staticmethod
    def _read_input(report: str) -> List[str]:
        return report.split('\n')

    def test_sample_input(self):
        report = self._read_input()
        self.assertEqual(198, Solution.binary_diagnostic(diagnostic_report=report))

    def test_real_problem(self):
        report = self._read_input()
        print(Solution.binary_diagnostic(diagnostic_report=report))
