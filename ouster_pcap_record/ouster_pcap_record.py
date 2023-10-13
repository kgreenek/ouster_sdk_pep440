import argparse
import contextlib
from datetime import datetime
import os

import ouster.client
import ouster.pcap

DEFAULT_LIDAR_PORT = 7502
DEFAULT_IMU_PORT = 7403
DEFAULT_OUT_DIR = "."
OUSTER_BUF_SIZE = 640
FILENAME_TIME_FMT = "%Y-%m-%d-%H-%M-%S"


def _parse_args():
    parser = argparse.ArgumentParser(description="Records pcap data from an ouster unit")
    parser.add_argument("--hostname", required=True, help="hostname of the ouster unit")
    parser.add_argument("--lidar_port", default=DEFAULT_LIDAR_PORT, help="Port for the lidar data")
    parser.add_argument("--imu_port", default=DEFAULT_IMU_PORT, help="Port for the IMU data")
    parser.add_argument("--out_dir",
                        "-o",
                        default=DEFAULT_OUT_DIR,
                        help="Directory where metadata and pcap files will be saved")
    return parser.parse_args()


def main():
    args = _parse_args()

    # Connect to sensor and record lidar/imu packets until ctrl-c is pressed.
    with contextlib.closing(
            ouster.client.Sensor(args.hostname,
                                 args.lidar_port,
                                 args.imu_port,
                                 buf_size=OUSTER_BUF_SIZE)) as source:

        time_part = datetime.now().strftime(FILENAME_TIME_FMT)
        meta = source.metadata
        fname_base = f"{meta.prod_line}_{meta.sn}_{meta.mode}_{time_part}"

        metadata_path = os.path.join(args.out_dir, f"{fname_base}.json")
        print(f"Saving sensor metadata to: {metadata_path}")
        source.write_metadata(metadata_path)

        pcap_path = os.path.join(args.out_dir, f"{fname_base}.pcap")
        print(f"Writing to: {pcap_path} (ctrl-c to stop)")
        ouster.pcap.record(source, pcap_path)


if __name__ == "__main__":
    main()

