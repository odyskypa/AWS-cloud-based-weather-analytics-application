import requests
import json
# Getting all coordinates of Spain provinces

# Replace {API key} with your actual API key

provinces = ['A Coruña', 'Vitoria-Gasteiz', 'Albacete', 'Alicante', 'Almería', 'Oviedo', 'Ávila', 'Badajoz', 'Barcelona', 'Burgos', 'Cáceres', 'Cádiz', 'Santander', 'Castellón de la Plana', 'Ciudad Real', 'Córdoba', 'Cuenca', 'Gerona', 'Granada', 'Guadalajara', 'San Sebastián', 'Huelva', 'Huesca', 'Palma de Mallorca', 'Jaén', 'Logroño', 'Las Palmas de Gran Canaria', 'León', 'Lérida', 'Lugo', 'Madrid', 'Málaga', 'Murcia', 'Pamplona', 'Orense', 'Palencia', 'Pontevedra', 'Salamanca', 'Santa Cruz de Tenerife', 'Segovia', 'Sevilla', 'Soria', 'Tarragona', 'Teruel', 'Toledo', 'Valencia', 'Valladolid', 'Bilbao', 'Zamora', 'Zaragoza']
print("\nNumber of provinces in Spain: ",len(provinces))
results = []
for province in provinces:
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={province}&limit=1&appid=08a8d302936096af9fd01832d92651df"
    response = requests.get(url)
    coordinates = response.json()
    results.append(coordinates)

with open('coordinates.json', 'w') as json_file:
    json.dump(results, json_file, ensure_ascii=False)


print('\nCoordinates of provinces in Spain are saved in coordinates.json file')
count = len(results)
print(f"There are {count} objects in the coordinates.json - refering to provinces")
print("\n")
