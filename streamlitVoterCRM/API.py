import requests

class API:
    def __init__(self, base_url:str,token:str):
        self.base_url=base_url
        self.base_headers={"token":token}

    def add_state(self,state_name,country):
        try:
            states={
                "state_name":state_name,
                "country":country
            }
            response=requests.post(self.base_url+"/state",json=states,headers=self.base_headers)
            if response.status_code==200:
                return True
        except:
            return False

    def get_states(self):
        try:
            response=requests.get(self.base_url+"/states",headers=self.base_headers)
            return response.json()['states']
        except:
            return None

    def login(self,username,password):
        try:
            credentials={
                "username":username,
                "password":password
            }
            response=requests.post(self.base_url+"/auth/login",json=credentials)
            body=response.json()
            token=body.get("token") if type(body)==dict else None

            return token
        except:
            return None

    def is_logged_in(self):
        response=requests.get(self.base_url+"/auth/is_logged_in",headers=self.base_headers)
        return response.status_code==200
