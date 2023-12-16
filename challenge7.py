from classes import BaseHashMapManager


class Shipment:
    DELIVERY_STATUS = {
        "DELIVERED": 1,
        "DELAYED": 2,
        "ON_STAND_BY": 3
    }

    def __init__(self, tracking_number: int, current_location: str, delivery_status: int, recipient_name: str) -> None:
        self.__tracking_number = tracking_number
        self.__current_location = current_location
        self.__delivery_status = delivery_status
        self.__recipient_name = recipient_name

    @property
    def tracking_number(self):
        return self.__tracking_number

    @property
    def current_location(self):
        return self.__current_location

    @current_location.setter
    def current_location(self, value):
        self.__current_location = value

    @property
    def delivery_status(self):
        return self.__delivery_status

    @delivery_status.setter
    def delivery_status(self, value):
        self.__delivery_status = value

    @property
    def recipient_name(self):
        return self.__recipient_name

    @recipient_name.setter
    def recipient_name(self, value):
        self.__recipient_name = value


shipment_one = Shipment(
    tracking_number=200,
    current_location="China",
    delivery_status=Shipment.DELIVERY_STATUS["ON_STAND_BY"],
    recipient_name="Kadson"
)
shipment_two = Shipment(
    tracking_number=320,
    current_location="Paris",
    delivery_status=Shipment.DELIVERY_STATUS["DELIVERED"],
    recipient_name="Carlos"
)
shipment_three = Shipment(
    tracking_number=400,
    current_location="Paris",
    delivery_status=Shipment.DELIVERY_STATUS["DELAYED"],
    recipient_name="Alyson"
)

shipment_tracking_map = BaseHashMapManager()
shipment_tracking_map.add_item(shipment_one.tracking_number, shipment_one)
shipment_tracking_map.add_item(shipment_two.tracking_number, shipment_two)
shipment_tracking_map.add_item(shipment_three.tracking_number, shipment_three)

shipment_tracking_map.update_item(shipment_one.tracking_number, delivery_status=Shipment.DELIVERY_STATUS["DELIVERED"])
print(shipment_tracking_map.find_item(shipment_one.tracking_number).delivery_status)
