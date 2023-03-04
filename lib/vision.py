import json
from turtle import distance
import numpy as np
from lib.payload import Boat, Garbage

def read_output(filename: str) -> tuple[Garbage | None, Boat] | None:
    try:
        with open(filename,'r') as f:
            data = json.load(f)
            # Return default values if boat can't be detected
            boat_visible = bool(data['boat_visible'])
            if not boat_visible:
                boat = Boat(
                    boat_visible=False,
                    distance_to_garbage_m=0,
                    angle_boat_garbage_deg=0
                )
                return [None, boat]
            garbage = Garbage(
                position_x_m=data['x_garbage'],
                position_y_m=data['y_garbage'],
                radius=0
            )
            distance_boat_garbage = distance_to_origin(garbage.position_x_m, garbage.position_y_m)
            angle_boat_garbage_deg = angle_x_axis_to_point_deg(garbage.position_x_m, garbage.position_y_m)
            boat = Boat(
                boat_visible=True,
                angle_boat_garbage_deg=angle_boat_garbage_deg,
                distance_to_garbage_m=distance_boat_garbage
            )
            return [garbage, boat]
    except Exception as e:
        print('Skipped reading vision output', e)
        return None


def distance_to_origin(x: float, y: float) -> float:
    origin = np.array([0,0])
    point = np.array([x,y])
    distance_m = np.linalg.norm(origin-point)
    return distance_m

# Ref: https://stackoverflow.com/questions/2827393/angles-between-two-n-dimensional-vectors-in-python
# Ref: https://stackoverflow.com/questions/14066933/direct-way-of-computing-clockwise-angle-between-2-vectors/16544330#16544330

def unit_vector(vector):
    """ Returns the unit vector of the vector."""
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    dot = np.dot(v1_u, v2_u)
    det = np.linalg.det(np.array([v1, v2]))
    return np.arctan2(det, dot) * -1

def angle_x_axis_to_point_deg(x: float, y: float) -> float:
    """Calculate angle between x-axis and vectir from origin to point."""
    origin = np.array([0,0])
    point = np.array([x,y])
    v_origin_point = point - origin
    v_x_axis = np.array([1,0])

    angle = angle_between(v_x_axis, v_origin_point)
    return np.rad2deg(angle)
