import requests

task = {"id": "vivek_1", "title": "vivek_post"}
resp = requests.post('https://jsonplaceholder.typicode.com/posts', json=task)
# if resp.status_code != 200:
#     raise ApiError('POST /tasks/ {}'.format(resp.status_code))
# print('Created task. ID: {}'.format(resp.json()["id"]))
print(resp.json())
res=requests.get("https://jsonplaceholder.typicode.com/posts")
for todo_item in res.json():
    print('{} {}'.format(todo_item['id'], todo_item['title']))