import requests

from configuration.environment_configuration import PCD_PY_CERT_SERVER_HOST


class ExternalService:
    def __init__(self):
        pass

    def download_certification_authority(self, certification_authority_id: str):
        # Placeholder for downloading CA certificates
        certification_authority = requests.request(method="GET",
                                                   url=f"{PCD_PY_CERT_SERVER_HOST}/certificate/ca/download/{certification_authority_id}",
                                                   timeout=10,
                                                   verify=False).text
        return certification_authority

    def download_certificate(self, certificate_id: str):
        # Placeholder for downloading a specific certificate by ID
        certificate, key = (requests.request(method="GET",
                                             url=f"{PCD_PY_CERT_SERVER_HOST}/certificate/download/{certificate_id}/crt",
                                             timeout=10,
                                             verify=False).text,
                            requests.request(method="GET",
                                             url=f"{PCD_PY_CERT_SERVER_HOST}/certificate/download/{certificate_id}/key",
                                             timeout=10,
                                             verify=False).text)
        return certificate, key
