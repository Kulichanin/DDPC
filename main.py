#!/usr/bin/env python3
import logging
from src import sending_command
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger("builder")


def main():
    devices = ["127.0.0.1", "127.0.0.1"]
    with ThreadPoolExecutor(max_workers=2) as executor:
        future_list = []
        for device in devices:
            future = executor.submit(
                sending_command.send_command(device, "mda", "1235789", ["timedatectl", ]))
            future_list.append(future)
        for f in future_list:
            print(f.result())


if __name__ == '__main__':
    main()
