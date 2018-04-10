class node:
    def __init__(self):
        self.content = None
        self.next = None

class linked_list:
    def __init__(self):
        self.current_node = None

    def add_node(self, content):
        new_node = node()
        new_node.content = content
        new_node.next = self.current_node
        self.current_node = new_node

    def list_print(self):
        node = self.current_node
        while node:
            print node.content
            node = node.next

countdown = linked_list()
countdown.add_node("one")
countdown.add_node("two")
countdown.add_node("three")
countdown.add_node("four")

countdown.list_print()

