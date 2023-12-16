from classes import BaseHashMapManager


class Product:
    def __init__(self, id: int, crumpled_box: bool, sealed: bool, feedbacks: str) -> None:
        self.__id = id
        self.__crumpled_box = crumpled_box
        self.__sealed = sealed
        self.__feedbacks = feedbacks

    @property
    def id(self):
        return self.__id

    @property
    def crumpled_box(self):
        return self.__crumpled_box

    @crumpled_box.setter
    def crumpled_box(self, value):
        self.__crumpled_box = value

    @property
    def sealed(self):
        return self.__sealed

    @sealed.setter
    def sealed(self, value):
        self.__sealed = value

    @property
    def feedbacks(self):
        return self.__feedbacks

    @feedbacks.setter
    def feedbacks(self, value):
        self.__feedbacks = value


product_quality_manager = BaseHashMapManager()
lies_of_p = Product(id=1, crumpled_box=False, sealed=False, feedbacks="semi-new Lies of P for PS4")
life_is_but_a_dream = Product(id=1, crumpled_box=False, sealed=True, feedbacks="brand-new LIBAD disc from A7X")

product_quality_manager.add_item(lies_of_p.id, lies_of_p)
product_quality_manager.add_item(life_is_but_a_dream.id, life_is_but_a_dream)

print("Oh no! LIBAD case was violated... Updating")

product_quality_manager.update_item(life_is_but_a_dream.id, sealed=False, feedbacks="barely used LIBAD disc from A7X")
print(life_is_but_a_dream.sealed)
print(life_is_but_a_dream.feedbacks)
