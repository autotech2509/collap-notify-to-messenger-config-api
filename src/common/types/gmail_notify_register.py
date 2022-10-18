from dataclasses import dataclass
import typing


@dataclass
class RegisterGmailNotifyDesktopBody:
    token: str
    refresh_token: str
    token_uri: str
    client_id: str
    client_secret: str
    scopes: typing.List[str]
    expiry: str
    email: str
