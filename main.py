#!/usr/bin/env python3
import logging
import click

from src import sending_command
from src import reading_files

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger("builder")


def send_command_file(path_file):
    data = reading_files.read_json_file(path_file)
    future_list = []
    for device_number, device_info in data.items():
        click.echo(f"Connecting to a device: {device_number}")
        click.echo(
            f"Device IP: {device_info['ip']}. Login: {device_info['login']}. List Command {device_info['command']}")
        result = sending_command.send_command(
            device_info["ip"], device_info["login"], device_info["pass"], device_info["command"])
        future_list.append(result)
    for result in future_list:
        click.echo(result)


def send_command_one_device(ip, login, passsword, command):
    future_list = list
    result = sending_command.send_command(ip, login, passsword, command)
    future_list.append(result)
    for result in future_list:
        click.echo(result)


@click.command()
@click.option("--name_file", "-f", default=None, help="Path to json file.", type=str)
@click.option("--command", "-c", default=None, help="Send one command to one device", type=(str, str, str, str))
def main(name_file, command):
    if name_file:
        return send_command_file(name_file)
    if command:
        ip, login, password, com = command
        return send_command_one_device(ip, login, password, com)


if __name__ == '__main__':
    main()
