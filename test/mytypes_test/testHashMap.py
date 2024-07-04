from unittest import TestCase

from mytypes import HashMap, KeyValue


class TestHashMap(TestCase):
    def setUp(self):
        self.hash_map = HashMap()

    def test_add(self):
        self.hash_map.add(KeyValue("a", 1))
        self.hash_map.add(KeyValue("b", 2))
        self.hash_map.add(KeyValue("c", 3))
        self.assertEqual(
            sorted([i for i in self.hash_map], key=lambda x: x.key),
            [KeyValue("a", 1), KeyValue("b", 2), KeyValue("c", 3)],
        )
        # Test adding duplicate
        self.hash_map.add(KeyValue("a", 4))
        self.assertListEqual(
            sorted([i for i in self.hash_map], key=lambda x: x.key),
            [KeyValue("a", 4), KeyValue("b", 2), KeyValue("c", 3)],
        )

    def test_get(self):
        self.hash_map.add(KeyValue("a", 1))
        self.hash_map.add(KeyValue("b", 2))
        self.hash_map.add(KeyValue("c", 3))
        self.assertEqual(self.hash_map.get("a"), 1)
        self.assertEqual(self.hash_map.get("b"), 2)
        self.assertEqual(self.hash_map.get("c"), 3)
        self.assertIsNone(self.hash_map.get("d"), None)
        self.assertEqual(self.hash_map.get("d", "default"), "default")

    def test_remove(self):
        self.hash_map.add(KeyValue("a", 1))
        self.hash_map.add(KeyValue("b", 2))
        self.hash_map.add(KeyValue("c", 3))
        self.hash_map.remove("a")
        self.hash_map.remove("b")
        self.hash_map.remove("c")
        self.assertListEqual([i for i in self.hash_map], [])

    def test_has(self):
        self.hash_map.add(KeyValue("a", 1))
        self.hash_map.add(KeyValue("b", 2))
        self.hash_map.add(KeyValue("c", 3))
        self.assertTrue(self.hash_map.has("a"))
        self.assertTrue(self.hash_map.has("b"))
        self.assertTrue(self.hash_map.has("c"))

        self.assertFalse(self.hash_map.has("d"))
        self.assertFalse(self.hash_map.has("e"))
        self.assertFalse(self.hash_map.has("f"))
        self.assertFalse(self.hash_map.has("g"))

    def test_in(self):
        self.hash_map.add(KeyValue("a", 1))
        self.hash_map.add(KeyValue("b", 2))
        self.hash_map.add(KeyValue("c", 3))
        self.assertTrue("a" in self.hash_map)
        self.assertTrue("b" in self.hash_map)
        self.assertTrue("c" in self.hash_map)

        self.assertFalse("d" in self.hash_map)
        self.assertFalse("e" in self.hash_map)
        self.assertFalse("f" in self.hash_map)
        self.assertFalse("g" in self.hash_map)

    def test_iteration(self):
        keys = ["a", "b", "c"]
        values = [1, 2, 3]
        for elem in zip(keys, values):
            self.hash_map.add(KeyValue(elem[0], elem[1]))
        self.assertEqual(
            sorted([i for i in self.hash_map], key=lambda x: x.key),
            [KeyValue("a", 1), KeyValue("b", 2), KeyValue("c", 3)],
        )

    def test_len(self):
        self.hash_map.add(KeyValue("a", 1))
        self.hash_map.add(KeyValue("b", 2))
        self.hash_map.add(KeyValue("c", 3))
        self.assertEqual(len(self.hash_map), 3)

    def test_is_full(self):
        self.assertFalse(self.hash_map._is_full())
        self.hash_map.add(KeyValue("a", 1))
        self.hash_map.add(KeyValue("b", 2))
        self.hash_map.add(KeyValue("c", 3))
        self.hash_map.add(KeyValue("d", 4))
        self.hash_map.add(KeyValue("e", 5))
        self.assertTrue(self.hash_map._is_full())

    def test_increase_size(self):
        self.hash_map.add(KeyValue("a", 1))
        self.hash_map.add(KeyValue("b", 2))
        self.hash_map.add(KeyValue("c", 3))
        self.hash_map.add(KeyValue("d", 4))
        self.assertFalse(self.hash_map._is_full())
        self.hash_map.add(KeyValue("e", 5))
        self.assertTrue(self.hash_map._is_full())
        self.assertEqual(len(self.hash_map._buckets), 5)
        self.hash_map.add(KeyValue("f", 6))
        self.assertFalse(self.hash_map._is_full())
        self.assertEqual(len(self.hash_map._buckets), 10)
        # additional test
        self.hash_map.add(KeyValue("g", 7))
        self.hash_map.add(KeyValue("h", 8))
        self.hash_map.add(KeyValue("i", 9))
        self.hash_map.add(KeyValue("j", 10))

    def test_set_item(self):
        self.hash_map["a"] = 1
        self.hash_map["b"] = 2
        self.hash_map["c"] = 3
        self.assertEqual(
            sorted([i for i in self.hash_map], key=lambda x: x.key),
            [KeyValue("a", 1), KeyValue("b", 2), KeyValue("c", 3)],
        )

    def test_get_item(self):
        self.hash_map["a"] = 1
        self.hash_map["b"] = 2
        self.hash_map["c"] = 3
        self.assertEqual(self.hash_map["a"], 1)
        self.assertEqual(self.hash_map["b"], 2)
        self.assertEqual(self.hash_map["c"], 3)

    def test_del_item(self):
        self.hash_map["a"] = 1
        self.hash_map["b"] = 2
        self.hash_map["c"] = 3
        del self.hash_map["a"]
        del self.hash_map["b"]
        del self.hash_map["c"]
        self.assertListEqual([i for i in self.hash_map], [])

    def test_str_and_repr(self):
        self.hash_map.add(KeyValue("a", 1))
        self.hash_map.add(KeyValue("b", 2))
        self.hash_map.add(KeyValue("c", 3))
        self.assertIsInstance(str(self.hash_map), str)
        self.assertIsInstance(repr(self.hash_map), str)
