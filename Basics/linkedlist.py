class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


## method : insert(data), delete(index), get_list()


class linked_list:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def insert(self, data):
        new_node = node(data)
        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete(self, index=0):
        if index == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        elif index == 1:
            self.head.next = None
            self.tail = self.head
        else:
            curruent = self.head
            count = 0
            while count != index - 1:
                curruent = curruent.next
                count += 1

            curruent.next = curruent.next.next
            if curruent.next == None:
                self.tail = curruent

    def get_list(self):
        elems = []
        if self.tail != None:
            current = self.head
            elems.append(current.data)
            while current != self.tail:
                current = current.next
                elems.append(current.data)
        return elems


m_l = linked_list()
m_l.insert(1)
m_l.insert(2)
m_l.insert(3)

print(m_l.get_list())

m_l.delete(0)
print(m_l.get_list())
m_l.delete(0)
print(m_l.get_list())
m_l.delete(0)
print(m_l.get_list())
