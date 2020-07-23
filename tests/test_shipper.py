import unittest
import socket
from metric_shipper.shipper import GraphiteShipper
import mock
from freezegun import freeze_time


class TestShipper(unittest.TestCase):
    def setUp(self):
        self.hostname = "4.3.2.1"
        self.prefix = "test.prefix"
        self.shipper = GraphiteShipper(self.hostname, self.prefix)

    @freeze_time("2001-01-01 00:04:31")
    @mock.patch("socket.socket.connect")
    @mock.patch("socket.socket.send")
    def test_send_metric(self, send, connect):
        test_metric = "testametric"
        test_value = 1001
        test_timestamp = 978307471  # Time since epoch for freezegun time

        self.shipper.send_metric(test_metric, test_value)

        connect.assert_called_with((self.hostname, 2003))

        result_string = f"{self.prefix}.{test_metric} {test_value} {test_timestamp}\n"
        send.assert_called_with(result_string.encode("utf-8"))