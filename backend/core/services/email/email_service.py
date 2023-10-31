import os
from dataclasses import dataclass, field
from typing import Type

from celery.app import task
from django.core.mail import EmailMultiAlternatives
from django.template import Template
from django.template.loader import get_template

from core.dataclasses import UserDataClass
from core.services.token import JWTService, ActivateToken, RecoveryToken
from configs.celery import app


@dataclass
class SendEmailArgs:
    subject: str
    to: [str]
    context: dict
    template: Type[Template] = get_template('email.html')
    from_email = os.getenv('EMAIL_HOST_USER')
    content: Type[Template] = field(init=False)

    def __post_init__(self):
        self.content = self.template.render(self.context)


testDataSet = SendEmailArgs(
    to=['pvs.versia@gmail.com'],
    subject='Test',
    context={'title': 'Title', 'body': 'Body'}
)


class EmailService:

    @staticmethod
    def send_email(args: SendEmailArgs = testDataSet):
        msg = EmailMultiAlternatives(
            from_email=args.from_email,
            to=args.to,
            subject=args.subject
        )
        msg.attach_alternative(
            content=args.content,
            mimetype='text/html'
        )
        msg.send()

    @classmethod
    def register_email(cls, user: UserDataClass):
        token = JWTService.create_token(user=user, token_class=ActivateToken)
        url = f'http://localhost/api/users/activate/{token}'
        args = SendEmailArgs(
            to=[os.getenv('EMAIL_HOST_USER')],
            subject='Register',
            template=get_template('email_register.html'),
            context={'name': user.profile.name, 'url': url}
        )
        cls.send_email(args)

    @classmethod
    def recovery_email(cls, user: UserDataClass):
        token = JWTService.create_token(user=user, token_class=RecoveryToken)
        print(token)
        url = f'http://localhost:3000/users/recovery/{token}'
        args = SendEmailArgs(
            to=[os.getenv('EMAIL_HOST_USER')],
            subject='Recovery',
            template=get_template('email_recovery.html'),
            context={'url': url},
        )
        cls.send_email(args)

    @staticmethod
    @app.task
    def spam():
        args = SendEmailArgs(
            to=['pvs.versia@gmail.com'],
            subject='Test',
            context={'title': 'Title', 'body': 'Body'},
            template=get_template('email.html')
        )
        EmailService.send_email(args)
