from unittest import TestCase

from mytypes.helpers import KeyValue
from mytypes.linkedList import KeyValueLinkedList


class TestKeyValueLinkedList(TestCase):

    def setUp(self):
        self.kv_linked_list = KeyValueLinkedList()

    def test_append(self):
        self.kv_linked_list.append(KeyValue(1, 1))
        self.kv_linked_list.append(KeyValue(2, 2))
        self.kv_linked_list.append(KeyValue(3, 3))
        self.assertEqual(
            self.kv_linked_list.to_list(),
            [KeyValue(1, 1), KeyValue(2, 2), KeyValue(3, 3)],
        )

    def test_prepend(self):
        self.kv_linked_list.prepend(KeyValue(1, 1))
        self.kv_linked_list.prepend(KeyValue(2, 2))
        self.kv_linked_list.prepend(KeyValue(3, 3))
        self.assertEqual(
            self.kv_linked_list.to_list(),
            [KeyValue(3, 3), KeyValue(2, 2), KeyValue(1, 1)],
        )

    def test_remove(self):
        self.kv_linked_list.append(KeyValue(1, 1))
        self.kv_linked_list.append(KeyValue(2, 2))
        self.kv_linked_list.append(KeyValue(3, 3))
        self.kv_linked_list.remove(2)
        self.assertEqual(
            self.kv_linked_list.to_list(), [KeyValue(1, 1), KeyValue(3, 3)]
        )

    def test_get_first(self):
        self.kv_linked_list.append(KeyValue(1, 1))
        self.kv_linked_list.append(KeyValue(2, 2))
        self.kv_linked_list.append(KeyValue(3, 3))
        self.assertEqual(self.kv_linked_list.get_first(2).data, KeyValue(2, 2))

    def test_get_length(self):
        self.kv_linked_list.append(KeyValue(1, 1))
        self.kv_linked_list.append(KeyValue(2, 2))
        self.kv_linked_list.append(KeyValue(3, 3))
        self.assertEqual(len(self.kv_linked_list), 3)

    def test_to_list(self):
        self.kv_linked_list.append(KeyValue(1, 1))
        self.kv_linked_list.append(KeyValue(2, 2))
        self.kv_linked_list.append(KeyValue(3, 3))
        self.assertEqual(
            self.kv_linked_list.to_list(),
            [KeyValue(1, 1), KeyValue(2, 2), KeyValue(3, 3)],
        )

    def test_empty_list(self):
        self.assertEqual(self.kv_linked_list.to_list(), [])

    def test_has_item(self):
        self.kv_linked_list.append(KeyValue(1, 1))
        self.kv_linked_list.append(KeyValue(2, 2))
        self.kv_linked_list.append(KeyValue(3, 3))
        self.assertTrue(2 in self.kv_linked_list)
