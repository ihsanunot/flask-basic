import requests

mydata = {
   "nama" : "Ayana"
}

req = requests.post('http://127.0.0.1:5000/cobarequest/', data=mydata)

print(req.text)