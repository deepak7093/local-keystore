import requests
import sys

SERVER = "http://localhost:5000/"

def help():
    print(''' 
    Usgae: 
    - keystore get <key> 
    - keystore set <key> <value>
    - keystore watch <key>
        ''')
    exit(0)

if __name__ == '__main__':
    # ks = KeyStore("name", "3")
    if len(sys.argv) < 2:
        help()
    command_options = [ "get", "set", "watch" ]
    if sys.argv[1] in command_options:
        if sys.argv[1] == "get" and len(sys.argv) == 3:
            params = {'key': sys.argv[2]}
            response = requests.get(SERVER+'/getKey', json=params)
            print(str(response.content))
        elif sys.argv[1] == "set" and len(sys.argv) == 4:
            params = {'key': sys.argv[2], 'value': sys.argv[3]}
            response = requests.post(SERVER+'/setKey', json=params)
            print(str(response.content))
        elif sys.argv[1] == "watch" and len(sys.argv) == 3:
            params = {'key': sys.argv[2]}
            response = requests.get(SERVER+'/watchKey', json=params)
            print(str(response.content))
        else:
            help()
    else:
        help()
