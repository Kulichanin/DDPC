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

## Постановка задачи

Необходимо написать небольшой скрипт, который принимает на вход строку или файла json с данными для подлючения к устройствам на UNIX-системах по OpenSSH.

После подключения дает следущие команды:

```bash
#первый сектор HDD bak
dd if=/dev/disks/mpx.vmhba0:C0:T0:L0 of=/vmfs/volumes/datastore1/hdd.mbr count=1 bs=512
```

```bash
#первый сектор EFI
dd if=/dev/disks/mpx.vmhba0:C0:T0:L0:1 of=/vmfs/volumes/datastore1/efi.boot count=1 bs=512
```
