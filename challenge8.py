from classes import BaseHashMapManager


class Review:
    def __init__(self, client_name: str, text: str):
        self.__client_name = client_name
        self.__text = text

    @property
    def client_name(self):
        return self.__client_name

    @client_name.setter
    def client_name(self, value):
        self.__client_name = value

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value

    def __repr__(self) -> str:
        return f"{self.client_name} - {self.text}"


class Category:
    DEMAND = {
        "HIGH": 1,
        "LOW": 0
    }

    def __init__(self, id: int, name: str, increase_in_sales: float, demand: int, client_reviews: list[Review]):
        self.__id = id
        self.__name = name
        self.__increase_in_sales = increase_in_sales
        self.__demand = demand
        self.__client_reviews = client_reviews

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def increase_in_sales(self):
        return self.__increase_in_sales

    @increase_in_sales.setter
    def increase_in_sales(self, value):
        self.__increase_in_sales = value

    @property
    def demand(self):
        return self.__demand

    @demand.setter
    def demand(self, value):
        self.__demand = value

    @property
    def client_reviews(self):
        return self.__client_reviews

    @client_reviews.setter
    def client_reviews(self, value):
        self.__client_reviews = value


review = Review("Alyson", "Very good")
review_two = Review("Kadson", "I don't like it that much")
review_three = Review("Karla", "So much to see, pretty good")

gaming = Category(1, "Gaming", increase_in_sales=50, demand=Category.DEMAND["HIGH"], client_reviews=[review, review_two])
clothing = Category(2, "Clothing", increase_in_sales=80, demand=Category.DEMAND["LOW"], client_reviews=[review_three])

market_tendency_map = BaseHashMapManager()
market_tendency_map.add_item(gaming.id, gaming)
market_tendency_map.add_item(clothing.id, clothing)

new_review = Review("Carlos", "Very good, first time wearing it and I already like it")
print(market_tendency_map.find_item(clothing.id).client_reviews)
market_tendency_map.update_item(clothing.id, client_reviews=new_review)
print(market_tendency_map.find_item(clothing.id).client_reviews)
