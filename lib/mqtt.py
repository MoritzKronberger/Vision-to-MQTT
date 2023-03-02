"""Handle MQTT functionality with convenience wrapper for paho-mqtt client."""

from typing import Any
import time
import json
import socket
from paho.mqtt import client as paho_client
from paho import mqtt


class MQTTClient:
    """Paho-mqtt client wrapper."""

    def __init__(self):
        self.mqtt_client = paho_client.Client(
            "", protocol=paho_client.MQTTv5)
        # self.mqtt_client.enable_logger(logger)
        # self.mqtt_client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

    def connect(self,
                broker: str,
                port: int | None = None,
                user: str | None = None,
                password: str | None = None,
                keepalive=10):
        """Connect MQTT client to broker start threaded client loop."""
        self.mqtt_client.username_pw_set(user, password)
        try:
            self.mqtt_client.connect(broker)
            #self.mqtt_client.connect(broker, port, keepalive)
            self.mqtt_client.loop_start()
            # Block until client is connected
            while not self.mqtt_client.is_connected():
                time.sleep(0.1)
        except socket.gaierror:
            print('Could not connect MQTT client')

    def reconnect(self):
        """Reconnect MQTT client to broker and start threaded client loop if disconnected."""
        if not self.mqtt_client.is_connected():
            self.mqtt_client.reconnect()
            self.mqtt_client.loop_start()
        # Block until client is connected
        while not self.mqtt_client.is_connected():
            time.sleep(0.1)

    def publish(self, topic: str, payload: Any, qos=1):
        """Publish payload as message on topic."""
        self.mqtt_client.publish(topic, json.dumps(payload), qos)

    def disconnect(self) -> None:
        """Disconnect mqtt client and stop loop."""
        self.mqtt_client.disconnect()
        self.mqtt_client.loop_stop()

    def is_connected(self):
        """Return client connection status."""
        return self.mqtt_client.is_connected() if self.mqtt_client is not None else False
