import logging

from paramiko import SSHClient
from time import sleep
from socket import timeout

MAX_BYTES = 60000

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger("builder")


def send_command(ip: str, username: str, password: str, commands: list) -> dict:
    client = SSHClient()
    client.connect(hostname=ip, username=username,
                   password=password, look_for_keys=False, allow_agent=False)

    logging.info(f"Connection in {ip}")

    result = {}

    with client.invoke_shell() as ssh:
        for command in commands:
            ssh.send(f"{command}\n")
            logging.info(f"Send {command}")
            ssh.settimeout(5)
            ssh.recv(MAX_BYTES)

            output = ""
            while True:
                try:
                    part = ssh.recv(MAX_BYTES).decode("utf-8")
                    output += part
                    sleep(0.5)
                except timeout:
                    break
            result[command] = output

        return result
