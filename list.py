from node import Node


class List:
    def __init__(self):
        self.head = None
        self.__size = 0

    def append(self, product):
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(product)
        else:
            self.head = Node(product)
        self.__size = self.__size + 1

    def __len__(self):
        return self.__size

    def remove(self, product):
        if self.head == None:
            raise ValueError(f"{product} has not found")
        elif self.head.product == product:
            self.head = self.head.next
            self.__size = self.__size - 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.product == product:
                    ancestor.next = pointer.next
                    pointer.next = None
                    self.__size = self.__size - 1
                    return True
                ancestor = pointer
                pointer = pointer.next
        raise ValueError(f"{product} has not found")

    def print(self):
        if self.head:
            pointer = self.head
            print("List of Market:")
            while(pointer):
                print(
                    f"    {pointer.product.get_name().ljust(12)} - {pointer.product.get_description()}")
                pointer = pointer.next
            print("End of List")
        else:
            raise ValueError(f"Emply List")
