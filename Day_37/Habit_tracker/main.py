import requests
from datetime import datetime

pixela_endpoint="https://pixe.la/v1/users"

USERNAME="nazeemkhan"
TOKEN="habittrackerDay37project"
GRAPH_ID="graph1"
today=datetime.now()

user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response=requests.post(url=pixela_endpoint,json=user_params)
# response.raise_for_status()
# print(response.text)

# Create Graph
graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config={
    
    "id":GRAPH_ID,
    "name":"Coding Graph",
    "unit":"commit",
    "type":"int",
    "color":"ajisai"
}

headers={
    "X-USER-TOKEN":TOKEN,
}


# call post method to make the request
# this step is created.
# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response)
# response.raise_for_status()
# print(response.text)

pixela_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity": "10",

} 
response=requests.post(url=pixela_creation_endpoint,json=pixel_data,headers=headers)
response.raise_for_status() 
print(response.text) 

# # Deleting pixel
# pixela_delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20220807"
# deleteparams={


# }
# header={
#     "X-USER-TOKEN":TOKEN,
# }
# response=requests.delete(url=pixela_delete_endpoint,headers=header)
# response.raise_for_status()
# print(response.text)