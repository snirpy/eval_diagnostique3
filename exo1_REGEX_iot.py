import re

iot_frame = "SensorID:123;Temperature:25.5;Humidity:60.2;Status:OK"

# Expressions régulières
sensor_id_pattern = re.compile(r'SensorID:(\d+);')
temperature_pattern = re.compile(r'Temperature:([\d.]+);')
humidity_pattern = re.compile(r'Humidity:([\d.]+);')
status_pattern = re.compile(r'Status:(\w+)$')

# Application des expressions régulières à la trame
sensor_id_match = sensor_id_pattern.search(iot_frame)
temperature_match = temperature_pattern.search(iot_frame)
humidity_match = humidity_pattern.search(iot_frame)
status_match = status_pattern.search(iot_frame)

# Affichage des informations extraites
if sensor_id_match:
    sensor_id = sensor_id_match.group(1)
    print(f"Identifiant du capteur: {sensor_id}")

if temperature_match:
    temperature = temperature_match.group(1)
    print(f"Température: {temperature} °C")

if humidity_match:
    humidity = humidity_match.group(1)
    print(f"Humidité: {humidity}%")

if status_match:
    status = status_match.group(1)
    print(f"Statut: {status}")
