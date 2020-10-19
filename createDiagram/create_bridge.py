import os

os.environ["PATH"] += os.pathsep + "C:\Program Files\Graphviz 2.44.1/bin/"
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
from diagrams.aws.iot import IotCamera
from diagrams.programming.framework import React
from diagrams.programming.language import NodeJS

graph_attr = {"fontsize": "45", "bgcolor": "transparent", "pad": "0.0"}


with Diagram(filename="pirate_bridge", show=False, graph_attr=graph_attr):
    with Cluster("Raspberry PI"):
        with Cluster("Pirate Bridge"):
            serial = Custom(
                "Serial-Interface", "./customImages/serialport-logo-small.png"
            )
            ardu_sent = NodeJS("Arduino Send Buffer")
            config = NodeJS("Config Data")
            client_sent = NodeJS("Client Send Buffer")
            httpapi = Custom("HTTP-API", "./customImages/Expressjs.png")
        caddy = Caddy("Pirate Map")

    with Cluster("Arduino Project"):
        with Cluster("Arduino"):
            hook = Custom("Pirate-Hook", "./customImages/720px-Arduino_Logo.png")

    caddy << Edge(color="firebrick") >> httpapi
    httpapi << [client_sent, config]
    httpapi >> ardu_sent

    [client_sent, config] << serial
    ardu_sent >> serial
    # Data from Arduino to Pi
    serial << Edge(label="Pirate Serial Protocol", color="firebrick") >> hook

