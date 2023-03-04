from lib.mqtt import MQTTClient


class Payload():
    TOPIC: str

    def __init__(self, topic: str) -> None:
        self.TOPIC = topic

    def publish(self, mqtt_client: MQTTClient):
        data = self.__dict__
        mqtt_client.publish(
            self.TOPIC,
            data
        )
        print(f'Publishing {data}\n to {self.TOPIC}')


class Boat(Payload):
    boat_visible: bool
    angle_boat_garbage_deg: float  # pos: clockwise, neg: counter-clockwise
    distance_to_garbage_m: float

    def __init__(self, 
                 boat_visible: bool,
                 angle_boat_garbage_deg: float,
                 distance_to_garbage_m: float) -> None:
        super().__init__('boat')
        self.boat_visible = boat_visible
        self.angle_boat_garbage_deg = angle_boat_garbage_deg  
        self.distance_to_garbage_m = distance_to_garbage_m
        


class Garbage(Payload):
    position_x_m: float
    position_y_m: float
    radius: float

    def __init__(self,     
                 position_x_m: float,
                 position_y_m: float,
                 radius: float) -> None:
        super().__init__('garbage')
        self.position_x_m = position_x_m
        self.position_y_m = position_y_m
        self.radius = radius


class Statistics(Payload):
    battery_percent: int
    garbage_empty: bool

    def __init__(self,
                 battery_percent: int,
                 garbage_empty: bool) -> None:
        super().__init__('statistics')
        self.battery_percent = battery_percent
        self.garbage_empty = garbage_empty
