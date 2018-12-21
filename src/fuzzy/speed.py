try:
    import src.fuzzy.fuzzy_variable as fuzzy_variable
    from src.fuzzy.rule import read_rule
except:
    import fuzzy_variable
    from rule import read_rule
# ============  LAMP ==============================================
def check_var_fuzzy_lamp( time, distance):
    var_fuzzy = []
    if fuzzy_variable.distance_near(distance) != 0.0:
        var_fuzzy.append("near")
    if fuzzy_variable.distance_normal(distance) != 0.0:
        var_fuzzy.append("medium")
    if fuzzy_variable.distance_far(distance) != 0.0:
        var_fuzzy.append("far")
    if fuzzy_variable.lamp_more_red(time) != 0.0:
        var_fuzzy.append("more_red")
    if fuzzy_variable.lamp_red(time) != 0.0:
        var_fuzzy.append("red")
    if fuzzy_variable.lamp_yellow(time) != 0.0:
        var_fuzzy.append("yellow")
    if fuzzy_variable.lamp_green(time) != 0.0:
        var_fuzzy.append("green")
    if fuzzy_variable.lamp_more_green(time) != 0.0:
        var_fuzzy.append("more_green")
    return var_fuzzy

def check_rule_fuzzy_lamp(time, distance):
    rule_use = []
    rule = read_rule.read_impediment_lamp_rule()
    var_fuzzy = check_var_fuzzy_lamp(time, distance)
    for i in range(len(rule)):
        attr1, atrr2, attr3 = 0, 0, 0
        for j in range(len(var_fuzzy)):
            if rule[i][0] == var_fuzzy[j]:
                attr1 = 1
            elif rule[i][1] == var_fuzzy[j]:
                atrr2 = 1
            # elif rule[i][2] == var_fuzzy[j]:
            #     attr3 = 1
            if attr1 == 1 and atrr2 == 1:
                rule_use.append(rule[i])
                break
    return rule_use

def calc_speed_lamp(time, distance):
    rules = check_rule_fuzzy_lamp(time, distance)
    # print (rules)
    speed = 0
    for i in range(len(rules)):
        if rules[i][0] == 'more_red':
            lamp_var = fuzzy_variable.lamp_more_red(time)
        elif rules[i][0] == 'red':
            lamp_var = fuzzy_variable.lamp_red(time)
        elif rules[i][0] == 'yellow':
            lamp_var = fuzzy_variable.lamp_yellow(time)
        elif rules[i][0] == 'green':
            lamp_var = fuzzy_variable.lamp_green(time)
        elif rules[i][0] == 'more_green':
            lamp_var = fuzzy_variable.lamp_more_green(time)

        if rules[i][1] == 'near':
            distance_var = fuzzy_variable.distance_near(distance)
        elif rules[i][1] == 'medium':
            distance_var = fuzzy_variable.distance_normal(distance)
        elif rules[i][1] == 'far':
            distance_var = fuzzy_variable.distance_far(distance)

        if rules[i][2] == 'slow':
            speed_avg = 0.0
        elif rules[i][2] == 'normal':
            speed_avg = 20.0
        elif rules[i][2] == 'fast':
            speed_avg = 30.0
        # print(speed, lamp_var, distance_var, speed_avg)
        speed += (lamp_var * distance_var * speed_avg)
    if len(rules) == 0:
        return 30.0
    return speed
# =======================================================================

# ============  STONE  ==============================================
def check_var_fuzzy_stone(distance):
    var_fuzzy = []
    if fuzzy_variable.distance_near(distance) != 0.0:
        var_fuzzy.append("near")
    if fuzzy_variable.distance_normal(distance) != 0.0:
        var_fuzzy.append("medium")
    if fuzzy_variable.distance_far(distance) != 0.0:
        var_fuzzy.append("far")
    return var_fuzzy

def check_rule_fuzzy_stone(distance):
    rule_use = []
    rule = read_rule.read_impediment_stone_rule()
    var_fuzzy = check_var_fuzzy_stone(distance)

    for i in range(len(rule)):
        attr1, atrr2 = 0, 0
        for j in range(len(var_fuzzy)):
            if rule[i][0] == var_fuzzy[j]:
                attr1 = 1
            if attr1 == 1 :
                rule_use.append(rule[i])
                break
    return rule_use

def calc_speed_stone(distance):
    rules = check_rule_fuzzy_stone(distance)
    speed = []
    for i in range(len(rules)):
        if rules[i][0] == 'near':
            distance_var = fuzzy_variable.distance_near(distance)
        elif rules[i][0] == 'medium':
            distance_var = fuzzy_variable.distance_normal(distance)
        elif rules[i][0] == 'far':
            distance_var = fuzzy_variable.distance_far(distance)

        if rules[i][1] == 'slow':
            speed_avg = 0.0
        elif rules[i][1] == 'normal':
            speed_avg = 15.0
        elif rules[i][1] == 'fast':
            speed_avg = 40.0
        # print(angle_var, lamp_var, distance_var, speed_avg)
        speed.append(distance_var * speed_avg)
    if len(speed) == 0:
        return 30.0
    return min(speed)
#==========================================================================

def get_speed (time, lamp_distance, stone_distance):
    return min([calc_speed_lamp(time, lamp_distance), calc_speed_stone(stone_distance)])

print(calc_speed_lamp(11,20))
# print(calc_speed_stone(20))









