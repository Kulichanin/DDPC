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
