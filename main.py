from classes import TemperatureSensor, PressureSensor
from utils import generate_random_float

hash_table = {}

for _ in range(3):
    read_value = generate_random_float()
    temperature_sensor = TemperatureSensor(read_value)
    temperature_key = f"{temperature_sensor.id}-{temperature_sensor.read_at}"
    hash_table[temperature_key] = temperature_sensor.read_value

print(hash_table)