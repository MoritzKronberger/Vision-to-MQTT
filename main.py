from gc import garbage
import time
from constants import BROKER_IP_ADDRESS, LOOP_TIMEOUT, VISION_OUTPUT_FILENAME
from lib.mqtt import MQTTClient
from lib.payload import Boat, Garbage
from lib.vision import read_output


def send_mock_data(mqtt_client: MQTTClient):
    boat = Boat(
        boat_visible=True,
        angle_boat_garbage_deg=120,
        distance_to_garbage_m=0.56
    )
    garbage = Garbage(
        position_x_m=0.87,
        position_y_m=0.65,
        radius=0
    )
    boat.publish(mqtt_client)
    garbage.publish(mqtt_client)


def send_vision_data(mqtt_client: MQTTClient, garbage: Garbage | None, boat: Boat):
    boat.publish(mqtt_client)
    if garbage is not None:
        garbage.publish(mqtt_client)


def main():
    mqtt_client = MQTTClient()
    mqtt_client.connect(BROKER_IP_ADDRESS)
    while True:
        vision_data = read_output(VISION_OUTPUT_FILENAME)
        if vision_data is not None:
            garbage, boat = vision_data
            send_vision_data(mqtt_client, garbage, boat)
        # send_mock_data(mqtt_client)
        time.sleep(LOOP_TIMEOUT)

if __name__ == "__main__":
    main()
