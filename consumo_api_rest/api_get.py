import requests

url = "https://jsonplaceholder.typicode.com/users"
respuesta = requests.get(url)

if respuesta.status_code == 200:
    usuarios = respuesta.json()
    for usuario in usuarios:
        print(
            f"ID: {usuario['id']}, Nombre: {usuario['name']}, Email: {usuario['email']}"
        )
else:
    print("Error al obtener usuarios")
