import secrets
import string
from app.core.config import settings


def generate_code() -> str:
    alphabet = string.ascii_letters + string.digits
    code = ''.join(secrets.choice(alphabet) for _ in range(settings.CODE_LENGTH))
    return code