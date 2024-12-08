
import requests



r = requests.get('https://www.google.com/', auth=('user', 'pass'))# направление запроса на сайт и плучение информации от сервера
print(r.status_code)# получение статуса запроса на сервер(200-299 успешно, 300-399 перенаправление, 400-499 ошибка обращения, 500 проблема на сайте
print(r.headers)#получение служебной информации по работе с сайтом
print(r.content)#получение страницы сайта в байтовом исполнении
print(r.text)#HTML код сайта
print(r.json)# встроенный декодер JSON на случай, если имеем дело с данными JSON
print(requests.post('https://www.google.com/', data={'key': 'value'}))#направление запроса в зашифрованном виде, для отправки логинов/паролей