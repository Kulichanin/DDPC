# DDPC  Convert and copy a file with python paramiko click

Данный скрипт создан для передачи команд на список устройств ввиде json

Создан на версии python 3.9.18

формат файла json:

```json
{
    "device_number1": {
        "ip": "адрес",
        "login": "логин",
        "pass": "пароль",
        "command": [
            "команда1",
            "команда2"
        ]
    },
    "device_number2": {
        "ip": "адрес",
        "login": "логин",
        "pass": "пароль",
        "command": [
            "команда3"
        ]
    }
}
```

Приведен пример в example.json

Основная информация по командам:

```bash
Usage: main.py [OPTIONS]

Options:
  -f, --name_file TEXT            Path to json file.
  -c, --command <TEXT TEXT TEXT TEXT>...
                                  Send one command to one device
  --help                          Show this message and exit.
```
