## Task 1
sparse файлы - файлы, в которых свободное место (нулевые байты) заменены на информацию о последовательности этих байтов(дырах)

экономит место, но имеет свои ограничения
## Task 2
Жесткие ссылки ссылаются на одну inode и имеют один набор разрешений, что и у исходного файла,
поэтому разные разрешения установить не удастся

## Task 3
![img_21.png](img_21.png)
## Task 4
![img_19.png](img_19.png)
## Task 5
```
sudo sfdisk -d /dev/sdb > part-sdb
sudo sfdisk -f /dev/sdc < part-sdb
```
![img_20.png](img_20.png)

## Task 6-16
```
sudo mdadm --create -l1  /dev/md0 -n2 /dev/sdb1 /dev/sdc1
sudo mdadm --create -l0  /dev/md1 -n2 /dev/sdb2 /dev/sdc2
sudo pvcreate -v /dev/md0
sudo pvcreate -v /dev/md1
sudo vgcreate -v VG-common /dev/md0 /dev/md1
sudo lvcreate -L 100M VG-common /dev/md1
sudo mkfs.ext4  /dev/VG-common/lvol0
sudo mkdir /mnt/disk
sudo mount /dev/VG-common/lvol0 /mnt/disk
sudo pvmove /dev/md1 /dev/md0
```
![img_22.png](img_22.png)
![img_23.png](img_23.png)
![img_26.png](img_26.png)
![img_25.png](img_25.png)
![img_24.png](img_24.png)
![img_27.png](img_27.png)
![img_28.png](img_28.png)

## Task 17-18
```
vagrant@sysadm-fs:~$ sudo mdadm /dev/md0 --fail /dev/sdb1
mdadm: set /dev/sdb1 faulty in /dev/md0
```
![img_29.png](img_29.png)
## Task 19
![img_30.png](img_30.png)