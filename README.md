# DataStructImplementations

Welcome to **DataStructImplementations**! This project showcases custom implementations of various data structures in
Python, built from scratch. The goal is to provide a deep understanding of how these data structures work under the
hood.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Node](#node)
    - [Algorithm of Operation](#algorithm-of-operation)
    - [Testing](#testing)
    - [Usage](#usage)
- [LinkedList](#linkedlist)
    - [Algorithm of Operation](#algorithm-of-operation-1)
    - [Testing](#testing-1)
    - [Usage](#usage-1)
- [KeyValueLinkedList](#keyvaluelinkedlist)
    - [Algorithm of Operation](#algorithm-of-operation-2)
    - [Testing](#testing-2)
    - [Usage](#usage-2)
- [HashSet](#hashset)
    - [Algorithm of Operation](#algorithm-of-operation-3)
    - [Testing](#testing-3)
    - [Usage](#usage-3)
- [HashMap](#hashmap)
    - [Algorithm of Operation](#algorithm-of-operation-4)
    - [Testing](#testing-4)
    - [Usage](#usage-4)
- [Contributing](#Contributing)
---

## Project Structure

```
DataStructImplementations
├── poetry.lock
├── pyproject.toml
├── README.md
├── src
│   ├── main.py
│   └── mytypes
│       ├── hashMap.py
│       ├── hashSet.py
│       ├── helpers.py
│       ├── __init__.py
│       ├── linkedList.py
│       └── node.py
└── test
    └── mytypes_test
        ├── __init__.py
        ├── testHashMap.py
        ├── testHashSet.py
        ├── testKeyValueLinkedList.py
        ├── testLinkedList.py
        └── testNode.py

5 directories, 16 files
```

---

## Node

### Algorithm of Operation

`Nodes` are a basic data structure which contain data and one or more links to
other nodes. Nodes can be used to represent a tree structure or a linked list.
In such structures where nodes are used, it is possible to traverse from one
node to another node.

Data structures containing nodes have typically two bits of information stored
in a `node`: data and link to next node.

The first part is a `value` and the second part is an address of sorts pointing
to the `next node`. In this way, a system of nodes is created. A NONE/NULL value in the
link part of a node’s info denotes that the path or data structure contains no
further nodes.

### Testing

The `Node` class is tested in `testNode.py` using the `unittest` framework.

```python
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
```

### Usage

```python
from mytypes.node import Node

node = Node(1, next=Node(2))
print(node)  # Node(1, Node(2))
print(node.chain_length())  # 2
print(node.next)  # Node(2)
print(node.next.data)  # 2
node.next = Node(3, next=Node(4))
print(node)  # Node(1, Node(3, Node(4)))
print(node.chain_length())  # 4
```

## LinkedList

### Algorithm of Operation

`Linked List` is basically `chains of nodes` where each node contains information
such as `data` and a `pointer to the next node` in the chain. It is a popular data
structure with a wide range of real-world applications. In this article, we will
provide a complete introduction of Linked List, which will help you tackle any
problem based on Linked List.

### Testing

The `LinkedList` class is tested in [testLinkedList.py](test/mytypes_test/testLinkedList.py) using the `unittest`
framework.

### Usage

```python
from mytypes.linkedList import LinkedList

# Create a new linked list
linked_list = LinkedList()

# Append elements to the linked list
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
print("After appending 1, 2, 3: ", linked_list.to_list())

# Prepend elements to the linked list
linked_list.prepend(0)
print("After prepending 0: ", linked_list.to_list())

# Remove an element from the linked list
linked_list.remove(2)
print("After removing 2: ", linked_list.to_list())

# Get the first node with a specific value
node = linked_list.get_first(3)
if node:
    print("First node with data 3: ", node.data)
else:
    print("Node with data 3 not found")

# Get the length of the linked list
length = len(linked_list)
print("Length of the linked list: ", length)

# Check if an item is in the linked list
has_item = 1 in linked_list
print("Linked list has 1: ", has_item)

# Convert the linked list to a list
lst = linked_list.to_list()
print("Linked list as a Python list: ", lst)

# Check an empty linked list
empty_list = LinkedList()
print("Empty linked list: ", empty_list.to_list())
```

## KeyValueLinkedList

### Algorithm of Operation

The `KeyValueLinkedList` class extends `LinkedList` to store key-value pairs, making it useful for implementing
associative arrays or dictionaries.

### Testing

The `KeyValueLinkedList` class is tested in [testKeyValueLinkedList.py](test/mytypes_test/testKeyValueLinkedList.py)
using the `unittest` framework.

### Usage

```python
from mytypes.helpers import KeyValue
from mytypes.linkedList import KeyValueLinkedList

# Create a new KeyValue linked list
kv_linked_list = KeyValueLinkedList()

# Append elements to the KeyValue linked list
kv_linked_list.append(KeyValue(1, 1))
kv_linked_list.append(KeyValue(2, 2))
kv_linked_list.append(KeyValue(3, 3))
print(
    "After appending KeyValue(1, 1), KeyValue(2, 2), KeyValue(3, 3):",
    kv_linked_list.to_list(),
)

# Prepend elements to the KeyValue linked list
kv_linked_list.prepend(KeyValue(0, 0))
print("After prepending KeyValue(0, 0):", kv_linked_list.to_list())

# Remove an element from the KeyValue linked list
kv_linked_list.remove(2)
print("After removing key 2:", kv_linked_list.to_list())

# Get the first node with a specific key
node = kv_linked_list.get_first(3)
if node:
    print("First node with key 3:", node.data)
else:
    print("Node with key 3 not found")

# Get the length of the KeyValue linked list
length = len(kv_linked_list)
print("Length of the KeyValue linked list:", length)

# Check if an item is in the KeyValue linked list
has_item = 1 in kv_linked_list
print("KeyValue linked list has key 1:", has_item)

# Convert the KeyValue linked list to a list
lst = kv_linked_list.to_list()
print("KeyValue linked list as a Python list:", lst)

# Check an empty KeyValue linked list
empty_kv_list = KeyValueLinkedList()
print("Empty KeyValue linked list:", empty_kv_list.to_list())
```

## HashSet

### Algorithm of Operation

The `HashSet` class in this project implements a hash set, which
is a collection of `unique` elements. It provides efficient operations
for `adding`, `removing`, and `checking` the membership of elements
using a hash table. Here’s an in-depth description of the algorithm

###### Initialization

The `hash set` is initialized with an `array of buckets`, where each bucket
is an `instance` of a `LinkedList`. The initial number of buckets is
determined by a predefined length. This array of buckets forms the
underlying structure for storing the elements.

###### Adding Elements

When `adding` an element to the hash set, the algorithm first checks if
the hash table `is full`. If it is, the table's size is doubled to
accommodate more elements.

The algorithm then calculates a hash code for the element using
Python's built-in `hash` function. This hash code is used to determine
the appropriate bucket by taking the modulus of the hash code with the
current length of the bucket array.

If the element is not `already present` in the determined bucket, it is
appended to the linked list at that bucket. This ensures that each
element is stored in a specific location based on its hash code, and
any duplicates are avoided.

###### Retrieving Elements

To `retrieve` an element, the algorithm calculates the hash code of the
desired element to locate the appropriate bucket. It then searches for
the element within the `linked list` at that bucket. If the element is
found, it is returned; otherwise, a default value is returned.

###### Removing Elements

The `removal process` involves calculating the hash code of the element
to locate the correct bucket and then removing the element from the
linked list within that bucket, if it exists.

###### Checking for Membership

To check if an element is present in the hash set, the algorithm calculates
the hash code of the element and checks the `corresponding bucket`. If the element
is found in the bucket, the algorithm confirms its presence.

###### Resizing the Hash Set

When the hash set becomes `full` (i.e., the number of elements equals or exceeds
the number of buckets), the size of the bucket array is `doubled`. This process
involves creating a new array of buckets with double the capacity and rehashing
all existing elements to distribute them across the new array. This helps in
maintaining efficient performance by reducing the likelihood of collisions.

###### Utility Functions

Additional utility functions are provided to support common operations such as
**_checking if an element is in the hash set_**, **_iterating over the elements_**, **_getting
the number of elements_**, and **_generating string representations_** of the hash set.

###### Key Points

* **Hash Table**: Utilizes a hash table with separate chaining (linked lists) to handle collisions efficiently.
* **Hashing**: Elements are hashed using Python's hash function, with the hash code used to determine the appropriate
  bucket.
* **Collision** Handling: Collisions are handled by storing colliding elements in a linked list at the corresponding
  bucket.
* **Resizing**: The hash table is resized and elements are rehashed when it becomes full to ensure continued efficiency.
* **Efficiency**: The average time complexity for basic operations (add, remove, check membership) is O(1), making the
  hash set highly efficient for these operations.

### Testing

The `HashSet` class is tested in [testHashSet.py](test/mytypes_test/testHashSet.py) using the `unittest` framework.

### Usage

```python
from mytypes.hashSet import HashSet

# Create a new hash set
hash_set = HashSet()

# Add elements to the hash set
hash_set.add("a")
hash_set.add("b")
hash_set.add("c")
print("After adding 'a', 'b', 'c':", set(hash_set))

# Add a duplicate element
hash_set.add("a")
print("After adding duplicate 'a':", set(hash_set))

# Get elements from the hash set
print("Get 'a':", hash_set.get("a"))
print("Get 'b':", hash_set.get("b"))
print("Get 'c':", hash_set.get("c"))
print("Get 'd' (default None):", hash_set.get("d"))
print("Get 'd' (with default 'default'):", hash_set.get("d", "default"))

# Remove elements from the hash set
hash_set.remove("a")
hash_set.remove("b")
hash_set.remove("c")
print("After removing 'a', 'b', 'c':", set(hash_set))

# Check if an element is in the hash set
hash_set.add("a")
hash_set.add("b")
hash_set.add("c")
print("'a' in hash set:", "a" in hash_set)
print("'d' in hash set:", "d" in hash_set)

# Iterate over the hash set
elements = ["a", "b", "c"]
for elem in elements:
    hash_set.add(elem)
print("Elements in hash set after iteration:", set(hash_set))

# Get the length of the hash set
hash_set.add("d")
hash_set.add("e")
print("Length of the hash set:", len(hash_set))

hash_set.add("f")
hash_set.add("g")

# Check the string and representation of the hash set
print("String representation:", str(hash_set))
print("Repr representation:", repr(hash_set))
```

## HashMap

### Algorithm of Operation

The `HashMap` class implements a hash map (or dictionary), providing efficient
`key-value pair` storage and retrieval using a `hash table` and `key-value linked lists` for
collision handling.

The HashMap class inherits from HashSet and initializes an array of
KeyValueLinkedList instances, one for each bucket. Initially, the length of
the _buckets array is determined by protected field _length, a value
inherited from HashSet.

Also, we override The `__setitem__`, `__getitem__`, and `__delitem__` methods
allow using the hash map with the dictionary-like syntax for setting, getting,
and deleting items.

###### Adding Elements

The add method inserts a new element into the hash set. If the hash set is
full, it doubles the size of the bucket array by calling protected method
_increase_size. The method calculates the hash code of the element to
determine the appropriate bucket. If the element is not already present
in the bucket, it appends it.

###### Adding, Retrieving, Removing, Checking for Membership

Adding, Retrieving, Removing, Checking for Membership overrides from
the HashSet, but use keys as the parameter for the hash function.

###### Utility Methods

The `__contains__`, `__iter__`, `__len__`, `__str__`, and `__repr__` methods
provide additional functionality for the hash set, allowing it to be used with
common Python operations and functions.

### Testing

The `HashMap` class is tested in [testHashMap.py](test/mytypes_test/testHashSet.py) using the `unittest` framework.

### Usage

```python
from mytypes import HashMap, KeyValue

# Create a new hash map
hash_map = HashMap()

# Add key-value pairs to the hash map
hash_map.add(KeyValue("a", 1))
hash_map.add(KeyValue("b", 2))
hash_map.add(KeyValue("c", 3))
print(
    "After adding KeyValue('a', 1), KeyValue('b', 2), KeyValue('c', 3):",
    sorted([i for i in hash_map], key=lambda x: x.key),
)

# Add a duplicate key with a new value
hash_map.add(KeyValue("a", 4))
print(
    "After adding KeyValue('a', 4):",
    sorted([i for i in hash_map], key=lambda x: x.key),
)

# Get values from the hash map
print("Get value for key 'a':", hash_map.get("a"))
print("Get value for key 'b':", hash_map.get("b"))
print("Get value for key 'c':", hash_map.get("c"))
print("Get value for key 'd' (default None):", hash_map.get("d"))
print(
    "Get value for key 'd' (with default 'default'):", hash_map.get("d", "default")
)

# Remove key-value pairs from the hash map
hash_map.remove("a")
hash_map.remove("b")
hash_map.remove("c")
print("After removing keys 'a', 'b', 'c':", [i for i in hash_map])

# Check if a key exists in the hash map
hash_map.add(KeyValue("a", 1))
hash_map.add(KeyValue("b", 2))
hash_map.add(KeyValue("c", 3))
print("Key 'a' in hash map:", "a" in hash_map)
print("Key 'd' in hash map:", "d" in hash_map)

# Iterate over the hash map
keys = ["a", "b", "c"]
values = [1, 2, 3]
for elem in zip(keys, values):
    hash_map.add(KeyValue(elem[0], elem[1]))
print(
    "Elements in hash map after iteration:",
    sorted([i for i in hash_map], key=lambda x: x.key),
)

# Get the length of the hash map
hash_map.add(KeyValue("d", 4))
hash_map.add(KeyValue("e", 5))
print("Length of the hash map:", len(hash_map))

# Increase the size of the hash map
hash_map.add(KeyValue("f", 6))
hash_map.add(KeyValue("g", 7))
hash_map.add(KeyValue("h", 8))
hash_map.add(KeyValue("i", 9))
hash_map.add(KeyValue("j", 10))
print(
    "Hash map after increasing size:",
    sorted([i for i in hash_map], key=lambda x: x.key),
)

# Use dictionary-like item setting
hash_map["k"] = 11
hash_map["l"] = 12
print(
    "Hash map after setting items 'k' and 'l':",
    sorted([i for i in hash_map], key=lambda x: x.key),
)

# Use dictionary-like item getting
print("Get item 'k':", hash_map["k"])
print("Get item 'l':", hash_map["l"])

# Use dictionary-like item deletion
del hash_map["k"]
del hash_map["l"]
print(
    "Hash map after deleting items 'k' and 'l':",
    sorted([i for i in hash_map], key=lambda x: x.key),
)

# Check string and representation of the hash map
print("String representation:", str(hash_map))
print("Repr representation:", repr(hash_map))
```

## Contributing

Contributions are welcome! Please fork this repository and submit a pull
request for any improvements or bug fixes.

