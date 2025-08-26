from service.external_service import ExternalService
from service.web_server_service import ApacheWebServerService, NginxWebServerService

external_service_bean = ExternalService()

apache_web_server_bean = ApacheWebServerService()
nginx_web_server_bean = NginxWebServerService()

web_server_beans = [apache_web_server_bean, nginx_web_server_bean]
