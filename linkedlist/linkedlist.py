from .node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        return self.head is None

    def print_list(self):
        temp = self.head
        current_iterate = 0
        while temp is not None:
            current_iterate += 1
            print(current_iterate, temp.data)
            temp = temp.next_node

    def append(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
        self.length += 1
        return True

    def unshift(self, value):
        """
            This method add one node or element to the beginning
            of the list
            (this method is equivalent as prepend() method on the example)

            Params
            ----------

            value: any
                value for new node in the beginning

            Return
            ----------

            True: boolean
                this method always return true
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        self.length += 1
        return True

    def shift(self):
        """
            This method removes the first element from an array
            and returns that removed element
            (this method is equivalent as pop_first() method on the example)

            Return
            -----------

            temp: Node 
                removed element

            None: 
                when the length = 0
        """

        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next_node
        temp.next_node = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def pop(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next_node

    def get(self, index):
        """
            This method returns the element with the given index

            Params
            ________

            index: int
                the index of the element

            Return
            ___________

            temp: Node
                wanted element
            None(when the index is out of the range)
        """

        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next_node
        return temp

    def update(self, index, value):
        """
            This method update the value at given index
            (this method is equivalent as set_value() method on the example)

            Params
            _________

            index: int
                index of the value that want to be update
            value: any
                new value of the existing data at given index 

            Return 
            ---------

            boolean
                true when the node is updated and false when the data at the given index cannot be found
        """
        temp = self.get(index)
        if temp:
            temp.data = value
            return True

        return False

    def insert_of_index(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.unshift(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index - 1)

        new_node.next_node = temp.next_node
        temp.next_node = new_node

        self.length += 1
        return True

    def remove_at_index(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.shift()
        if index == self.length - 1:
            return self.pop()

        pre = self.get(index - 1)
        temp = pre.next_node
        pre.next_node = temp.next_node
        temp.next_node = None

        self.length -= 1
        return temp
