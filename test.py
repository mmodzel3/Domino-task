#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from main import simulate_domino


class Test(unittest.TestCase):
    def test_when_simulate_forward_domino_then_got_correct_domino_arrangement(self):
        test_domino = '||//||\\||/\\|'
        self.assertEqual('||///\\\\||/\\|', simulate_domino(test_domino, True))

    def test_when_simulate_forward_domino_on_vertical_domino_then_domino_arrangement_not_change(self):
        test_domino = '||||||||'
        self.assertEqual('||||||||', simulate_domino(test_domino, True))


if __name__ == "__main__":
    unittest.main()
