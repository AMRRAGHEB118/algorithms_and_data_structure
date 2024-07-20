from typing import Optional


class Node:
    def __init__(self, data: int, next: Optional['Node'] = None) -> None:
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.data}, {self.next})"

    def __str__(self) -> str:
        return f"Node({self.data}, {self.next})"

    def __eq__(self, other) -> bool:
        return self.data == other.data

    def __ne__(self, other) -> bool:
        return self.data != other.data


class LinkedList:
    def __init__(self, head: Optional[Node] = None) -> None:
        self.head: Optional[Node] = head

    def append(self, data: int) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self) -> None:
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def search(self, data: int) -> bool:
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
