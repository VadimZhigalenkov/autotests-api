#
#
import httpx
# """"""
# response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
# print(response.status_code)
# print(response.json())
# """"""
# data = {
#     "title": "Новая задача",
#     "completed": False,
#     "userid": 1
# }
#
# response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
# print(response.status_code)
# print(response.json())
# """"""
# # headers = {"Authorization": f"Bearer my_token"}
# # response = httpx.get("https://httpbin.org/get", headers=headers)
# # print(response.request.headers)
# # print(response.json())
# """"""
# # params = {"userid":1}
# # response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
# # print(response.url)
# # print(response.status_code)
# # print(response.json())
# """"""
# with httpx.Client() as client:
#
#     response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
#     response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
#     print(response1.status_code)
#     print(response1.json())
#     print(response2.status_code)
#     print(response2.json())
""""""
try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalidurl")
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f'Ошибка запроса {e}')

try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.Timeout as e:
    print("Запрос превысил лимит времени")
