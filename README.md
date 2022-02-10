# trade_env

- 报错 dmidecode not found

  通常默认都有装，加一下dmidecode命令的相关路径到PATH，一般是/usr/sbin
- 报一堆 permission denied

  给dmidecode加下权限`sudo chmod a+s /usr/sbin/dmidecode`

- 拿不到硬盘序列号

  Debian系可以`sudo adduser username disk`把自己加到disk组（加完需要重新登录，输入`groups`确认自己已经在disk组里），或者直接给磁盘设备文件加读权限`sudo chmod a+r /dev/sda`

- 不知道什么情况，xx数据拿不到

  用以下python脚本自己慢慢试吧，当打印出来是第一行结果是0则成功了，否则是-1。第二行是取到的信息，格式为```(操作系统类型)@(信息采集时间)@(内网IP1)@(内网IP2)@(网卡MAC1)@(网卡MAC2)@(设备名)@(操作系统版本)@(Disk_ID)@(CPU_ID)@(BIOS_ID)```



## 参考
https://github.com/keli/ctp-python
