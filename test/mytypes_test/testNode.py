from unittest import TestCase

from mytypes.node import Node


class TestNode(TestCase):
    def test_chain_length(self):
        node = Node(1)
        self.assertEqual(node.chain_length(), 1)
        node.next = Node(5)
        self.assertEqual(node.chain_length(), 2)
        node.next.next = Node(12)
        self.assertEqual(node.chain_length(), 3)
