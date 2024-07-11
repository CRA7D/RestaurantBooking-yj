from unittest import TestCase
from communication import SmsSender


class TestableSmsSender(SmsSender):
    def __init__(self):
        super().__init__()
        self.__send_method_is_called = False

    def send(self, schedule):
        print("[Test] send SMS")
        self.__send_method_is_called = True

    def is_send_method_is_called(self):
        return self.__send_method_is_called


class TestSmsSender(TestCase):
    def test_send(self):
        self.fail()
