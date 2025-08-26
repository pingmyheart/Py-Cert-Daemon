import os

import dotenv
import yaml

dotenv.load_dotenv()

PCD_PY_CERT_SERVER_HOST = os.getenv("PCD_PY_CERT_SERVER_HOST")
PCD_CLIENT_CONFIG_FILE = os.getenv("PCD_CLIENT_CONFIG_FILE")
PCD_SERVER_CONFIG_FILE = os.getenv("PCD_SERVER_CONFIG_FILE")

if os.path.isfile(PCD_CLIENT_CONFIG_FILE):
    with open(PCD_CLIENT_CONFIG_FILE, 'r') as file:
        config_yaml_client = yaml.safe_load(file)
else:
    config_yaml_client = {
        'daemon': {
            'server': {
                'cas': []
            }
        }
    }

if os.path.isfile(PCD_SERVER_CONFIG_FILE):
    with open(PCD_SERVER_CONFIG_FILE, 'r') as file:
        config_yaml_server = yaml.safe_load(file)
else:
    config_yaml_server = {
        'daemon': {
            'server': {
                'certificates': []
            }
        }
    }
