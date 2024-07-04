from typing import Hashable, Any

from .hashSet import HashSet
from .helpers import KeyValue
from .linkedList import KeyValueLinkedList


class HashMap(HashSet):
    def __init__(self) -> None:
        self._buckets: list[KeyValueLinkedList] = []

        for _ in range(self._length):
            self._buckets.append(KeyValueLinkedList())

    def add(self, element: KeyValue) -> None:
        if self._is_full():
            self._increase_size()

        hash_code = hash(element.key) % self._length
        if element.key not in self._buckets[hash_code]:
            self._buckets[hash_code].append(element)
        else:
            self._buckets[hash_code].get_first(element.key).data.value = element.value

    def get(self, value: Hashable, default: Any = None) -> Any | None:
        hash_code = hash(value) % self._length
        if res_node := self._buckets[hash_code].get_first(value):
            return res_node.data.value
        return default

    def remove(self, key: Hashable) -> None:
        hash_code = hash(key) % self._length
        if res_node := self._buckets[hash_code].get_first(key):
            self._buckets[hash_code].remove(res_node.data.key)

    def _increase_size(self) -> None:
        self._length *= 2
        new_buckets = [KeyValueLinkedList() for _ in range(self._length)]
        for bucket in self._buckets:
            for kv_node in bucket:
                hash_code = hash(kv_node.key) % self._length
                new_buckets[hash_code].append(kv_node)
        self._buckets = new_buckets

    def __setitem__(self, key: Hashable, value: Any) -> None:
        self.add(KeyValue(key, value))

    def __getitem__(self, key: Hashable) -> Any:
        return self.get(key)

    def __delitem__(self, key: Hashable) -> None:
        self.remove(key)
