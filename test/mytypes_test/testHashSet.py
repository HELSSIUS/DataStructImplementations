import unittest

from src.mytypes.hashSet import HashSet


class TestHashSet(unittest.TestCase):

    def setUp(self):
        self.hash_set = HashSet()

    def test_add(self):
        self.hash_set.add("a")
        self.hash_set.add("b")
        self.hash_set.add("c")
        self.assertEqual(set(self.hash_set), {"a", "b", "c"})
        # Test adding duplicate
        self.hash_set.add("a")
        self.assertEqual(set(self.hash_set), {"a", "b", "c"})

    def test_get(self):
        self.hash_set.add("a")
        self.hash_set.add("b")
        self.hash_set.add("c")
        self.assertEqual(self.hash_set.get("a"), "a")
        self.assertEqual(self.hash_set.get("b"), "b")
        self.assertEqual(self.hash_set.get("c"), "c")
        self.assertIsNone(self.hash_set.get("d"))
        self.assertEqual(self.hash_set.get("d", "default"), "default")

    def test_remove(self):
        self.hash_set.add("a")
        self.hash_set.add("b")
        self.hash_set.add("c")
        self.hash_set.remove("a")
        self.hash_set.remove("b")
        self.hash_set.remove("c")
        self.assertEqual(set(self.hash_set), set())

    def test_has(self):
        self.hash_set.add("a")
        self.hash_set.add("b")
        self.hash_set.add("c")
        self.assertTrue(self.hash_set.has("a"))
        self.assertTrue(self.hash_set.has("b"))
        self.assertTrue(self.hash_set.has("c"))

        self.assertFalse(self.hash_set.has("d"))
        self.assertFalse(self.hash_set.has("e"))
        self.assertFalse(self.hash_set.has("f"))
        self.assertFalse(self.hash_set.has("g"))

    def test_in(self):
        self.hash_set.add("a")
        self.hash_set.add("b")
        self.hash_set.add("c")
        self.assertTrue("a" in self.hash_set)
        self.assertTrue("b" in self.hash_set)
        self.assertTrue("c" in self.hash_set)

        self.assertFalse("d" in self.hash_set)
        self.assertFalse("e" in self.hash_set)
        self.assertFalse("f" in self.hash_set)
        self.assertFalse("g" in self.hash_set)

    def test_iteration(self):
        elements = ["a", "b", "c"]
        for elem in elements:
            self.hash_set.add(elem)
        self.assertEqual(set(self.hash_set), set(elements))

    def test_len(self):
        self.hash_set.add("a")
        self.hash_set.add("b")
        self.hash_set.add("c")
        self.hash_set.add("d")
        self.hash_set.add("e")
        self.assertEqual(len(self.hash_set), 5)

    def test_is_full(self):
        self.assertFalse(self.hash_set._is_full())
        self.hash_set.add("a")
        self.hash_set.add("b")
        self.hash_set.add("c")
        self.hash_set.add("d")
        self.hash_set.add("e")
        self.assertTrue(self.hash_set._is_full())

    def test_increase_size(self):
        self.hash_set.add("a")
        self.hash_set.add("b")
        self.hash_set.add("c")
        self.hash_set.add("d")
        self.assertFalse(self.hash_set._is_full())
        self.hash_set.add("e")
        self.assertTrue(self.hash_set._is_full())
        self.assertEqual(len(self.hash_set._buckets), 5)
        self.hash_set.add("f")
        self.assertFalse(self.hash_set._is_full())
        self.assertEqual(len(self.hash_set._buckets), 10)

    def test_str_and_repr(self):
        self.hash_set.add("a")
        self.hash_set.add("b")
        self.hash_set.add("c")
        self.assertIsInstance(str(self.hash_set), str)
        self.assertIsInstance(repr(self.hash_set), str)
