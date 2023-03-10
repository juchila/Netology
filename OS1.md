## Task 1
```bash
strace bin/bash -c 'cd /tmp'

stat("/tmp", {st_mode=S_IFDIR|S_ISVTX|0777, st_size=4096, ...}) = 0
chdir("/tmp")
```

## Task 2

file ищет информацию в файлах magic, magic.mgc  в домашней папке, /etc, /usr/share/misc/

```bash
stat("/home/vagrant/.magic.mgc", 0x7ffd7ee17000) = -1 ENOENT (No such file or directory)
stat("/home/vagrant/.magic", 0x7ffd7ee17000) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/magic.mgc", O_RDONLY) = -1 ENOENT (No such file or directory)
stat("/etc/magic", {st_mode=S_IFREG|0644, st_size=111, ...}) = 0
openat(AT_FDCWD, "/etc/magic", O_RDONLY) = 3
```

## Task 3 + UPDATE
```bash
lsof -p <PID> | grep deleted -  смотрим, какие файлы удалены, но запись продолжается
hard link на файл удален, но у процесса в директории /proc/<PID>/fd будет дескриптор, например:
vagrant@vagrant:~$ ps aux | grep ping
vagrant     7766  0.0  0.0   7092   928 pts/0    S    16:57   0:00 ping 127.0.0.1
vagrant@vagrant:~$ sudo lsof -p 7766 | grep delete
ping    7766 vagrant    1w   REG  253,0   180441 1310814 /home/vagrant/test (deleted)
vagrant@vagrant:~$ cat test
cat: test: No such file or directory
vagrant@vagrant:~$ sudo cat /proc/7766/fd/1 > /home/vagrant/test
vagrant@vagrant:~$ cat test
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=2.27 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.028 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.056 ms
64 bytes from 127.0.0.1: icmp_seq=4 ttl=64 time=0.037 ms
64 bytes from 127.0.0.1: icmp_seq=5 ttl=64 time=0.040 ms
64 bytes from 127.0.0.1: icmp_seq=6 ttl=64 time=0.033 ms
64 bytes from 127.0.0.1: icmp_seq=7 ttl=64 time=0.040 ms
64 bytes from 127.0.0.1: icmp_seq=8 ttl=64 time=0.029 ms
64 bytes from 127.0.0.1: icmp_seq=9 ttl=64 time=0.047 ms

данные восстановились, но, как я понял, не обновляются, т.е данные можно вытащить, но придется каждый раз копировать их,
ну или перезапускать процесс, для создания ссылки на новый файл.
```
#### UPDATE 3
по поводу замечания:  
![img_16.png](img_16.png)  
судя по выводу - команда cat не встроенная, должна запускаться в новом процессе, а по поведению - получается встроенная
```bash
для обнуления данных можно использовать команды:
1. sudo bash -c 'echo > /proc/7766/fd/1' 
2. sudo bash -c 'cat /dev/null > /proc/7766/fd/1'
3. sudo truncate -s 0 /proc/7766/fd/1
но это все работает при условии, что перенаправление вывода было сделано через '>>', а не '>', т.е
команда выглядела так: ping 127.0.0.1 >> test &
```
![img_10.png](img_10.png)
```
тут PID уже другой, но сути не меняет.
как сделать обнуление, если перенаправление было через '>' - я не нашел, точнее есть вариант через GDB - но это другой вопрос.
ну а по найденой информации обнулить можно, если файл был открыт с директивой O_APPEND(т.е на добавление изменений), что в общем то соотвествует '>>'
На этом я сдаюсь, не понимаю куда копать.
```

## Task 4
Зомби процессы не занимают никаких ресурсов

## Task 5

```bash
openat(AT_FDCWD, "/etc/ld.so.cache
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libpthread.so.0", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libdl.so.2", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libutil.so.1", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libm.so.6", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libexpat.so.1", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libz.so.1", O_RDONLY|O_CLOEXEC) = 3
далее много файлов для работы с python3
```

## Task 6
'uname -a' использует системный вызов 'uname'
```
man 2 uname
Part of the utsname information is also accessible via /proc/sys/kernel/{ostype, hostname, osrelease, version, domainname}
```

## Task 7
```
; - используется для последовательного запуска команд
&& - следующая команда запустится только в случае успешного выполнения предыдущей команды, т.е после возвращения ею 0
установка set -e завершит выполнение текущего терминала в случае ошибки,
поэтому , видимо, нет особого смысла использовать set -e и &&, ну или точнее я пока не вижу такого смысла
```

## Task 8
```
set -euxo pipefail - устанавливает вывод в консоль команды, которая завершилась с ошибкой, со всеми параметрами и переменными, которые могли быть заданы
удобно для отладки и выявления проблемы
```
## Task 9
```bash
ps -o stat
STAT
S   
S   
S+  
S+  
Ss+ 

S    interruptible sleep (waiting for an event to complete)
s    is a session leader
+    is in the foreground process group
```
