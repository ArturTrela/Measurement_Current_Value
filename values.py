import random
import datetime as dt
CURRENT_LIMIT = 160
VOLTAGE_MIN = 2200
VOLTAGE_MAX = 2300


def make_measure():
    """ In next step values bellow could be changed with data from analog module raspberry pi """

    current_l1 = random.randrange(0, CURRENT_LIMIT) / 10
    voltage_l1 = random.randrange(VOLTAGE_MIN, VOLTAGE_MAX) / 10
    current_l2 = random.randrange(0, CURRENT_LIMIT) / 10
    voltage_l2 = random.randrange(VOLTAGE_MIN, VOLTAGE_MAX) / 10
    current_l3 = random.randrange(0, CURRENT_LIMIT) / 10
    voltage_l3 = random.randrange(VOLTAGE_MIN, VOLTAGE_MAX) / 10

    now = dt.datetime.now()
    act_date = now.strftime("%Y-%m-%d")
    act_hour = now.strftime("%H:%M:%S")

    insert_data = {
        'measure_count': 0,
        'Date': act_date,
        'Hour': act_hour,
        'L1_Current': current_l1,
        'L1_Voltage': voltage_l1,
        'L2_Current': current_l2,
        'L2_Voltage': voltage_l2,
        'L3_Current': current_l3,
        'L3_Voltage': voltage_l3,
    }
    return insert_data
