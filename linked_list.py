from typing import Any
 
 # Estilo consistente con la base del código - Mejoras a clases
 
class Node:
    def __init__(self, song: str, artist: str, album: str):
        self.song: dict = {
            'song': song,
            'artist': artist,
            'album': album,
        }
        self.next: Node = None
        self.prev: Node = None
 
    def __repr__(self) -> str:
        return f'(Node: {self.song["song"]} - {self.song["artist"]})'
 
 
class LinkedList:
    def __init__(self):
        self.start: Node = None
        self.end: Node = None
 
    def __repr__(self) -> str:
        nodes = ['START']
        for node in self:
            nodes.append(f'{node.song["song"]}')
        nodes.append('NIL')
        return '\n' + ' <--> '.join(nodes)
 
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
            print(node.song)
 
    def insert_at_beginning(self, element: Node) -> None:
        element.next = self.start
        element.prev = None
        if self.start is not None:
            self.start.prev = element
        self.start = element
        if self.end is None:
            self.end = element
 
    def insert_at_end(self, element: Node) -> None:
        element.prev = self.end
        element.next = None
        if self.end is not None:
            self.end.next = element
        self.end = element
        if self.start is None:
            self.start = element
 
    def insert_after_node(self, element: Node, node_reference: Any) -> None:
        for node in self:
            if node.song['song'] == node_reference:
                element.prev = node
                element.next = node.next
                if node.next is not None:
                    node.next.prev = element
                else:
                    self.end = element
                node.next = element
                return
 
    def delete_node(self, element_data: Any) -> None:
        for node in self:
            if node.song['song'] == element_data:
                if node.prev is not None:
                    node.prev.next = node.next
                else:
                    self.start = node.next
                if node.next is not None:
                    node.next.prev = node.prev
                else:
                    self.end = node.prev
                return
 
    def search(self, element_data: Any) -> Node:
        for node in self:
            if node.song['song'] == element_data:
                return node
        return None