from typing import Any


class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f'(Node: {self.data})'


class LinkedList:
    def __init__(self):
        self.start = None

    def __repr__(self) -> str:
        nodes = ['START']
        for node in self:
            nodes.append(str(node.data))
        nodes.append('NIL')
        return '\n' + ' --> '.join(nodes)

    def __iter__(self):
        node = self.start
        while node is not None:
            yield node
            node = node.next

    def __len__(self) -> int:
        length = 0
        for _ in self:
            length += 1
        return length

    def traverse(self) -> None:
        for node in self:
            print(node.data)

    def insert_at_beginning(self, element: Node) -> None:
        element.next = self.start
        self.start = element

    def insert_at_end(self, element: Node) -> None:
        pass

    def insert_after_node(self, element: Node, node_reference: Any) -> None:
        pass

    def delete_node(self, element_data: Any) -> None:
        pass

    def search(self, element_data: Any) -> Node:
        pass