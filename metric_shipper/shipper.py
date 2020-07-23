import graphyte
from typing import List, Any, Tuple, Dict


class GraphiteShipper:
    def __init__(self, graphite_endpoint: str, prefix: str):
        self.graphite_endpoint: str = graphite_endpoint
        self.prefix: str = prefix
        self.sender = graphyte.Sender(self.graphite_endpoint, prefix=self.prefix)

    def send_metric(self, metric_name: str, metric_value: int) -> None:
        self.sender.send(metric_name, metric_value)
