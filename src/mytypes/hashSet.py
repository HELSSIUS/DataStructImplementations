from typing import Hashable, Any, Iterator

from mytypes.linkedList import LinkedList


class HashSet:
    _length = 5

    def __init__(self) -> None:
        self._buckets: list[LinkedList] = []

        for _ in range(self._length):
            self._buckets.append(LinkedList())

    def add(self, element: Hashable) -> None:
        if self._is_full():
            self._increase_size()

        hash_code = hash(element) % self._length
        if element not in self._buckets[hash_code]:
            self._buckets[hash_code].append(element)

    def get(self, value: Hashable, default: Any = None) -> Hashable | None:
        hash_code = hash(value) % self._length
        if res_node := self._buckets[hash_code].get_first(value):
            return res_node.data
        return default

    def remove(self, value: Hashable) -> None:
        hash_code = hash(value) % self._length
        if res_node := self._buckets[hash_code].get_first(value):
            self._buckets[hash_code].remove(res_node.data)

    def has(self, value: Hashable) -> bool:
        hash_code = hash(value) % self._length
        return bool(self._buckets[hash_code].get_first(value))

    def _is_full(self) -> bool:
        return len(self) >= len(self._buckets)

    def _increase_size(self) -> None:
        self._length *= 2
        new_buckets = [LinkedList() for _ in range(self._length)]
        for bucket in self._buckets:
            for value in bucket:
                hash_code = hash(value) % self._length
                new_buckets[hash_code].append(value)
        self._buckets = new_buckets

    def __contains__(self, item):
        return self.has(item)

    def __iter__(self) -> Iterator[Hashable]:
        for bucket in self._buckets:
            for value in bucket:
                yield value

    def __len__(self):
        return sum(len(bucket) for bucket in self._buckets)

    def __str__(self) -> str:
        return f"{", ".join(str(node.to_list()) for node in self._buckets)}"

    def __repr__(self) -> str:
        return str(bucket.to_list() for bucket in self._buckets)
