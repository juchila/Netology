## Task 1
```bash
strace bin/bash -c 'cd /tmp'

stat("/tmp", {st_mode=S_IFDIR|S_ISVTX|0777, st_size=4096, ...}) = 0
chdir("/tmp")
```

## Task 2

file ищет информацию в файлах magic, magic.mgc  в домашней папке, /etc, /usr/share/misc/

```commandline
stat("/home/vagrant/.magic.mgc", 0x7ffd7ee17000) = -1 ENOENT (No such file or directory)
stat("/home/vagrant/.magic", 0x7ffd7ee17000) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/magic.mgc", O_RDONLY) = -1 ENOENT (No such file or directory)
stat("/etc/magic", {st_mode=S_IFREG|0644, st_size=111, ...}) = 0
openat(AT_FDCWD, "/etc/magic", O_RDONLY) = 3
```

## Task 3
```bash
echo > log.log
```

## Task 4
Зомби процессы не занимают никаких ресурсов

## Task 5

```
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
```commandline
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
