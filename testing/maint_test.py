"""
Imports for testing."""
import unittest
from sys import path
from os import getcwd
from os.path import dirname

path.append(dirname(getcwd()))
from node_test import TestClassNode


if __name__ == "__main__":
    unittest.main()
