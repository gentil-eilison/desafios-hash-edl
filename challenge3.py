from classes import BaseHashMapManager


class Sensor:
    def __init__(self, id: int, read_value: float) -> None:
        self.__id = id
        self.__read_value = read_value

    @property
    def id(self) -> int:
        return self.__id

    @property
    def read_value(self) -> float:
        return self.__read_value

    @read_value.setter
    def read_value(self, value) -> None:
        self.__read_value = value

    def __str__(self) -> str:
        return f"Sensor ID: {self.id} - {self.read_value}"


class SensorsSet(BaseHashMapManager):
    pass


sensor_one = Sensor(1, 35.6)
sensor_two = Sensor(2, 59.3)
sensor_three = Sensor(3, 12.0)
sensor_set = SensorsSet()

print(sensor_set.find_item(4))
sensor_set.add_item(sensor_one.id, sensor_one)
sensor_set.add_item(sensor_two.id, sensor_two)
sensor_set.add_item(sensor_three.id, sensor_three)
print(sensor_set.find_item(3))
print(sensor_set.update_item(2, read_value=60))
print(sensor_set.find_item(2))