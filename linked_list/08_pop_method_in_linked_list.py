class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ""

        while temp_node is not None:
            result += str(temp_node.value)

            if temp_node.next is not None:
                result += " -> "

            temp_node = temp_node.next

        return result

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)

        if index < 0 or index > self.length:
            return False
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head

            for _ in range(index - 1):
                temp_node = temp_node.next

            new_node.next = temp_node.next
            temp_node.next = new_node

        self.length += 1
        return True

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def search(self, target):
        """Returns True if it finds the target value or false if it does not find the target value"""

        current = self.head

        while current is not None:
            if current.value == target:
                return True

            current = current.next

        return False

    def search_index(self, target):
        """Returns the index of the target value"""

        current = self.head

        index = 0

        while current is not None:
            if current.value == target:
                return index

            current = current.next
            index += 1

        return -1

    def get(self, index):
        """Returns the value of the node on the provided index"""
        if index == -1:
            return self.tail.value

        if index < -1 or index >= self.length:
            return None

        current = self.head

        for _ in range(index):
            current = current.next
        return current.value

    def get_v2(self, index):
        if index == -1:
            return self.tail.value

        if index < -1 or index >= self.length:
            return None

        current = self.head

        for _ in range(index):
            current = current.next
        return current

    def set_value(self, index, value):
        """This method changes the value of a node of a given index. Then returns True if successfully works or False
         if it does not work."""

        temp = self.get_v2(index)

        if temp is not None:
            temp.value = value
            return True

        return False

    def pop_first(self):
        """This method delete the first node of a Linked List and returns it."""

        if self.length == 0:
            return None

        popped_node = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None

        self.length -= 1
        return popped_node.value

    def pop_last(self):
        """This method delete the last node of a Linked List and returns it."""

        if self.length == 0:
            return None

        popped_node = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_node.value


new_linked_list = LinkedList()

new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)

print(new_linked_list)
print(new_linked_list.pop_last())
print(new_linked_list)

