from src.common.push_message_to_kafka import push_message_to_confluent_kafka
from src.common.types.gmail_notify_register import RegisterGmailNotifyDesktopBody
from src.settings.kafka_settings import KafkaTopic
from dataclasses import asdict
from flask import Response


class RegisterGmailNotifyController:
    @classmethod
    def register_gmail_notify_for_desktop(cls, request_data: RegisterGmailNotifyDesktopBody):
        push_message_to_confluent_kafka(
            data=asdict(request_data),
            topic=KafkaTopic.REGISTER_GMAIL_NOTIFY
        )
        return Response(status=200)
