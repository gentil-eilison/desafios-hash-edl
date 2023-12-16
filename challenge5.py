import datetime

from classes import BaseHashMapManager


class Product:
    ORDER_STATUS = {
        "PUT_AWAY": 0,
        "SENT": 1,
        "DELIVERY_ERROR": 2,
        "DELIVERED": 3
    }

    def __init__(self, production_order_number: int, order_status: int, details: str, delivery_time: datetime.datetime):
        self.__production_order_number = production_order_number
        self.__order_status = order_status
        self.__details = details
        self.__delivery_time = delivery_time

    @property
    def production_order_number(self) -> int:
        return self.__production_order_number

    @production_order_number.setter
    def production_order_number(self, value)  -> None:
        self.__production_order_number = value

    @property
    def order_status(self)  -> int:
        return self.__order_status

    @order_status.setter
    def order_status(self, value)  -> None:
        self.__order_status = value

    @property
    def details(self)  -> str:
        return self.__details

    @details.setter
    def details(self, value) -> None:
        self.__details = value

    @property
    def delivery_time(self)  -> datetime.datetime:
        return self.__delivery_time

    @delivery_time.setter
    def delivery_time(self, value) -> None:
        self.__delivery_time = value


class ProductionOrders(BaseHashMapManager):
    def __init__(self, company_name: str) -> None:
        super().__init__()
        self.__company_name = company_name

    @property
    def company_name(self) -> str:
        return self.__company_name

    @company_name.setter
    def company_name(self, value) -> None:
        self.__company_name = value


production_orders = ProductionOrders(company_name="Amazon")
kindle = Product(production_order_number=12, order_status=Product.ORDER_STATUS["SENT"], details="Paperwhite Kindle", delivery_time=datetime.timedelta(days=18))
alexa = Product(production_order_number=24, order_status=Product.ORDER_STATUS["DELIVERED"], details="Alexa version 3", delivery_time=datetime.timedelta(days=10))

production_orders.add_item(kindle.production_order_number, kindle)
production_orders.add_item(alexa.production_order_number, alexa)

print(production_orders.find_item(kindle.production_order_number).details)
print(production_orders.find_item(alexa.production_order_number).details)
production_orders.update_item(alexa.production_order_number, order_status=Product.ORDER_STATUS["DELIVERY_ERROR"], delivery_time=datetime.timedelta(days=50))
print("-------------------------- AFTER UPDATE -------------------------")
print(production_orders.find_item(alexa.production_order_number).details)
print(production_orders.find_item(alexa.production_order_number).order_status)
print(production_orders.find_item(alexa.production_order_number).delivery_time.days)