from metric_shipper.shipper import GraphiteShipper
import os


DEFAULT_OPTIONS = {
    "Period": 60,  # 1 minute
    "Count": 5,  # 5 periods
    "Formatter": (
        "cloudwatch.%(Namespace)s.%(dimension)s.%(MetricName)s"
        ".%(statistic)s.%(Unit)s"
    ),
}


GRAPHITE_ENDPOINT = os.environ.get("GRAPHITE_ENDPOINT")
GRAPHITE_PREFIX = os.environ.get("GRAPHITE_PREFIX")

shipper: GraphiteShipper = GraphiteShipper(GRAPHITE_ENDPOINT, GRAPHITE_PREFIX)


def handler(event, context):

    shipper.run()
