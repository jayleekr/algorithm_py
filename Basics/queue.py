class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


#
# FIFO
# position : head, tail
# method : insert, delete, get_list


class queue:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def insert(self, data):
        new_node = node(data)
        if self.tail == None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def delete(self):
        if self.head == None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

    def get_list(self):
        elems = []
        if self.tail != None:
            current = self.head
            elems.append(current.data)
            while current != self.tail:
                current = current.next
                elems.append(current.data)

        return elems


my_queue = queue()
my_queue.insert("이재원")
my_queue.insert("이현호")
my_queue.insert("원승재")

print(my_queue.get_list())
my_queue.delete()
print(my_queue.get_list())
