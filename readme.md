## script1 и script2

 комплект скриптов предназначенных для наполнения Elasticsearch фейковыми данными, консолидации серверных и локальных логов, а также фильтрации подозрительных логов за последний месяц

## Требования к системе

![enter image description here](https://img.shields.io/badge/python-2+-green.svg)
![enter image description here](https://img.shields.io/badge/elasticsearch-6.6.0-green.svg)
## Пользовательский интерфейс
реализован в формате CLI.
## Конфигурация
конфигурация программы настраивается в коде скриптов. Доступные для изменения параметры:

 script1: 

 - es_url - адрес и порт, на котором запущен elasticsearch
 - user_list - список имен, для генерации случайных данных
 - url_list- список внешних url, для генерации случайных данных
 - user_commands - список команд, для генерации случайных данных
 
 script2:
 - es_url - адрес и порт, на котором запущен elasticsearch
 
 ## Запуск
    путь_к_python.exe script1
    путь_к_python.exe script2
В результате выполнения будет сгенерировано 20 фейковых записей в Elasticsearch, и сформирован итоговый консолидированный JSON о подозрительной активности пользователей за последний месяц.

    {
		"timestamp": "2019.02.01 17:35:12.456",
		"user": "Ivanov_Ivan",
		"src_ip": "192.168.0.1",
		"dst_ip": "192.0.2.0",
		"url": "http://example.com",
		"cmd": "wget http://example.com"
	}
