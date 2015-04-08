# getip
Get the target pc ip adress.

本项目用于获取另一网络中某台机器的内网和外网ip地址.


很多家庭宽带用户的ip地址是动态获取的，经常会发生变化，而且通常PC机等设备是通过路由器连上互联网的。 本项目的意义在于，可以在其它网络中随时获取到某局域网中PC机的内外网IP地址，有个内外网IP你可以做很多事情，比如可能通过VNC这样的软件去远程连接该局域网中的PC机(可能需要在路由上进行端口映射)。


项目中包含两个文件夹，即"go"和"python"，分别是两种编程语言的实现，但是目前只有python完成了完整功能并且作者已测试通过，可以正式使用。


项目包含三个应用，分别是IpCollector(见IpCollector.py文件), IpReport(见IpReport文件夹), IpAdmin(见IpAdmin.py)。


IpCollector是服务端，运行在公网服务器上，会启动一个udp服务。负责收集连接过来的客户端的内外网ip地址，并缓存到内存中，一段时间内没有收到某客户端的信息汇报会自动删除该客户端的缓存信息。 直接运行start_IpCollector.sh即是后台运行IpCollector。


IpReport是客户端，运行在众多用户PC机上(暂时只支持windows xp/win7/win8/win10 32位和64位)。 该应用软件会以windows后台服务的形式运行，自动定时向指定的服务器上汇报自己的网络地址。运行过程中定时读取名为C:/IpReport.conf的配置文件。配置文件内容使用json格式，其中比较重要的配置项是uid，指定你的身份信息，如果没有读取到则使用默认值。 默认的uid是使用guid，你可以配置成任意不容易重要的字符串，最好是你经常使用邮箱。


IpAdmin是管理端，用户想要获取IpReport所在机器的内外网ip地址时使用该管理端。使用时输入你在IpReport端配置的uid，就会从IpCollector立即取到uid对应机器的内外网ip地址。



