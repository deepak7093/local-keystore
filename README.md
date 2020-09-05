# Redis like local keystore

## Problem Statement
    - Create a Key - Value store server and client (client will be cli) and will talk to server by any method of your choosing (TCP, http etc.)
    - Expected output:
        methods: 
        1. get <key> -> value
        2. set <key> <value>
        3. watch <key> -> keep watching key for changes and output new value
    - Dockerfile and documentation

## Usage Instructions

Clone the repo

`git clone https://github.com/deepak7093/keystore-sample`

Switch dir

`cd keystore-sample`

### Starting Keystore Server with Docker
Build docker image

` docker build -t keystore:v1 . `

Start Keystore Server

` docker run -p 5000:5000 keystore:v1`

Check for docker process

` docker ps`

### Using client from local
Create virtual env

` python3 -m venv venv; source venv/bin/activate`

Install python dependecies

` pip install -r requirements.txt`

### Sample CLI commands

Set Keys

`python keystore-client.py set sea pacific`

`python keystore-client.py set mountain himalaya`

Get Keys

`python keystore-client.py get sea`

`python keystore-client.py get mountain`

Watch key changes

`python keystore-client.py watch mountain`




