import datetime as dt

import requests

USER_NAME = "robinburri"
TOKEN = "fhsaj324lfsa34235df"

pixela_endpoint = "https://pixe.la/v1/users"

headers = {"X-USER-TOKEN": TOKEN}

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# create user at pixela (use only once)
# response = requests.post(url=pixela_endpoint, json=user_params, timeout=5)
# delete a user
# response = requests.delete(url=f"{pixela_endpoint}/{USER_NAME}", timeout=5, headers=headers)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_params = {
    "id": "first-graph",
    "name": "workout",
    "unit": "workouts",
    "type": "int",
    "color": "shibafu",
}

# create a graph
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers, timeout=5)
# delete a graph
# response = requests.delete(url=f"{graph_endpoint}/{graph_params['id']}", timeout=5, headers=headers)


update_endpoint = f"{graph_endpoint}/{graph_params['id']}"
update_params = {
    "name": "workout",
    "unit": "workouts",
}

# update a graph
response = requests.put(
    url=update_endpoint,
    json=update_params,
    headers=headers,
    timeout=5,
)

# post a pixel
pixel_endpoint = f"{graph_endpoint}/{graph_params['id']}"
pixel_params = {
    "date": dt.datetime.today().strftime("%Y%m%d"),
    "quantity": "1",
}
# response = requests.post(url=pixel_endpoint, json=pixel_params, timeout=5, headers=headers)

# update the main page

update_page_params = {
    "displayName": "Robin Burri",
    "pinnedGraphID": graph_params["id"],
}
response = requests.put(
    url=f"https://pixe.la/@{USER_NAME}",
    timeout=15,
    headers=headers,
    json=update_page_params,
)
print(response.text)
