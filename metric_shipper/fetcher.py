import boto3


class CloudwatchMetricFetcher:
    def __init__(self, metrics={}):
        self.metrics = metrics
        pass

    def fetch_metric(self, metric):
        pass
