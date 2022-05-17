"""Testing of Node class."""
from sys import path
from os import getcwd
from os.path import dirname
import unittest

path.append(dirname(getcwd()))

from src.node import SimpleNode
from mocks.node_mocks import MOCK_INFORMATION, MOCK_LIST_OF_ITEMS


class TestClassNode(unittest.TestCase):
    """Testing class for Node."""

    def setUp(self):
        """Action performed before run tests."""
        self.simple_node = SimpleNode(MOCK_INFORMATION)
        self.simple_node.add_array_at_end(MOCK_LIST_OF_ITEMS)

    def test_init_and_str_success(self):
        """Testing success of initializing."""
        simple_node = SimpleNode(MOCK_INFORMATION)

        self.assertIsNone(simple_node.next_node)
        self.assertIsNone(simple_node.previous_node)
        self.assertEqual(simple_node.information, MOCK_INFORMATION)
        self.assertEqual(str(simple_node), f"node_x: {MOCK_INFORMATION}")

    def test_quantity_success(self):
        """Testing quantity method success."""
        simple_node = SimpleNode()
        simple_node.add_array_at_end(list(MOCK_LIST_OF_ITEMS))
        self.assertEqual(simple_node.quantity(), len(MOCK_LIST_OF_ITEMS))

    def test_add_first_node(self):
        """Testing adding and taking the first node"""
        testing_node = SimpleNode(MOCK_INFORMATION)
        self.simple_node.add_first_node(testing_node)


if __name__ == "__main__":
    unittest.main()
