from unittest import TestCase

from mytypes.linkedList import LinkedList


class TestLinkedList(TestCase):

    def setUp(self):
        self.linked_list = LinkedList()

    def test_append(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)
        self.assertEqual(self.linked_list.to_list(), [1, 2, 3])

    def test_prepend(self):
        self.linked_list.prepend(1)
        self.linked_list.prepend(2)
        self.linked_list.prepend(3)
        self.assertEqual(self.linked_list.to_list(), [3, 2, 1])

    def test_remove(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)
        self.linked_list.remove(2)
        self.assertEqual(self.linked_list.to_list(), [1, 3])

    def test_get_first(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)
        self.assertEqual(self.linked_list.get_first(2).data, 2)

    def test_get_length(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)
        self.assertEqual(len(self.linked_list), 3)

    def test_to_list(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)
        self.assertEqual(self.linked_list.to_list(), [1, 2, 3])

    def test_empty_list(self):
        self.assertEqual(self.linked_list.to_list(), [])

    def test_has_item(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)
        self.assertTrue(2 in self.linked_list)
