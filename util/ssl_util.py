from cryptography import x509
from cryptography.hazmat.backends import default_backend


def parse_certificate(cert: str):
    # Load certificate (DER format assumed)
    cert = x509.load_pem_x509_certificate(cert.encode("utf-8"), default_backend())
    subject = cert.subject

    # Extract fields
    def get_attr(oid):
        try:
            return subject.get_attributes_for_oid(oid)[0].value
        except IndexError:
            return ""

    return {
        "domain": get_attr(x509.NameOID.COMMON_NAME),
        "country": get_attr(x509.NameOID.COUNTRY_NAME),
        "location": get_attr(x509.NameOID.LOCALITY_NAME),
        "state": get_attr(x509.NameOID.STATE_OR_PROVINCE_NAME),
        "organization": get_attr(x509.NameOID.ORGANIZATION_NAME),
        "organization_unit": get_attr(x509.NameOID.ORGANIZATIONAL_UNIT_NAME),
    }
