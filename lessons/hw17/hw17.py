import requests


base_url = "https://petstore.swagger.io/v2/pet"
pet_id = 123456789

pet_data = {
    "id": pet_id,
    "name": "Barsik",
    "photoUrls": [
        "https://upload.wikimedia.org/wikipedia/commons/f/f2/Cat_image.jpg"
    ],
    "status": "available"
}


# POST
post_response = requests.post(base_url, json=pet_data)

print("POST")
print(post_response.status_code)
print(post_response.json())


# GET
get_response = requests.get(f"{base_url}/{pet_id}")

print("GET")
print(get_response.status_code)
print(get_response.json())


# PUT
updated_pet_data = {
    "id": pet_id,
    "name": "Barsik Updated",
    "photoUrls": [
        "https://upload.wikimedia.org/wikipedia/commons/f/f2/Cat_image.jpg"
    ],
    "status": "sold"
}

put_response = requests.put(base_url, json=updated_pet_data)

print("PUT")
print(put_response.status_code)
print(put_response.json())


# DELETE
delete_response = requests.delete(f"{base_url}/{pet_id}")

print("DELETE")
print(delete_response.status_code)
print(delete_response.text)