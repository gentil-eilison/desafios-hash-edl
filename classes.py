import datetime
from abc import ABC
from uuid import uuid4


class Sensor(ABC):
    def __init__(self, read_value: float):
        self.__id = self.generate_sensor_id()
        self.__read_value = read_value
        self.__read_at = datetime.datetime.now().time()

    @property
    def read_value(self) -> float:
        return self.__read_value
    
    @read_value.setter
    def read_value(self, new_value: float) -> None:
        self.__read_value = new_value

    @property
    def read_at(self) -> datetime.time:
        return self.__read_at
    
    @read_at.setter
    def read_at(self, new_read_at: datetime.time) -> None:
        self.__read_at = new_read_at
    
    @property
    def id(self) -> str:
        return self.__id
    
    def generate_sensor_id(self):
        pass

    def print_info(self):
        pass

    def read_new_value(self, value: float) -> None:
        read_at = datetime.datetime.now().time()
        self.__read_value = value
        self.__read_at = read_at

    def get_formatted_read_at(self) -> str:
        # Converts datetime.time object to str representation in format 23:59:59
        return self.__read_at.strftime("%H:%M:%S")


class TemperatureSensor(Sensor):
    UNIT_OF_MEASUREMENT = "ºC"
    ID_PARTIAL = "temperature"

    def __init__(self, read_value: float):
        super().__init__(read_value)
    
    def generate_sensor_id(self):
        return self.ID_PARTIAL + "-" + uuid4().hex
    
    def print_info(self):
        print(f"{self.ID_PARTIAL} sensor read value {self.read_value} {self.UNIT_OF_MEASUREMENT} at {self.get_formatted_read_at()}")
    

class PressureSensor(Sensor):
    UNIT_OF_MEASUREMENT = "Pa"
    ID_PARTIAL = "pressure"

    def __init__(self, read_value: float):
        super().__init__(read_value)

    def print_info(self):
        print(f"{self.ID_PARTIAL} sensor read value {self.read_value} {self.UNIT_OF_MEASUREMENT} at {self.get_formatted_read_at()}")
    
    def generate_sensor_id(self):
        return self.ID_PARTIAL + "-" + uuid4().hex


class BaseHashMapManager:
    def __init__(self):
        self.__items_hash_map = {}
    
    def add_item(self, id, item):
        self.__items_hash_map[id] = item
    
    def find_item(self, id):
        try:
            return self.__items_hash_map[id]
        except KeyError:
            return None
    
    def update_item(self, id, **kwargs):
        item = self.find_item(id)
        if item:
            for key, value in kwargs.items():
                if hasattr(item, key):
                    if isinstance(getattr(item, key), list):
                        new_list = getattr(item, key).copy()
                        new_list.append(value)
                        setattr(item, key, new_list)
                    else:
                        setattr(item, key, value)
            return True
        return False
