import time
from dummy_data import (
    dummy_speed,
    dummy_battery_temp,
    dummy_motor_rpm,
    dummy_battery_voltage,
    dummy_fault_flag,
    dummy_telemetry_packet
)

def main():
    while True:
        speed = dummy_speed()
        battery_temp = dummy_battery_temp()
        motor_rpm = dummy_motor_rpm()
        battery_voltage = dummy_battery_voltage()
        fault = dummy_fault_flag()

        print("Speed (km/h):", speed)
        print("Battery Temp (C):", battery_temp)
        print("Motor RPM:", motor_rpm)
        print("Battery Voltage (V):", battery_voltage)
        print("Fault:", fault)
        print("-" * 30)

        packet = dummy_telemetry_packet()
        print("Telemetry Packet:", packet)
        print("=" * 30)

        time.sleep(1)

if __name__ == "__main__":
    main()

