#!/usr/bin/env python

import requests
from requests import api
import auth_token
import json

token = auth_token.get_token()

def main():
    #This function will be used to return a list of devices from DNA Center
    
    #declare useful local variables to simplify request process
    api_path = "https://sandboxdnac.cisco.com/dna"
    headers = {"Content-Type": "application/json",
    "X-Auth-Token": token}

    req_response = requests.get(
        f"{api_path}/intent/api/v1/network-device/", headers=headers
    )

    #raise an exception if error
    req_response.raise_for_status()
    #print(json.dumps(req_response.json(), indent=2))

    if req_response.ok:
        for device in req_response.json()["response"]:
            print(f"ID: {device['id']}   IP: {device['managementIpAddress']}")
    else:
        print(f"Device collection failed with code {req_response.status_code}")
        print(f"Failure body: {req_response.text}")

if __name__ == "__main__":
    main()
