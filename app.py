from configparser import ConfigParser
import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth

#importing own modules
from module_template import module_class

#MY_ENV_VAR = os.getenv('MY_ENV_VAR')

#reading potential config
config = ConfigParser()
config.read("config/conf.conf")

base_url = config['GENERAL']['BASE_URL']
sample_file = config['GENERAL']['SAMPLE_FILE']

if 'AM_I_IN_A_DOCKER_CONTAINER' not in os.environ:
    load_dotenv()
    
username = os.environ['USER_NAME']
password = os.environ['USER_PASSWORD']

auth = HTTPBasicAuth(username, password)

if __name__ == "__main__":
    #simple get request
    url = f"{base_url}/"
    response = requests.get(url)
    print(response.text)

    #simple post request
    url_post = f"{base_url}/post/"
    response = requests.post(url_post)
    print(response.text)

    #get request with auth
    url_get_auth = f"{base_url}/secured/"
    response = requests.get(url_get_auth, auth=auth)
    print(response.text)

    #post file with auth
    url_post_file_auth = f"{base_url}/postfile/"
    with open(sample_file, 'rb') as file:
        bytes = file.read()
        content = {'file_to_process' : bytes}
    
    response = requests.post(url_post_file_auth, files=content, auth=auth)
    print(response.text)




