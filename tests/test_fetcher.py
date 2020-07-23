import unittest
from moto import mock_cloudwatch
import boto3
from metric_shipper.fetcher import CloudwatchMetricFetcher


@mock_cloudwatch
class TestFetcher(unittest.TestCase):
    def setUp(self):
        self.cloudwatch_client = boto3.client("cloudwatch")
        self.cloudwatch_client.put_metric_data(
            MetricData=[
                {
                    "MetricName": "testmetric",
                    "Unit": "Seconds",
                    "Values": [10],
                    "Counts": [1],
                    "Dimensions": [{"Name": "AuditType", "Value": "all"}],
                }
            ],
            Namespace="custom-namespace",
        )

    def test_send_metric(self):
        fetcher = CloudwatchMetricFetcher()
