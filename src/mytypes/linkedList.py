from typing import Optional, Any, Hashable

from .helpers import KeyValue
from .node import Node


class LinkedList:
    def __init__(self, head: Optional[Node] = None) -> None:
        if isinstance(head, (Node, type(None))):
            self._head = head
            self._length = head.chain_length() if head is not None else 0
        else:
            raise TypeError(
                f"head must be an instance of Node or None, not {type(head)}"
            )

    def get_first(self, value: Any) -> Optional[Node]:
        current = self._head
        while current is not None:
            if current.data == value:
                return current
            current = current.next
        return None

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if self._head is None:
            self._head = new_node
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self._length += 1

    def prepend(self, value: Any) -> None:
        new_node = Node(value)
        new_node.next = self._head
        self._head = new_node
        self._length += 1

    def remove(self, value: Any) -> None:
        if self._head is None:
            return
        if self._head.data == value:
            self._head = self._head.next
            self._length -= 1
            return
        current = self._head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                self._length -= 1
                return
            current = current.next

    def to_list(self):
        list_ = []
        current = self.head
        while current is not None:
            list_.append(current.data)
            current = current.next
        return list_

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def __len__(self):
        return self._length

    def __str__(self):
        return f"{type(self)}({str("->".join([str(value) for value in self]))})"

    @property
    def head(self):
        return self._head


class KeyValueLinkedList(LinkedList):
    def get_first(self, key: Hashable) -> Optional[Node[KeyValue]]:
        current = self._head
        while current is not None:
            if current.data.key == key:
                return current
            current = current.next
        return None

    def append(self, value: KeyValue) -> None:
        super().append(value)

    def prepend(self, value: KeyValue) -> None:
        super().prepend(value)

    def remove(self, key: Hashable) -> None:
        if self._head is None:
            return
        if self._head.data.key == key:
            self._head = self._head.next
            self._length -= 1
            return
        current = self._head
        while current.next is not None:
            if current.next.data.key == key:
                current.next = current.next.next
                self._length -= 1
                return
            current = current.next

    def __contains__(self, key: Hashable) -> bool:
        return self.get_first(key) is not None
