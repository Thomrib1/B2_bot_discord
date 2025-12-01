class CommandNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CommandLinkedList:
    def __init__(self):
        self.head = None

    def add(self, command):
        new_node = CommandNode(command)
        new_node.next = self.head
        self.head = new_node

    def get_last(self):
        if self.head:
            return self.head.data
        return "Aucun historique."

    def get_all(self):
        if not self.head:
            return "Historique vide."
        
        current = self.head
        result = ""
        while current:
            result += f"- {current.data}\n"
            current = current.next
        return result

    def clear(self):

        self.head = None