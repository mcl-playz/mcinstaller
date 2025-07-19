import requests
import typing

class ResponseHandler:
    def parse(response: requests.Response):
        try:
            responseJSON = response.json()
        except Exception:
            print(f"Failed to parse response JSON. Status code: {response.status_code}")
            return None
        
        return responseJSON

    def ensureSafeStatus(response: requests.Response):
        if not response.ok:
            print(f"Error {response.status_code}: {response.json().get('error', 'Unknown error')}")
            return False
        
        return True