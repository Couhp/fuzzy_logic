def lamp_yellow(time):
    if time == 0:
        return 1.0
    elif 0 <= time and time <= 2:
        return (2 - time) / 2.0
    elif -2 <= time and time <= 0:
        return (time + 2) / 2.0
    else:
        return 0.0

def lamp_green(time):
    if 5 <= time and time <= 7:
        return 1.0
    elif 1 <= time and time <= 5:
        return (time - 1) / 4.0
    elif 7 <= time and time <= 10:
        return (10 - time) / 3.0
    else:
        return 0.0

def lamp_more_green(time):
    if time >= 10:
        return 1.0
    elif 7 <= time and time <= 10:
        return (time - 7) / 3.0
    else:
        return 0.0

def lamp_red(time):
    if -7 <= time and time <= -5:
        return 1.0
    elif -5 <= time and time <= -1:
        return (-time - 1) / 4.0
    elif -10 <= time and time <= -5:
        return (time + 10) / 3.0
    else:
        return 0.0

def lamp_more_red(time):
    if time <= -10:
        return 1.0
    elif -10 <= time and time <= -7:
        return (-time - 7) / 3.0
    else:
        return 0.0

def speed_slow(speed):
    if 0<= speed and speed <= 15:
        return 1.0
    elif 15 <= speed and speed <= 30:
        return (30 - speed) / 15.0
    else:
        return 0.0

def speed_normal(speed):
    if speed == 35:
        return 1.0
    elif 15 <= speed and speed <= 40:
        return (speed - 15) / 25.0
    elif 40 <= speed and speed <= 65:
        return (65 - speed) / 25.0
    else:
        return 0.0

def speed_fast(speed):
    if speed >= 65:
        return 1.0
    elif 40 <= speed and speed <= 65:
        return (speed - 40) / 25.0
    else:
        return 0.0

def distance_near(distance):
    if 0 <= distance and distance <= 10:
        return 1.0
    elif 10 <= distance and distance <= 20:
        return (20 - distance) / 10.0
    else:
        return 0.0

def distance_normal(distance):
    if distance == 30:
        return 1.0
    elif 10 <= distance and distance <= 30:
        return (distance - 10) / 20.0
    elif 30 <= distance and distance <= 50:
        return (50 - distance) / 20.0
    else:
        return 0.0

def distance_far(distance):
    if distance >= 50 and distance < 300:
        return 1.0
    elif 30 <= distance and distance <= 50:
        return (distance - 30) / 20.0
    else:
        return 0.0
