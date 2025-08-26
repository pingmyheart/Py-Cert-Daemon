import re

from configuration.logging_configuration import logger as log


def recognize_web_server(host: str):
    header = __obtain_server_header(host)
    if re.findall(r"nginx/*", header, re.IGNORECASE):
        return "nginx"
    elif re.findall(r"apache/*", header, re.IGNORECASE) or re.findall(r"httpd/*", header, re.IGNORECASE):
        return "apache"
    else:
        return "unknown"


def __obtain_server_header(host: str):
    import requests

    response = requests.head(host)

    log.debug("Status:", response.status_code)
    for key, value in response.headers.items():
        log.debug(f"{key}: {value}")
    return response.headers.get("Server")
