
# class LinkedList:

#     def __init__(self):
#         self.head = None
#         self._size = 0


#     def prepend(self, data):
#         self.size += 1
#         new_node = Node(data)
#         if self.head:
#             new_node.next = self.head
#         self.head = new_node
#         return None


#     def append(self, data):
#         self.size += 1
#         node = self.head
#         while node.next is not None:
#             node = node.next
#         node.next = Node(data)
#         return None


#     def insert(self, data, position):
#         self.size += 1
        
#         if position == 0:
#             self.prepend(data)
#             return None

#         new_node = Node(data)
#         current = self.head
#         prev = None
#         count = 0
        
#         while current and count < position:
#             prev = current
#             current = current.next
#             count += 1

#         if count < position:
#             prev.next = new_node
#             return None
        
#         prev.next = new_node
#         new_node.next = current
#         return None

#     def remove(self, data):
#         if not self.head:
#             return None

#         current = self.head
#         prev = None
#         while current is not None:
#             if current.data == data:
#                 break
#             prev = current
#             current = current.next
        
#         if current is None:
#             return None
        
#         self.size -= 1
#         if prev is None:
#             self.head = current.next
#         else:
#             prev.next = current.next
#         return None

#     def __repr__(self):
#         string = []
#         node = self.head
#         while node is not None:
#             string.append(node.data)
#             node = node.next
#         return str(string)


#     @property
#     def size(self):
#         return self._size


#     @size.setter
#     def size(self, value):
#         self._size = value


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"node(data={self.data})"


class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    
    def __repr__(self):
        linkedlist = []
        node = self.head
        while node is not None:
            linkedlist.append(node.data)
            node = node.next
        return str(linkedlist)


    def append(self, data):
        node = Node(data)
        if not self.tail:
            self.head = node
            self.tail = node
            return None
        
        self.tail.next = node
        self.tail = node
        return None


    def search(self, data):
        if not self.tail:
            return None
        
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next
        return None


    def remove(self, data):
        if not self.head:
            return None
        
        if self.head.data == data:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
            return None

        prev = self.head
        current = self.head.next

        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = prev

                prev.next = current.next
                return None
            
            prev = current
            current = current.next
        
        return None

if __name__ == "__main__":
    linked_list = LinkedList()
    print(linked_list)

    linked_list.append(9)
    print(linked_list)
    print(linked_list.head)
    print(linked_list.tail)

    linked_list.append(11)
    linked_list.append(2)
    linked_list.append(98)
    linked_list.append(35)
    print(linked_list)
    print(linked_list.head)
    print(linked_list.tail)

    node = linked_list.search(98)
    print(node)

    linked_list.remove(2)
    linked_list.remove(9)
    linked_list.remove(35)
    print(linked_list)
    print(linked_list.head)
    print(linked_list.tail)



# if __name__ == "__main__":
#     linked_list = LinkedList()
#     print(linked_list)
#     print(linked_list.size)
#     print()

#     print(f'prepend 20 to the head:')
#     linked_list.prepend(20)
#     print(linked_list)
#     print(linked_list.size)
#     print()

#     print(f'append 30 to the tail:')
#     linked_list.append(30)
#     print(linked_list)
#     print(linked_list.size)
#     print()

#     print(f'insert 0 to the position 1:')
#     linked_list.insert(0, 1)
#     print(linked_list)
#     print(linked_list.size)
#     print()

#     print(f'insert 1 to the position 0:')
#     linked_list.insert(1, 0)
#     print(linked_list)
#     print(linked_list.size)
#     print()

#     print(f'insert 100 to the position 2:')
#     linked_list.insert(100, 2)
#     print(linked_list)
#     print(linked_list.size)
#     print()

#     print(f'append 200 to the tail:')
#     linked_list.append(200)
#     print(linked_list)
#     print(linked_list.size)
#     print()

#     print(f'prepend 300 to the head:')
#     linked_list.prepend(300)
#     print(linked_list)
#     print(linked_list.size)
#     print()

#     print(f'remove 10:')
#     linked_list.remove(10)
#     print(linked_list)
#     print(linked_list.size)
#     print()

#     print(f'remove 100:')
#     linked_list.remove(100)
#     print(linked_list)
#     print(linked_list.size)
#     print()



