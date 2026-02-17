# Third Library
from ldap3 import ALL, Connection, Server
from ldap3.core.exceptions import LDAPBindError, LDAPCertificateError

from config.settings import settings


def authenticate(user: str, password: str):
    server = Server(settings.LDAP_SERVER, get_info=ALL)
    user_dn = f"{user}@{settings.DOMAIN}"  # Make sure this format is correct
    try:
        conn = Connection(server, user=user_dn, password=password, auto_bind=True)
        if not conn.bound:
            return False
    except LDAPBindError:
        return False

    return True


if __name__ == "__main__":
    try:
        if authenticate("", ""):
            print("SUCCESS")
    except LDAPCertificateError as e:
        print(f"Authentication failed: {e.detail}")
