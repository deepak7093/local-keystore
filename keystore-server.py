
#!/usr/bin/env python3

import json
from time import sleep
import sys
from flask import Flask, render_template, request
# import requests


app = Flask(__name__)
@app.route('/')
def base():
    for item in request.args:
        # print(item)
        print("Welcome to KeyStore")
    return "200OK"

@app.route('/getKey', methods=['GET'])
def getKeyValue():
    print(request.json)
    key =  request.json['key']
    # print("key=", request.json)
    ks = KeyStore(key)
    response = ks.getKey()
    print(response)
    return response

@app.route('/setKey', methods=['POST'])
def setKeyValue():
    print()
    key = request.json['key']
    value = request.json['value']
    ks = KeyStore(key, value)
    response = ks.setKey()
    return response

@app.route('/watchKey')
def watchKeyValue():
    key = request.json['key']
    ks = KeyStore(key)
    response = ks.watchKey()
    return response


class KeyStore:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value

    def getKey(self):
        with open('./keys.json', 'r') as f:
            json_data = json.load(f)
        # print(json_data.keys())
        if self.key in json_data.keys():
            return json_data[self.key]
        else:
            return "404: Key {} Not Found".format(self.key)

    def setKey(self):
        with open('./keys.json', 'r') as f:
            json_data = json.load(f)
        print(json_data.keys())
        if self.key in json_data.keys():
            print("Overwriting key {} with value: {} ".format(self.key, self.value))
            json_data[self.key] = self.value
        else:
            print("Creating new Key {} with value".format(self.key, self.value))
            json_data[self.key] = self.value
        print(json_data)
        with open('./keys.json', 'w') as f:
            json.dump(json_data, f)
        return "Success"

    def watchKey(self):
        timer = 0
        with open('./keys.json', 'r') as f:
            json_data = json.load(f)
        if self.key in json_data.keys():
            while True:
                # print("Watching on key {} since {}sec".format(self.key, timer))
                current_value = json_data[self.key]

                with open('./keys.json', 'r') as f:
                    new_json_data = json.load(f)

                new_value = new_json_data[self.key]
                if self.key in new_json_data.keys():
                    if current_value == new_value:
                        pass
                    else:
                        print(new_value)
                        with open('./keys.json', 'w') as f:
                            json.dump(json_data, f)
                        return new_value
                timer = timer+1
                sleep(1)
                
        else:
            return "Key {} Not Found".format(self.key)







if __name__ == '__main__':
    
    app.run(debug=True,host='0.0.0.0')
    



            