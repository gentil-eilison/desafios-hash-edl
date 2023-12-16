from classes import BaseHashMapManager


class Component:
    STATUS = {
        "FAULTY": -1,
        "WORKING": 1,
        "OFF": 0
    }

    def __init__(self, id: int, location: str, current_status: int) -> None:
        self.__id = id
        self.__current_status = current_status
        self.__processes_history = []
        self.__location = location

    @property
    def location(self) -> str:
        return self.__location
    
    @location.setter
    def location(self, new_location) -> None:
        self.__location = new_location

    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def current_status(self) -> int:
        return self.__current_status
    
    @current_status.setter
    def current_status(self, new_current_status: int):
        self.__current_status = new_current_status

    @property
    def processes_history(self) -> list[str]:
        return self.__processes_history

    @processes_history.setter
    def processes_history(self, new_history: list[str]) -> None:
        self.__processes_history = new_history
    
    def __str__(self):
        return f"{self.id} - Component - Status: {self.current_status}"
    
    def __repr__(self):
        return f"{self.id} - Component - Status: {self.current_status}"
    

class ProductionLine(BaseHashMapManager):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name


first_component = Component(1, "Sector A", Component.STATUS["OFF"])
second_component = Component(2, "Sector B", Component.STATUS["WORKING"])
third_component = Component(3, "Sector C", Component.STATUS["FAULTY"])

second_component.processes_history.append("Creation of base material for later use")
third_component.processes_history.append("Warm metal plate for bolt production")
third_component.processes_history.append("Overheat")

production_line = ProductionLine("Playstation 5")
production_line.add_item(first_component.id, first_component)
production_line.add_item(second_component.id, second_component)
production_line.add_item(third_component.id, third_component)

print(production_line.find_item(2))
print(third_component.processes_history)
production_line.update_item(third_component.id, current_status=Component.STATUS["WORKING"], location="Sector C", processes_history="A new line")
print(production_line.find_item(third_component.id))
print(production_line.find_item(third_component.id).processes_history)
