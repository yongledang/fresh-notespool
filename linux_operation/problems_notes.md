[TOC]

Note:  

- `for ubuntu: install command begins with`<font color='red'>` "sudo apt-get"`</font>` in general, such as "sudo apt-get install lrzsz"; `
- `for centOS: install command begins with`  <font color=red>`"yum "`</font> `in general, such as "yum install lrzsz" `

### 1. 安装deb文件

- cd到deb所在目录，`sudo dpkg -i <deb_file>`
- 安装依赖： `sudo apt -f install`

### 2. 查看ip信息和端口

- LINUX

`ifconfig -a`     (`windows: ipconfig`) 

`netstat -a` (`查看已经连接的服务端口（ESTABLISHED）`)

`sudo netstat -ap` (`查看所有的服务端口（LISTEN，ESTABLISHED）`)

`lsof  -i:port` or `netstat -nap | grep port` (查看端口`port`对应的应用程序 )

```
klaus@ubuntu:~/Downloads$ netstat -nap | grep 8080
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to seesudo it all.)
udp        0      0 0.0.0.0:8080            0.0.0.0:*     23490/mNetAssist

klaus@ubuntu:~/Downloads$ lsof -i:8080
COMMAND     PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
mNetAssis 23490 klaus   23u  IPv4 169491      0t0  UDP *:http-alt 
```

- WINDOS

  `ipconfig` (`查看ip`)

  `netstat -ano` (`查看端口`)

  `netstat  -aon | findstr  1044`  查看端口1044是否被占用，若被占用最后面的数字就是当前程序或服务的`pid`

  `tasklist|findstr 2612`    查看`pid 2612`(`该pid对应的端口号是1044`)对应的应用程序 

  > `input: tasklist|findstr 9744`
  >
  > `output: SkypeApp.exe                  9744 Console                    1     58,520 K`

### 3. 查看用户列表   用户管理

```
cat /etc/passwd			# 查看用户列表
cat /etc/group			# 查看所有用户组
```

### 4. `ssh`远程连接服务器

```
sudo ps -e | grep ssh			# 查看ssh是否启动，有sshd说明已经启动
sudo service ssh start 			# 启动ssh服务

# 安装文件传输工具包 lrzsz,xshell连接上之后，在xshell命令框输入：
sudo apt-get install lrzsz		# 安装工具包
# 上传文件从windows打linux，在xshell命令框中输入：
rz							  # 弹窗让选择需上传的文件(貌似只能传单个或多个文件，不能直接传文件夹）
# 从linux服务器下载文件到windows，在xshell命令框中输入：sz [需要下载的文件名]
sz testfile.py				   # 执行时会弹窗让你选择文件保存的路径
```

- 连接不上ssh：**SSH的配置文件中默认不用于使用root账户进行远程SSH登录**

  修改配置文件：`etc/ssh/sshd_config: ` `PermitRootLogin prohibit-password` --> `PermitRootLogin yes`

  

  

### 5. CPU和GPU相关

- 查看CPU和内存

  ```
  free -m			         	# 单独查看内存使用情况 -m也可以不要
  $ top						#查看内存及CPU使用情况的命令
  
  $ sudo apt-get install htop   #安装htop
  $ htop 						#查看内存及CPU使用情况
  ```

- 查看是否有`GPU:` 

  ```
  $ nvidia-smi #查看一次
  $ watch -n 1 nvidia-smi 		#实时查看，1秒刷新1次
  
  $ pip install gpustat
  $ watch --color -n1 gpustat -cpu #动态实时监控GPU的使用情况
  
  $ nvidia-smi -L 				#list all available NVIDIA devices
  
  $ sudo fuser -v /dev/nvidia* 	 #查找占用GPU资源的PID
  
  $ sudo kill -9 ***(PID) 		 #解除显存占用
  
  $ lspci | grep -i vga 			#查看显卡信息
  $ lspci | grep -i nvidia 		#查看nvidia显卡信息
  $ lspci | egrep 'VGA|3D' 		#显示所有显卡信息
  ```

  `lspci | grep -i nvidia`

  

### 6. vim相关

1. `vim 使用了 ctrl+s 之后出现界面锁死情况解决方法：``ctrl+q解除锁死`



### 7. Error

- 鼠标拖动终端的窗口，就会产生一个^C中断:  将WIN上运行的各种词典关闭屏幕取词



## CentOS

### 1. General Command

#### 1. 图形化界面启动

- centOS命令行界面后输入 startx  即可进入图形化界面（有安装的话）

#### 2. 关机指令

```
centos关机命令：
1、halt 立马关机(不建议使用)
2、shutdown -h 10 1分钟后自动关机
3、poweroff 立刻关机,并且电源也会断掉
4、shutdown -h now 立刻关机(root用户使用, 推荐使用)
如果是通过shutdown命令设置关机的话，可以用shutdown -c命令取消重启
```




