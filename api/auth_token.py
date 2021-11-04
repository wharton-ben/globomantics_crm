#!/usr/bin/env python

import requests

def get_token():
    """
    This will get the access token from Cisco DNA Center. Returns the token string if successful
    or false if not.
    """

    #declare useful local variables to simplify request process
    api_path = "https://sandboxdnac.cisco.com/dna"
    auth = ("devnetuser", "Cisco123!")
    headers = {"Content-Type": "application/json"}

    #issue Http POST request to the proper URL to request a token
    auth_resp = requests.post(
            f"{api_path}/system/api/v1/auth/token", auth=auth, headers=headers
            )

    #if successful, print token. Else, raise HTTPError with details
    auth_resp.raise_for_status()
    token = auth_resp.json()["Token"]
    return token

def main():
    token = get_token()
    print(token)

if __name__ == "__main__":
    main()


