# DDPC  Convert and copy a file with python paramiko click

Данный скрипт создан для передачи команд на список устройств ввиде json

Создан на версии python 3.9.18

формат файла json:

```json
{
"номер устройства": {
                    "ip": "адрес",
                    "login": "логин",
                    "pass": "пароль"
                    } ,
"номер устройства": {
                    "ip": "адрес",
                    "login": "логин",
                    "pass": "пароль"
                    } , 
}
```

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

Затем забирает вывод команд

Переименовыват по номеру

/dev/disk/by-id/

dd if=/dev/disk/by-id/dm-uuid-LVM-vhNrqTchbdgoTmNNdNR9PJNJTgZsatOy3e8yewCRr4Rt2gXsiLosvF2RPjpqWqA6 of=./efi.boot count=1 bs=512
