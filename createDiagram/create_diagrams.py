import os
os.environ["PATH"] += os.pathsep + 'C:\Program Files\Graphviz 2.44.1/bin/'
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


with Diagram(name="Pirate Architecture", show=False):
    with Cluster("Raspberry PI"):
        with Cluster("Docker"):
            nodeJs = NodeJS("Pirate-Bridge")

        with Cluster("Docker2"):
            Janus = Custom("Janus", "./customImages/janus-logo.png")

        with Cluster("Docker3"):
            Gstreamer = Custom("Gstreamer", "./customImages/gstreamer-logo.png")
            
        Janus << Edge(label="RTSP Stream",color="firebrick") << Gstreamer
        react = React("Pirate-Flag")
        caddy = Caddy("Reverse Proxy")
        caddy << Edge(color="firebrick") >> Janus
        caddy << Edge(color="firebrick") >> react
        caddy << Edge(color="firebrick") >> nodeJs


    piCamera = IotCamera("Camera")
    arduino = Custom("Pirate-Hook", "./customImages/720px-Arduino_Logo.png")

    # Data from Arduino to Pi
    nodeJs << Edge(label="Pirate Serial",color="firebrick") >> arduino

    Gstreamer << Edge(color="firebrick") << piCamera

    client = Client("User")
    client << Edge(color="firebrick") >> caddy
    
with Diagram(name="Pirate Overview", show=False):
    with Cluster("Pirate Modul"):
        pi = Custom("Module Pi", "./customImages/RPi-Logo-SCREEN.png")
            
            
        

        with Cluster("RS Project"):
            piCamera = IotCamera("Camera")
            arduino = Custom("Arduino", "./customImages/720px-Arduino_Logo.png")



    # Data from Arduino to Pi
    pi << Edge(label="Pirate Serial",color="firebrick") >> arduino


    pi << Edge(color="firebrick") << piCamera

    client = Client("User")
    client << Edge(color="firebrick") >> pi
    