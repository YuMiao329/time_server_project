import requests

server_name = "http://127.0.0.1:5000"

r = requests.get(server_name + "/time")
print(r.text)

r = requests.get(server_name + "/date")
print(r.text)

out_data = {"date": "10/10/1999", "units": "years"}
l = requests.post(server_name + "/age", json=out_data)
print(l.text)

#r = requests.get(server_name + "/until_next_meal")
#print(r.text)

