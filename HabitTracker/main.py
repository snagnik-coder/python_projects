import requests
from datetime import datetime as dt

hours_today = 3

TOKEN = "ljkbdsvkfwygo3yvoljbpe6"
pix_endpoint = "https://pixe.la/v1/users"

# parameters = {
#     "token": TOKEN,
#     "username": "snagnik",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(url = pix_endpoint, json = parameters)
# print(response.text)

graph_endpoint = f"{pix_endpoint}/snagnik/graphs"

graph_config = {
    "id": "graph1",
    "name": "Work",
    "unit": "hours",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url = graph_endpoint, json = graph_config, headers = headers)

pixel_create_end = f"{pix_endpoint}/snagnik/graphs/graph1"

today = dt.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": str(hours_today),
}

response = requests.post(url = pixel_create_end, json = pixel_data, headers = headers)
print(response.text)