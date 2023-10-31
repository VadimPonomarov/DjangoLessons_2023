from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.services.email import EmailService


class TestEmailView(GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, *args, **kwargs):
        EmailService.send_email()
        return Response('Ok')
