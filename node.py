"""Implementation of nodes."""


class BaseNode:
    """Base node class to extend."""

    def __init__(self, information=None) -> None:
        self.__information = information

    @property
    def information(self):
        """Getter for information property."""
        return self.__information

    # @information.setter
    # def information(self, information):
    #     """Setter of information property."""
    #     self.__information = information


class SimpleNode(BaseNode):
    """SimpleNode for queue implementation."""

    def __init__(self, information=None) -> None:
        super().__init__(information)
        self.__previous_node = None
        self.__next_node = None

    def __str__(self) -> str:
        return f"node information: {self.information}"

    def get_last(self, order=1):
        """Recursive funcion to get last node in the queue."""
        if self.__next_node is None:
            self.__next_node = None
            return self, order

        order += 1
        return self.__next_node.get_last(order)

    def add_first_node(self, node):
        """Add a node at the begining of the queue."""
        node.__next_node = self
        node.__previous_node = self.__previous_node
        self.__previous_node.__next_node = node
        self.__previous_node = node

    def add_last_node(self, node):
        """Add a node at the end of the queue."""
        if self.__next_node is None:
            node.__previous_node = self
            node.__next_node = None
            self.__next_node = node
            return

        return self.add_last_node(node)

    def add_information(self, information):
        """Add new node at the end with information attribute only."""
        if self.__next_node is None:
            new_node = SimpleNode(information)
            new_node.__previous_node = self
            self.__next_node = new_node
            return

        return self.__next_node.add_information(information)

    def take_first(self):
        """Returns the first node, and the next one."""
        self.__next_node.__previous_node = None
        return self, self.__next_node

    def take_last(self):
        """Returns the last node, and the previous one."""
        if self.__next_node is None:
            last_one = self
            self.__previous_node.__next_node = None
            return last_one

        return self.__next_node.take_last()

    def find_information(self, some_information: any, order=1):
        """Find the node with certain information.
        Returns referenced node, not modifying the queue."""
        if self.information == some_information:
            return self, order

        order += 1

        if self.__next_node is None:
            return None, -1

        return self.__next_node.find_information(some_information, order)

    def find_node(self, some_node):
        """Find certain node in the queue."""
        if self == some_node:
            return self

        return self.__next_node.find_node(some_node)

    def quantity(self) -> int:
        """Return the quantity of nodes linked to it."""
        return self.__hidden_quantity()

    def __hidden_quantity(self, order=1) -> int:
        """Hidden method for count elements."""
        if self.__next_node is None:
            return order

        order += 1
        return self.__next_node.__hidden_quantity(order)


if __name__ == "__main__":
    node = SimpleNode("ola")
    print(node)
