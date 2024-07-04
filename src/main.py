from mytypes import Node, LinkedList, KeyValueLinkedList, KeyValue, HashMap, HashSet


def example_node() -> None:
    # example for Node
    node = Node(1, next=Node(2))
    print(node)  # Node(1, Node(2))
    print(node.chain_length())  # 2
    print(node.next)  # Node(2)
    print(node.next.data)  # 2
    node.next = Node(3, next=Node(4))
    print(node)  # Node(1, Node(3, Node(4)))
    print(node.chain_length())  # 4


def example_linkedList() -> None:
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


def example_kv_linked_list() -> None:
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


def example_hash_set():
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


def example_hash_map():
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


def main() -> None:
    print("=" * 50)
    example_node()
    print("=" * 50)
    example_linkedList()
    print("=" * 50)
    example_kv_linked_list()
    print("=" * 50)
    example_hash_set()
    print("=" * 50)
    example_hash_map()
    print("=" * 50)


if __name__ == "__main__":
    main()
