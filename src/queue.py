"""Queue implementation with linked list."""

from src.node import SimpleNode


class SimpleQueue:
    """Queue of same items."""

    def __init__(self) -> None:
        self.__first_node = None
        self.__quantity = 0

    @property
    def quantity(self):
        """Property of items counting."""
        self.__quantity = self.__first_node.quantity()

        return self.__quantity

    def add(self, information):
        """Add a new item to the end of the queue."""
        if self.__first_node is None:
            self.__first_node = SimpleNode(information)
            return

        self.__first_node.add_information(information)
        self.__quantity += 1

    def show_last(self):
        """Show the last item of the queue, no altering items."""
        node, self.__quantity = self.__first_node.get_last()
        return f"{node} {self.__quantity}"

    def show_first(self):
        """Show the first item of the queue, no altenering items."""
        return f"{self.__first_node}"

    def take(self):
        """Returns the information of first node of queue."""
        if self.__first_node is None:
            return None
        __first_node, self.__first_node = self.__first_node.take_first()
        self.__quantity -= 1
        return __first_node.information

    def find(self, information):
        """Find information in the queue. Returns information and order
        if exists. Else None, 0."""
        if self.__first_node is None:
            return None, 0

        found, order = self.__first_node.find_information(information)

        if found is None:
            return None, order

        return found.information, order

    def give_all(self):
        """Return and array with all items."""
        return self.__first_node.get_all_items()

    def insert_array_at_end(self, items):
        """Add all array's items at the end of the queue."""
        return self.__first_node.add_array_at_end(items)


if __name__ == "__main__":
    queue = SimpleQueue()
    queue.add("oli")
    queue.add("olo")
    queue.add("ole")

    print("first:", queue.show_first())
    print("last:", queue.show_last())
    # print("found:", queue.find("olo"))
    print("quantity:", queue.quantity)

    items = [1, 2, 3, 4, 5, 6]
    queue.insert_array_at_end(items)

    itms = queue.give_all()
    print(itms)
