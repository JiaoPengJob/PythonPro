#!/usr/bin/python3

# 文件/目录
# 需要导入os包

import os

# 使用当前的uid/gid尝试访问路径
# 第一个参数，用来检测是否有访问权限的路径
# 第二个参数，os.F_OK:测试path是否存在，os.R_OK:测试path是否可读，os.W_OK:测试path是否可写，os.X_OK:测试path是否可执行
ret = os.access("../files/testA.txt", os.F_OK)
print("F--", ret)
ret = os.access("../files/testA.txt", os.R_OK)
print("R--", ret)
ret = os.access("../files/testA.txt", os.W_OK)
print("W--", ret)
ret = os.access("../files/testA.txt", os.X_OK)
print("X--", ret)

# 改变当前工作目录到指定的路径
# path 要切换到的新路径
# os.chdir("path")

# 设置路径的标记为数字标记，多个标记可以使用OR来组合，只支持在Unix下使用
# path 文件名路径或目录路径
# flags ：
"""
stat.UF_NODUMP: 非转储文件
stat.UF_IMMUTABLE: 文件是只读的
stat.UF_APPEND: 文件只能追加内容
stat.UF_NOUNLINK: 文件不可删除
stat.UF_OPAQUE: 目录不透明，需要通过联合堆栈查看
stat.SF_ARCHIVED: 可存档文件(超级用户可设)
stat.SF_IMMUTABLE: 文件是只读的(超级用户可设)
stat.SF_APPEND: 文件只能追加内容(超级用户可设)
stat.SF_NOUNLINK: 文件不可删除(超级用户可设)
stat.SF_SNAPSHOT: 快照文件(超级用户可设)
"""
# os.chflags("path", flags=[])

# 更改文件或目录的权限
# os.chmod("path", mode="")
# path 文件名路径或目录路径
# mode 用以下选项或操作生成，目录的读权限表示可以获取目录里的文件名列表，
# 执行权限表示可以把工作目录切换到此目录，删除添加目录里的文件必须同时拥有写和执行权限
# 文件权限以用户id -- 组id -- 其他顺序检验，最先匹配的允许或禁止权限被应用
"""
stat.S_IXOTH: 其他用户有执行权0o001
stat.S_IWOTH: 其他用户有写权限0o002
stat.S_IROTH: 其他用户有读权限0o004
stat.S_IRWXO: 其他用户有全部权限(权限掩码)0o007
stat.S_IXGRP: 组用户有执行权限0o010
stat.S_IWGRP: 组用户有写权限0o020
stat.S_IRGRP: 组用户有读权限0o040
stat.S_IRWXG: 组用户有全部权限(权限掩码)0o070
stat.S_IXUSR: 拥有者具有执行权限0o100
stat.S_IWUSR: 拥有者具有写权限0o200
stat.S_IRUSR: 拥有者具有读权限0o400
stat.S_IRWXU: 拥有者有全部权限(权限掩码)0o700
stat.S_ISVTX: 目录里文件目录只有拥有者才可删除更改0o1000
stat.S_ISGID: 执行此文件其进程有效组为文件所在组0o2000
stat.S_ISUID: 执行此文件其进程有效用户为文件所有者0o4000
stat.S_IREAD: windows下设为只读
stat.S_IWRITE: windows下取消只读
"""

# 更改文件所有者，如果不修改可以设置为-1，你需要超级用户权限来执行权限修改操作
# 只支持在Unix下操作
# path 设置权限的文件路径
# uid 所属用户id
# gid 所属用户组id
# os.chmwn("path", uid, gid)

# 更改当前进程的根目录为指定的目录，使用该函数需要管理员权限
os.chroot("")

# 关闭指定的文件描述符fd
# fd 即os.open() 打开的对象
os.close()

# 关闭所有文件描述符fd，从fd_low（最小文件描述符）（包含）到fd_high（最大文件描述符）（不包含），错误会忽略
os.closerange(fd_low="", fd_high="")

# 复制文件描述符
os.dup()

# 将一个文件描述符复制到另一个描述符
os.dup2(fd="", fd2="")

# 通过文件描述符改变当前工作目录
os.fchdir(fd="")

# 改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限
"""
mode 可以是以一个或多个组成，多个使用 | 隔开
stat.S_ISUID:设置 UID 位
stat.S_ISGID: 设置组 ID 位
stat.S_ENFMT: 系统文件锁定的执法行动
stat.S_ISVTX: 在执行之后保存文字和图片
stat.S_IREAD: 对于拥有者读的权限
stat.S_IWRITE: 对于拥有者写的权限
stat.S_IEXEC: 对于拥有者执行的权限
stat.S_IRWXU:对于拥有者读、写、执行的权限
stat.S_IRUSR: 对于拥有者读的权限
stat.S_IWUSR: 对于拥有者写的权限
stat.S_IXUSR: 对于拥有者执行的权限
stat.S_IRWXG: 对于同组的人读写执行的权限
stat.S_IRGRP: 对于同组读的权限
stat.S_IWGRP:对于同组写的权限
stat.S_IXGRP: 对于同组执行的权限
stat.S_IRWXO: 对于其他组读写执行的权限
stat.S_IROTH: 对于其他组读的权限
stat.S_IWOTH: 对于其他组写的权限
stat.S_IXOTH:对于其他组执行的权限
"""
os.fchmod(fd="", mode="")

# 修改一个文件的所有权，这个函数修改一个文件的用户id和用户组id，该文件由文件描述符指定
os.fchown(fd="", uid="", gid="")

# 强制将文件写入磁盘，该文件由文件描述符指定，但是不确定更新文件的状态信息，如果需要刷新缓冲区可以使用该方法
os.fdatasync(fd="")

# ？？？？
# 通过文件描述符创建一个文件对象，并返回这个文件对象
# mode 可选，可以指定【r,w,r+,w+,...】（同file的open()）
# bufsize 可选，指定返回的文件对象是否带有缓冲， = 0 表示无缓冲， = 1 表示该文件对象是行缓冲的
#  = 正数 表示使用一个指定大小的缓冲，单位为byte，但是这个大小不是精确的
#  = 负数 表示使用一个系统默认大小的缓冲，对于tty字元设备一般是行缓冲，对于其他文件一般是全缓冲
# 如果该参数未设定，使用系统默认的缓冲设定
os.fdopen(fd="", mode="", bufsize="")

# 16

