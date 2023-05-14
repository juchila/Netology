# Домашнее задание к занятию «Языки разметки JSON и YAML»

### Цель задания

В результате выполнения задания вы:

* познакомитесь с синтаксисами JSON и YAML;
* узнаете, как преобразовать один формат в другой при помощи пары строк.

### Чеклист готовности к домашнему заданию

1. Установлена библиотека PyYAML для Python 3.

### Инструкция к заданию 

1. Скопируйте в свой .md-файл содержимое этого файла, исходники можно посмотреть [здесь](https://raw.githubusercontent.com/netology-code/sysadm-homeworks/devsys10/04-script-03-yaml/README.md).
3. Заполните недостающие части документа решением задач — заменяйте `???`, остальное в шаблоне не меняйте, чтобы не сломать форматирование текста, подсветку синтаксиса. Вместо логов можно вставить скриншоты по желанию.
4. Любые вопросы по выполнению заданий задавайте в чате учебной группы или в разделе «Вопросы по заданию» в личном кабинете.

### Дополнительные материалы

1. [Полезные ссылки для модуля «Скриптовые языки и языки разметки».](https://github.com/netology-code/sysadm-homeworks/tree/devsys10/04-script-03-yaml/additional-info)

------

## Задание 1

Мы выгрузили JSON, который получили через API-запрос к нашему сервису:

```
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            }
            { "name" : "second",
            "type" : "proxy",
            "ip : 71.78.22.43
            }
        ]
    }
```
  Нужно найти и исправить все ошибки, которые допускает наш сервис.

### Ваш скрипт:
"ip" : 7175 - вот тут не понятно, это криво преобразованные данные,
которые надо поправить в нормальный ip адрес и заключить в кавычки,
или все-таки необходимое цифровое значение?  
А также знак табуляции в первой строке - это необходимый элемент текстовой части?  
```
{"info": "Sample JSON output from our service\t",
        "elements": [
            {"name": "first",
            "type": "server",
            "ip" : 7175 
            },
            {"name": "second",
            "type" : "proxy",
            "ip" : "71.78.22.43"
            }
        ]
    }
```

---

## Задание 2

В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML-файлов, описывающих наши сервисы. 

Формат записи JSON по одному сервису: `{ "имя сервиса" : "его IP"}`. 

Формат записи YAML по одному сервису: `- имя сервиса: его IP`. 

Если в момент исполнения скрипта меняется IP у сервиса — он должен так же поменяться в YAML и JSON-файле.

### Ваш скрипт:

```python
#! /usr/bin/env python3

import json, yaml, os, socket
hosts=["drive.google.com","mail.google.com","google.com"]
file_js="oldip.json"
file_yml='oldip.yaml'
str1 = {}
rewr = False
if os.path.exists(file_js):
    with open(file_js, 'r') as f:
        oldip = f.read()
    print("Прошлые значения "+oldip)
    oldip=json.loads(oldip)
else:
    oldip = {}
print("Новые значения:")
for h in hosts:
    host=socket.gethostbyname(h)
    str0 = h+" - "+host
    str1[h] = host
    print(str0)
    if len(oldip)>0:
        if oldip.get(h)!=host:
            print("[ERROR] "+h+" IP mismatch: "+oldip[h]+" "+host)
            rewr = True
    else:
        rewr = True
    if rewr:
        with open(file_js, 'w') as f:
            f.write(json.dumps(str1))
        with open(file_yml, 'w') as f:
            f.write(yaml.dump(str1, explicit_start=True, explicit_end=True))
```
Вариант 2, в котором, как я понимаю, ERROR не выскочит, так как полные списки адресов обычно не меняются
```python
#! /usr/bin/env python3
import json, yaml, os, socket
hosts=["drive.google.com","mail.google.com","google.com"]
file_js="oldip.json"
file_yml='oldip.yaml'
str1 = {}
rewr = False
if os.path.exists(file_js):
    with open(file_js, 'r') as f:
        oldip = f.read()
    print("Прошлые значения "+oldip)
    oldip=json.loads(oldip)
else:
    oldip = {}
print("Новые значения:")
for h in hosts:
    host=socket.gethostbyname_ex(h)
    str0 = h+" - "+str(host[2])
    str1[h] = host
    print(str0)
    if len(oldip)>0:
         dfr=list(set(oldip[h][2]) ^ set(host[2]))
         print("[info] "+h+"different IP: "+str(dfr))
         if len(dfr)>0:
            print("[ERROR] "+h+" IP mismatch: "+str(dfr))
            rewr = True
    else:
        rewr = True
    if rewr:
        with open(file_js, 'w') as f:
            f.write(json.dumps(str1))
        with open(file_yml, 'w') as f:
            f.write(yaml.dump(str1, explicit_start=True, explicit_end=True))
```

### Вывод скрипта при запуске во время тестирования:

```
Прошлые значения {"drive.google.com": "64.233.165.194", "mail.google.com": "74.125.205.19", "google.com": "209.85.233.139"}
Новые значения:
drive.google.com - 64.233.165.194
mail.google.com - 74.125.205.19
google.com - 209.85.233.139
```

### JSON-файл(ы), который(е) записал ваш скрипт:
[json](oldip.json)
```json
{"drive.google.com": "64.233.165.194", "mail.google.com": "74.125.205.19", "google.com": "209.85.233.139"}
```

### YAML-файл(ы), который(е) записал ваш скрипт:
[yaml](oldip.yaml)
```yaml
---
drive.google.com: 64.233.165.194
google.com: 209.85.233.139
mail.google.com: 74.125.205.19
...
```
### Вывод скрипта при запуске во время тестирования 2:
```
Прошлые значения {"drive.google.com": ["wide-docs.l.google.com", ["drive.google.com"], ["64.233.165.194"]], "mail.google.com": ["mail.google.com", [], ["74.125.205.19", "74.125.205.18", "74.125.205.17", "74.125.205.83"]], "google.com": ["google.com", [], ["209.85.233.139", "209.85.233.100", "209.85.233.102", "209.85.233.101", "209.85.233.113", "209.85.233.138"]]}
Новые значения:
drive.google.com - ['64.233.165.194']
[info] drive.google.com different IP: []
mail.google.com - ['74.125.205.19', '74.125.205.18', '74.125.205.17', '74.125.205.83']
[info] mail.google.com different IP: []
google.com - ['209.85.233.139', '209.85.233.100', '209.85.233.102', '209.85.233.101', '209.85.233.113', '209.85.233.138']
[info] google.com different IP: []
drive.google.com: !!python/tuple
- wide-docs.l.google.com
- - drive.google.com
- - 64.233.165.194
google.com: !!python/tuple
- google.com
- []
- - 209.85.233.139
  - 209.85.233.100
  - 209.85.233.102
  - 209.85.233.101
  - 209.85.233.113
  - 209.85.233.138
mail.google.com: !!python/tuple
- mail.google.com
- []
- - 74.125.205.19
  - 74.125.205.18
  - 74.125.205.17
  - 74.125.205.83
```
### JSON-файл(ы), который(е) записал ваш скрипт:
[json](oldip2.json)
```json
{"drive.google.com": ["wide-docs.l.google.com", ["drive.google.com"], ["64.233.165.194"]], "mail.google.com": ["mail.google.com", [], ["74.125.205.19", "74.125.205.18", "74.125.205.17", "74.125.205.83"]], "google.com": ["google.com", [], ["209.85.233.139", "209.85.233.100", "209.85.233.102", "209.85.233.101", "209.85.233.113", "209.85.233.138"]]}
```

### YAML-файл(ы), который(е) записал ваш скрипт:
[yaml](oldip2.yaml)
```yaml
---
drive.google.com: !!python/tuple
- wide-docs.l.google.com
- - drive.google.com
- - 64.233.165.194
google.com: !!python/tuple
- google.com
- []
- - 209.85.233.139
  - 209.85.233.100
  - 209.85.233.102
  - 209.85.233.101
  - 209.85.233.113
  - 209.85.233.138
mail.google.com: !!python/tuple
- mail.google.com
- []
- - 74.125.205.19
  - 74.125.205.18
  - 74.125.205.17
  - 74.125.205.83
...

```
---

## Задание со звёздочкой* 

Это самостоятельное задание, его выполнение необязательно.
____

Так как команды в нашей компании никак не могут прийти к единому мнению о том, какой формат разметки данных использовать: JSON или YAML, нам нужно реализовать парсер из одного формата в другой. Он должен уметь:

   * принимать на вход имя файла;
   * проверять формат исходного файла. Если файл не JSON или YAML — скрипт должен остановить свою работу;
   * распознавать, какой формат данных в файле. Считается, что файлы *.json и *.yml могут быть перепутаны;
   * перекодировать данные из исходного формата во второй доступный —  из JSON в YAML, из YAML в JSON;
   * при обнаружении ошибки в исходном файле указать в стандартном выводе строку с ошибкой синтаксиса и её номер;
   * полученный файл должен иметь имя исходного файла, разница в наименовании обеспечивается разницей расширения файлов.

### Ваш скрипт:

```python
#! /usr/bin/env python3

import os, sys, json, yaml, re, magic

mime = magic.Magic(mime=True)

file_f=sys.argv[1]
fn=os.path.splitext(file_f)[0]
ext=os.path.splitext(file_f)[1]
some_dict = {}
print("file "+fn+" ext  "+ext+"\nmagic type "+magic.from_file(file_f))
with open(file_f, 'r') as f:
    if ext==".json":
        try:
            some_dict = json.load(f)
            print("format is JSON")
            with open(fn+".yml",'w') as f:
                f.write(yaml.dump(some_dict, explicit_start=True, explicit_end=True))
        except json.JSONDecodeError as e:
                print(e)
#                print("File "+file_f+" is not JSON or YAML or file have a mistake")
    elif re.match('(\.yaml|\.yml)',ext):
        try:
            some_dict = yaml.safe_load(f)
            print("format is YAML")
            with open(fn+".json",'w') as f:
                f.write(json.dumps(some_dict))
        except yaml.YAMLError as e:
            print(e)
#            print("File "+file_f+" is not YAML or JSON or file have a mistake")

    else:
        print("Not right extension")

```

### Пример работы скрипта:

./py-format.py js.yml
file js ext  .yml
magic type JSON text data
format is YAML

./py-format.py json.json
file json ext  .json
magic type JSON text data
format is JSON

./py-format.py json.json
file json ext  .json
magic type ASCII text
Expecting ',' delimiter: line 7 column 13 (char 183)
----

### Правила приёма домашнего задания

В личном кабинете отправлена ссылка на .md-файл в вашем репозитории.

-----

### Критерии оценки

Зачёт:

* выполнены все задания;
* ответы даны в развёрнутой форме;
* приложены соответствующие скриншоты и файлы проекта;
* в выполненных заданиях нет противоречий и нарушения логики.

На доработку:

* задание выполнено частично или не выполнено вообще;
* в логике выполнения заданий есть противоречия и существенные недостатки.  
 
Обязательными являются задачи без звёздочки. Их выполнение необходимо для получения зачёта и диплома о профессиональной переподготовке.

Задачи со звёздочкой (*) являются дополнительными или задачами повышенной сложности. Они необязательные, но их выполнение поможет лучше разобраться в теме.