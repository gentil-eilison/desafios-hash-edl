class Sensor:
    def __init__(self, id: int, read_value: float) -> None:
        self.__id = id
        self.__read_value = read_value

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def _id(self, value) -> None:
        self.__id = value

    @property
    def read_value(self) -> float:
        return self.__read_value

    @read_value.setter
    def read_value(self, value) -> None:
        self.__read_value = value

    def __str__(self) -> str:
        return f"Sensor ID: {self.id} - {self.read_value}"


class SensorsSet:
    def __init__(self):
        self.__sensors_set = {}

    def add_sensor(self, sensor: Sensor) -> None:
        self.__sensors_set[sensor.id] = sensor

    def find_sensor(self, id: int) -> Sensor|None:
        try:
            return self.__sensors_set[id]
        except KeyError:
            return None
    
    def update_sensor(self, id: int, new_read_value: float) -> bool:
        sensor = self.find_sensor(id)
        if sensor:
            sensor.read_value = new_read_value
            return True
        return False


sensor_one = Sensor(1, 35.6)
sensor_two = Sensor(2, 59.3)
sensor_three = Sensor(3, 12.0)
sensor_set = SensorsSet()

print(sensor_set.find_sensor(4))
sensor_set.add_sensor(sensor_one)
sensor_set.add_sensor(sensor_two)
sensor_set.add_sensor(sensor_three)
print(sensor_set.find_sensor(3))
print(sensor_set.update_sensor(2, 60))
print(sensor_set.find_sensor(2))