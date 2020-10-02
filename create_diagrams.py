from diagrams import Cluster, Diagram, Edge
from diagrams.custom import Custom
from diagrams.onprem.analytics import Spark
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.logging import Fluentd
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.network import Caddy
from diagrams.onprem.queue import Kafka
from diagrams.generic.device import Tablet
from diagrams.onprem.client import Client
from diagrams.generic.blank import Blank
from diagrams.generic.device import Mobile

with Diagram(name="Pirate Architecture", show=False):
    client = Client("User")

    ingress = Caddy("Reverse Proxy")

    with Cluster("Raspberry PI"):
        pi = Custom("session", "RPi-Logo-SCREEN.png")

    arduino = Custom("Arduino Project", "./720px-Arduino_Logo.svg.png")

    pi << Edge(color="firebrick", style="dashed") << arduino

    with Cluster("Service Cluster"):
        grpcsvc = [Server("grpc1"), Server("grpc2"), Server("grpc3")]

    with Cluster("Sessions HA"):
        master = Redis("session")
        master - Edge(color="brown", style="dashed") - Redis("replica") << Edge(
            label="collect"
        ) << arduino
    grpcsvc >> Edge(color="brown") >> master

    with Cluster("Database HA"):
        master = PostgreSQL("users")
        master - Edge(color="brown", style="dotted") - PostgreSQL("slave") << Edge(
            label="collect"
        ) << arduino
        grpcsvc >> Edge(color="black") >> master

    aggregator = Fluentd("logging")
    aggregator >> Edge(label="parse") >> Kafka("stream") >> Edge(
        color="black", style="bold"
    ) >> Spark("analytics")

    client >> ingress >> Edge(color="darkgreen") << grpcsvc >> Edge(
        color="darkorange"
    ) >> aggregator

