class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


#
# FILO
# position : top, bottom
# method : push, pop, get_list


class stack:
    def __init__(self, node=None):
        self.top = node
        self.bottom = node

    def push(self, data):
        new_node = node(data)
        if self.top == None:
            self.top = new_node
            self.bottom = new_node
            return
        else:
            self.top.next = new_node
            self.top = new_node

    def pop(self):
        if self.top == None:
            return
        else:
            current = self.bottom
            while current != self.top:
                if current.next != self.top:
                    current = current.next
                else:
                    break
            self.top = current

    def get_list(self):
        elems = []
        if self.top != None:
            current = self.bottom
            elems.append(current.data)
            while current != self.top:
                current = current.next
                elems.append(current.data)
        return elems


my_stack = stack()
my_stack.push(1)
my_stack.push(3)
my_stack.push(5)

print(my_stack.get_list())

my_stack.pop()
print(my_stack.get_list())
