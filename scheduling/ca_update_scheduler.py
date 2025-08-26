import os.path
import subprocess

import util.ssl_util as ssl_util
from configuration.environment_configuration import config_yaml_client
from configuration.logging_configuration import logger as log
from service import external_service_bean


class CAUpdateScheduler:
    def __init__(self):
        pass

    def schedule(self):
        try:
            reload_ca_certificates = False
            for ca in config_yaml_client['daemon']['server']['cas']:
                log.info(f"Synchronizing CA with id: {ca['id']}")
                ca = external_service_bean.download_certification_authority(ca['id'])
                domain = ssl_util.parse_certificate(ca).get("domain")

                # check if file exists and content is the same
                dest_path = f'/usr/local/share/ca-certificates/{domain}.crt'
                if os.path.isfile(dest_path):
                    with open(dest_path, 'r') as f:
                        if ca != f.read():
                            with open(dest_path, 'w') as file:
                                file.write(ca)
                            reload_ca_certificates = True
                else:
                    with open(dest_path, 'w') as file:
                        file.write(ca)
                    reload_ca_certificates = True
            if reload_ca_certificates:
                subprocess.run(["update-ca-certificates"], check=True)
        except Exception as e:
            log.error(f"Error during CA update scheduling: {e}")
