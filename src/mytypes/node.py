from dataclasses import dataclass
from typing import Optional


@dataclass
class Node[T]:
    data: T
    next: Optional["Node"] = None

    def chain_length(self) -> int:
        current = self
        length = 0
        while current is not None:
            length += 1
            current = current.next
        return length

    def __str__(self) -> str:
        return f"{type(self)}({self.data})"
