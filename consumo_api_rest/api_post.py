import requests


def crear_post(titulo, contenido):
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {"title": titulo, "body": contenido, "userId": 1}

    respuesta = requests.post(url, json=payload)

    if respuesta.status_code == 201:
        print("Creado exitosamente:")
        print(respuesta.json())
    else:
        print(f"Error: {respuesta.status_code}")


crear_post("Mi primer post", "Este es el contenido del ejercicio")
