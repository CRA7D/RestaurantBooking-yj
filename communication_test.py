from unittest import TestCase
from communication import SmsSender, MailSender


class TestableSmsSender(SmsSender):
    def __init__(self):
        super().__init__()
        self.__send_method_is_called = False

    def send(self, schedule):
        print("[Test] send SMS")
        self.__send_method_is_called = True

    def is_send_method_is_called(self):
        return self.__send_method_is_called


class TestableMailSender(MailSender):
    def __init__(self):
        super().__init__()
        self.__count_send_mail_is_called = 0

    def send_mail(self, schedule):
        print("[Test] send SMS")
        self.__count_send_mail_is_called += 1

    def get_count_send_mail_is_called(self):
        return self.__count_send_mail_is_called


class TestSmsSender(TestCase):
    def test_send(self):
        self.fail()
