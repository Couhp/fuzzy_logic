def lamp_more_green(time):
    if 0 <= time and time <= 3:
        return 1.0
    elif 4 <= time and time <= 6:
        return (time - 4.0)/2.0
    else:
        return 0
   
def lamp_green(time):
    if 6<= time and time<= 8:
        return 1.0
    elif 3<= time and time <= 5:
        return (time-3)/3.0
    elif 8<=time and time  <= 11:
        return (11-time)/4.0
    else:
        return 0

def lamp_yellow(time):
    if 12 <= time and time <= 13:
        return 1.0
    elif 9 <= time and time <= 11:
        return (time-9)/3.0
    elif 14<= time and time <= 16:
        return (16-time)/3.0
    return 0

def lamp_more_red(time):
    if 14 <= time and time <= 18:
        return (time-14)/5.0
    elif 19 <= time and time <= 22:
        return (22-time)/4.0
    else:
        return 0

def lamp_red(time):
    if 18 <= time and time <= 21:
        return (time-18)/4.0
    elif 22 <= time and time <= 25:
        return (25-time)/4.0
    return 0

#================================================

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
#============================================================
def distance_near(distance):
    if 0 <= distance and distance <= 30:
        return 1.0
    elif 30 <= distance and distance <= 50:
        return (50 - distance) / 20.0
    else:
        return 0.0

def distance_normal(distance):
    if distance == 50:
        return 1.0
    elif 20 <= distance and distance <= 50:
        return (distance - 20) / 30.0
    elif 50 <= distance and distance <= 70:
        return (70 - distance) / 20.0
    else:
        return 0.0

def distance_far(distance):
    if distance > 70 :
        return 1.0
    elif 40 <= distance and distance <= 70:
        return (distance - 40) / 30.0
    else:
        return 0.0


# print (lamp_yellow(16))