class Provider:
    def __init__(self, code: int, name: str) -> None:
        self.__name = name
        self.__code = code

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name
    
    @property
    def code(self) -> int:
        return self.__code
    
    @code.setter
    def code(self, new_code: int) -> None:
        self.__code = new_code


class Item:
    def __init__(self, code: int, in_stock_amount: int, location: str, provider: Provider) -> None:
        self.__code = code
        self.__in_stock_amount = in_stock_amount
        self.__location = location
        self.__provider = provider

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value):
        self.__code = value

    @property
    def in_stock_amount(self):
        return self.__in_stock_amount

    @in_stock_amount.setter
    def in_stock_amount(self, value):
        self.__in_stock_amount = value

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        self.__location = value

    @property
    def provider(self):
        return self.__provider

    @provider.setter
    def provider(self, value):
        self.__provider = value
    
    def __repr__(self) -> str:
        return f"{self.code} - {self.in_stock_amount} in stock from {self.provider.name} provider in {self.location}"


class Inventory:
    def __init__(self) -> None:
        self.__inventory_items = {}

    def add_item(self, item: Item):
        self.__inventory_items[item.code] = item

    def find_item(self, code: int) -> Item:
        try:
            return self.__inventory_items[code]
        except KeyError:
            return None

    def update_item(self, code: int, in_stock_amount: int, location: str, provider: Provider) -> Item:
        item = self.find_item(code)
        if item:
            item.in_stock_amount = in_stock_amount
            item.location = location
            item.provider = provider
            return True
        return False


fornecedor_amazon = Provider(250, "Amazon")
fornecedor_americanas = Provider(300, "Americanas")
kindle = Item(340, 20, "Brazil", fornecedor_amazon)
alexa = Item(341, 200, "USA", fornecedor_amazon)
gamepad_ps4 = Item(203, 100, "Brazil", fornecedor_americanas)

invetory = Inventory()
invetory.add_item(kindle)
invetory.add_item(alexa)
invetory.add_item(gamepad_ps4)

print(invetory.find_item(341))
print(invetory.find_item(1000))  # None for it didn't found the item
print(invetory.update_item(341, 200, "Brazil", fornecedor_amazon))  # True because it sucessfully updated it
print(invetory.find_item(341))
