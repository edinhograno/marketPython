class Product:
    def __init__(self, name, size, weight, price, description):
        self.__name = name
        self.__size = size
        self.__weight = weight
        self.__price = price
        self.__description = description

    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def get_weight(self):
        return self.__weight

    def get_price(self):
        return self.__price

    def get_description(self):
        return self.__description

    def set_name(self, name):
        self.__name = name

    def set_size(self, size):
        self.__size = size

    def set_weight(self, weight):
        self.__weight = weight

    def set_price(self, price):
        self.__price = price

    def set_description(self, description):
        self.__description = description   