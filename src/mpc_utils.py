import hashlib
import secrets
from typing import Tuple

def hash_ioc(ioc: str, salt: str) -> str:
    """One-way deterministic masking of an IOC. Returns hex SHA-256."""
    return hashlib.sha256((salt + ioc).encode("utf-8")).hexdigest()


def xor_bytes(a: bytes, b: bytes) -> bytes:
    """XOR two byte sequences of equal length."""
    if len(a) != len(b):
        raise ValueError("Inputs must have the same length")
    return bytes(x ^ y for x, y in zip(a, b))


def split_secret(secret: bytes) -> Tuple[bytes, bytes]:
    """
    XOR-based secret sharing (binary).
    Returns two byte-string shares where share1 ^ share2 = secret.
    Uses cryptographically secure randomness for share1.
    """
    share1 = secrets.token_bytes(len(secret))
    share2 = xor_bytes(secret, share1)
    return share1, share2


def reconstruct_secret(share1: bytes, share2: bytes) -> bytes:
    """Reconstruct the original secret from two byte-string shares."""
    return xor_bytes(share1, share2)


# Convenience helpers for text secrets (hex-encoded shares)
def split_secret_str(secret: str, encoding: str = "utf-8") -> Tuple[str, str]:
    """Split a text secret and return hex-encoded shares."""
    s = secret.encode(encoding)
    share1, share2 = split_secret(s)
    return share1.hex(), share2.hex()


def reconstruct_secret_str(share1_hex: str, share2_hex: str, encoding: str = "utf-8") -> str:
    """Reconstruct a text secret from hex-encoded shares."""
    s = reconstruct_secret(bytes.fromhex(share1_hex), bytes.fromhex(share2_hex))
    return s.decode(encoding)