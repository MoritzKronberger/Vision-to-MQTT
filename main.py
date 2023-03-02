from constants import BROKER_IP_ADDRESS
from lib.mqtt import MQTTClient
from lib.payload import Boat, Garbage


def send_vision_data(mqtt_client: MQTTClient):
    boat = Boat(
        position_x_px=500,
        position_y_px=200,
        direction_x=1,
        direction_y=-1,
        angle_boat_garbage_deg=24,
        speed_boat_m_per_s=0.02
    )

    boat.publish(mqtt_client)


def main():
    mqtt_client = MQTTClient()
    mqtt_client.connect(BROKER_IP_ADDRESS)
    send_vision_data(mqtt_client)

if __name__ == "__main__":
    main()
