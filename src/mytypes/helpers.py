from dataclasses import dataclass
from typing import Hashable, Any


@dataclass
class KeyValue:
    key: Hashable
    value: Any
