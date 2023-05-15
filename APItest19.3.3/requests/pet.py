import requests

base_url = 'https://petstore.swagger.io/v2'
headers = {'accept': 'application/json'}
status = 'available'
pet_id = '520'
data = {'name' : 'GOSHA', 'status' : 'available'}
pet = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "bobik",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

# Поиск питомца по ID
res_find_byID = requests.get(f"{base_url}/pet/{pet_id}", headers = headers)
print(res_find_byID.text)

# Обновление имени и статуса питомца по ID
res_upd_pet = requests.post(f"{base_url}/pet/{pet_id}", headers = {'accept': 'application/json', "Content-Type" : "application/x-www-form-urlencoded"}, data = data)
print(res_upd_pet.text)

# Обновление питомца
res_update_pet = requests.put(f"{base_url}/pet", headers={'accept': 'application/json', 'Content-Type': 'application/json'}, json = pet)
print(res_update_pet.text)

# Добавление питомца
res_add_pet = requests.post(f"{base_url}/pet", headers = {'accept': 'application/json', "Content-Type": "application/json"}, json = pet)
print(res_add_pet.text)

# Поиск питомцев по статусу
res_pet_findByStatus = requests.get(f"{base_url}/pet/findByStatus?status={status}", headers = headers)
print(res_pet_findByStatus.text)

# Удалить питомца
res_delete = requests.delete(f'{base_url}/pet/9223372036854758097', headers={'accept': 'application/json', 'api_key': '123'})
print(res_delete.status_code)
