import os

os.environ["PATH"] += os.pathsep + "C:\Program Files\Graphviz 2.44.1/bin/"
os.environ["PATH"] += os.pathsep + "C:/Program Files (x86)/Graphviz2.38/bin/"

from diagrams import Cluster, Diagram, Edge
from diagrams.custom import Custom
from diagrams.programming.language import JavaScript
from diagrams.onprem.client import Client
from diagrams.aws.iot import IotCamera
from diagrams.programming.language import Go

graph_attr = {"fontsize": "45", "bgcolor": "transparent", "pad": "0.0"}

with Diagram(filename="pirate_spyglass", show=False, graph_attr=graph_attr):
    
    with Cluster("Experiment"):
        piCamera = IotCamera("PiCamera")
        with Cluster("Raspberry Pi"):
            v4l2 = Custom("PiCamera Driver\n+ V4L2", "./customImages/RPi-Logo-SCREEN.png")
            go = Go("BerryMSE")

    v4l2 << Edge(label="Raw Image", color="firebrick") << piCamera
    go << Edge(label="MPEG-4 Part 10 AVC\nH.264 NAL Units", color="firebrick") << v4l2

    with Cluster("Client"):
        website = Client("Website")
        javaScript = JavaScript("MSE")

    javaScript << Edge(label="MPEG-4 Part 15 AVCFF\nH.264 NAL Units", color="firebrick") << go
    website << Edge(label="Video", color="firebrick") << javaScript

