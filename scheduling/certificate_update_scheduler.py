import os

import util.web_server_util as web_server_util
from configuration.environment_configuration import config_yaml_server
from configuration.logging_configuration import logger as log
from service import external_service_bean, web_server_beans


class CertificateUpdateScheduler:
    def __init__(self):
        pass

    def schedule(self):
        try:
            reload_web_server = False
            for certificate in config_yaml_server['daemon']['server']['certificates']:
                log.info(f"Synchronizing certificate with id: {certificate['id']}")
                dest_crt = certificate['destinations']['certificate']
                dest_key = certificate['destinations']['key']
                certificate, key = external_service_bean.download_certificate(certificate_id=certificate['id'])
                # check if file exists and content is the same
                # Certificate check
                if os.path.isfile(dest_crt):
                    with open(dest_crt, 'r') as f:
                        if certificate != f.read():
                            with open(dest_crt, 'w') as file:
                                file.write(certificate)
                            reload_web_server = True
                else:
                    with open(dest_crt, 'w') as file:
                        file.write(certificate)
                    reload_web_server = True

                # Key check
                if os.path.isfile(dest_key):
                    with open(dest_key, 'r') as f:
                        if key != f.read():
                            with open(dest_key, 'w') as file:
                                file.write(key)
                            reload_web_server = True
                else:
                    with open(dest_key, 'w') as file:
                        file.write(key)
                    reload_web_server = True
            if reload_web_server:
                web_server = web_server_util.recognize_web_server(os.getenv("TEST_WEB_SERVER_HOST"))
                for bean in web_server_beans:
                    if bean.web_server() == web_server:
                        bean.reload()
                        break
        except Exception as e:
            log.error(e.args)
            log.error(f"Error during certificate update scheduling: {e}")
