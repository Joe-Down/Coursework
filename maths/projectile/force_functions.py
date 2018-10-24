from math import sin, cos, degrees, atan


def resultant_magnitude_calc(x_component: float, y_component: float):
    return ((x_component ** 2) + (y_component ** 2)) ** 0.5


def vertical_component_calc(magnitude: float, direction: float):
    if direction == ('x' or '-x' or 0 or 180):  # Avoid floating point rounding errors giving no 0 values later
        return 0
    else:
        return magnitude * sin(direction)


def horizontal_component_calc(magnitude: float, direction: float):
    if direction == ('y' or '-y' or 90 or 270):  # Avoid floating point rounding errors giving no 0 values later
        return 0
    else:
        return magnitude * cos(direction)


def resultant_direction_calc(x_component: float, y_component: float):
    if x_component == 0:
        if y_component > 0:
            return 90
        elif y_component < 0:
            return 270
        else:
            return "N/A"
    else:
        return degrees(atan(y_component / x_component))


def acceleration_calc(force: float, mass: float):
    if mass == 0:
        return 0
    else:
        return force / mass


def velocity_calc(initial_velocity: float, acceleration: float, time: float):
    return initial_velocity + acceleration * time
