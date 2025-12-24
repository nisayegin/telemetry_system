import random

CAN_IDS = {
    "speed_kmh": 0x101,
    "battery_temp_c": 0x102,
    "motor_rpm": 0x201,
    "battery_voltage_v": 0x301,
    "fault": 0x401
}

def dummy_speed():
    return round(random.uniform(0, 120), 1)

def dummy_battery_temp():
    return round(random.uniform(20, 60), 1)

def dummy_motor_rpm():
    return random.randint(0, 12000)

def dummy_battery_voltage():
    return round(random.uniform(300, 420), 1)

def dummy_fault_flag():
    return random.choice(["OK", "OVERTEMP", "OVERVOLTAGE", "UNDERVOLTAGE"])

def dummy_can_frames():
    return [
        {"can_id": CAN_IDS["speed_kmh"], "data": dummy_speed()},
        {"can_id": CAN_IDS["battery_temp_c"], "data": dummy_battery_temp()},
        {"can_id": CAN_IDS["motor_rpm"], "data": dummy_motor_rpm()},
        {"can_id": CAN_IDS["battery_voltage_v"], "data": dummy_battery_voltage()},
        {"can_id": CAN_IDS["fault"], "data": dummy_fault_flag()}
    ]
