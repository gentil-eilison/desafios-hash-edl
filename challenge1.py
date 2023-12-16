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
    
    def __str__(self):
        return f"{self.id} - Component - Status: {self.current_status}"
    
    def __repr__(self):
        return f"{self.id} - Component - Status: {self.current_status}"
    

class ProductionLine:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__components_table = {}

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name

    def add_component(self, component: Component) -> None:
        self.__components_table[component.id] = component

    def find_component(self, id: int) -> Component:
        try:
            return self.__components_table[id]
        except KeyError:
            return None

    def update_component(self, id: int, new_status: int, new_location: str, new_process: str) -> bool:
        component = self.find_component(id)
        if component:
            component.current_status = new_status
            component.location = new_location
            component.processes_history.append(new_process)
            return True
        else:
            return False



first_component = Component(1, "Sector A", Component.STATUS["OFF"])
second_component = Component(2, "Sector B", Component.STATUS["WORKING"])
third_component = Component(3, "Sector C", Component.STATUS["FAULTY"])

second_component.processes_history.append("Creation of base material for later use")
third_component.processes_history.append("Warm metal plate for bolt production")
third_component.processes_history.append("Overheat")

production_line = ProductionLine("Playstation 5")
production_line.add_component(first_component)
production_line.add_component(second_component)
production_line.add_component(third_component)

print(production_line.find_component(2))
production_line.update_component(third_component.id, Component.STATUS["WORKING"], "Sector C", "Gamepad button production")
print(production_line.find_component(third_component.id))
