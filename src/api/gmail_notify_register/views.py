from flask import Blueprint

from src.api import HttpMethod
from src.api.gmail_notify_register.controllers import RegisterGmailNotifyController
from src.common.utils.docs_register import register_view
from src.common.types.gmail_notify_register import RegisterGmailNotifyDesktopBody
from src.api.urls import Endpoint
from flask import request
from dacite import from_dict

blueprint = Blueprint('gmail_notify_register_desktop', __name__)


@blueprint.route(Endpoint.REGISTER_GMAIL_NOTIFY_DESKTOP, methods=[HttpMethod.POST])
def register_gmail_notify_for_desktop():
    return RegisterGmailNotifyController.register_gmail_notify_for_desktop(
        from_dict(data_class=RegisterGmailNotifyDesktopBody, data=request.json)
    )


def register_docs(docs):
    register_view(docs, blueprint, [
        register_gmail_notify_for_desktop
    ])
