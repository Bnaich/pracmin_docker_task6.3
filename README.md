# pracmin_docker_task6.3
simple socket server


Сервер на сокетах, который слушает порт 65432 и писать в файл /var/log/server.log все входящие запросы

Для работы необходимо собрать образ:
```
make build 
```
или просто 
```
make
```
запустить сервер:
```
make start 
```
## Работа...
```
telnet localhost 65432
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
2
OK:2
2
OK:2
3
OK:3
4
OK:4
```
Завершить работу:
```
make stop 
```
Почистить за собой:

```
make clean 
```
