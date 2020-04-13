from urllib import request
import json

content = request.urlopen("https://jsonblob.com/api/53f3a330-7d90-11ea-9563-fdc45b5abb31").read()
dictionary = json.loads(content.decode())
print(dictionary)
print(dictionary["data"][0]["hobbies"])