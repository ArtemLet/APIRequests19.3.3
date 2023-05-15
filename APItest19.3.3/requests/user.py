import requests

base_url = 'https://petstore.swagger.io/v2'
headers = {'accept': 'application/json', 'Content-Type' : 'application/json'}
users = [
  {
    "id": 0,
    "username": "Василий",
    "firstName": "Вася",
    "lastName": "Васильев",
    "email": "asda@asd.as",
    "password": "123123",
    "phone": "111",
    "userStatus": 0
  },
    {
    "id": 0,
    "username": "Петруша",
    "firstName": "петя",
    "lastName": "петров",
    "email": "asda1@asd.as",
    "password": "123123",
    "phone": "222",
    "userStatus": 0
  }
]
username = 'Петруша'

# Создать список пользователей
res_create_listOfUsers = requests.post(f'{base_url}/user/createWithList', headers=headers, json=users)
print(res_create_listOfUsers.text)

# Создать пользователя
res_create_user = requests.post(f'{base_url}/user', headers=headers, json = {
    "id": 0,
    "username": "Василий",
    "firstName": "GG",
    "lastName": "WP",
    "email": "asda@asd.as",
    "password": "123123",
    "phone": "111",
    "userStatus": 0
  })
print(res_create_user.text)

# Получить пользователя по имени
res_get_user = requests.get(f'{base_url}/user/{username}', headers=headers)
print(res_get_user.text)

# Обновить даныне пользователя
res_upd_user = requests.put(f'{base_url}/user/{username}', headers=headers, json={
    "id": 0,
    "username": "Василий",
    "firstName": "GG",
    "lastName": "WP",
    "email": "asda@asd.as",
    "password": "123123",
    "phone": "111",
    "userStatus": 0
  })
print(res_upd_user.text)

# Удалить пользователя
res_del_user = requests.delete(f'{base_url}/user/{username}', headers=headers)
print(res_del_user.status_code)

# Логин
res_login = requests.get(f'{base_url}/user/login?username=test&password=abc123', headers=headers)
print(res_login.text)

# Логаут
res_logout = requests.get(f'{base_url}/user/logout', headers=headers)
print(res_logout.text)

