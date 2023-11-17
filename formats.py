from Crypto.PublicKey import RSA
from OpenSSL.crypto import load_certificate, FILETYPE_ASN1
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePublicKey
from cryptography.hazmat.primitives.asymmetric.dsa import DSAPublicKey
from typing import Union


def importPem(filename: str) -> RSA.RsaKey:
    with open(filename) as f:
        data = f.read()

    return RSA.importKey(data)


def importDer(filename: str) -> Union[RSAPublicKey, EllipticCurvePublicKey, DSAPublicKey]:
    with open(filename, "rb") as f:
        data = f.read()
        cert = load_certificate(FILETYPE_ASN1, data)

    return cert.to_cryptography().public_key()


def importRSAKey(filename: str) -> RSA.RsaKey:
    with open(filename) as f:
        data = f.read()

    return RSA.importKey(data)
