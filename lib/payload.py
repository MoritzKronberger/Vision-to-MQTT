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
    position_x_px: float
    position_y_px: float
    direction_x: float
    direction_y: float
    angle_boat_garbage_deg: float  # pos: clockwise, neg: counter-clockwise
    speed_boat_m_per_s: float

    def __init__(self, 
                 position_x_px: float,
                 position_y_px: float,
                 direction_x: float,
                 direction_y: float,
                 angle_boat_garbage_deg: float,
                 speed_boat_m_per_s: float) -> None:
        super().__init__('boat')
        self.position_x_px = position_x_px
        self.position_y_px = position_y_px
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.angle_boat_garbage_deg = angle_boat_garbage_deg  
        self.speed_boat_m_per_s = speed_boat_m_per_s
        


class Garbage(Payload):
    position_x_px: float
    position_y_px: float
    radius: float

    def __init__(self,     
                 position_x_px: float,
                 position_y_px: float,
                 radius: float) -> None:
        super().__init__('garbage')
        self.position_x_px = position_x_px
        self.position_y_px = position_y_px
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
