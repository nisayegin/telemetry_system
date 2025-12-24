import time
from dummy_data import dummy_telemetry_packet
from logger import log_to_csv

def main():
    while True:
        packet = dummy_telemetry_packet()

        print("Telemetry Data")
        print("-" * 30)
        for key, value in packet.items():
            print(f"{key}: {value}")

        log_to_csv(packet)

        print("=" * 30)
        time.sleep(1)

if __name__ == "__main__":
    main()
