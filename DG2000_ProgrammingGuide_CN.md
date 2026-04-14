# DG2000 系列函数/任意波形发生器

2019 年 8 月 

RIGOL (SUZHOU) TECHNOLOGIES INC. 

# 保证和声明

# 版权

$©$ 2019 苏州普源精电科技有限公司 

# 商标信息

RIGOL 是苏州普源精电科技有限公司的注册商标。 

# 文档编号

PGB12000-1110 

# 软件版本

00.02.01 

软件升级可能更改或增加产品功能，请关注 RIGOL 网站获取最新版本手册或联系 RIGOL 升级软件。 

# 声明

本公司产品受中国及其它国家和地区的专利（包括已取得的和正在申请的专利）保护。 

本公司保留改变规格及价格的权利。 

本手册提供的信息取代以往出版的所有资料。 

本手册提供的信息如有变更，恕不另行通知。 

. 对于本手册可能包含的错误，或因手册所提供的信息及演绎的功能以及因使用本手册而导致的任何偶然 或继发的损失，RIGOL 概不负责。 

未经 RIGOL 事先书面许可，不得影印、复制或改编本手册的任何部分 

# 产品认证

RIGOL 认证本产品符合中国国家产品标准和行业产品标准及 ISO9001:2015 标准和 ISO14001:2015 标准， 并进一步认证本产品符合其它国际标准组织成员的相关标准。 

# 联系我们

如您在使用此产品或本手册的过程中有任何问题或需求，可与 RIGOL 联系： 

电子邮箱：service@rigol.com 

网址：www.rigol.com 

# 文档概述

本手册详细介绍通过远程接口对信号发生器进行编程的操作方法。 

# 文档的主要内容：

# 第 1 章 编程概述

本章简介如何建立信号发生器与计算机之间的远程通信，远程控制信号发生器的方法和 SCPI 命令的格式、 符号、参数类型以及缩写规则。 

# 第 2 章 命令系统

本章以字母 A-Z的顺序逐条介绍 DG2000 各命令的格式、功能、参数以及使用说明等。 

# 第 3 章 应用实例

本章给出信号发生器主要功能的应用实例。该实例由一系列命令组合而成，实现信号发生器的基本功能。 

# 第 4 章 编程实例

本章给出如何使用 Visual $\complement + +$ 、Visual Basic 以及 LabVIEW 等开发工具编程控制 DG2000。 

# 第 5 章 附录

本章给出命令列表、出厂设置值列表等信息。 

# 提示

本手册的最新版本可登陆RIGOL官网（www.rigol.com）进行下载。 

# 文档的格式约定：

# 1. 按键：

本手册中通常用“文本框 $^ +$ 文字（加粗）”表示前面板上的一个按键，如 Pulse/Utility。 

# 2. 菜单标签：

本手册通常用“字符底纹 $^ +$ 文字（加粗）”表示一个菜单标签，如 系统设置。 

# 3. 操作步骤：

本手册中通常用箭头“”表示下一步操作。例如：在 Shift 键背灯变亮状态，按 Pulse/Utility  系 统设置 表示按下前面板上的 Pulse/Utility 功能键后再触摸点击 系统设置 菜单标签。 

# 文档的内容约定：

DG2000系列函数/任意波形发生器包含以下型号。如无特殊说明，本手册以DG2102为例介绍各命令的使用 方法。 

<table><tr><td>型号</td><td>通道数</td><td>最大输出频率</td></tr><tr><td>DG2052</td><td>2</td><td>50MHz</td></tr><tr><td>DG2072</td><td>2</td><td>70MHz</td></tr><tr><td>DG2102</td><td>2</td><td>100MHz</td></tr></table>

# 目录

保证和声明.. 

文档概述. 

第 1 章 编程概述.. .1-1 

建立远程通信. . 1-2 

远程控制方法. . 1-4 

SCPI 命令简介 .. . 1-4 

命令格式.. . 1-4 

符号说明. .. 1-5 

参数类型. . 1-5 

命令缩写.. .. 1-6 

第 2 章 命令系统... ..2-1 

:COUNter 命令.. . 2-2 

:COUPling 命令 .. . 2-8 

:DISPlay 命令 ........... .. 2-19 

:HCOPy 命令 ...... . 2-21 

IEEE488.2 通用命令.. . 2-22 

:LXI 命令... . 2-28 

:MEMory 命令.. . 2-29 

:MMEMory 命令 . . 2-32 

:OUTPut 命令 .. . 2-41 

:ROSCillator 命令 .. . 2-46 

:SOURce 命令.. . 2-47 

:SOURce:APPLy 命令 . . 2-48 

:SOURce:BURSt 命令.. . 2-55 

:SOURce:FREQuency 命令 . . 2-62 

:SOURce:FUNCtion 命令 . 2-69 

:SOURce:HARMonic 命令 . . 2-84 

:SOURce:MARKer 命令 . . 2-88 

:SOURce[:MOD]:AM 命令 . . 2-89 

:SOURce[:MOD]:ASKey 命令.. . 2-93 

:SOURce[:MOD]:FM 命令.. . 2-96 

:SOURce[:MOD]:FSKey 命令 . . 2-99 

:SOURce[:MOD]:PM 命令.. . 2-102 

:SOURce[:MOD]:PSKey 命令 . . 2-105 

:SOURce[:MOD]:PWM 命令.. . 2-109 

:SOURce:MOD 命令... . 2-113 

:SOURce:PERiod 命令.. . 2-115 

:SOURce:PHASe 命令 . 2-116 

:SOURce:PULSe 命令.. . 2-117 

:SOURce:SUM 命令 . . 2-119 

:SOURce:SWEep 命令.. . 2-122 

:SOURce:TRACe 命令 . 2-128 

:SOURce:TRACK 命令.. . 2-129 

:SOURce:VOLTage 命令 .. . 2-129 

:SYSTem 命令.. . 2-134 

:TRIGger 命令 .......... .. 2-148 

第 3 章 应用实例... ..3-1 

输出基本波.. .. 3-2 

输出任意波.. .3-2 

输出谐波 . ..3-3 

输出 AM 调制波形 .3-3 

输出 FSK 调制波形 .. ....3-4 

输出 Sweep 波形. .3-4 

输出 Burst 波形 .. ..3-5 

使用频率计功能 ..3-5 

# 第 4 章 编程实例.. . 4-1

编程准备 . ..4-2 

Excel 编程实例. ..4-3 

Matlab 编程实例.. ..4-6 

LabVIEW 编程实例 . ..4-8 

Visual Basic 编程实例 . ..4-15 

Visual $\complement + +$ 编程实例. ..4-18 

# 第 5 章 附录. . 5-1

附录 A：出厂设置 . ..5-1 

附录 B：保修概要. ..5-5 

# 第1章 编程概述

本章简介如何建立信号发生器与计算机之间的远程通信，远程控制信号发生器的方法和 SCPI 命令的格式、 符号、参数类型以及缩写规则。 

# 本章主要内容：

$\spadesuit$ 建立远程通信 

$\spadesuit$ 远程控制方法 

 SCPI 命令简介 

# 建立远程通信

您可以通过 USB（USB DEVICE）、LAN 或 GPIB（通过 USB HOST 接口由 USB-GPIB 模块扩展）接口建立 DG2000 与计算机之间的远程通信。 

# 操作步骤：

# 1. 安装 Ultra Sigma 通用 PC 软件

请登陆 RIGOL 官网（www.rigol.com）下载 Ultra Sigma 通用 PC 软件并按照指导进行安装。 

# 2. 连接并配置仪器的接口参数

DG2000 支持 USB、LAN 和 GPIB（通过 USB HOST 接口由 USB-GPIB 模块扩展）三种通信接口，如下 图所示。 

![](images/d091ff44fae5985f2028809684cdd9a8e2519a2feea6b0ca1d2f5a7eeaaa0748.jpg)



图 1-1 DG2000 通信接口


1) 使用 USB 接口：使用 USB 数据线连接 DG2000 后面板 USB DEVICE 接口和计算机的 USB HOST 接 口，计算机上将弹出“硬件更新向导”对话框，请按照向导的提示安装“USB Test and Measurement Device (IVI)”（请参考《DG2000用户手册》第 3章“远程控制”中的“通过 USB 控制”一节）。 

2) 使用 LAN 接口： 

确保您的计算机已经接入局域网。 

确认您的局域网是否支持 DHCP 或自动 IP 模式。若不支持，您需要获取可用的网络接口参数， 包括 IP 地址、子网掩码、默认网关和 DNS服务器。 

使用网线将 DG2000接入局域网。 

在 Shift 键背灯变亮状态，按 Pulse/Utility 接口设置 LAN，配置仪器的 IP 地址、 子网掩码、默认网关和 DNS 服务器。 

3) 使用 GPIB 接口： 

使用 USB-GPIB 模块连接 DG2000 前面板 USB HOST 接口扩展出 GPIB 接口。 

使用 GPIB 电缆将仪器与您的计算机相连接。 

在 Shift 键背灯变亮状态，按 Pulse/Utility 接口配置 GPIB，设置仪器的 GPIB 地 址。 

# 3. 验证连接是否成功

运行 Ultra Sigma，搜索资源并右击资源名称，在弹出的菜单中选择“SCPI Panel Control”。在弹出的 

SCPI 控制面板中输入正确的命令并依次点击 Send Comand 和 Read Response 或者直接点击 

Send & Eead 

以验证连接是否成功，如下图所示（以 USB 接口为例）。 

![](images/d582ec1c23bd6b9d49e84dae14d9555947fd6982a75d4fbbc84b4a2c6f81be49.jpg)


![](images/94381307f5ae4046b7c50d291d3494ae9acfc60a7b16941b888c6e04a01e43d3.jpg)


# 远程控制方法

# 1. 用户自定义编程

您可以使用本手册第 2 章“命令系统”部分所列的 SCPI（Standard Commands for Programmable Instruments）命令在 Visual $\complement + +$ 、Visual Basic、LabVIEW 等开发环境中对仪器进行编程控制，详见本 手册第 4 章“编程实例”部分的介绍。 

# 2. 使用 PC 软件发送 SCPI 命令

用户可以直接使用PC软件发送命令对信号发生器进行远程控制。推荐使用RIGOL提供的PC软件Ultra Sigma。登录 RIGOL 官网（www.rigol.com）下载该软件。 

# SCPI 命令简介

SCPI（Standard Commands for Programmable Instruments，即可编程仪器标准命令集）是一种建立在现有 标准 IEEE488.1 和 IEEE 488.2 基础上，并遵循了 IEEE754 标准中浮点运算规则、ISO646 信息交换 7 位编码 符号（相当于 ASCII 编程）等多种标准的标准化仪器编程语言。本节简介 SCPI 命令的格式、符号、参数和 缩写规则。 

# 命令格式

SCPI 命令为树状层次结构，包括多个子系统，每个子系统由一个根关键字和一个或数个层次关键字构成。 命令行通常以冒号“:”开始；关键字之间用冒号“:”分隔，关键字后面跟随可选的参数设置；命令行后面 添加问号“?”，表示对此功能进行查询；命令和参数以空格分开。 

例如： 

:SYSTem:COMMunicate:LAN:IPADdress <ip_address> 

:SYSTem:COMMunicate:LAN:IPADdress? 

SYSTem 是命令的根关键字，COMMunicate、LAN和 IPADdress 分别是第二级、第三级和第四级关键字。命 令行以冒号“:”开始，同时用冒号“:”将各级关键字分开，<ip_address>表示可设置的参数；问号“?” 

表示查询，当接收到查询命令时，仪器会返回相应信息（仪器的输出值或内部设置值）； 

命令:SYSTem:COMMunicate:LAN:IPADdress 和参数<ip_address >之间用空格分开。 

在一些带参数的命令中，通常用逗号“,”分隔多个参数，例如： 

:DISPlay:TEXT[:SET] <string>[,x[,y]] 

# 符号说明

下面四种符号不是 SCPI 命令中的内容，不随命令发送，但是通常用于辅助说明命令中的参数。 

# 1. 大括号 { }

大括号中通常包含多个可选参数，发送命令时必须选择其中一个参数。例 

如：:COUPling[<n>]:PHASe:MODE {OFFSet|RATio}命令。 

# 2. 竖线 |

竖线用于分隔多个参数选项，发送命令时必须选择其中一个参数。例如：:COUPling[<n>]:PHASe:MODE {OFFSet|RATio}命令。 

# 3. 方括号 [ ]

方括号中的内容（命令关键字或参数）是可省略的。如果省略参数，仪器将该参数设置为默认值。例如： 对于:COUNter:STATIstics[:STATe]?命令，发送下面两条命令的效果是一样的： 

:COUNter:STATIstics? 

:COUNter:STATIstics:STATe? 

# 4. 三角括号 < >

三角括号中的参数必须用一个有效值来替换。例如：以:COUNter:LEVEl 1.5 的形式发送:COUNter:LEVEl <value>命令。 

# 参数类型

本手册介绍的命令中所含的参数可以分为以下 5种类型：布尔型、整型、实型、离散型、ASCII 字符串。 

# 1. 布尔型

参数取值为“ON（1）”或“OFF（0）”。例如：:COUNter:HF {ON|1|OFF|0}。 

# 2. 整型

除非另有说明，参数在有效值范围内可以取任意整数值。注意：此时，请不要设置参数为小数格式，否 则将出现异常。例如：:DISPlay:BRIGhtness <brightness>，参数<brightness>可取 0 到 100 范围内的 任一整数。 

# 3. 实型

除非另有说明，参数在有效值范围内可以取任意值。 

例如：:COUNter:LEVEl $<$ <value>命令中的<value>的取值范围分别为-2.5V 至 $2 . 5 \mathsf { V }$ 。 

# 4. 离散型

参数只能取指定的几个数值或字符。例如：:COUPling[<n>]:PHASe:MODE {OFFSet|RATio}，参数只能 取值为 OFFSet 或 RATio。 

# 5. ASCII 字符串

参数取值为 ASCII 字符的组合。例如：:MMEMory:LOAD:STATe <filename> 

参数<filename>为需要加载的外部存储器当前路径下的状态文件的文件名，可为英文字符或数字。 

此外，可以用 MINimum 或 MAXimum代替许多命令中的参数，分别表示将参数设置为最小值或最大值。 例如：:DISPlay:BRIGhtness {<brightness>|MINimum|MAXimum}命令中的 MINimum 和 MAXimum 分别表 示将亮度设置为最小亮度或最大亮度。 

# 命令缩写

所有命令对大小写不敏感，可以全部采用大写或小写。如果要缩写，必须输完命令格式中的所有大写字母， 例如：:COUNter:COUPling?，可缩写成：:COUN:COUP?。 

# 第2章 命令系统

本章以字母 A-Z的顺序逐条介绍 DG2000 各命令的格式、功能、参数以及使用说明等。 

# 本章主要内容：

$\spadesuit$  :COUNter 命令 

:COUPling 命令 

:DISPlay 命令 

 :HCOPy 命令 

 IEEE488.2 通用命令 

 :LXI 命令 

 :MEMory 命令 

:MMEMory 命令 

:OUTPut 命令 

 :ROSCillator 命令 

:SOURce 命令 

:SYSTem 命令 

$\spadesuit$ :TRIGger 命令 

说明：本命令集中，涉及频率、幅度等参数设置的命令，允许带单位发送命令。各参数支持的单位及缺省单 位如下表所示： 

<table><tr><td>参数类型</td><td>支持的单位</td><td>缺省单位</td></tr><tr><td>频率</td><td>MHz/kHz/Hz/uHz</td><td>Hz</td></tr><tr><td>采样率</td><td>MSa/s、kSa/s、Sa/s、uSa/s</td><td>Sa/s</td></tr><tr><td>幅度</td><td>Vpp/mVpp/Vrms/mVrms/dBm</td><td>Vpp/Vrms/dBm（与设置的当前幅度单位有关）</td></tr><tr><td>偏移</td><td>Vdc/mVdc</td><td>Vdc</td></tr><tr><td>高电平/低电平</td><td>V/mV</td><td>V</td></tr><tr><td>时间</td><td>Ms/ks/s/ms/us/ns</td><td>s</td></tr><tr><td>相位</td><td>°</td><td>°</td></tr><tr><td>占空比/调制深度/亮度</td><td>%</td><td>%</td></tr><tr><td>阻抗</td><td>Ω</td><td>Ω</td></tr></table>

# 注意：

对于命令中参数范围的说明，本手册以 DG2102 为例。 

由于所有命令对大小写不敏感，DG2000 将 MHZ（mhz）和 MSA/S（msa/s）分别解释为兆赫兹和兆点 每秒，而将 MVPP（mvpp）、MVRMS（mvrms）、MVDC（mvdc）、MV（mv）和 MS（ms）分别解释为 毫伏（峰峰值）、毫伏（有效值）、毫伏（DC）、毫伏和毫秒。 

输出阻抗为高阻时，幅度单位 dBm 无效。 

# :COUNter 命令

:COUNter 命令用来打开、关闭频率计功能以及设置频率计的相关信息。 

# 命令列表[1]：

 :COUNter:AUTO 

 :COUNter:COUPling 

 :COUNter:GATEtime 

:COUNter:HF 

:COUNter:LEVEl 

:COUNter:MEASure? 

 :COUNter:SENSitive 

:COUNter[:STATe] 

:COUNter:STATIstics:CLEAr 

:COUNter:STATIstics[:STATe] 

注[1]：本手册“命令列表”中的命令均省略设置命令的参数部分和查询命令，您可根据此处的关键字查看正 文中的完整介绍。 

# :COUNter:AUTO

# 命令格式

:COUNter:AUTO 

# 功能描述

发送该命令，仪器将根据被测信号的特征自动选择合适的闸门时间。 

# 说明

您也可以发送:COUNter:GATEtime 命令设置所需的闸门时间。 

# :COUNter:COUPling

# 命令格式

:COUNter:COUPling {AC|DC} 

:COUNter:COUPling? 

# 功能描述

设置输入信号的耦合方式为交流（AC）或直流（DC）。 

查询输入信号的耦合方式。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{AC|DC}</td><td>离散型</td><td>AC|DC</td><td>AC</td></tr></table>

# 返回格式

返回 AC 或 DC。 

# 举例

:COUN:COUP DC /*设置输入信号的耦合方式为直流*/ 

:COUN:COUP? /*查询输入信号的耦合方式，返回 $\mathsf { D C } ^ { \star } /$ 

# :COUNter:GATEtime

# 命令格式

:COUNter:GATEtime {USER1|USER2|USER3|USER4|USER5|USER6} 

:COUNter:GATEtime? 

# 功能描述

选择测量系统的闸门时间。 

查询测量系统的闸门时间。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{USER1|USER2|USER3|USER4|USER5|USER6}</td><td>离散型</td><td>USER1|USER2|USER3|USER4|USER5|USER6</td><td>USER1</td></tr></table>

# 说明

USER1 至 USER6所代表的闸门时间如下表所示。 

<table><tr><td>USER1</td><td>USER2</td><td>USER3</td><td>USER4</td><td>USER5</td><td>USER6</td></tr><tr><td>1.048ms</td><td>8.389ms</td><td>134.218ms</td><td>1.074s</td><td>8.590s</td><td>&gt;8.590s</td></tr></table>

对于低频信号（例如频率小于 5Hz）建议选择闸门时间为 USER6。 

发送:COUNter:AUTO 命令，仪器根据被测信号的特征自动选择合适的闸门时间。在仪器选择期间，频 

率计界面闸门时间区域显示“AUTO”；在仪器已选择合适的闸门时间之后，频率计界面闸门时间区域显示仪 器当前自动选择的闸门时间。 

# 返回格式

若用户当前选择了某一闸门时间，则返回相应的名称 USER1、USER2、USER3、USER4、USER5 或 USER6。 若用户发送:COUNter:AUTO 命令使仪器自动选择合适的闸门时间，则在仪器选择期间，返回“AUTO”；在 仪器已选择合适的闸门时间之后，返回相应的名称 USER1、USER2、USER3、USER4、USER5 或 USER6。 

# 举例

:COUN:GATE USER2 /*选择测量系统的闸门时间为 USER2（10.48ms）*/ 

:COUN:GATE? /*查询选择的测量系统的闸门时间，返回 USER2*/ 

# :COUNter:HF

# 命令格式

:COUNter:HF {ON|1|OFF|0} 

:COUNter:HF? 

# 功能描述

打开或关闭频率计的高频抑制功能。 

查询频率计的高频抑制功能的开关状态。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 说明

在测量频率小于 150kHz 的低频信号时，打开高频抑制，以滤除高频噪声干扰，提高测量精确度；在测量频 率大于 150kHz 的高频信号时，关闭高频抑制，此时，最大输入频率可为 240MHz。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:COUN:HF ON /*打开频率计的高频抑制功能*/ 

:COUN:HF? /*查询频率计的高频抑制功能的开关状态，返回 ON*/ 

# :COUNter:LEVEl

# 命令格式

:COUNter:LEVEl {<value>|MINimum|MAXimum} 

:COUNter:LEVEl? [MINimum|MAXimum] 

# 功能描述

设置频率计的触发电平。 

查询频率计的触发电平。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>(value)</td><td>实型</td><td>-2.5V至2.5V</td><td>0V</td></tr></table>

# 说明

当输入信号达到指定的触发电平时，触发频率计执行测量。 

最小分辨率为 6mV。 

# 返回格式

以科学计数形式返回触发电平，有效位数为 7位，如 $1 . 5 0 0 0 0 0 0 \mathsf { E } + 0 0$ ，表示触发电平为 1.5V。 

# 举例

:COUN:LEVE 1.5 /*设置频率计的触发电平为 $1 . 5 \mathsf { V } ^ { \star } /$ 

:COUN:LEVE? /*查询频率计的触发电平，返回 1.500000E+00*/ 

# :COUNter:MEASure?

# 命令格式

:COUNter:MEASure? 

# 功能描述

查询频率计的测量结果。 

# 说明

当频率计处于“RUN”或“SINGLE”状态时，发送该命令查询测量值；当频率计处于“STOP”状态时，发 送该命令查询已执行的最后一次测量的测量值。 

# 返回格式

返回一个字符串，由 5 部分组成，各部分之间以逗号隔开，分别表示测量的频率、周期、占空比、正脉宽和 负脉宽值。每一部分均以科学计数形式表示，有效位数为 10位， 

如 2.000000000E+03,5.000000000E-04,4.760800000E+01,2.380415000E-04, 

2.619585000E-04，该结果表示测量值为频率：2kHz，周期：500us，占空比： $4 7 . 6 0 8 \%$ ，正脉宽：238.0415us， 负脉宽：261.9585us。 

关闭频率计功能时，发送该命令，返回 0.000000000E+00,0.000000000E+00, 

0.000000000E+00,0.000000000E+00,0.000000000E+00 

# 举例

:COUN:MEAS? /*查询频率计的测量结果，返回 2.000000000E+03,5.000000000E-04, 

4.760800000E+01,2.380415000E-04,2.619585000E-04*/ 

# :COUNter:SENSitive

# 命令格式

:COUNter:SENSitive {LOW|HIGh} 

:COUNter:SENSitive? [LOW|HIGh] 

# 功能描述

设置频率计的触发灵敏度。 

查询频率计的触发灵敏度。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{LOW|HIGH}</td><td>实型</td><td>LOW|HIGH</td><td>LOW</td></tr></table>

# 说明

对于小幅度信号，建议选择高灵敏度；对于低频大幅度信号或者上升沿比较慢的信号，选择低灵敏度可使测 量结果更准确。 

# 返回格式

返回 LOW 或 HIG。 

# 举例

:COUN:SENS LOW /*设置频率计的触发灵敏度为低*/ 

:COUN:SENS? /*查询频率计的触发灵敏度，返回 LOW*/ 

# :COUNter[:STATe]

# 命令格式

:COUNter[:STATe] {ON|1|OFF|0|RUN|STOP|SINGLE} 

:COUNter[:STATe]? 

# 功能描述

设置频率计的状态。 

查询频率计的状态。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{ON|1|OFF|0|RUN|STOP|SINGLE}</td><td>离散型</td><td>ON|1|OFF|0|RUN|STOP|SINGLE</td><td>OFF</td></tr></table>

# 说明

“ON”和“1”均表示打开频率计功能；“OFF”和“0”均表示关闭频率计功能；“RUN”、“STOP”和 “SINGLE”分别表示设置频率计的运行状态为“运行”、“停止”和“单次”。 

 仅当打开频率计功能时，设置运行状态的命令（参数为 RUN、STOP 或 SINGLE）才有效。 

打开频率计功能时，CH2的同步输出将被关闭。 

“运行”状态下，频率计以当前的配置连续对输入信号进行测量；“SINGLE”状态下，频率计执行一次 测量后进入“STOP”状态，停止测量；“STOP”状态下，频率计停止测量。 

 打开频率计时，默认的运行状态为“运行”，仪器以当前的配置连续对输入信号进行测量。此时，发 送:COUNter:STATe SINGLE 命令，频率计首先进入“单次”状态，完成正在进行的测量后进入“停止” 状态；发送:COUNter:STATe STOP 命令，频率计将立即进入“停止”状态。 

当频率计处于“STOP”状态时，每发送一次:COUNter:STATe SINGLE 命令，频率计完成一次测量后进 入“STOP”状态，停止测量。 

# 返回格式

当频率计功能打开时，返回当前运行状态 RUN、STOP 或 SINGLE；当关闭频率计功能时，返回 OFF。 

# 举例

:COUN OFF /*关闭频率计功能*/ 

:COUN? /*查询频率计的状态，返回 OFF*/ 

:COUN 1 /*打开频率计功能*/ 

:COUN? /*查询频率计的状态，返回 RUN（默认运行状态）*/ 

:COUN STOP /*设置频率计的运行状态为“停止”*/ 

:COUN? /*查询频率计的状态，返回 STOP*/ 

# :COUNter:STATIstics:CLEAr

# 命令格式

:COUNter:STATIstics:CLEAr 

# 功能描述

清除统计结果。 

# 说明

仅当打开频率计的统计功能（:COUNter:STATIstics[:STATe]）时，该命令有效。 

关闭频率计的统计功能时，自动清除统计结果。 

# :COUNter:STATIstics[:STATe]

# 命令格式

:COUNter:STATIstics[:STATe] {ON|1|OFF|0} 

:COUNter:STATIstics[:STATe]? 

# 功能描述

打开或关闭频率计的测量结果统计功能。 

查询频率计测量结果统计功能的开关状态。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 返回格式

返回 ON 或 OFF。 

# 举例

:COUN:STATI ON /*打开频率计的测量结果统计功能*/ 

:COUN:STATI? /*查询频率计测量结果统计功能的开关状态，返回 $\mathsf { O N } ^ { \star } /$ 

# :COUPling 命令

:COUPling 命令用来设置通道频率耦合、幅度耦合和相位耦合的相关信息以及打开和关闭这三种耦合功能。 

# 命令列表：

:COUPling[<n>]:AMPL:DEViation 

 :COUPling[<n>]:AMPL:MODE 

:COUPling[<n>]:AMPL:RATio 

 :COUPling[<n>]:AMPL[:STATe] 

:COUPling[<n>]:FREQuency:DEViation 

 :COUPling[<n>]:FREQuency:MODE 

:COUPling[<n>]:FREQuency:RATio 

 :COUPling[<n>]:FREQuency[:STATe] 

 :COUPling[<n>]:PHASe:DEViation 

:COUPling[<n>]:PHASe:MODE 

:COUPling[<n>]:PHASe:RATio 

:COUPling[<n>]:PHASe[:STATe] 

:COUPling[<n>][:STATe] 

 :COUPling[<n>]:TRIgger[:STATe] 

注意：耦合功能仅在两通道均为基本波（正弦、方波、锯齿波或任意波）模式时有效。 

# :COUPling[<n>]:AMPL:DEViation

# 命令格式

:COUPling[ $\mathsf { < n > j }$ ]:AMPL:DEViation <deviation> 

:COUPling[ $< n >$ ]:AMPL:DEViation? 

# 功能描述

设置指定通道幅度耦合中的幅度差值。 

查询指定通道幅度耦合中的幅度差值。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;deviation&gt;</td><td>实型</td><td>-19.998Vpp至19.998Vpp</td><td>0Vpp</td></tr></table>

# 说明

省略参数 $[ < n > ]$ 时，默认设置和查询 CH1的相关参数。 

请在打开幅度耦合功能（:COUPling[<n>]:AMPL[:STATe]）之前选择所需的幅度耦合模式 （:COUPling[<n>]:AMPL:MODE）并设置相应的幅度差值或幅度比例（:COUPling[<n>]:AMPL:RATio）。 打开幅度耦合功能后，不可以设置幅度耦合模式和幅度差值/比例。 

幅度耦合功能关闭时，若当前幅度耦合模式为幅度差值，发送该命令可以设置幅度差值；若当前幅度耦 合模式为幅度比例，发送该命令可以选择幅度差值耦合模式并设置幅度差值。 

# 返回格式

以科学计数形式返回幅度差值，有效位数为 7 位，如 $1 . 0 0 0 0 0 0 0 \mathsf { E } + 0 0$ ，表示幅度差值为 1Vpp。 

# 举例

:COUP1:AMPL:DEV 1 /*设置 CH1 幅度耦合中的幅度差值为 ${ 1 } \mathsf { V } \mathsf { p } \mathsf { p } ^ { \star } /$ 

:COUP1:AMPL:DEV? /*查询 CH1 幅度耦合中的幅度差值，返回 1.000000E+00*/ 

# :COUPling[<n>]:AMPL:MODE

# 命令格式

:COUPling[ $< \mathsf { n } >$ ]:AMPL:MODE {OFFSet|RATio} 

:COUPling[ $< n >$ ]:AMPL:MODE? 

# 功能描述

选择指定通道幅度耦合模式为幅度差值（OFFSet）或幅度比例（RATio）。 

查询指定通道选择的幅度耦合模式。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{OFFSET|RATio}</td><td>离散型</td><td>OFFSET|RATio</td><td>RATio</td></tr></table>

# 说明

省略参数 $\cdot < n > ]$ 时，默认设置和查询 CH1的相关参数。 

. 幅度差值模式：CH1和 CH2两通道的幅度具有一定的差值关系。参数关系为 $\mathsf { A } _ { \mathsf { C H 2 } } = \mathsf { A } _ { \mathsf { C H 1 } } + \mathsf { A } _ { \mathsf { D e v } }$ （基准源 为 CH1）； $\mathsf { A } _ { \mathsf { C H } 1 } = \mathsf { A } _ { \mathsf { C H } 2 } - \mathsf { A } _ { \mathsf { D e v } }$ （基准源为 CH2）。其中， $\mathsf { A } _ { \mathsf { C H 1 } }$ 为 CH1 的幅度值， $\mathsf { A } _ { \mathsf { C H 2 } }$ 为 CH2 的幅度值， $\mathsf { A } _ { \sf D e v }$ 为设置的幅度差值。 

幅度比例模式：CH1 和 CH2 两通道的幅度具有一定的比值关系。参数关系为 $\mathsf { A } _ { \mathsf { C H } 2 } { = } \mathsf { A } _ { \mathsf { C H } 1 } { } ^ { \star } \mathsf { A } _ { \mathsf { R a t i o } }$ （基准源 为 CH1）； $\mathsf { A } _ { \mathsf { C H } 1 } = \mathsf { A } _ { \mathsf { C H } 2 } / \mathsf { A } _ { \mathsf { R a t i o } }$ （基准源为 CH2）。其中， $\mathsf { A } _ { \mathsf { C H 1 } }$ 为 CH1 的幅度值， $\mathsf { A } _ { \mathsf { C H 2 } }$ 为 CH2 的幅度值， $\mathsf { A } _ { \mathsf { R a t i o } }$ 为设置的幅度比例。 

如果经过耦合后，CH1 和 CH2中任意一个通道的幅度超过本通道的幅度上限或下限，仪器将自动调整 另外一个通道的幅度上限或下限以避免参数超限。 

请在打开幅度耦合功能（:COUPling[<n>]:AMPL[:STATe]）之前选择所需的幅度耦合模式并设置相应的 幅度差值（:COUPling[<n>]:AMPL:DEViation）或幅度比例（:COUPling[<n>]:AMPL:RATio）。打开幅度 耦合功能后，不可以设置幅度耦合模式和幅度差值/比例。 

# 返回格式

返回 OFFS 或 RAT。 

# 举例

:COUP1:AMPL:MODE OFFS /*选择 CH1的幅度耦合模式为幅度差值*/ 

:COUP1:AMPL:MODE? /*查询 CH1的幅度耦合模式，返回 OFFS*/ 

# :COUPling[ $< \mathsf { n } >$ ]:AMPL:RATio

# 命令格式

:COUPling[ $\mathsf { < n > }$ ]:AMPL:RATio {<value>|MINimum|MAXimum} 

:COUPling[ $\tt { < n > }$ ]:AMPL:RATio? 

# 功能描述

设置指定通道幅度耦合中的幅度比例。 

查询指定通道幅度耦合中的幅度比例。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;value&gt;</td><td>实型</td><td>0.001至1000</td><td>1</td></tr></table>

# 说明

省略参数 $\cdot < n > ]$ 时，默认设置和查询 CH1的相关参数。 

请在打开幅度耦合功能（:COUPling[<n>]:AMPL[:STATe]）之前选择所需的幅度耦合模式 （:COUPling[<n>]:AMPL:MODE）并设置相应的幅度差值（:COUPling[<n>]:AMPL:DEViation）或幅度 比例。打开幅度耦合功能后，不可以设置幅度耦合模式和幅度差值/比例。 

幅度耦合功能关闭时，若当前幅度耦合模式为幅度比例，发送该命令可以设置幅度比例；若当前幅度耦 合模式为幅度差值，发送该命令可以选择幅度比例耦合模式并设置幅度比例。 

# 返回格式

以科学计数形式返回幅度比例，有效位数为 7位，如 1.123000E $+ 0 0$ ，表示幅度比例为 1.123。 

# 举例

:COUP1:AMPL:RAT 1.123 /*设置 CH1的幅度耦合中的幅度比例为 $1 . 1 2 3 ^ { \star } /$ 

:COUP1:AMPL:RAT? /*查询 CH1 的幅度耦合中的幅度比例，返回 1.123000E+00*/ 

:COUPling[<n>]:AMPL[:STATe] 

# 命令格式

:COUPling[ $\mathsf { < n > j }$ ]:AMPL[:STATe] {ON|1|OFF|0} 

:COUPling[ $< n >$ ]:AMPL[:STATe]? 

# 功能描述

打开或关闭指定通道的幅度耦合功能。 

查询指定通道的幅度耦合功能的开关状态。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 说明

省略参数 $[ < n > ]$ 时，默认设置和查询 CH1的相关参数。 

打开幅度耦合功能后，CH1 和 CH2两个通道互为基准源，当改变其中一个通道（该通道作为基准源） 的幅度时，另一通道的幅度将自动调整，并总是与基准通道保持指定的幅度差值或比例。 

请在打开幅度耦合功能之前选择所需的幅度耦合模式（:COUPling[<n>]:AMPL:MODE）并设置相应的幅 度差值（:COUPling[<n>]:AMPL:DEViation）或幅度比例（:COUPling[<n>]:AMPL:RATio）。打开幅度耦 合功能后，不可以设置幅度耦合模式和幅度差值/比例。 

. 您也可以发送[:SOURce[<n>]]:VOLTage:COUPle[:STATe]命令设置和查询幅度耦合功能的开关状态。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:COUP1:AMPL ON /*打开 CH1的幅度耦合功能*/ 

:COUP1:AMPL? /*查询 CH1的幅度耦合功能的开关状态，返回 ON*/ 

:COUPling[<n>]:FREQuency:DEViation 

# 命令格式

:COUPling[ $< n >$ ]:FREQuency:DEViation <deviation> 

:COUPling[ $< n >$ ]:FREQuency:DEViation? 

# 功能描述

设置指定通道的频率耦合中的频率差值。 

查询指定通道的频率耦合中的频率差值。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;deviation&gt;</td><td>实型</td><td>-99.999 999 999 9MHz至99.999 999 999 9MHz</td><td>0Hz</td></tr></table>

# 说明

省略参数 $[ < n > ]$ 时，默认设置和查询 CH1的相关参数。 

 请在打开频率耦合功能（:COUPling[<n>]:FREQuency[:STATe]）之前选择所需的频率耦合模式 

（:COUPling[<n>]:FREQuency:MODE）并设置相应的频率差值或频率比例 

（:COUPling[<n>]:FREQuency:RATio）。频率耦合功能打开时，不可以设置频率耦合模式和频率差值/ 比例。 

频率耦合功能关闭时，若当前频率耦合模式为频率差值，发送该命令可以设置频率差值；若当前频率耦 

合模式为频率比例，发送该命令可以选择频率差值耦合模式并设置频率差值。 

您也可以发送[:SOURce[<n>]]:FREQuency:COUPle:OFFSet 命令设置和查询频率耦合中的频率差值。 

# 返回格式

以科学计数形式返回频率差值，有效位数为 7位，如 1.000000E $+ 0 2$ ，表示频率差值为 100Hz。 

# 举例

:COUP1:FREQ:DEV 100 /*设置 CH1 的频率耦合中的频率差值为 $1 0 0 \mathsf { H z } ^ { \star } /$ 

:COUP1:FREQ:DEV? /*查询 CH1 的频率耦合中的频率差值，返回 1.000000E+02*/ 

# :COUPling[<n>]:FREQuency:MODE

# 命令格式

:COUPling[ $\tt { < n > }$ ]:FREQuency:MODE {OFFSet|RATio} 

:COUPling[ $\tt { < n > }$ ]:FREQuency:MODE? 

# 功能描述

选择指定通道的频率耦合模式为频率差值（OFFSet）或频率比例（RATio）。 

查询指定通道选择的频率耦合模式。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{OFFSET|RATio}</td><td>离散型</td><td>OFFSET|RATio</td><td>RATio</td></tr></table>

# 说明

省略参数 $[ < n > ]$ 时，默认设置和查询 CH1的相关参数。 

频率差值模式：CH1和 CH2 两通道的频率具有一定的差值关系。参数关系为 $\mathsf { F } _ { \mathsf { C H 2 } } { = } \mathsf { F } _ { \mathsf { C H 1 } } { + } \mathsf { F } _ { \mathsf { D e v } }$ （基准源为 CH1）； $\mathsf { F } _ { \mathsf { C H } 1 } { = } \mathsf { F } _ { \mathsf { C H } 2 } { - } \mathsf { F } _ { \mathsf { D e v } }$ （基准源为 CH2）。其中， $\mathsf { F } _ { \mathrm { C H 1 } }$ 为 CH1 的频率值， $\mathsf { F } _ { \mathsf { C H 2 } }$ 为 CH2 的频率值， $\mathsf { F } _ { \mathsf { D e v } }$ 为 设置的频率差值。 

频率比例模式：CH1和 CH2两通道的频率具有一定的比值关系。参数关系为 $\mathsf { F } _ { \mathsf { C H 2 } } { = } \mathsf { F } _ { \mathsf { C H 1 } } { ^ { \star } } \mathsf { F } _ { \mathsf { R a t i o } }$ （基准源 为 CH1）； $\mathsf { F } _ { \mathsf { C H } 1 } { = } \mathsf { F } _ { \mathsf { C H } 2 } / \mathsf { F } _ { \mathsf { R a t i o } }$ （基准源为 CH2）。其中， $\mathsf { F } _ { \mathsf { C H 1 } }$ 为 CH1 的频率值， $\mathsf { F } _ { \mathsf { C H 2 } }$ 为 CH2 的频率值，FRatio 为设置的频率比例。 

如果经过耦合后，CH1 和 CH2中任意一个通道的频率超过本通道的频率上限或下限，仪器将自动调整 另外一个通道的频率上限或下限以避免参数超限。 

请在打开频率耦合功能（:COUPling[<n>]:FREQuency[:STATe]）之前选择所需的频率耦合模式并设置 相应的频率差值（:COUPling[<n>]:FREQuency:DEViation）或频率比例 （:COUPling[<n>]:FREQuency:RATio）。打开频率耦合功能后，不可以设置频率耦合模式和频率差值/ 比例。 

您也可以发送[:SOURce[<n>]]:FREQuency:COUPle:MODE 命令设置和查询指定通道的频率耦合模式。 

# 返回格式

返回 OFFS 或 RAT。 

# 举例

:COUP1:FREQ:MODE OFFS /*设置 CH1的频率耦合模式为频率差值*/ 

:COUP1:FREQ:MODE? /*查询 CH1选择的频率耦合模式，返回 OFFS*/ 

# :COUPling[<n>]:FREQuency:RATio

# 命令格式

:COUPling[ $\mathsf { < n > j }$ ]:FREQuency:RATio {<value>|MINimum|MAXimum} 

:COUPling[ $< n >$ ]:FREQuency:RATio? 

# 功能描述

设置指定通道频率耦合中的频率比例。 

查询指定通道频率耦合中的频率比例。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;value&gt;</td><td>实型</td><td>0.000 001 至 1 000 000</td><td>1</td></tr></table>

# 说明

省略参数 $[ < n > ]$ 时，默认设置和查询 CH1的相关参数。 

请在打开频率耦合功能（:COUPling[<n>]:FREQuency[:STATe]）之前选择所需的频率耦合模式 （:COUPling[<n>]:FREQuency:MODE）并设置相应的频率差值 

（:COUPling[<n>]:FREQuency:DEViation）或频率比例。打开频率耦合功能后，不可以设置频率耦合模 式和频率差值/比例。 

频率耦合功能关闭时，若当前频率耦合模式为频率比例，发送该命令可以设置频率比例；若当前频率耦 合模式为频率差值，发送该命令可以选择频率比例耦合模式并设置频率比例。 

. 您也可以发送[:SOURce[<n>]]:FREQuency:COUPle:RATio 命令设置和查询频率耦合中的频率比例。 

# 返回格式

以科学计数形式返回频率比例，有效位数为 7位，如 $1 . 0 0 1 2 3 0 \mathsf { E } + 0 2$ ，表示频率比例为 100.123。 

# 举例

:COUP1:FREQ:RAT 100.123 /*设置 CH1 频率耦合中的频率比例为 $1 0 0 . 1 2 3 ^ { \star } /$ 

:COUP1:FREQ:RAT? /*查询 CH1频率耦合中的频率比例，返回 $1 . 0 0 1 2 3 0 \mathsf E + 0 2 ^ { \star } /$ 

# :COUPling[<n>]:FREQuency[:STATe]

# 命令格式

:COUPling[ $< n >$ ]:FREQuency[:STATe] {ON|1|OFF|0} 

:COUPling[ $\mathsf { < n > j }$ ]:FREQuency[:STATe]? 

# 功能描述

打开或关闭指定通道的频率耦合功能。 

查询指定通道的频率耦合功能的开关状态。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 说明

省略参数 $[ < n > ]$ 时，默认设置和查询 CH1的相关参数。 

. 频率耦合功能关闭时，您可以选择频率耦合模式并设置相应的频率差值或比例。打开频率耦合功能后， CH1和 CH2 两个通道互为基准源，当改变其中一个通道（该通道作为基准源）的频率时，另一通道的 频率将自动调整，并总是与基准通道保持指定的频率差值或比例。 

请在打开频率耦合功能之前选择所需的频率耦合模式（:COUPling[<n>]:FREQuency:MODE）并设置相 

应的频率差值（:COUPling[<n>]:FREQuency:DEViation）或频率比例 

（:COUPling[<n>]:FREQuency:RATio）。打开频率耦合功能后，不可以设置频率耦合模式和频率差值/ 比例。 

 您也可以发送[:SOURce[<n>]]:FREQuency:COUPle[:STATe]命令设置或查询频率耦合功能状态。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:COUP1:FREQ ON /*打开 CH1的频率耦合功能*/ 

:COUP1:FREQ? /*查询 CH1的频率耦合功能的开关状态，返回 $\mathsf { O N } ^ { \star } /$ 

# :COUPling[<n>]:PHASe:DEViation

# 命令格式

:COUPling[ $< \mathsf { n } >$ ]:PHASe:DEViation <deviation> 

:COUPling[ $\mathsf { < n > j }$ ]:PHASe:DEViation? 

# 功能描述

设置指定通道相位耦合中的相位差值。 

查询指定通道相位耦合中的相位差值。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;deviation&gt;</td><td>实型</td><td>-360°至360°</td><td>0</td></tr></table>

# 说明

省略参数[<n>]时，默认设置和查询 CH1的相关参数。 

请在打开相位耦合功能（:COUPling[<n>]:PHASe[:STATe]）之前选择所需的相位耦合模式 

（:COUPling[<n>]:PHASe:MODE）并设置相应的相位差值或相位比例 

（:COUPling[<n>]:PHASe:RATio）。打开相位耦合功能后，不可以设置相位耦合模式和相位差值/比例。 

. 相位耦合功能关闭时，若当前相位耦合模式为相位差值，发送该命令可以设置相位差值；若当前相位耦 合模式为相位比例，发送该命令可以选择相位差值耦合模式并设置相位差值。 

# 返回格式

以科学计数形式返回相位差值，有效位数为 7位，如 $9 . 0 0 0 0 0 0 0 \mathsf { E } + 0 1$ ，表示相位差值为 $9 0 ^ { \circ }$ 。 

# 举例

:COUP1:PHAS:DEV 90 /*设置 CH1相位耦合中的相位差值为 $9 0 ^ { \circ \star } /$ 

:COUP1:PHAS:DEV? /*查询 CH1相位耦合中的相位差值，返回 $9 . 0 0 0 0 0 0 0 \mathsf { E } { + } 0 1 ^ { \star } /$ 

# :COUPling[<n>]:PHASe:MODE

# 命令格式

:COUPling[ $\mathsf { < n > j }$ ]:PHASe:MODE {OFFSet|RATio} 

:COUPling[ $< n >$ ]:PHASe:MODE? 

# 功能描述

选择指定通道的相位耦合模式为相位差值（OFFSet）或相位比例（RATio）。 

查询指定通道选择的相位耦合模式。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{OFFSET|RATio}</td><td>离散型</td><td>OFFSET|RATio</td><td>RATio</td></tr></table>

# 说明

省略参数 $[ < n > ]$ 时，默认设置和查询 CH1的相关参数。 

相位差值模式：CH1和 CH2两通道的相位具有一定的差值关系。参数关系为 $\mathsf { P } _ { \mathsf { C H 2 } } { = } \mathsf { P } _ { \mathsf { C H 1 } } { + } \mathsf { P } _ { \mathsf { D e v } }$ （基准源 为 CH1）； $\mathsf { P } _ { \mathsf { C H 1 } } { = } \mathsf { P } _ { \mathsf { C H 2 } } { - } \mathsf { P } _ { \mathsf { D e v } }$ （基准源为 CH2）。其中， $\mathsf { P } _ { \mathsf { C H 1 } }$ 为 CH1 的相位值， $\mathsf { P } _ { \mathsf { C H 2 } }$ 为 CH2 的相位值， $\mathsf { P } _ { \mathsf { D e v } }$ 为设置的相位差值。 

相位比例模式：CH1 和 CH2 两通道的相位具有一定的比值关系。参数关系为 $\mathsf { P } _ { \mathtt { C H 2 } } { = } \mathsf { P } _ { \mathtt { C H 1 } } { \star } \mathsf { P } _ { \mathtt { R a t i o } }$ （基准源 为 CH1）； $\mathsf { P } _ { \mathtt { C H } 1 } { = } \mathsf { P } _ { \mathtt { C H } 2 } / \mathsf { P } _ { \mathtt { R a t i o } }$ 基准源为 CH2）。其中， $\mathsf { P } _ { \mathsf { C H 1 } }$ 为 CH1 的相位值， $\mathsf { P } _ { \mathsf { C H 2 } }$ 为 CH2 的相位值，PRatio 为设置的相位比例。 

如果经过耦合后，CH1 和 CH2中任意一个通道的相位超过本通道的相位上限或下限，仪器将自动调整 另外一个通道的相位上限或下限以避免参数超限。 

请在打开相位耦合功能（:COUPling[<n>]:PHASe[:STATe]）之前选择所需的相位耦合模式并设置相应 的相位差值（:COUPling[<n>]:PHASe:DEViation）或相位比例（:COUPling[<n>]:AMPL:RATio）。打开 相位耦合功能后，不可以设置相位耦合模式和相位差值/比例。 

# 返回格式

返回 OFFS 或 RAT。 

# 举例

:COUP1:PHAS:MODE OFFS /*选择 CH1的相位耦合模式为相位差值*/ 

:COUP1:PHAS:MODE? /*查询 CH1选择的相位耦合模式，返回 OFFS*/ 

# :COUPling[<n>]:PHASe:RATio

# 命令格式

:COUPling[ $\mathsf { < n > j }$ ]:PHASe:RATio {<value>|MINimum|MAXimum} 

:COUPling[ $< n >$ ]:PHASe:RATio? 

# 功能描述

设置指定通道相位耦合中的相位比例。 

查询指定通道相位耦合中的相位比例。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>营养价值</td><td>实型</td><td>0.01至100</td><td>1</td></tr></table>

# 说明

省略参数 $[ < n > ]$ 时，默认设置和查询 CH1的相关参数。 

请在打开相位耦合功能（:COUPling[<n>]:PHASe[:STATe]）之前选择所需的相位耦合模式 （:COUPling[<n>]:PHASe:MODE）并设置相应的相位差值或相位比例 

（:COUPling[<n>]:PHASe:RATio）。打开相位耦合功能后，不可以设置相位耦合模式和相位差值/比例。 

相位耦合功能关闭时，若当前相位耦合模式为相位比例，发送该命令可以设置相位比例；若当前相位耦 合模式为相位差值，发送该命令可以选择相位比例耦合模式并设置相位比例。 

# 返回格式

以科学计数形式返回相位比例，有效位数为 7位，如 $1 . 1 2 0 0 0 0 \mathsf { E } + 0 0$ ，表示相位比例为 1.12。 

# 举例

:COUP1:PHAS:RAT 1.12 /*设置 CH1 相位耦合中的相位比例为 $1 . 1 2 ^ { \star } /$ 

:COUP1:PHAS:RAT? /*查询 CH1相位耦合中的相位比例，返回 $1 . 1 2 0 0 0 0 \mathsf { E } { + } 0 0 ^ { \star } /$ 

# :COUPling[<n>]:PHASe[:STATe]

# 命令格式

:COUPling[ $\tt { < n > }$ ]:PHASe[:STATe] {ON|1|OFF|0} 

:COUPling[ $\tt { < n > }$ ]:PHASe[:STATe]? 

# 功能描述

打开或关闭指定通道的相位耦合功能。 

查询指定通道的相位耦合功能的开关状态。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 说明

省略参数 $[ < n > ]$ 时，默认设置和查询 CH1的相关参数。 

打开相位耦合功能后，CH1 和 CH2两个通道互为基准源，当改变其中一个通道（该通道作为基准源） 的相位时，另一通道的相位将自动调整，并总是与基准通道保持指定的相位差值或比例。 

请在打开相位耦合功能之前选择所需的相位耦合模式（:COUPling[<n>]:PHASe:MODE）并设置相应的 相位差值（:COUPling[<n>]:PHASe:DEViation）或相位比例（:COUPling[<n>]:PHASe:RATio）。打开相 位耦合功能后，不可以设置相位耦合模式和相位差值/比例。 

相位耦合功能关闭时，您可以选择相位耦合模式并设置相应的相位差值或比例。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:COUP1:PHAS ON /*打开 CH1的相位耦合功能*/ 

:COUP1:PHAS? /*查询 CH1的相位耦合功能的开关状态，返回 $\mathsf { O N } ^ { \star } /$ 

# :COUPling[<n>][:STATe]

# 命令格式

:COUPling[ $< n >$ ][:STATe] {ON|1|OFF|0} 

:COUPling[<n>][:STATe]? 

# 功能描述

同时打开或关闭指定通道的频率耦合、相位耦合和幅度耦合功能。 

查询指定通道的频率耦合、相位耦合和幅度耦合功能的开关状态。 

# 参数

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 说明

省略参数 $[ < n > ]$ 时，默认设置和查询 CH1的相关参数。 

 DG2000支持频率、幅度和相位耦合功能。当打开耦合功能后，CH1和 CH2 两个通道互为基准源，当改 变其中一个通道（该通道作为基准源）的频率、幅度或相位时，另一通道的频率、幅度或相位将自动调 整，并总是与基准通道保持指定的频率差值/比例、幅度差值/比例或相位差值/比例。 

. 您也可以分别打开或关闭频率耦合（:COUPling[<n>]:FREQuency[:STATe]）、相位耦合 

（:COUPling[<n>]:PHASe[:STATe]）和幅度耦合（:COUPling[<n>]:AMPL[:STATe]）功能。 

# 返回格式

返回一个字符串，由 3部分组成，各部分之间以逗号隔开，顺序表示频率耦合、相位耦合和幅度耦合功能的 开关状态，如 FREQ:ON,PHASE:OFF,AMPL:OFF。 

# 举例

:COUP1 ON /*同时打开 CH1的频率耦合、相位耦合和幅度耦合功能*/ 

:COUP1? /*查询 CH1 的频率耦合、相位耦合和幅度耦合功能的开关状态，返回 

FREQ:ON,PHASE:ON,AMPL:ON*/ 

# :COUPling[<n>]:TRIgger[:STATe]

# 命令格式

:COUPling[ $< \mathsf { n } >$ ]:TRIgger [:STATe] {ON|1|OFF|0} 

:COUPling[ $\mathsf { < n > j }$ ]:TRIgger [:STATe]? 

# 功能描述

打开或关闭指定通道的触发耦合功能。 

查询指定通道的触发耦合功能的开关状态。 

# 参数

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 说明

省略参数[ $\cdot < n > ]$ 时，默认设置和查询 CH1的相关参数。 

打开触发耦合功能后，CH1 和 CH2两个通道互为基准源，当其中一个通道（该通道作为基准源）执行 触发时，另一通道将自动触发。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:COUP1:TRI ON /*打开 CH1的触发耦合功能*/ 

:COUP1:TRI? /*查询 CH1的触发耦合功能的开关状态，返回 $\mathsf { O N } ^ { \star } /$ 

# :DISPlay 命令

:DISPlay 命令用来设置显示的相关信息，在屏幕上显示指定字符以及清除屏幕上显示的字符等。 

# 命令列表：

 :DISPlay:BRIGhtness 

 :DISPlay:SAVer:IMMediate 

:DISPlay:SAVer[:STATe] 

# :DISPlay:BRIGhtness

# 命令格式

:DISPlay:BRIGhtness {<brightness>|MINimum|MAXimum} 

:DISPlay:BRIGhtness? [MINimum|MAXimum] 

# 功能描述

设置屏幕亮度。 

查询屏幕亮度。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>&lt;brightness&gt;</td><td>整型</td><td>1%至100%</td><td>50%</td></tr></table>

# 返回格式

以科学计数形式返回屏幕亮度，有效位数为 7位，如 $5 . 1 0 0 0 0 0 0 \mathsf { E } + 0 1$ ，表示屏幕亮度为 $5 1 \%$ 。 

# 举例

:DISP:BRIG 51 /*设置屏幕亮度为 $5 1 \% ^ { \star } /$ 

:DISP:BRIG? /*查询屏幕亮度，返回 5.100000E+01*/ 

# :DISPlay:SAVer:IMMediate

# 命令格式

:DISPlay:SAVer:IMMediate 

# 功能描述

无需等待，立即启用屏保。 

# :DISPlay:SAVer[:STATe]

# 命令格式

:DISPlay:SAVer[:STATe] {ON|1|OFF|0} 

:DISPlay:SAVer[:STATe]? 

# 功能描述

打开或关闭屏幕保护功能。 

查询屏幕保护功能的开关状态。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>ON</td></tr></table>

# 说明

打开屏幕保护功能时，当超过 15分钟不操作前面板时，仪器自动进入屏幕保护模式，若再超过 30 分钟不操 作前面板时，仪器自动进入黑屏幕状态。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:DISP:SAV OFF /*关闭屏幕保护功能*/ 

:DISP:SAV? /*查询屏幕保护功能的状态，返回 OFF*/ 

:DISP:SAV 1 /*打开屏幕保护功能*/ 

:DISP:SAV? /*查询屏幕保护功能的状态，返回 $0 N ^ { \star } /$ 

# :HCOPy 命令

:HCOPy 命令用来设置和查询屏幕截图返回图像的格式以及执行屏幕截图操作。 

# 命令列表：

 :HCOPy:SDUMp:DATA? 

:HCOPy:SDUMp:DATA:FORMat 

# :HCOPy:SDUMp:DATA?

# 命令格式

:HCOPy:SDUMp:DATA? 

# 功能描述

查询前面板显示屏图像（屏幕截图）。 

# 返回格式

返回一个确定长度的二进制数据块，该数据块包含图像，且以#开头， 

如#9000230456BM6\x84\x03\x00......，其中，“#”后的“9”表示“9”后面的 9 个字符（000230456）用 来表示数据长度。 

# :HCOPy:SDUMp:DATA:FORMat

# 命令格式

:HCOPy:SDUMp:DATA:FORMat {BMP|PNG} 

:HCOPy:SDUMp:DATA:FORMat? 

# 功能描述

设置屏幕截图返回图像的格式为 BMP 或 PNG格式。 

查询屏幕截图返回图像的格式。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{BMP|PNG}</td><td>离散型</td><td>BMP|PNG</td><td>BMP</td></tr></table>

# 返回格式

返回 BMP 或 PNG。 

# 举例

:HCOP:SDUM:DATA:FORM BMP /*设置屏幕截图返回图像的格式为 BMP 格式*/ 

:HCOP:SDUM:DATA:FORM? /*查询屏幕截图返回图像的格式，返回 BMP*/ 

# IEEE488.2 通用命令

IEEE488.2 标准定义了一组常用命令，可执行复位、自检以及状态操作等功能。 

# 命令列表：

 *CLS 

 *ESE 

*ESR? 

*IDN? 

 *OPC 

 *PSC 

 *RCL 

? *RST 

*SAV 

*SRE 

*STB? 

 *TRG 

*WAI 

# *CLS

# 命令格式

*CLS 

# 功能描述

清除所有寄存器组中的事件寄存器和错误队列。 

# *ESE

# 命令格式

*ESE <value> 

*ESE? 

# 功能描述

启用要向状态字节寄存器报告的标准事件寄存器中的位。 

查询标准事件寄存器中使能的位。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>(value&gt;</td><td>整型</td><td>参考“说明”</td><td>0</td></tr></table>

# 说明

参数<value>是一个十进制值，该值与要向状态字节寄存器报告的标准事件寄存器中的位的二进制加权 和相对应。 

参数<value>设为 0时，执行该命令可以清除标准事件寄存器的使能寄存器。 

若已使用*PSC 1命令配置了仪器，则在下一次仪器通电时清除标准事件寄存器的使能寄存器。注意若 

已使用*PSC 0 命令配置了仪器，则在下一次仪器通电时不会清除标准事件寄存器的使能寄存器。 

# 返回格式

返回一个十进制值，该值与标准事件寄存器中使能的位的二进制加权和相对应。 

# *ESR?

# 命令格式

*ESR? 

# 功能描述

查询标准事件寄存器的事件寄存器。 

# 说明

标准事件寄存器的事件寄存器是一个只读寄存器，其中的位被锁存，查询该寄存器将清除该寄存器。一旦某 一位被置位，随后发生的该位所对应的事件将被忽略，直到该寄存器被查询命令或清除状态命令（*CLS）清 除。 

# 返回格式

返回一个十进制值，该值与标准事件寄存器的事件寄存器中所有位的二进制加权和相对应。 

# *IDN?

# 命令格式

*IDN? 

# 功能描述

查询仪器的标识字符串。 

# 返回格式

返回仪器的标识字符串，包括 4个部分，各部分之间用逗号隔开， 

如：Rigol Technologies,DG2102,DG20000000001,01.00.01，第 1 部分是制造商名称，第 2 部分是仪器型号， 第 3部分是仪器序列号，第 4部分是数字版版本号。 

# *OPC

# 命令格式

*OPC 

*OPC? 

# 功能描述

执行完之前已发送的所有的命令之后，置位标准事件寄存器中的 OPC（操作完成）位。 

查询之前已发送的所有的命令是否均已被执行，执行完之后，返回 1到输出缓冲区。 

# 说明

操作完成是指之前已发送的所有命令，包括*OPC 命令，都已被执行。 

. 您可以使用 $\star _ { \mathsf { O P C } }$ （操作完成）命令或*OPC?（操作完成查询）命令使系统在完成扫描或脉冲串时发出 信号。*OPC 命令在执行完之前已发送的所有的命令之后置位标准事件寄存器中的 OPC（操作完成）位， 使用总线触发扫描或脉冲串时，在该位被置位之前可以执行其他命令。*OPC?命令在执行完之前已发送 的所有的命令之后返回 1到输出缓冲区，在该命令完成之前不能执行其他命令。 

发送查询命令*OPC?并读取结果可以确保同步。 

编程设置仪器配置（通过执行命令串）时，将*OPC 命令作为最后一条命令可以确定何时命令队列已全 部被执行（命令队列全部被执行后，置位标准事件寄存器中的 OPC（操作完成）位）。 

# 返回格式

返回 1或 0。 

# 举例

*OPC /*配置仪器在执行完之前已发送的所有的命令之后，置位标准事件寄存器中的 OPC （操作完成）位*/ 

*OPC? /*查询之前所有的命令是否均已被执行，执行完之后，返回 1到输出缓冲区*/ 

# *PSC

# 命令格式

*PSC {0|1} 

*PSC? 

# 功能描述

启用或禁用通电时清除状态字节使能寄存器和标准事件使能寄存器。 

查询通电时是否清除状态字节使能寄存器和标准事件使能寄存器。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{0|1}</td><td>离散型</td><td>0|1</td><td>1</td></tr></table>

# 说明

*PSC 1 命令表示通电时清除状态字节使能寄存器和标准事件使能寄存器，*PSC 0命令表示通电时状态 字节使能寄存器和标准事件使能寄存器不受影响。 

您也可以分别发送*SRE 0和*ESE 0命令清除状态字节使能寄存器和标准事件使能寄存器。 

# 返回格式

返回 0或 1。 

# 举例

*PSC 1 /*启用通电时清除状态字节使能寄存器和标准事件使能寄存器*/ 

*PSC? /*查询通电时状态清除设置，返回 ${ 1 ^ { \star } } /$ 

# *RCL

# 命令格式

*RCL {0|1|2|3|4|5} 

# 功能描述

调用存储在指定的内部非易失性存储器位置的状态文件。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{0|1|2|3|4|5}</td><td>离散型</td><td>0|1|2|3|4|5</td><td>无</td></tr></table>

# 说明

 仪器内部分别提供 6个存储位置用于存储状态文件，编号分别为 0至 5。发送该命令可以调用仪器内部 非易失性存储器中指定存储位置的状态文件，选择编号0至5可以分别调用存储在相应位置的状态文件。 

 仅当指定的仪器内部非易失性存储器位置已存有有效的状态文件时，该命令有效。 

存储的状态文件包含：两通道选定的波形、频率、幅度、偏移、占空比、对称性、相位，使用的调制、 扫频、猝发参数和频率计参数以及 Utility 菜单下的辅助功能参数和系统参数。 

# *RST

# 命令格式

*RST 

# 功能描述

将仪器恢复至其出厂默认状态。 

# 说明

将仪器恢复至其出厂默认状态（请参考“出厂设置”），而不受:MEMory:STATe:RECall:AUTO 命令设置的 影响。 

该命令将异常中断正在进行的扫描或脉冲串。 

# *SAV

# 命令格式

*SAV {0|1|2|3|4|5} 

# 功能描述

以默认名称在指定的内部非易失性存储器位置存储当前的仪器状态。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{0|1|2|3|4|5}</td><td>离散型</td><td>0|1|2|3|4|5</td><td>无</td></tr></table>

# 说明

仪器内部分别提供 6个存储位置用于存储仪器状态，编号分别为 0至 5。默认的状态文件名称为 Scpin.RSF，n对应存储位置的编号。 

若指定的存储位置已存有文件，该命令将存储当前仪器状态到指定位置，直接覆盖原文件。 

有关状态文件的介绍请参考*RCL 命令下的“说明”。 

您可以发送*RCL 命令调用仪器内部非易失性存储器中已存储的状态文件。 

# 举例

*SAV 1 

/*将当前的仪器状态存储到仪器内部非易失性存储器中状态文件的存储位置 1， 文件名为 Scpi1.RSF*/ 

# *SRE

# 命令格式

*SRE <value> 

*SRE? 

# 功能描述

启用状态字节寄存器中的位，使其能够生成服务请求。 

查询状态字节寄存器中使能的位。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>(value&gt;</td><td>整型</td><td>见下文“说明”</td><td>无</td></tr></table>

# 说明

. 参数<value>是一个十进制值，该值与状态字节寄存器中要使能的位的二进制加权和相对应。在状态字 节寄存器的 bit6（主累加位）上对选定的位进行累加，如果有任一个选定的位从 0 变为 1，则都将产生 服务请求信号。 

参数<value>设为 0时，执行该命令可以清除状态字节寄存器的使能寄存器。 

若已使用*PSC 1命令配置了仪器，则在下一次仪器通电时清除状态字节寄存器的使能寄存器。若已使 用*PSC 0命令配置了仪器，则在下一次仪器通电时不会清除状态字节寄存器的使能寄存器。 

# 返回格式

返回一个十进制值，该值与状态字节寄存器中使能的位的二进制加权和相对应。 

# *STB?

# 命令格式

*STB? 

# 功能描述

查询状态字节寄存器的状态寄存器。 

# 说明

该命令不能清除服务请求，只要产生服务请求的条件仍然保留，就不清除状态字节寄存器的 bit6（主累加位）。 

# 返回格式

返回一个十进制值，该值与状态字节寄存器的状态寄存器中所有位的二进制加权和相对应。 

# *TRG

# 命令格式

*TRG 

# 功能描述

触发一次扫描或脉冲串。 

# 说明

只有当前扫描或脉冲串功能已打开并且触发源设为手动（使用 [:SOURce[<n>]]:SWEep:TRIGger:SOURce 或[:SOURce[<n>]]:BURSt:TRIGger:SOURce 命令）时，才 能从远程接口中触发扫描或脉冲串。 

当前扫描或脉冲串功能已打开并且触发源设为手动时，您也可以发送 

[:SOURce[<n>]]:SWEep:TRIGger[:IMMediate]命令或[:SOURce[<n>]]:BURSt:TRIGger[:IMMediate] 命令触发一次扫描或脉冲串。 

# *WAI

# 命令格式

*WAI 

# 功能描述

等待所有未完成操作完成之后，再通过接口执行任何其他的命令。 

# 说明

仅用于触发扫描模式或触发脉冲串模式，该命令可用来确保同步。 

# :LXI 命令

# 命令列表：

 :LXI:MDNS:ENABle 

:LXI:RESet 

:LXI:RESTart 

# :LXI:MDNS:ENABle

# 命令格式

:LXI:MDNS:ENABle {ON|1|OFF|0} 

:LXI:MDNS:ENABle? 

# 功能描述

启用或禁用多播域名系统（mDNS）。 

查询多播域名系统的启用状态。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>ON</td></tr></table>

# 返回格式

返回 ON 或 OFF。 

# 举例

:LXI:MDNS:ENAB ON /*启用多播域名系统*/ 

:LXI:MDNS:ENAB? /*查询多播域名系统的启用状态，返回 $\mathsf { O N } ^ { \star } /$ 

# :LXI:RESet

# 命令格式

:LXI:RESet 

# 功能描述

将 LAN设置重置为已知操作状态，从 DHCP 开始，如果 DHCP 失败，将使用 AutoIP。 

# 说明

发送该命令后 LAN接口可能需要几秒钟才能重新启动，具体取决于您的网络。 

如果已禁用 LAN 接口或特定的 LAN服务，您必须单独重新启用接口或服务，并关闭再重新打开仪器以 使 LAN正常运行。 

# :LXI:RESTart

# 命令格式

:LXI:RESTart 

# 功能描述

根据当前设置重新启动 LAN。 

# 说明

发送该命令后 LAN接口可能需要几秒钟才能重新启动，具体取决于您的网络。 

. 如果已禁用 LAN 接口或特定的 LAN服务，您必须单独重新启用接口或服务，并关闭再重新打开仪器以 使 LAN正常运行。 

# :MEMory 命令

:MEMory 命令用来查询仪器内部非易失性存储器提供的状态文件的存储空间以及已存储的状态文件，查询指 定位置是否已存有状态文件，删除、锁定及解锁内部存储器中的状态文件，查询和更改已存状态文件的文件 名以及设置开机配置。 

# 命令列表：

 :MEMory:NSTates? 

:MEMory:STATe:CATalog? 

:MEMory:STATe:DELete 

:MEMory:STATe:NAME 

 :MEMory:STATe:RECall:AUTO 

:MEMory:STATe:VALid? 

# :MEMory:NSTates?

# 命令格式

:MEMory:NSTates? 

# 功能描述

查询仪器内部非易失性存储器提供的状态文件存储位置的个数。 

# 返回格式

固定返回 6。 

# :MEMory:STATe:CATalog?

# 命令格式

:MEMory:STATe:CATalog? 

# 功能描述

查询仪器内部非易失性存储器中已存储的状态文件。 

# 说明

仪器内部非易失性存储器提供 6个状态文件存储位置。 

# 返回格式

返回一个字符串，由六部分组成，各部分之间以逗号隔开，顺序表示位置 1至 6 已存储文件的文件名，如 "Scpi1.RSF","Scpi2.RSF","0.RSF","1.RSF","012.RSF",""，其中双引号中的内容为相应位置处已存文件的文件 名，相应位置无已存文件时，仅返回双引号。 

# :MEMory:STATe:DELete

# 命令格式

:MEMory:STATe:DELete {0|1|2|3|4|5} 

# 功能描述

删除仪器内部非易失性存储器中指定位置的已存状态文件。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{0|1|2|3|4|5}</td><td>离散型</td><td>0|1|2|3|4|5</td><td>无</td></tr></table>

# 说明

 仪器内部非易失性存储器提供 6个状态文件存储位置，0至 5依次代表指定位置的已存状态文件。 

仅当指定的存储位置已存有状态文件时，该命令有效。 

# 举例

:MEM:STAT:DEL 1 /*删除仪器内部非易失性存储器中位置 1 的已存状态文件*/ 

# :MEMory:STATe:NAME

# 命令格式

:MEMory:STATe:NAME {0|1|2|3|4|5}[,<name>] 

:MEMory:STATe:NAME? {0|1|2|3|4|5} 

# 功能描述

更改仪器内部非易失性存储器中指定存储位置已存状态文件的文件名。 

查询仪器内部非易失性存储器中指定存储位置已存状态文件的文件名。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{0|1|2|3|4|5}</td><td>离散型</td><td>0|1|2|3|4|5</td><td>无</td></tr><tr><td></td><td>ASCII字符串</td><td>见下文“说明”</td><td>空</td></tr></table>

# 说明

仪器内部非易失性存储器提供 6个状态文件存储位置，0至 5顺序代表指定位置的已存状态文件。 

参数<name>为指定的文件名，长度不超过 7个字符，可以为中文字符、英文大写字符和数字，其中一 个中文字符占 2 个字符。若省略该参数，文件名为空。 

仅当指定的存储位置已存有状态文件（:MEMory:STATe:VALid?）时，该命令有效。 

# 返回格式

返回一个带双引号的字符串，如"123.RSF"，其中 123 为文件名，.RSF 为状态文件的文件名后缀。 

# 举例

:MEM:STAT:VAL? 2 

/*查询仪器内部非易失性存储器中存储位置 2是否已存有状态文件，返回 ${ 1 ^ { \star } } /$ 

:MEM:STAT:NAME 2,123 

/*更改仪器内部非易失性存储器中存储位置 2已存状态文件的文件名为 123.RSF*/ 

:MEM:STAT:NAME? 2 

/*查询仪器内部非易失性存储器中存储位置 2已存状态文件的文件名，返回 "123.RSF"*/ 

# :MEMory:STATe:RECall:AUTO

# 命令格式

:MEMory:STATe:RECall:AUTO {ON|1|OFF|0} 

:MEMory:STATe:RECall:AUTO? 

# 功能描述

设置下次通电开机时使用的仪器配置为上次值（ON 或 1）或默认值（OFF或 0）。 

查询下次通电开机时使用的仪器配置。 

# 参数

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 说明

上次值（ON或 1）：仪器上电时使用上次关机前的系统配置，包括除通道输出开关状态之外的所有系统 参数和状态。 

默认值（OFF或 0）：仪器上电时使用出厂默认值，某些不受恢复出厂值影响的参数除外，见“出厂设 置”。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:MEM:STAT:RECall:AUTO ON /*设置下次通电开机时使用的仪器配置为上次值*/ 

:MEM:STAT:RECall:AUTO? /*查询下次通电开机时使用的仪器配置，返回 $\mathsf { O N } ^ { \star } /$ 

# :MEMory:STATe:VALid?

# 命令格式

:MEMory:STATe:VALid? {0|1|2|3|4|5} 

# 功能描述

查询仪器内部非易失性存储器中指定存储位置是否已存有状态文件。 

# 参数

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{0|1|2|3|4|5}</td><td>离散型</td><td>0|1|2|3|4|5</td><td>无</td></tr></table>

# 说明

仪器内部非易失性存储器提供 6个状态文件存储位置，0至 5顺序代表指定位置的已存状态文件。 

# 返回格式

返回 1或 0，1 表示指定存储位置已存有状态文件，0 表示指定存储位置没有存储状态文件。 

# :MMEMory 命令

:MMEMory 命令用来查询和设置与仪器内部和外部存储器相关的信息。仪器内部存储器一直存在，而外部存 储器仅当后面板 USB HOST 接口检测到 U盘时可用。 

# 命令列表：

$\spadesuit$ :MMEMory:CATalog[:ALL]? 

$\spadesuit$  :MMEMory:CATalog:DATA:ARBitrary? 

:MMEMory:CATalog:STATe? 

:MMEMory:CDIRectory 

:MMEMory:COPY 

:MMEMory:DOWNload:FNAMe 

:MMEMory:DOWNload:DATA 

 :MMEMory:LOAD[:ALL] 

:MMEMory:LOAD:DATA 

 :MMEMory:LOAD:STATe 

:MMEMory:MDIRectory 

:MMEMory:MOVE 

:MMEMory:RDIRectory? 

:MMEMory:RDIRectory 

:MMEMory:STORe[:ALL] 

 :MMEMory:STORe:DATA 

:MMEMory:STORe:STATe 

# :MMEMory:CATalog[:ALL]?

# 命令格式

:MMEMory:CATalog[:ALL]? [<folder>] 

# 功能描述

查询当前路径下的所有文件和文件夹。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>&lt;folder&gt;</td><td>ASCII字符串</td><td>有效路径</td><td>无</td></tr></table>

# 说明

参数<folder>为内部或外部存储器中的有效路径，格式为带双引号的字符串，如"C:\"、"D:\Rigol"。 

# 返回格式

返回一个字符串，格式：已用空间,可用空间,"大小,属性,名称",……，其中，已用空间和可用空间的单位为 字节；文件的属性为空，大小为其所占空间的大小；文件夹的属性为 DIR，大小为文件夹中的文件和文件夹 的个数和再加 1。例如：28672,4102361088,"3,DIR,Rigol","80,,Rigol1.RAF","1360,,Rigol0.RSF"，表示当前 路径的已用空间为 28672字节，可用空间为 4102361088 字节；包含 1 个文件夹 Rigol，且 Rigol 中含有 2 个文件或文件夹；包含 2个文件，任意波文件 Rigol1.RAF 的大小为 80 字节，状态文件 Rigol0.RSF 的大小为 1360 字节。 

# 举例

假设当前路径为 D:\， 

:MMEM:CAT? 

/*查询外部存储器中的所有文件和文件夹，返回 

28672,4102361088,"3,DIR,Rigol","80,,Rigol1.RAF","1360,,Rigol0.RSF"*/ 

# :MMEMory:CATalog:DATA:ARBitrary?

# 命令格式

:MMEMory:CATalog:DATA:ARBitrary? [<folder>] 

# 功能描述

查询当前操作路径下的任意波和序列波（*.RAF）文件。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>&lt;folder&gt;</td><td>ASCII字符串</td><td>有效路径</td><td>无</td></tr></table>

# 说明

参数<folder>为内部或外部存储器中的有效路径，格式为带双引号的字符串，如"C:\"、"D:\Rigol"。 

# 返回格式

返回一个字符串，格式：已用空间,可用空间,"大小,属性,名称",……，其中，已用空间和可用空间的单位为字 节；文件的属性为空，大小为其所占空间的大小。例如：28672,4102361088,"80,,Rigol1.RAF"，表示当前路 径的已用空间为 28672 字节，可用空间为 4102361088 字节；包含 1个任意波文件 Rigol1.RAF，其大小为 80字节。 

# 举例

假设当前路径为 D:\， 

:MMEM:CAT:DATA:ARB? /*查询外部存储器目录下的任意波和序列波文件，返回 

28672,4102361088,"80,,Rigol1.RAF"*/ 

# :MMEMory:CATalog:STATe?

# 命令格式

:MMEMory:CATalog:STATe? [<folder>] 

# 功能描述

查询当前操作路径下的状态文件。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>&lt;folder&gt;</td><td>ASCII字符串</td><td>有效路径</td><td>无</td></tr></table>

# 说明

参数<folder>为内部或外部存储器中的有效路径，格式为带双引号的字符串，如"C:\"、"D:\Rigol"。 

# 返回格式

返回一个字符串，格式：已用空间,可用空间,"大小,属性,名称",……，其中，已用空间和可用空间的单位为字 节；文件的属性为空，大小为其所占空间的大小。例如：28672,4102361088,"1360,,Rigol0.RSF"，表示当前 路径的已用空间为 28672 字节，可用空间为 4102361088 字节；包含 1 个状态文件 Rigol0.RSF，其大小为 1360 字节。 

# 举例

假设当前路径为 D:\， 

:MMEM:CAT:STAT? /*查询外部存储器目录下的状态文件，返回 

28672,4102361088,"1360,,Rigol0.RSF"*/ 

# :MMEMory:CDIRectory

# 命令格式

:MMEMory:CDIRectory $<$ <directory_name> 

:MMEMory:CDIRectory? 

# 功能描述

设置当前路径。 

查询当前路径。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>&lt;directory_name&gt;</td><td>ASCII字符串</td><td>有效路径</td><td>&quot;C:\&quot;</td></tr></table>

# 说明

参数<directory_name>为内部或外部存储器中的有效路径，格式为带双引号的字符串，如"C:\"、"D:\Rigol"。 

# 返回格式

返回一个字符串，格式为带双引号的字符串，双引号中的内容为当前路径，例如"D:"。 

# 举例

:MMEM:CDIR "D:\" /*设置当前路径为 D盘（外部存储器）*/ 

:MMEM:CDIR? /*查询当前路径，返回"D:"*/ 

# :MMEMory:COPY

# 命令格式

:MMEMory:COPY $<$ <directory_name>,<file_name> 

# 功能描述

将当前路径下的文件复制到指定的路径（非当前路径）下。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td></td><td>ASCII字符串</td><td>有效路径</td><td>无</td></tr><tr><td></td><td>ASCII字符串</td><td>当前路径下的文件的文件名</td><td>无</td></tr></table>

# 说明

参数<directory_name $>$ 为内部或外部存储器中的有效路径，格式为带双引号的字符串，如"C:\"、"D:\Rigol"。 

# 举例

假设当前路径为 D:\， 

:MMEM:COPY "D:\Rigol","Rigol1.RAF" /*将外部存储器目录下的 Rigol1.RAF 文件复制到 "D:\Rigol"路径（即 D 盘下的 Rigol 文件夹）下*/ 

# :MMEMory:DELete

# 命令格式

:MMEMory:DELete <file_name> 

# 功能描述

删除当前路径下的指定文件或空文件夹。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td></td><td>ASCII字符串</td><td>当前路径下的文件的文件名或空文件夹的文件夹名</td><td>无</td></tr></table>

# 说明

参数<file_name>为当前路径下的文件的文件名或空文件夹的文件夹名，格式为带双引号的字符串，如 "Rigol1.RAF"。 

# 举例

假设当前路径为 D:\， 

:MMEM:DEL " D:\Rigol1.RAF" /*删除外部存储器（D:\）下的文件 Rigol1.RAF*/ 

# :MMEMory:DOWNload:FNAMe

# :MMEMory:DOWNload:DATA

# 命令格式

:MMEMory:DOWNload:FNAMe <file_name> 

:MMEMory:DOWNload:DATA <binary_block> 

# 功能描述

在当前路径下创建一个文件。 

加载二进制数据至当前创建的文件中。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>&lt;file_name&gt;</td><td>ASCII字符串</td><td>有效文件名</td><td>无</td></tr><tr><td>&lt;binary_block&gt;</td><td>ASCII字符串</td><td>有效数据</td><td>无</td></tr></table>

# 说明

参数<file_name>的格式为带双引号的字符串，文件名长度不超过 7个字符，可以为中英文字符和数字，其 中，一个中文字符占 2 个字符。 

# 举例

假设当前路径为 C:\， 

:MMEM:DOWN:FNAM "C:\state" /*在内部存储器 C 盘创建一个“state”文件*/ 

:MMEM:DOWN:DATA #15Hello /*将数据“Hello”加载至内部存储器的“state”文件中*/ 

# :MMEMory:LOAD[:ALL]

# 命令格式

:MMEMory:LOAD[:ALL] <file_name> 

# 功能描述

加载当前路径下的指定状态文件或任意波文件。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>&lt;file_name&gt;</td><td>ASCII字符串</td><td>当前路径下的状态文件或任意波文件的文件名</td><td>无</td></tr></table>

# 说明

参数<file_name>为内部或外部存储器当前路径下的状态文件或任意波文件的文件名，格式为带双引号 的字符串，如"Rigol0.RSF"。 

若要加载的文件为任意波文件，则加载到当前通道。 

# 举例

假设当前路径为 D:\， 

:MMEM:LOAD "Rigol0.RSF" /*加载外部存储器（D:\）下的文件 Rigol0.RSF*/ 

# :MMEMory:LOAD:DATA

# 命令格式

:MMEMory:LOAD:DATA $\tt { < n > }$ ] <file_name> 

# 功能描述

加载当前路径下的指定任意波或序列波（*.RAF）文件到指定通道。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;file_name&gt;</td><td>ASCII字符串</td><td>当前路径下的任意波或序列波文件的文件名</td><td>无</td></tr></table>

# 说明

参数 $[ < n >$ ]表示加载当前路径下的指定任意波或序列波文件到 CH1还是 CH2，省略该参数时，默认加载 到 CH1。 

参数<file_name>为当前路径下的任意波或序列波文件的文件名，格式为带双引号的字符串，如 "Rigol4.RAF"。 

# 举例

假设当前路径为 D:\Rigol， 

:MMEM:LOAD:DATA "Rigol4.RAF" 

/*加载当前路径（D:\Rigol）下的任意波文件 Rigol4.RAF 到当前 通道*/ 

# :MMEMory:LOAD:STATe

# 命令格式

:MMEMory:LOAD:STATe <file_name> 

# 功能描述

加载当前路径下的指定状态文件。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td></td><td>ASCII字符串</td><td>当前路径下的状态文件的文件名</td><td>无</td></tr></table>

# 说明

参数<file_name>为当前路径下的状态文件的文件名，格式为带双引号的字符串，如"Rigol0.RSF"。 

# 举例

假设当前路径为 D:\， 

:MMEM:LOAD:STAT " D:\Rigol0.RSF" 

/*加载外部存储器（D:\）下的状态文件 Rigol0.RSF*/ 

# :MMEMory:MDIRectory

# 命令格式

:MMEMory:MDIRectory <dir_name> 

# 功能描述

在当前路径下以指定名称创建一个文件夹。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

# 说明

参数<dir_name>的格式为带双引号的字符串，双引号中的内容为要创建的文件夹的名称，长度不超过 7个字符，可以为中文字符、英文大写字符和数字，其中，一个中文字符占 2 个字符。 

若当前路径已存在同名文件夹，则提示远程命令错误。 

该命令仅适用于外部存储器。 

# 举例

假设当前路径为 D:\， 

:MMEM:MDIR "RIGOL1" /*在 D盘目录下创建一个名为“RIGOL1”的文件夹*/ 

# :MMEMory:MOVE

# 命令格式

:MMEMory:MOVE <file1>,<file2> 

# 功能描述

将当前路径下的文件 1 移动到路径 2。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>&lt;file1&gt;</td><td>ASCII字符串</td><td>当前路径中的文件</td><td>无</td></tr><tr><td>&lt;file2&gt;</td><td>ASCII字符串</td><td>有效路径</td><td>无</td></tr></table>

# 说明

参数<file1 $>$ 为当前路径中的文件，格式为带双引号的字符串，如"Rigol.RSF"。 

 参数<file2>为内部或外部存储器中的有效路径，格式为带双引号的字符串，如"C:\"、"D:\Rigol"。 

# 举例

假设当前路径为 D:\， 

:MMEM:MOVE "D:\Rigol.RSF","D:\Rigol" 

/*将外部存储器目录下的 Rigol.RSF文件移动到 D 盘下的 Rigol 文件夹中*/ 

# :MMEMory:RDIRectory?

# 命令格式

:MMEMory:RDIRectory? 

# 功能描述

查询当前可用盘符。 

# 返回格式

返回一个字符串，格式："可用盘符数,"可用盘符名称:""，例如"1,"D:""，表示当前有一个可用盘符，名称为 D:。如果当前没有可用盘符，返回"0,"NULL""。 

# :MMEMory:RDIRectory

# 命令格式

:MMEMory:RDIRectory <folder> 

# 功能描述

删除当前路径中的指定目录（空文件夹）。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>&lt;folder&gt;</td><td>ASCII字符串</td><td>空文件夹的文件夹名</td><td>无</td></tr></table>

# 举例

假设当前路径为 D:\，其中包含一个空文件夹且其文件夹名为 111， 

:MMEM:RDIR "111" /*删除外部存储器中的空文件夹 $1 1 1 ^ { \star } /$ 

# :MMEMory:STORe[:ALL]

# 命令格式

:MMEMory:STORe[:ALL] <file_name> 

# 功能描述

以指定名称将当前仪器状态或当前通道的任意波数据以状态文件或任意波文件的形式存储到当前路径下。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>&lt;file_name&gt;</td><td>ASCII字符串</td><td>指定的状态文件或任意波文件的文件名</td><td>无</td></tr></table>

# 说明

参数<file_name $>$ 的格式为带双引号的字符串，双引号中的内容为指定的状态文件名或任意波文件名（包含 文件类型后缀.RSF 或.RAF），文件名长度不超过 7个字符，可以为中英文字符和数字，其中，一个中文字符 占 2个字符。 

# 举例

假设当前路径为 D:\， 

:MMEM:STOR "R00.RSF" /*将当前仪器状态以状态文件的形式存储到 D 盘目录下，文件名为 R00.RSF*/ 

# :MMEMory:STORe:DATA

# 命令格式

:MMEMory:STORe:DATA[<n>] <file_name> 

# 功能描述

以指定名称将指定通道的任意波或序列波数据以任意波或序列波（*.RAF）文件的形式存储到当前路径下。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;file_name&gt;</td><td>ASCII字符串</td><td>指定的任意波或序列波的文件名</td><td>无</td></tr></table>

# 说明

参数<file_name>的格式为带双引号的字符串，双引号中的内容为指定的任意波或序列波文件名（包含文件 类型后缀.RAF），文件名长度不超过 7个字符，可以为中英文字符和数字，其中，一个中文字符占 2个字符。 

# 举例

假设当前路径为 D:\， 

:MMEM:STOR:DATA "R11.RAF" /*将当前通道的任意波形数据以任意波文件的形式存储到 D 盘目录下，文 件名为 R11.RAF*/ 

# :MMEMory:STORe:STATe

# 命令格式

:MMEMory:STORe:STATe <file_name> 

# 功能描述

以指定名称将当前的仪器状态以状态文件的形式存储到当前路径下。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>&lt;file_name&gt;</td><td>ASCII字符串</td><td>见下文“说明”</td><td>无</td></tr></table>

# 说明

参数<file_name>的格式为带双引号的字符串，双引号中的内容为指定的状态文件文件名（包含文件类型后 缀.RSF），文件名长度不超过 7个字符，可以为中英文字符和数字，其中，一个中文字符占 2个字符。 

# 举例

假设当前路径为 D:\， 

:MMEM:STOR:STAT "R22.RSF" /*将当前仪器状态以状态文件的形式存储到 D 盘目录下，文件名为 R22.RSF*/ 

# :OUTPut 命令

:OUTPut 命令用来设置和查询与通道输出和同步信号相关的信息，包括设置和查询通道输出状态、输出极性、 输出阻抗、输出模式以及门控极性，还包括设置和查询同步信号的输出状态、输出极性和延时时间。 

# 命令列表：

 :OUTPut[<n>]:IMPedance 

 :OUTPut[<n>]:LOAD 

:OUTPut[<n>]:POLarity 

:OUTPut[<n>][:STATe] 

 :OUTPut[<n>]:SYNC:POLarity 

:OUTPut[<n>]:SYNC[:STATe] 

 :OUTPut[<n>]:VOLLimit:HIGH 

:OUTPut[<n>]:VOLLimit:LOW 

:OUTPut[<n>]:VOLLimit[:STATe] 

```txt
:OUTPUT [<n>]:IMPedance :OUTPUT [<n>]:LOAD 
```

# 命令格式

:OUTPut[ $\mathsf { < n > j }$ ]:IMPedance {<ohms>|INFinity|MINimum|MAXimum} 

:OUTPut[ $\mathsf { < n > }$ ]:LOAD {<ohms $>$ |INFinity|MINimum|MAXimum} 

:OUTPut $\cdot < n >$ ]:IMPedance? [MINimum|MAXimum] 

:OUTPut $\cdot < n > \bar { . }$ ]:LOAD? [MINimum|MAXimum] 

# 功能描述

设置指定通道输出连接器的输出阻抗值。 

查询指定通道输出连接器的输出阻抗值。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;ohms&gt;</td><td>整型</td><td>1Ω至10kΩ</td><td>50Ω</td></tr></table>

# 说明

省略参数 $[ < n > ]$ 时，默认设置和查询 CH1的相关参数。 

 参数<ohms $>$ 表示设置指定通道输出连接器的输出阻抗值为其可设范围中的某一指定值；参数 INFinity 表示设置指定通道输出连接器的输出阻抗为高阻（HighZ）。 

 输出阻抗的设置影响输出振幅和 DC 偏移。如果实际负载与指定的值不同，则显示的电压电平将不匹配 被测部件的电压电平。要确保正确的电压电平，必须保证负载阻抗设置与实际负载匹配。 

# 返回格式

以科学计数形式返回输出阻抗，有效位数为 7位，如 $1 . 0 0 0 0 0 0 0 \mathsf { E } + 0 2$ ，表示输出阻抗为 100Ω；若设置指定 通道输出连接器的输出阻抗值为高阻（INFinity），则返回 $9 . 9 0 0 0 0 0 0 \mathsf { E } + 3 7$ 。 

# 举例

:OUTP1:IMP INF /*设置 CH1输出连接器的输出阻抗为高阻*/ 

:OUTP1:IMP? /*查询 CH1输出连接器的输出阻抗值，返回 $9 . 9 0 0 0 0 0 0 \mathsf { E } + 3 7 ^ { \star } /$ 

:OUTP1:LOAD 100 /*设置 CH1 输出连接器的输出阻抗值为 $1 0 0 \Omega ^ { \star } /$ 

:OUTP1:LOAD? /*查询 CH1输出连接器的输出阻抗值，返回 $1 . 0 0 0 0 0 0 0 \mathsf { E } { + } 0 2 ^ { \star } /$ 

# :OUTPut[<n>]:POLarity

# 命令格式

:OUTPut[ $\angle 1 = 1 7 ^ { \circ }$ ]:POLarity {NORMal|INVerted} 

:OUTPut[ $\mathsf { \ / { < n > } }$ ]:POLarity? 

# 功能描述

设置指定通道的输出极性为常规（NORMal）或反相（INVerted）。 

查询指定通道的输出极性。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{NORMAL|INVerted}</td><td>离散型</td><td>NORMAL|INVerted</td><td>NORMAL</td></tr></table>

# 说明

省略参数 $\cdot < n > ]$ 时，默认设置和查询 CH1的相关参数。 

通道的输出极性是指通道输出连接器上的信号为常规（NORMal）输出或反相（INVerted）输出。常规 模式下，输出正常波形；反相模式下，将波形反相后输出。 

波形反相是相对于偏移电压进行反相。波形反相后，任何偏移电压都不变，与波形相关的同步信号也不 反相。 

# 返回格式

返回 NORM 或 INV。 

# 举例

:OUTP1:POL NORM /*设置 CH1 输出极性为常规*/ 

:OUTP1:POL? /*查询 CH1 的输出极性，返回 NORM*/ 

# :OUTPut[<n>][:STATe]

# 命令格式

:OUTPut[ $< \mathsf { n } >$ ][:STATe] {ON|1|OFF|0} 

:OUTPut[ $< \mathsf { n } >$ ][:STATe]? 

# 功能描述

打开或关闭指定通道的输出。 

查询指定通道的输出状态。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 说明

省略参数 $\cdot < n > .$ ]时，默认设置和查询 CH1的相关参数。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:OUTP1? /*查询 CH1的输出状态，返回 $\tt O F F ^ { \star } /$ 

:OUTP1 ON /*打开 CH1 的输出*/ 

:OUTP1? /*查询 CH1的输出状态，返回 $\mathsf { O N } ^ { \star } /$ 

# :OUTPut[<n>]:SYNC:POLarity

# 命令格式

:OUTPut[ $< \mathsf { n } >$ ]:SYNC:POLarity {POSitive|NEGative} 

:OUTPut[ $\mathsf { < n > }$ ]:SYNC:POLarity? 

# 功能描述

选择指定通道后面板 [Sync/Ext Mod/Trig/FSK] 连接器上同步信号的输出极性为常规（POSitive）或反 相（NEGative）。 

查询指定通道后面板 [Sync/Ext Mod/Trig/FSK] 连接器上同步信号的输出极性。 

# 参数

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{POSitive|NEGative}</td><td>离散型</td><td>POSitive|NEGative</td><td>POSitive</td></tr></table>

# 说明

省略参数 $[ < n > ]$ 时，默认设置和查询 CH1的相关参数。 

同步信号的输出极性是指通道后面板 [Sync/Ext Mod/Trig/FSK] 连接器上同步信号为常规 （POSitive）输出或反相（NEGative）输出。常规模式下，输出正常同步信号；反相模式下，将同步信 号反相后输出。 

波形反相（:OUTPut[<n>]:POLarity）后，与波形相关的同步信号并不反相。 

# 返回格式

返回 POS 或 NEG。 

# 举例

:OUTP1:SYNC:POL POS /*选择后面板 [CH1/Sync/Ext Mod/Trig/FSK] 连接器上同步信号的输出极 性为常规*/ 

:OUTP1:SYNC:POL? /*查询后面板 [CH1/Sync/Ext Mod/Trig/FSK] 连接器上同步信号的输出极 性，返回 POS*/ 

# :OUTPut[<n>]:SYNC[:STATe]

# 命令格式

:OUTPut[ $\tt { < n > }$ ]:SYNC[:STATe] {ON|1|OFF|0} 

:OUTPut $\angle 1 = 1 7 ^ { \circ }$ ]:SYNC[:STATe]? 

# 功能描述

启用或禁用从指定通道后面板 [Sync/Ext Mod/Trig/FSK] 连接器输出同步信号。 

查询指定通道后面板 [Sync/Ext Mod/Trig/FSK] 连接器同步信号的输出状态。 

# 参数

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>ON</td></tr></table>

# 说明

DG2000可以从单通道或同时从双通道输出基本波形（噪声除外）、任意波形、谐波、扫频波形、脉冲 串波形、已调制波形的同步信号。该同步信号从后面板相应通道的 [Sync/Ext Mod/Trig/FSK] 连接 器输出。 

省略参数 $[ < n > ]$ 时，默认设置和查询 CH1的相关参数。 

当载波频率大于 30MHz 时，同步信号将分频输出。 

如果已禁用同步信号，则扫描使用的标志信号也禁用。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:OUTP1:SYNC 1 /*启用从后面板 [CH1/Sync/Ext Mod/Trig/FSK] 连接器输出同步信号*/ 

:OUTP1:SYNC? /*查询后面板 [CH1/Sync/Ext Mod/Trig/FSK] 连接器同步信号的输出状态，返回 $\mathrm { O N } ^ { \star } /$ 

:OUTP1:SYNC OFF /*禁用从后面板 [CH1/Sync/Ext Mod/Trig/FSK] 连接器输出同步信号*/ 

:OUTP1:SYNC? /*查询后面板 [CH1/Sync/Ext Mod/Trig/FSK] 连接器同步信号的输出状态，返回 $\tt O F F ^ { \star } /$ 

# :OUTPut[<n>]:VOLLimit:HIGH

# 命令格式

:OUTPut[ $\mathsf { \ / { < n > } }$ ]:VOLLimit:HIGH <amp> 

:OUTPut[ $\mathsf { < n > j }$ ]:VOLLimit:HIGH? 

# 功能描述

设置电压限制高电平幅值。 

查询电压限制高电平幅值。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;amp&gt;</td><td>实型</td><td>见下文“说明”</td><td>0V</td></tr></table>

# 说明

省略参数[ $< n > ]$ 时，默认设置和查询 CH1的相关参数。 

高电平限制可设置范围取决于当前幅度和偏移的设置值。 

# 返回格式

以科学计数形式返回高电平限制值，有效位数为 7 位，如 1.000000E $+ 0 0$ ，表示高电平限制值为 1V。 

# 举例

:OUTP1:VOLLimit:HIGH 1 /*设置 CH1的电压限制高电平幅值为 ${ 1 \vee ^ { \star } / }$ 

:OUTP1:VOLLimit:HIGH? /*查询 CH1的电压限制高电平幅值，返回 $1 . 0 0 0 0 0 0 0 \mathsf { E } { + } 0 0 ^ { \star } /$ 

# :OUTPut[<n>]:VOLLimit:LOW

# 命令格式

:OUTPut[ $\mathsf { < n > }$ ]:VOLLimit:LOW <amp> 

:OUTPut[ $\mathsf { < n > }$ ]:VOLLimit:LOW? 

# 功能描述

设置电压限制低电平幅值。 

查询电压限制低电平幅值。 

# 参数

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;amp&gt;</td><td>实型</td><td>见下文“说明”</td><td>0V</td></tr></table>

# 说明

省略参数 $[ < n > ]$ 时，默认设置和查询 CH1的相关参数。 

低电平限制的可设置范围取决于当前幅度和偏移的设置值。 

# 返回格式

以科学计数形式返回低电平限制值，有效位数为 7 位，如-1.000000E $+ 0 0$ ，表示低电平限制值为-1V。 

# 举例

:OUTP1:VOLLimit:LOW /*设置 CH1的电压限制低电平幅值为- ${ 1 \vee ^ { \star } / }$ 

:OUTP1:VOLLimit:LOW? /*查询 CH1 的电压限制低电平幅值，返回-1.000000E+00*/ 

# :OUTPut[<n>]:VOLLimit[:STATe]

# 命令格式

:OUTPut[ $\mathsf { < n > j }$ ]:VOLLimit[:STATe] {ON|1|OFF|0} 

:OUTPut $\cdot < n > \bar { . }$ ]:VOLLimit[:STATe]? 

# 功能描述

打开或关闭电压限制开关。 

查询电压限制开关的设置状态。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>ON</td></tr></table>

# 说明

省略参数 $[ < n > ]$ 时，默认设置和查询 CH1的相关参数。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:OUTP1:VOLLimit? /*查询 CH1的电压限制开关状态，返回 OFF*/ 

:OUTP1:VOLLimit ON /*打开 CH1的电压限制开关*/ 

:OUTP1:VOLLimit? /*查询 CH1 的电压限制开关状态，返回 $\mathsf { O N } ^ { \star } /$ 

# :ROSCillator 命令

:ROSCillator 命令用来设置系统时钟源和查询当前选择的系统时钟源。 

# 命令列表：

:ROSCillator:SOURce 

:ROSCillator:SOURce:CURRent? 

# :ROSCillator:SOURce

# 命令格式

:ROSCillator:SOURce {INTernal|EXTernal} 

# 功能描述

选择系统时钟源为内部源（INTernal）或外部源（EXTernal）。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{INTernal|EXTernal}</td><td>离散型</td><td>INTernal|EXTernal</td><td>INTernal</td></tr></table>

# 说明

DG2000提供 10MHz 的内部时钟源，也接收从后面板 [10MHz In/Out] 连接器输入的外部时钟源， 还可以从 [10MHz In/Out] 连接器输出时钟源，供其他设备使用。 

若选择外部源（EXTernal），系统将检测后面板 [10MHz In/Out] 连接器是否有有效的外部时钟信号 输入。若没有检测到有效的时钟源，则弹出提示消息“系统没有检测到有效的外部时钟！”，并自动将时 钟源切换成“内部”。 

. 您可以发送:ROSCillator:SOURce:CURRent?命令查询当前选择的系统时钟源类型。 

您可以通过时钟源的设置使两台仪器或多台仪器之间同步。两台仪器同步时，不能使用“同相位”功能 （“同相位”功能只适用于调整同一台仪器的两个输出通道之间的相位关系，不能改变两台仪器之间的 输出通道的相位关系）。您可以通过改变每个输出通道的起始相位（[:SOURce[<n>]]:PHASe[:ADJust]） 来改变两台仪器之间的相位关系。 

# 举例

:ROSC:SOUR INT /*选择系统时钟源为内部源*/ 

# :ROSCillator:SOURce:CURRent?

# 命令格式

:ROSCillator:SOURce:CURRent? 

# 功能描述

查询当前选择的系统时钟源。 

# 说明

您可以发送:ROSCillator:SOURce 命令选择系统时钟源为内部源或外部源。 

# 返回格式

返回 INT 或 EXT。 

# 举例

:ROSC:SOUR:CURR? /*查询当前选择的系统时钟源，返回 INT*/ 

# :SOURce 命令

:SOURce 命令用来设置和查询通道参数，调制、扫频、脉冲串功能相关参数，耦合、波形叠加参数以及打开 和关闭相应功能。 

DG2000系列不同型号和不同波形的频率可设范围如下表所示。 


表 2-1 DG2000 系列不同型号和不同波形的频率可设范围


<table><tr><td>频率特性</td><td>DG2052</td><td>DG2072</td><td>DG2102</td></tr><tr><td>正弦波</td><td>1μHz至50MHz</td><td>1μHz至70MHz</td><td>1μHz至100MHz</td></tr><tr><td>方波</td><td>1μHz至15MHz</td><td>1μHz至20MHz</td><td>1μHz至25MHz</td></tr><tr><td>锯齿波</td><td>1μHz至1.5MHz</td><td>1μHz至1.5MHz</td><td>1μHz至2MHz</td></tr><tr><td>脉冲</td><td>1μHz至15MHz</td><td>1μHz至20MHz</td><td>1μHz至25MHz</td></tr><tr><td>谐波</td><td>1μHz至20MHz</td><td>1μHz至20MHz</td><td>1μHz至25MHz</td></tr><tr><td>噪声(-3dB)</td><td colspan="3">100MHz带宽</td></tr><tr><td>任意波</td><td>1μHz至15MHz</td><td>1μHz至20MHz</td><td>1μHz至20MHz</td></tr><tr><td>双音</td><td>1μHz至20MHz</td><td>1μHz至20MHz</td><td>1μHz至20MHz</td></tr><tr><td>PRBS</td><td>2kbps至40Mbps</td><td>2kbps至50Mbps</td><td>2kbps至60Mbps</td></tr><tr><td>RS232</td><td colspan="3">波特率范围:9600, 14400, 19200, 38400, 57600, 115200, 128000, 230400</td></tr><tr><td>序列</td><td>2k至60MSa/s</td><td>2k至60MSa/s</td><td>2k至60MSa/s</td></tr></table>

# 命令列表：

 :SOURce:APPLy 命令 

 :SOURce:BURSt 命令 

 :SOURce:FREQuency 命令 

 :SOURce:FUNCtion 命令 

 :SOURce:HARMonic 命令 

:SOURce:MARKer 命令 

:SOURce[:MOD]:AM 命令 

 :SOURce[:MOD]:ASKey 命令 

:SOURce[:MOD]:FM 命令 

:SOURce[:MOD]:FSKey 命令 

 :SOURce[:MOD]:PM 命令 

:SOURce[:MOD]:PSKey 命令 

 :SOURce[:MOD]:PWM 命令 

:SOURce:MOD 命令 

 :SOURce:PERiod 命令 

 :SOURce:PHASe 命令 

 :SOURce:PULSe 命令 

:SOURce:SUM 命令 

 :SOURce:SWEep 命令 

 :SOURce:TRACe 命令 

:SOURce:TRACK 命令 

:SOURce:VOLTage 命令 

# :SOURce:APPLy 命令

# 命令列表：

$\spadesuit$ [:SOURce[<n>]]:APPLy? 

? [:SOURce[<n>]]:APPLy:DC 

$\spadesuit$  [:SOURce[<n>]]:APPLy:DUALTone 

 [:SOURce[<n>]]:APPLy:HARMonic 

 [:SOURce[<n>]]:APPLy:NOISe 

 [:SOURce[<n>]]:APPLy:PRBS 

[:SOURce[<n>]]:APPLy:PULSe 

 [:SOURce[<n>]]:APPLy:RAMP 

[:SOURce[<n>]]:APPLy:RS232 

 [:SOURce[<n>]]:APPLy:SEQuence 

[:SOURce[<n>]]:APPLy:SINusoid 

 [:SOURce[<n>]]:APPLy:SQUare 

? [:SOURce[<n>]]:APPLy:USER 

# [:SOURce[<n>]]:APPLy?

# 命令格式

[:SOURce[<n>]]:APPLy? 

# 功能描述

查询指定通道的波形类型及其频率、幅度、偏移和相位值。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr></table>

# 说明

省略[:SOURce[<n>]]或[<n>]时，默认查询 CH1 的相关参数。 

通道波形类型以及与其对应的返回的波形名称如下表所示： 

<table><tr><td>正弦波</td><td>方波</td><td>锯齿波</td><td>脉冲</td><td>噪声</td><td>直流</td><td>任意波</td></tr><tr><td>SIN</td><td>SQU</td><td>RAMP</td><td>PULSE</td><td>NOISE</td><td>DC</td><td>USER</td></tr></table>

# 返回格式

返回一个带双引号的字符串，由 5 部分组成，各部分之间以逗号隔开，第 1 部分为指定通道的波形名称，后 4部分依次为指定通道的波形的频率、幅度、偏移和相位值（均以科学计数形式表示，有效位数为 7 位，默 认单位分别为 $\mathsf { H z }$ ，Vpp， ${ \mathsf { V } } _ { \mathrm { d c } }$ 和°；没有的项用 DEF 代替）。例如 

"SQU,1.000000E+03,2.000000E+00,3.000000E+00,4.000000E+00"，表示当前波形为方波，频率为 1kHz， 幅度为 2Vpp，偏移为 $3 V _ { \mathrm { d c } }$ ，起始相位为 $4 ^ { \circ }$ 。 

# 举例

:SOUR1:APPL? 

/*查询 CH1 的波形类型及其频率、幅度、偏移和相位值，返回 

"SQU,1.000000E+03,2.000000E+00,3.000000E+00,4.000000E+00"*/ 

# [:SOURce[<n>]]:APPLy:DC

# 命令格式

$$
[: S O U R c e [ <   n > ]: A P P L y: D C
$$

$$
[ \{\langle f r e q u e n c y > | D E F \} [, \{\langle a m p l i t u d e > | D E F \} [, \{\langle o f f s e t > | D E F a u l t | M I N i m u m | M A X i m u m \} ] ] ]
$$

# 功能描述

设置指定通道的波形为具有指定偏移的直流。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;offset&gt;</td><td>实型</td><td>见下文“说明”</td><td>0Vdc</td></tr></table>

# 说明

省略[:SOURce[ $< n > ] ]$ ]或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

 参数<frequency $>$ 和<amplitude>不适用于 DC 函数，但必须指定为一个占位符。 

偏移<offset>的可设置范围受“阻抗”（:OUTPut[<n>]:IMPedance 或:OUTPut[<n>]:LOAD）设置的限 制。 

# 举例

:SOUR1:APPL:DC 1,1,2 /*设置 CH1的波形为直流且偏移为 $2 V _ { \mathrm { d c } } { } ^ { \star } /$ 

# [:SOURce[<n>]]:APPLy:DUALTone

# 命令格式

$$
\begin{array}{l} [: S O U R c e <   n > ]: A P P L y: D U A L T o n e \\ \left. \begin{array}{l} \left[ <   \text {f r e q} > | \text {D E F a u l t} | \text {M I N i m u m} | \text {M A X i m u m} [, <   \text {a m p} > | \text {D E F a u l t} | \text {M I N i m u m} | \text {M A X i m u m} [, <   \text {o f f s e t} > | \text {D E F a u l t} | \text {M I N i m u m} | \text {M A X i m u m} ] \right] \end{array} \right] \\ \end{array}
$$

# 功能描述

设置指定通道的波形为具有指定频率、幅度、偏移的双音波。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td></td><td>实型</td><td>1μHz至20MHz</td><td>1kHz</td></tr><tr><td></td><td>实型</td><td>见下文“说明”</td><td>5Vpp</td></tr><tr><td></td><td>实型</td><td>见下文“说明”</td><td>0Vdc</td></tr></table>

# 说明

省略[:SOURce[<n>]]或[<n>]时，默认设置 CH1 的相关参数。 

幅度的可设置范围受“阻抗”（:OUTPut[<n>]:IMPedance 或:OUTPut[<n>]:LOAD）和“频率/周期” 设置的限制，偏移的可设置范围受“阻抗”和“幅度/高电平”设置的限制。 

# 举例

:SOUR1:APPL:DUALT 100,1,2 /*设置 CH1 的波形为双音波且频率为 100Hz，幅度为 1Vpp，偏移为 $2 V _ { \mathrm { d c } } { } ^ { \star } /$ 

# [:SOURce[<n>]]:APPLy:HARMonic

# 命令格式

[:SOURce[<n>]]:APPLy:HARMonic 

[<freq>|DEFault|MINimum|MAXimum[,<amp>|DEFault|MINimum|MAXimum[,<offset>|DEFault|MINimu m|MAXimum[,<phase $>$ |DEFault|MINimum|MAXimum]]]] 

# 功能描述

启用指定通道的谐波功能并设置基波（正弦波）参数（频率、幅度、偏移和相位）。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td></td><td>实型</td><td>1uHz至25MHz</td><td>1kHz</td></tr><tr><td></td><td>实型</td><td>见下文“说明”</td><td>5Vpp</td></tr><tr><td></td><td>实型</td><td>见下文“说明”</td><td>0Vdc</td></tr><tr><td></td><td>实型</td><td>0°至360°</td><td>0°</td></tr></table>

# 说明

省略[:SOURce[<n>]]或[<n>]时，默认设置 CH1 的相关参数。 

幅度<amp>的可设置范围受“阻抗”（:OUTPut[<n>]:IMPedance 或:OUTPut[<n>]:LOAD）和“频率/ 周期”设置的限制，偏移<offset>的可设置范围受“阻抗”和“幅度/高电平”设置的限制。 

执行该命令时使用默认谐波参数或者上一次设置的谐波参数，您可以发送[:SOURce[<n>]]:HARMonic 系列命令设置所需的谐波参数以及启用或禁用谐波功能。 

# 举例

:SOUR1:APPL:HARM 100,1,2,3 /*启用 CH1 的谐波功能并设置基波（正弦波）参数为：频率 100Hz，幅度 1Vpp，偏移 $2 V _ { \mathrm { d c } }$ ，起始相位 $3 ^ { \circ \star } /$ 

# [:SOURce[<n>]]:APPLy:NOISe

# 命令格式

[:SOURce[<n>]]:APPLy:NOISe 

[<amp>|DEFault|MINimum|MAXimum[,<offset>|DEFault|MINimum|MAXimum]] 

# 功能描述

设置指定通道的波形为具有指定幅度和偏移的噪声。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td></td><td>实型</td><td>见下文“说明”</td><td>5Vpp</td></tr><tr><td></td><td>实型</td><td>见下文“说明”</td><td>0Vdc</td></tr></table>

# 说明

省略[:SOURce[<n>]]或[<n>]时，默认设置 CH1 的相关参数。 

幅度<amp>的可设置范围受“阻抗”（:OUTPut[<n>]:IMPedance 或:OUTPut[<n>]:LOAD）设置的限制， 偏移<offset $>$ 的可设置范围受“阻抗”和“幅度/高电平”设置的限制。 

# 举例

:SOUR1:APPL:NOIS 1,2 /*设置 CH1 的波形为噪声且幅度为 1Vpp，偏移为 $2 V _ { \mathrm { d c } } { } ^ { \star } /$ 

# [:SOURce[<n>]]:APPLy:PRBS

# 命令格式

$$
\begin{array}{l} [: S O U R c e [ <   n > ]: A P P L y: P R B S \\ \left. \begin{array}{l} \left[ <   \text {f r e q} > | \text {D E F a u l t} | \text {M I N i m u m} | \text {M A X i m u m} [, <   \text {a m p} > | \text {D E F a u l t} | \text {M I N i m u m} | \text {M A X i m u m} [, <   \text {o f f s e t} > | \text {D E F a u l t} | \text {M I N i m u m} | \text {M A X i m u m} ] \right] \end{array} \right] \\ \end{array}
$$

# 功能描述

设置指定通道的波形为具有指定频率、幅度、偏移的 PRBS 波。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td></td><td>实型</td><td>2kbps至60Mbps</td><td>2kbps</td></tr><tr><td></td><td>实型</td><td>见下文“说明”</td><td>5Vpp</td></tr><tr><td></td><td>实型</td><td>见下文“说明”</td><td>0Vdc</td></tr></table>

# 说明

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1 的相关参数。 

幅度的可设置范围受“阻抗”（:OUTPut[<n>]:IMPedance 或:OUTPut[<n>]:LOAD）和“频率/周期” 设置的限制，偏移的可设置范围受“阻抗”和“幅度/高电平”设置的限制。 

# 举例

:SOUR1:APPL:PRBS 10000,1,2 /*设置 CH1 的波形为 PRBS 波且频率为 10kHz，幅度为 1Vpp，偏移为 2Vdc*/ 

# [:SOURce[<n>]]:APPLy:PULSe

# 命令格式

$$
\begin{array}{l} [: S O U R c e [ <   n > ] ]: A P P L y: P U L S e \\ \begin{array}{l} \left[ <   \text {f r e q} > | \text {D E F a u l t} | \text {M I N i m u m} | \text {M A X i m u m} [, <   \text {a m p} > | \text {D E F a u l t} | \text {M I N i m u m} | \text {M A X i m u m} [, <   \text {o f f s e t} > | \text {D E F a u l t} | \text {M I N i m u m} | \text {M A X i m u m} [, <   \text {p h a s e} > | \text {D E F a u l t} | \text {M I N i m u m} | \text {M A X i m u m} ] ] ] \right] \end{array} \\ \end{array}
$$

# 功能描述

设置指定通道的波形为具有指定频率、幅度、偏移和相位的脉冲。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td></td><td>实型</td><td>1uHz至25MHz</td><td>1kHz</td></tr><tr><td></td><td>实型</td><td>见下文“说明”</td><td>5Vpp</td></tr><tr><td></td><td>实型</td><td>见下文“说明”</td><td>0Vdc</td></tr><tr><td></td><td>实型</td><td>0°至360°</td><td>0°</td></tr></table>

# 说明

省略[:SOURce[<n>]]或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

幅度<amp $>$ 的可设置范围受“阻抗”（:OUTPut[<n>]:IMPedance 或:OUTPut[<n>]:LOAD）和“频率/ 周期”设置的限制，偏移<offset>的可设置范围受“阻抗”和“幅度/高电平”设置的限制。 

# 举例

:SOUR1:APPL:PULS 100,3,2,1 /*设置 CH1 的波形为脉冲且频率为 100Hz，幅度为 3Vpp，偏移为 $2 V _ { \mathrm { d c } }$ ， 起始相位为 $1 ^ { \circ \star } /$ 

# [:SOURce[<n>]]:APPLy:RAMP

# 命令格式

[:SOURce[<n>]]:APPLy: RAMP 

[<freq>|DEFault|MINimum|MAXimum[,<amp>|DEFault|MINimum|MAXimum[,<offset>|DEFault|MINimu m|MAXimum[,<phase $>$ |DEFault|MINimum|MAXimum]]]] 

# 功能描述

设置指定通道的波形为具有指定频率、幅度、偏移和相位的锯齿波。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td></td><td>实型</td><td>1uHz至2MHz</td><td>1kHz</td></tr><tr><td></td><td>实型</td><td>见下文“说明”</td><td>5Vpp</td></tr><tr><td></td><td>实型</td><td>见下文“说明”</td><td>0Vdc</td></tr><tr><td></td><td>实型</td><td>0°至360°</td><td>0°</td></tr></table>

# 说明

省略[:SOURce[<n>]]或[ $< n > ]$ 时，默认设置 CH1的相关参数。 

幅度的可设置范围受“阻抗”（:OUTPut[<n>]:IMPedance 或:OUTPut[<n>]:LOAD）和“频率/周期” 设置的限制，偏移的可设置范围受“阻抗”和“幅度/高电平”设置的限制。 

# 举例

:SOUR1:APPL:RAMP 100,1,2,3 /*设置 CH1 的波形为锯齿波且频率为 100Hz，幅度为 1Vpp，偏移为 $2 V _ { \mathrm { d c } }$ ， 起始相位为 $3 ^ { \circ \star } /$ 

# [:SOURce[<n>]]:APPLy:RS232

# 命令格式

[:SOURce[<n>]]:APPLy:RS232 

[<amp $>$ |DEFault|MINimum|MAXimum[, $<$ <offse $>$ |DEFault|MINimum|MAXimum]] 

# 功能描述

设置指定通道的波形为具有指定幅度、偏移的 RS232 波。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td></td><td>实型</td><td>见下文“说明”</td><td>5Vpp</td></tr><tr><td></td><td>实型</td><td>见下文“说明”</td><td>0Vdc</td></tr></table>

# 说明

省略[:SOURce[<n>]]或[<n>]时，默认设置 CH1 的相关参数。 

幅度的可设置范围受“阻抗”（:OUTPut[<n>]:IMPedance 或:OUTPut[<n>]:LOAD）和“频率/周期” 设置的限制，偏移的可设置范围受“阻抗”和“幅度/高电平”设置的限制。 

# 举例

:SOUR1:APPL:RS232 1,2 /*设置 CH1 的波形为 RS232 波且幅度为 1Vpp，偏移为 $2 \mathsf { V _ { d c } } ^ { \star } /$ 

# [:SOURce[<n>]]:APPLy:SEQuence

# 命令格式

$$
\begin{array}{l} [: S O U R c e [ <   n > ] ]: A P P L y: S E Q u e n c e \\ [ \{\langle \text {s a m p l e} _ {\text {r a t e}} \rangle | \text {D E F a u l t} | \text {M I N i m u m} | \text {M A X i m u m} \} [, \{\langle \text {a m p l i t u d e} \rangle | \text {D E F a u l t} | \text {M I N i m u m} | \text {M A X i m u m} \} [, \{\langle \text {o f f s e t} \rangle | \text {D E F a u l t} | \text {M I N i m u m} | \text {M A X i m u m} \} ] \\ > | D E F a u l t | M I N i m u m | M A X i m u m \} [, \{\langle p h a s e > | D E F a u l t | M I N i m u m | M A X i m u m \} ] ]) \\ \end{array}
$$

# 功能描述

设置指定通道的波形为具有指定采样率、幅度、偏移和起始相位的序列波形。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;sample_rate&gt;</td><td>实型</td><td>2kSa/s至60MSa/s</td><td>1MSa/s</td></tr><tr><td>&lt;amplitude&gt;</td><td>实型</td><td>见下文“说明”</td><td>5Vpp</td></tr><tr><td>&lt;offset&gt;</td><td>实型</td><td>见下文“说明”</td><td>0Vdc</td></tr><tr><td>&lt;phase&gt;</td><td>实型</td><td>0°至360°</td><td>0°</td></tr></table>

# 说明

省略[:SOURce[ $< n > ] ]$ 或[<n>]时，默认设置 CH1的相关参数。 

该命令仅选择和设置通道序列波形的参数。 

幅度<amplitude $>$ 的可设置范围受“阻抗”（:OUTPut[<n>]:IMPedance 或:OUTPut[<n>]:LOAD）设置 的限制，偏移<offset>的可设置范围受“阻抗”和“幅度/高电平”设置的限制。 

# 举例

:SOUR1:APPL:SEQ 10000,1,2,1 /*设置 CH1 的波形为序列波形且采样率为 10kSa/s，幅度为 1Vpp，偏移 为 $2 V _ { \mathrm { d c } }$ ，起始相位为 $1 ^ { \circ \star } /$ 

# [:SOURce[<n>]]:APPLy:SINusoid

# 命令格式

$$
\begin{array}{l} [: S O U R c e [ <   n > ] ]: A P P L y: S I N u s o i d \\ [ <   \text {f r e q} > | \text {D E F a u l t} | \text {M I N i m u m} | \text {M A X i m u m} [, <   \text {a m p} > | \text {D E F a u l t} | \text {M I N i m u m} | \text {M A X i m u m} [, <   \text {o f f s e t} > | \text {D E F a u l t} | \text {M I N i m u m} ] \\ m | M A X i m u m [, <   p h a s e > | D E F a u l t | M I N i m u m | M A X i m u m ] ]) ] \\ \end{array}
$$

# 功能描述

设置指定通道的波形为具有指定频率、幅度、偏移和相位的正弦波。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td></td><td>实型</td><td>1uHz至100MHz</td><td>1kHz</td></tr><tr><td></td><td>实型</td><td>见下文“说明”</td><td>5Vpp</td></tr><tr><td></td><td>实型</td><td>见下文“说明”</td><td>0Vdc</td></tr><tr><td></td><td>实型</td><td>0°至360°</td><td>0°</td></tr></table>

# 说明

省略[:SOURce[<n>]]或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

幅度的可设置范围受“阻抗”（:OUTPut[<n>]:IMPedance 或:OUTPut[<n>]:LOAD）和“频率/周期” 设置的限制，偏移的可设置范围受“阻抗”和“幅度/高电平”设置的限制。 

# 举例

:SOUR1:APPL:SIN 100,3,2,1 /*设置 CH1 的波形为正弦波且频率为 100Hz，幅度为 3Vpp，偏移为 $2 V _ { \mathrm { d c } }$ ， 起始相位为 $1 ^ { \circ \star } /$ 

# [:SOURce[<n>]]:APPLy:SQUare

# 命令格式

[:SOURce[<n>]]:APPLy:SQUare 

[<freq>|DEFault|MINimum|MAXimum[,<amp>|DEFault|MINimum|MAXimum[,<offset>|DEFault|MINimu m|MAXimum[,<phase>|DEFault|MINimum|MAXimum]]]] 

# 功能描述

设置指定通道的波形为具有指定频率、幅度、偏移和相位的方波。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td></td><td>实型</td><td>1uHz至25MHz</td><td>1kHz</td></tr><tr><td></td><td>实型</td><td>见下文“说明”</td><td>5Vpp</td></tr><tr><td></td><td>实型</td><td>见下文“说明”</td><td>0Vdc</td></tr><tr><td></td><td>实型</td><td>0°至360°</td><td>0°</td></tr></table>

# 说明

省略[:SOURce[<n>]]或[ $< n > ]$ 时，默认设置 CH1的相关参数。 

幅度的可设置范围受“阻抗”（:OUTPut[<n>]:IMPedance 或:OUTPut[<n>]:LOAD）和“频率/周期” 设置的限制，偏移的可设置范围受“阻抗”和“幅度/高电平”设置的限制。 

# 举例

:SOUR1:APPL:SQU 100,1,2,3 /*设置 CH1 的波形为方波且频率为 100Hz，幅度为 1Vpp，偏移为 $2 V _ { \mathrm { d c } }$ ， 起始相位为 $3 ^ { \circ \star } /$ 

# [:SOURce[<n>]]:APPLy:USER

# 命令格式

[:SOURce[<n>]]:APPLy:USER [<freq>|DEFault|MINimum|MAXimum[,<amp>|DEFault|MINimum|MAXimum[,<offset>|DEFault|MINimu m|MAXimum[,<phase>|DEFault|MINimum|MAXimum]]]] 

# 功能描述

设置指定通道的波形为具有指定频率、幅度、偏移和相位的任意波。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td></td><td>实型</td><td>1uHz至20MHz</td><td>1kHz</td></tr><tr><td></td><td>实型</td><td>见下文“说明”</td><td>5Vpp</td></tr><tr><td></td><td>实型</td><td>见下文“说明”</td><td>0Vdc</td></tr><tr><td></td><td>实型</td><td>0°至360°</td><td>0°</td></tr></table>

# 说明

省略[:SOURce[<n>]]或 $\cdot < n > ]$ ]时，默认设置 CH1的相关参数。 

该命令仅选择和设置通道任意波形的参数，不设置任意波形类型。默认的任意波形为 Sinc，您可以发送 命令[:SOURce[<n>]]:FUNCtion[:SHAPe]命令选择指定通道的波形为所需的任意波形。 

幅度的可设置范围受“阻抗”（:OUTPut[<n>]:IMPedance 或:OUTPut[<n>]:LOAD）和“频率/周期” 设置的限制，偏移的可设置范围受“阻抗”和“幅度/高电平”设置的限制。 

# 举例

:SOUR1:APPL:USER 100,1,2,3 /*设置 CH1 的波形为任意波且频率为 100Hz，幅度为 1Vpp，偏移为 $2 V _ { \mathrm { d c } }$ 起始相位为 $3 ^ { \circ \star } /$ 

# :SOURce:BURSt 命令

# 命令列表：

$\spadesuit$ [:SOURce[<n>]]:BURSt:GATE:POLarity 

$\spadesuit$  [:SOURce[<n>]]:BURSt:INTernal:PERiod 

$\spadesuit$  [:SOURce[<n>]]:BURSt:MODE 

[:SOURce[<n>]]:BURSt:NCYCles 

[:SOURce[<n>]]:BURSt:PHASe 

 [:SOURce[<n>]]:BURSt[:STATe] 

 [:SOURce[<n>]]:BURSt:TDELay 

[:SOURce[<n>]]:BURSt:TRIGger[:IMMediate] 

 [:SOURce[<n>]]:BURSt:TRIGger:SLOPe 

 [:SOURce[<n>]]:BURSt:TRIGger:SOURce 

 [:SOURce[<n>]]:BURSt:TRIGger:TRIGOut 

 [:SOURce[<n>]]:BURSt:IDLE 

# [:SOURce[<n>]]:BURSt:GATE:POLarity

# 命令格式

[:SOURce[<n>]]:BURSt:GATE:POLarity {NORMal|INVerted} 

[:SOURce[<n>]]:BURSt:GATE:POLarity? 

# 功能描述

设置指定通道的门控脉冲串的门控极性为正极性（NORMal）或负极性（INVerted）。 查询指定通道的门控脉冲串的门控极性。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{NORMal|INVerted}</td><td>离散型</td><td>NORMal|INVerted</td><td>NORMal</td></tr></table>

# 说明

省略[:SOURce[<n>]]或[<n>]时，默认设置 CH1 的相关参数。 

门控极性仅适用于门控脉冲串模式（[:SOURce[<n>]]:BURSt:MODE）。信号发生器根据后面板相应通道 的 [Sync/Ext Mod/Trig/FSK] 连接器上输入的外部信号电平（即门控信号）控制脉冲串输出。 

. 正极性（NORMal）：外部信号电平为高（低）电平时，门控信号为真（假）；负极性（INVerted）：外部 信号电平为低（高）电平时，门控信号为真（假）。 

信号发生器在门控信号为“真”时，输出一个连续波形，在门控信号为“假”时，首先完成当前的波形 周期，然后停止。对于噪声波形，在门控信号变为“假”时立即停止输出。 

# 返回格式

返回 NORM 或 INV。 

# 举例

:SOUR1:BURS:GATE:POL NORM /*设置 CH1的门控脉冲串的门控极性为正极性*/ :SOUR1:BURS:GATE:POL? /*查询 CH1的门控脉冲串的门控极性，返回 NORM*/ 

# [:SOURce[<n>]]:BURSt:INTernal:PERiod

# 命令格式

[:SOURce[<n>]]:BURSt:INTernal:PERiod {<period>|MINimum|MAXimum} 

[:SOURce[<n>]]:BURSt:INTernal:PERiod? [MINimum|MAXimum] 

# 功能描述

设置指定通道的 N循环脉冲串的内部猝发周期。 

查询指定通道的 N循环脉冲串的内部猝发周期。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;period&gt;</td><td>实型</td><td>2.016 6us 至 500s</td><td>10ms</td></tr></table>

# 说明

省略[:SOURce[ $< n > ] ]$ 或[ $\cdot < n > ]$ 时，默认设置 CH1的相关参数。 

猝发周期（即脉冲串周期）仅适用于内部触发 N循环脉冲串模式（[:SOURce[<n>]]:BURSt:MODE）， 定义为从一个脉冲串开始到下一个脉冲串开始的时间。 

 猝发周期与波形周期（脉冲串函数（正弦波、方波等）的周期）和脉冲串循环数的关系为 

$$
P _ {b u r s t} \geq P _ {\text {w a v e f o r m}} \times N _ {\text {c y c l e}} + 2 \mathrm {u s}
$$

其中， 

Pburst $P _ { b u r s t }$ 猝发周期； 

Pwaveform $P _ { w a v e f o r m }$ 波形周期； 

$N _ { c y c l e }$ 循环数。 

如果设置的猝发周期过小，信号发生器将自动增加该周期以允许指定数量的循环输出。 

# 返回格式

以科学计数形式返回猝发周期，有效位数为 7位，如 1.000000E-01，表示猝发周期为 0.1s。 

# 举例

:SOUR1:BURS:INT:PER 0.1 /*设置 CH1的 N循环脉冲串的内部猝发周期为 $0 . 1 \mathsf { s } ^ { \star } /$ 

:SOUR1:BURS:INT:PER? /*查询 CH1 的 N 循环脉冲串的内部猝发周期，返回 1.000000E-01*/ 

# [:SOURce[<n>]]:BURSt:MODE

# 命令格式

[:SOURce[<n>]]:BURSt:MODE {TRIGgered|INFinity|GATed} 

[:SOURce[<n>]]:BURSt:MODE? 

# 功能描述

设置指定通道的脉冲串类型为 N循环（TRIGgered）、无限（INFinity）或门控（GATed）。 

查询指定通道的脉冲串类型。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{TRIGgered|INfinity|GATed}</td><td>离散型</td><td>TRIGgered|INfinity|GATed</td><td>TRIGgered</td></tr></table>

# 说明

DG2000可输出 N 循环、无限和门控三种类型的脉冲串。 

 N循环脉冲串模式下，信号发生器在接收到触发信号时，输出具有特定循环数目的波形。支持 N循环脉 冲串的波形函数有正弦波、方波、锯齿波、脉冲波、任意波、PRBS、RS232和序列。对于 N循环脉冲 串，可以使用“内部”、“外部”或“手动”触发源触发输出。此外您还可以设置“猝发周期”（内部触 发）、“延时”、“触发输入”（外部触发）和“触发输出”（内部触发和手动触发）参数。 

 无限脉冲串相当于将波形循环次数设为无限大，信号发生器在接收到触发信号时，输出连续的波形。支 持无限脉冲串的波形函数有正弦波、方波、锯齿波、脉冲波、任意波、PRBS、RS232和序列。对于无 限脉冲串，需要使用“外部”或“手动”触发源触发输出。此外您还可以设置“延时”、“触发输入”（外 部触发）和“触发输出”（手动触发）参数。 

 门控脉冲串模式下，信号发生器根据后面板相应通道的 [Sync/Ext Mod/Trig/FSK] 连接器上输入的 外部信号电平控制波形输出。支持门控脉冲串的波形函数有正弦波、方波、锯齿波、脉冲波、噪声、任 意波、PRBS、RS232和序列。对于门控脉冲串，只能使用“外部”触发源触发输出。 

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

# 返回格式

返回 TRIG、INF 或 GAT。 

# 举例

:SOUR1:BURS:MODE TRIG /*设置 CH1 的脉冲串类型为 N 循环*/ 

:SOUR1:BURS:MODE? /*查询 CH1 的脉冲串类型，返回 TRIG*/ 

# [:SOURce[<n>]]:BURSt:NCYCles

# 命令格式

[:SOURce[<n>]]:BURSt:NCYCles {<cycles>|MINimum|MAXimum} 

[:SOURce[<n>]]:BURSt:NCYCles? [MINimum|MAXimum] 

# 功能描述

设置指定通道的 N循环脉冲串的循环数。 

查询指定通道的 N循环脉冲串的循环数。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;cycles&gt;</td><td>整型</td><td>1至1000000（外部触发或手动）
1至500000（内部触发）</td><td>1</td></tr></table>

# 说明

N循环脉冲串模式（[:SOURce[<n>]]:BURSt:MODE）下，信号发生器在接收到触发信号时，输出具有 特定循环数目的波形。 

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1 的相关参数。 

# 返回格式

以科学计数形式返回循环数，有效位数为 7 位，如 $1 . 0 0 0 0 0 0 0 \mathsf { E } + 0 1$ ，表示循环数为 10。 

# 举例

:SOUR1:BURS:NCYC 10 /*设置 CH1 的 N 循环脉冲串的循环数为 ${ 1 0 ^ { \star } } /$ 

:SOUR1:BURS:NCYC? /*查询 CH1 的 N 循环脉冲串的循环数，返回 1.000000E+01*/ 

# [:SOURce[<n>]]:BURSt:PHASe

# 命令格式

[:SOURce[<n>]]:BURSt:PHASe {<phase>|MINimum|MAXimum} 

[:SOURce[<n>]]:BURSt:PHASe? [MINimum|MAXimum] 

# 功能描述

设置指定通道脉冲串函数的起始相位。 

查询指定通道脉冲串函数的起始相位。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;phase&gt;</td><td>实型</td><td>0°至360°</td><td>0°</td></tr></table>

# 说明

省略[:SOURce[ $< n > ] ]$ 或 $\cdot < n > ]$ 时，默认设置 CH1 的相关参数。 

# 返回格式

以科学计数形式返回起始相位，有效位数为 7位，如 1.000000E $+ 0 1$ ，表示起始相位为 $ { 1 0 ^ { \circ } }$ 。 

# 举例

:SOUR1:BURS:PHAS 10 /*设置 CH1 的脉冲串函数的起始相位为 $1 0 ^ { \circ } \star /$ 

:SOUR1:BURS:PHAS? /*查询 CH1 的脉冲串函数的起始相位，返回 1.000000E+01*/ 

# [:SOURce[<n>]]:BURSt[:STATe]

# 命令格式

[:SOURce[<n>]]:BURSt[:STATe] {ON|1|OFF|0} 

[:SOURce[<n>]]:BURSt[:STATe]? 

# 功能描述

启用或禁用指定通道的脉冲串功能。 

查询指定通道的脉冲串功能的开关状态。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 说明

 DG2000可从单通道或同时从双通道输出具有指定循环数目的波形（即脉冲串）。启用脉冲串功能后， 调制或扫频功能将自动关闭（如果当前已打开）。此时，信号发生器将按照当前的配置从相应的通道（如 果当前已打开）输出脉冲串波形。 

为了避免大量的波形改变，请在配置其他脉冲串参数之后再启用脉冲串功能。 

省略[:SOURce[ $< n > ] ]$ ]或[ $\cdot < n > ]$ 时，默认设置 CH1的相关参数。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:SOUR1:BURS ON /*启用 CH1的脉冲串功能*/ 

:SOUR1:BURS? /*查询 CH1的脉冲串功能的开关状态，返回 ON*/ 

# [:SOURce[<n>]]:BURSt:TDELay

# 命令格式

[:SOURce[<n>]]:BURSt:TDELay {<delay>|MINimum|MAXimum} 

[:SOURce[<n>]]:BURSt:TDELay? [MINimum|MAXimum] 

# 功能描述

设置指定通道 N 循环或无限脉冲串的脉冲串延时。 

查询指定通道 N 循环或无限脉冲串的脉冲串延时。 

# 参数

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;delay&gt;</td><td>实型</td><td>见下文“说明”</td><td>0s</td></tr></table>

# 说明

脉冲串延时仅适用于 N 循环和无限脉冲串模式（[:SOURce[<n>]]:BURSt:MODE），是指信号发生器从 接收到触发信号到开始输出 N循环或无限脉冲串之间的时间。 

对于外部触发或手动触发（[:SOURce[<n>]]:BURSt:TRIGger:SOURce）的 N 循环或无限脉冲串模式， <delay>的范围为 0s 至 100s。 

对于内部触发 N 循环脉冲串模式，<delay $>$ 的范围为 0s 至 $\mathrm { ' } P _ { b u r s t } - P _ { w a \nu e f o r m } \times N _ { c y c l e } - 2 \mathrm { u s ) }$ ，且小于等于 100s。 

其中， 

Pburst $P _ { b u r s t }$ 猝发周期； 

Pwaveform 波形周期（即脉冲串函数（正弦波、方波等）的周期）； 

Ncycle $N _ { c y c l e }$ 脉冲串个数。 

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

# 返回格式

以科学计数形式返回脉冲串延时，有效位数为 7位，如 1.000000E-01，表示脉冲串延时为 0.1s。 

# 举例

:SOUR1:BURS:TDEL 0.1 /*设置 CH1的 N循环或无限脉冲串的脉冲串延时为 $0 . 1 \mathsf { s } ^ { \star } /$ 

:SOUR1:BURS:TDEL? /*查询 CH1 的 N 循环或无限脉冲串的脉冲串延时，返回 1.000000E-01*/ 

# [:SOURce[<n>]]:BURSt:TRIGger[:IMMediate]

# 命令格式

[:SOURce[<n>]]:BURSt:TRIGger[:IMMediate] 

# 功能描述

在指定通道立即触发一次脉冲串输出。 

# 参数

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr></table>

# 说明

该命令仅适用于手动触发脉冲串模式（[:SOURce[<n>]]:BURSt:TRIGger:SOURce）。如果对应通道的输 出没有打开（:OUTPut[<n>][:STATe]），触发将被忽略。 

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认在 CH1产生一次触发。 

# 举例

:SOUR1:BURS:TRIG /*在 CH1立即触发一次脉冲串输出*/ 

# [:SOURce[<n>]]:BURSt:TRIGger:SLOPe

# 命令格式

[:SOURce[<n>]]:BURSt:TRIGger:SLOPe {POSitive|NEGative} 

[:SOURce[<n>]]:BURSt:TRIGger:SLOPe? 

# 功能描述

设置指定通道脉冲串模式中触发输入信号的边沿类型为上升沿（POSitive）或下降沿（NEGative）。 

查询指定通道脉冲串模式中触发输入信号的边沿类型。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{POSitive|NEGative}</td><td>离散型</td><td>POSitive|NEGative</td><td>POSitive</td></tr></table>

# 说明

该命令仅适用于选择外部触发（[:SOURce[<n>]]:BURSt:TRIGger:SOURce）的脉冲串（N 循环、无限 或门控）模式。选择外部触发时，信号发生器接收从后面板相应通道的 [Sync/Ext Mod/Trig/FSK] 连 接器输入的触发信号，每次接收到一个具有指定极性的 TTL脉冲时，就启动一次脉冲串（N循环、无限 或门控）输出。 

省略[:SOURce $: < n > ] ]$ 或 $[ < n > ]$ ]时，默认设置 CH1的相关参数。 

# 返回格式

返回 POS 或 NEG。 

# 举例

:SOUR1:BURS:TRIG:SLOP NEG /*设置 CH1 在触发输入信号的下降沿进行触发*/ 

:SOUR1:BURS:TRIG:SLOP? /*查询 CH1触发输入信号的边沿类型，返回 ${ \tt N E G } ^ { \star } /$ 

# [:SOURce[<n>]]:BURSt:TRIGger:SOURce

# 命令格式

[:SOURce[<n>]]:BURSt:TRIGger:SOURce {INTernal|EXTernal|MANual} 

[:SOURce[<n>]]:BURSt:TRIGger:SOURce? 

# 功能描述

设置指定通道脉冲串模式的触发源类型为内部（INTernal）、外部（EXTernal）或手动（MANual）。 

查询指定通道脉冲串模式的触发源类型。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{INTERNAL|EXTERNAL|MANual}</td><td>离散型</td><td>INTERNAL|EXTERNAL|MANual</td><td>INTERNAL</td></tr></table>

# 说明

脉冲串的触发源可以是内部源、外部源或手动源。信号发生器在接收到一个触发信号时，产生一次脉冲 串输出，然后等待下一个触发信号。 

仅 N循环脉冲串（[:SOURce[<n>]]:BURSt:MODE）支持内部触发。选择内部触发时，N循环脉冲串的 频率由“猝发周期”（[:SOURce[<n>]]:BURSt:INTernal:PERiod）决定。您还可以设置指定通道后面板 

相应通道的 [Sync/Ext Mod/Trig/FSK] 连接器输出具有指定边沿（上升沿或下降沿）的触发信号或 关闭触发输出信号（[:SOURce[<n>]]:BURSt:TRIGger:TRIGOut）。 

N循环、无限和门控脉冲串均支持外部触发。选择外部触发时，信号发生器接收从指定通道后面板相应 的 [Sync/Ext Mod/Trig/FSK] 连接器输入的触发信号，每次接收到一个具有指定极性的 TTL脉冲 时，就启动一次脉冲串输出。您可以指定触发输入信号的边沿类型（上升沿或下降沿）。 

N循环或无限脉冲串支持手动触发。选择手动触发且对应通道的输出打开时，发送 *TRG、:TRIGger[<n>][:IMMediate]或[:SOURce[<n>]]:BURSt:TRIGger[:IMMediate]命令可输出 N 循 环或无限脉冲串。如果对应通道的输出没有打开，触发将被忽略。您还可以设置后面板相应通道的 [Sync/Ext Mod/Trig/FSK] 连接器输出具有指定边沿（上升沿或下降沿）的触发信号或关闭触发输 出信号。 

# 返回格式

返回 INT、EXT 或 MAN。 

# 举例

:SOUR1:BURS:TRIG:SOUR EXT /*设置 CH1脉冲串模式的触发源类型为外部*/ :SOUR1:BURS:TRIG:SOUR? /*查询 CH1脉冲串模式的触发源类型，返回 EXT*/ 

# [:SOURce[<n>]]:BURSt:TRIGger:TRIGOut

# 命令格式

[:SOURce[<n>]]:BURSt:TRIGger:TRIGOut {POSitive|NEGative|OFF} 

[:SOURce[<n>]]:BURSt:TRIGger:TRIGOut? 

# 功能描述

设置指定通道脉冲串模式中触发输出信号的边沿类型为上升沿（POSitive）或下降沿（NEGative）或禁用触 发输出信号。 

查询指定通道脉冲串模式中触发输出信号的类型。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{POSitive|NEGative|OFF}</td><td>离散型</td><td>POSitive|NEGative|OFF</td><td>OFF</td></tr></table>

# 说明

该命令仅适用于选择内部或手动触发（[:SOURce[<n>]]:BURSt:TRIGger:SOURce）的脉冲串（N 循环、 无限或门控）模式（[:SOURce[<n>]]:BURSt:MODE）。选择内部或手动触发时，可以设置在仪器被触发 时，仪器后面板相应的 [Sync/Ext Mod/Trig/FSK] 连接器输出具有指定边沿（上升沿或下降沿）的 触发信号或关闭触发输出信号。 

省略[:SOURce[ $< n > ] ]$ 或[ $\cdot < n > ]$ 时，默认设置 CH1 的相关参数。 

# 返回格式

返回 POS、NEG 或 OFF。 

# 举例

:SOUR:BURS:TRIG:TRIGO POS /*设置 CH1 脉冲串模式中触发输出信号的边沿类型为上升沿*/ 

:SOUR:BURS:TRIG:TRIGO? /*查询 CH1脉冲串模式中触发输出信号的类型，返回 $\mathsf { P O S } ^ { \star } /$ 

# [:SOURce[<n>]]:BURSt:IDLE

# 命令格式

[:SOURce[<n>]]:BURSt:IDLE {<idle>|FPT|TOP|CENTER|BOTTOM} 

[:SOURce[<n>]]:BURSt:IDLE? 

# 功能描述

设置指定通道脉冲串模式中空闲电平的位置为第一个点、波形顶部、波形中间、波形底部或自定义。 

查询指定通道脉冲串模式中空闲电平的位置。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;idle&gt;</td><td>整型</td><td>0至16383</td><td>FPT</td></tr></table>

# 说明

省略[:SOURce[ $< n > ] ]$ 或[ $\cdot < n > ]$ 时，默认设置 CH1 的相关参数。 

# 返回格式

返回 FPT、TOP、CENTER、BOTTOM 或以整数形式返回自定义设置的空闲电平的位置。 

# 举例

[:SOURce[<n>]]:BURSt:IDLE FPT /*设置 CH1 脉冲串模式中空闲电平的位置为第一个点*/ 

[:SOURce[<n>]]:BURSt:IDLE? /*查询 CH1脉冲串模式中空闲电平的位置，返回 FPT*/ 

# :SOURce:FREQuency 命令

# 命令列表：

$\spadesuit$ [:SOURce[<n>]]:FREQuency:CENTer 

$\spadesuit$ [:SOURce[<n>]]:FREQuency:COUPle:MODE 

 $\spadesuit$ [:SOURce[<n>]]:FREQuency:COUPle:OFFSet 

 [:SOURce[<n>]]:FREQuency:COUPle:RATio 

[:SOURce[<n>]]:FREQuency:COUPle[:STATe] 

 [:SOURce[<n>]]:FREQuency[:FIXed] 

 [:SOURce[<n>]]:FREQuency:SPAN 

 $\spadesuit$ [:SOURce[<n>]]:FREQuency:STARt 

$\spadesuit$  [:SOURce[<n>]]:FREQuency:STOP 

# [:SOURce[<n>]]:FREQuency:CENTer

# 命令格式

[:SOURce[<n>]]:FREQuency:CENTer {<frequency>|MINimum|MAXimum} 

[:SOURce[<n>]]:FREQuency:CENTer? [MINimum|MAXimum] 

# 功能描述

设置指定通道扫频功能的中心频率。 

查询指定通道扫频功能的中心频率。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;frequency&gt;</td><td>实型</td><td>见下文“说明”</td><td>550Hz</td></tr></table>

# 说明

您可以通过中心频率和频率跨度（[:SOURce[<n>]]:FREQuency:SPAN）来设定扫频的边界。不同扫频 波形对应的中心频率和频率跨度范围不同，且中心频率与频率跨度相互影响。定义当前波形的最小频率 为 $F _ { \mathrm { m i n } }$ ，最大频率为 $F _ { \mathrm { m a x } }$ ， $F _ { m } = ( F _ { \operatorname* { m i n } } + F _ { \operatorname* { m a x } } ) / 2$ 。中心频率（定义为 $F _ { c e n t e r }$ ）的可设置范围为 $F _ { \mathrm { m i n } }$ 至 $F _ { \mathrm { m a x } }$ ， 频率跨度（定义为 $F _ { s p a n }$ ）的范围受中心频率影响。当中心频率小于 $F _ { m }$ 时，频率跨度的范围为 $\pm 2 \times ( F _ { c e n t e r } - F _ { \mathrm { { m i n } } } )$ ；当中心频率大于 $F _ { m }$ 时，频率跨度的范围为 $\pm 2 \times ( { F _ { \mathrm { m a x } } } - { F _ { c e n t e r } } )$ 。 

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

起始频率、终止频率、中心频率和频率跨度满足如下关系式 

$$
F _ {c e n t e r} = \left(\left| F _ {s t a r t} + F _ {s t o p} \right|\right); \quad F _ {s p a n} = \left(\left| F _ {s t o p} - F _ {s t a r t} \right|\right)
$$

其中， 

$F _ { c e n t e r }$ Fcenter 中心频率； 

Fspan $F _ { s p a n }$ 频率跨度； 

Fstart $F _ { s t a r t }$ 起始频率； 

Fstop $F _ { s t o p }$ 终止频率。 

修改“中心频率“后，信号发生器将重新从指定的“起始频率”开始扫频输出。大范围扫频时，输出信 号的幅度特性可能会有变化。 

# 返回格式

以科学计数形式返回中心频率，有效位数为 7位，如 5.000000E+02，表示中心频率为 500Hz。 

# 举例

:SOUR1:FREQ:CENT 500 /*设置 CH1的扫频功能的中心频率为 $5 0 0 \mathsf { H z } ^ { \star } /$ 

:SOUR1:FREQ:CENT? /*查询 CH1 的扫频功能的中心频率，返回 5.000000E+02*/ 

# [:SOURce[<n>]]:FREQuency:COUPle:MODE

# 命令格式

[:SOURce[<n>]]:FREQuency:COUPle:MODE {OFFSet|RATio} 

[:SOURce[<n>]]:FREQuency:COUPle:MODE? 

# 功能描述

设置频率耦合模式为频率差值（OFFSet）或频率比例（RATio）。 

查询频率耦合模式。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{OFFSET|RATio}</td><td>离散型</td><td>OFFSET|RATio</td><td>RATio</td></tr></table>

# 说明

频率差值模式：CH1和 CH2 两通道的频率具有一定的差值关系。参数关系为 $\mathsf { F } _ { \mathsf { C H 2 } } { = } \mathsf { F } _ { \mathsf { C H 1 } } { + } \mathsf { F } _ { \mathsf { D e v } }$ （基准源为 CH1）； $\mathsf { F } _ { \mathsf { C H } 1 } { = } \mathsf { F } _ { \mathsf { C H } 2 } { - } \mathsf { F } _ { \mathsf { D e v } }$ （基准源为 CH2）。其中， $\mathsf { F } _ { \mathsf { C H 1 } }$ 为 CH1 的频率值， $\mathsf { F } _ { \mathsf { C H 2 } }$ 为 CH2 的频率值， $\mathsf { F } _ { \mathsf { D e v } }$ 为 设置的频率差值。 

频率比例模式：CH1 和 CH2 两通道的频率具有一定的比值关系。参数关系为 $\mathsf { F } _ { \mathsf { C H 2 } } { = } \mathsf { F } _ { \mathsf { C H 1 } } { ^ { \star } } \mathsf { F } _ { \mathsf { R a t i o } }$ （基准源 为 CH1）； $\mathsf { F } _ { \mathsf { C H } 1 } { = } \mathsf { F } _ { \mathsf { C H } 2 } / \mathsf { F } _ { \mathsf { R a t i o } }$ （基准源为 CH2）。其中， $\mathsf { F } _ { \mathsf { C H 1 } }$ 为 CH1 的频率值， $\mathsf { F } _ { \mathsf { C H 2 } }$ 为 CH2 的频率值，FRatio 为设置的频率比例。 

如果经过耦合后，CH1 和 CH2中任意一个通道的频率超过本通道的频率上限或下限，仪器将自动调整 另外一个通道的频率上限或下限以避免参数超限。 

请在打开频率耦合功能（[:SOURce[<n>]]:FREQuency:COUPle[:STATe]）之前选择所需的频率耦合模式 并设置相应的频率差值（[:SOURce[<n>]]:FREQuency:COUPle:OFFSet）或频率比例 （[:SOURce[<n>]]:FREQuency:COUPle:RATio）。打开频率耦合功能后，不可以设置频率耦合模式和频 率差值/比例。 

您也可以发送:COUPling[<n>]:FREQuency:MODE 命令设置和查询频率耦合模式。 

# 返回格式

返回 OFFS 或 RAT。 

# 举例

:FREQ:COUP:MODE OFFS /*设置频率耦合模式为频率差值*/ 

:FREQ:COUP:MODE? /*查询频率耦合模式，返回 OFFS*/ 

# [:SOURce[<n>]]:FREQuency:COUPle:OFFSet

# 命令格式

[:SOURce[<n>]]:FREQuency:COUPle:OFFSet <frequency> 

[:SOURce[<n>]]:FREQuency:COUPle:OFFSet? 

# 功能描述

设置频率耦合中的频率差值。 

查询频率耦合中的频率差值。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;frequency&gt;</td><td>实型</td><td>-99.999 999 999 9MHz 至 99.999 999 999 9MHz</td><td>0</td></tr></table>

# 说明

请在打开频率耦合功能（[:SOURce[<n>]]:FREQuency:COUPle[:STATe]）之前选择所需的频率耦合模式 （[:SOURce[<n>]]:FREQuency:COUPle:MODE）并设置相应的频率差值或频率比例 （[:SOURce[<n>]]:FREQuency:COUPle:RATio）。频率耦合功能打开时，不可以设置频率耦合模式和频 率差值/比例。 

频率耦合功能关闭时，若当前频率耦合模式为频率差值，发送该命令可以设置频率差值；若当前频率耦 合模式为频率比例，发送该命令可以选择频率差值耦合模式并设置频率差值。 

您也可以发送:COUPling[<n>]:FREQuency:DEViation 命令设置和查询指定通道的频率耦合模式的频率 差值。 

# 返回格式

以科学计数形式返回频率差值，有效位数为 7位，如 1.000000E+02，表示频率耦合中的频率差值为 100Hz。 

# 举例

:FREQ:COUP:OFFS 100 /*设置频率耦合中的频率差值为 $1 0 0 \mathsf { H z } ^ { \star } /$ 

:FREQ:COUP:OFFS? /*查询频率耦合中的频率差值，返回 1.000000E+02*/ 

# [:SOURce[<n>]]:FREQuency:COUPle:RATio

# 命令格式

[:SOURce[<n>]]:FREQuency:COUPle:RATio <ratio> 

[:SOURce[<n>]]:FREQuency:COUPle:RATio? 

# 功能描述

设置频率耦合中的频率比例。 

查询频率耦合中的频率比例。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;ratio&gt;</td><td>实型</td><td>0.000 001 至 1 000 000</td><td>1</td></tr></table>

# 说明

请在打开频率耦合功能（[:SOURce[<n>]]:FREQuency:COUPle[:STATe]）之前选择所需的频率耦合模式 （[:SOURce[<n>]]:FREQuency:COUPle:MODE）并设置相应的频率差值 （[:SOURce[<n>]]:FREQuency:COUPle:OFFSet）或频率比例。频率耦合功能打开时，不可以设置频率 耦合模式和频率差值/比例。 

频率耦合功能关闭时，若当前频率耦合模式为频率比例，发送该命令可以设置频率比例；若当前频率耦 合模式为频率差值，发送该命令可以选择频率比例耦合模式并设置频率比例。 

. 您也可以发送:COUPling[<n>]:FREQuency:RATio 命令设置和查询频率耦合模式的频率比例。 

# 返回格式

以科学计数形式返回频率比例，有效位数为 7位，如 $1 . 0 0 1 2 3 0 \mathsf { E } + 0 2$ ，表示频率比例为 100.123。 

# 举例

:FREQ:COUP:RAT 100.123 /*设置频率耦合中的频率比例为 $1 0 0 . 1 2 3 ^ { \star } /$ 

:FREQ:COUP:RAT? /*查询频率耦合中的频率比例，返回 1.001230E+02*/ 

# [:SOURce[<n>]]:FREQuency:COUPle[:STATe]

# 命令格式

[:SOURce[<n>]]:FREQuency:COUPle[:STATe] {ON|1|OFF|0} 

[:SOURce[<n>]]:FREQuency:COUPle[:STATe]? 

# 功能描述

打开或关闭频率耦合功能。 

查询频率耦合功能的开关状态。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 说明

. 频率耦合功能关闭时，您可以选择频率耦合模式并设置相应的频率差值或比例。打开频率耦合功能后， CH1和 CH2 两个通道互为基准源，当改变其中一个通道（该通道作为基准源）的频率时，另一通道的 频率将自动调整，并总是与基准通道保持指定的频率差值或比例。 

请在打开频率耦合功能之前选择所需的频率耦合模式（[:SOURce[<n>]]:FREQuency:COUPle:MODE） 并设置相应的频率差值（[:SOURce[<n>]]:FREQuency:COUPle:OFFSet）或频率比例 （[:SOURce[<n>]]:FREQuency:COUPle:RATio）。打开频率耦合功能后，不可以设置频率耦合模式和频 率差值/比例。 

. 您也可以发送:COUPling[<n>]:FREQuency[:STATe]命令设置或查询频率耦合功能状态。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:FREQ:COUP ON /*打开频率耦合功能*/ 

:FREQ:COUP? /*查询频率耦合功能的开关状态，返回 $\mathsf { O N } ^ { \star } /$ 

# [:SOURce[<n>]]:FREQuency[:FIXed]

# 命令格式

[:SOURce[<n>]]:FREQuency[:FIXed] {<frequency>|MINimum|MAXimum} 

[:SOURce[<n>]]:FREQuency[:FIXed]? [MINimum|MAXimum] 

# 功能描述

设置指定通道的波形频率。 

查询指定通道的波形频率。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;frequency&gt;</td><td>实型</td><td>请参考表 2-1</td><td>1kHz</td></tr></table>

# 说明

省略[:SOURce[<n>]]或 $\cdot < n > ]$ ]时，默认设置 CH1的相关参数。 

若实际发送的命令中的频率值大于相应的频率上限或者低于相应的频率下限，则设置指定通道的波形频 率为其频率上限或频率下限。 

指定通道波形类型改变时，若该频率在新的波形类型下有效，则仪器依然使用该频率；若该频率在新的 波形类型下无效，仪器则弹出提示消息，并自动将频率设置为新的波形类型的频率上限值。 

# 返回格式

以科学计数形式返回波形频率，有效位数为 7位，如 $1 . 0 0 0 0 0 0 0 \mathsf { E } + 0 2$ ，表示波形频率为 100Hz。 

# 举例

:SOUR1:FREQ 100 /*设置 CH1的波形频率为 $1 0 0 \mathsf { H z } ^ { \star } /$ 

:SOUR1:FREQ? /*查询 CH1 的波形频率，返回 1.000000E+02*/ 

# [:SOURce[<n>]]:FREQuency:SPAN

# 命令格式

[:SOURce[<n>]]:FREQuency:SPAN {<frequency $>$ |MINimum|MAXimum} 

[:SOURce[<n>]]:FREQuency:SPAN? [MINimum|MAXimum] 

# 功能描述

设置指定通道扫频功能的频率跨度。 

查询指定通道扫频功能的频率跨度。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;frequency&gt;</td><td>实型</td><td>指定通道当前波形的频率范围</td><td>900Hz</td></tr></table>

# 说明

您可以通过中心频率和频率跨度（[:SOURce[<n>]]:FREQuency:SPAN）来设定扫频的边界。不同扫频 波形对应的中心频率和频率跨度范围不同，且中心频率与频率跨度相互影响。定义当前波形的最小频率 为 $F _ { \mathrm { m i n } }$ ，最大频率为 $F _ { \mathrm { m a x } }$ ， $F _ { m } = ( F _ { \operatorname* { m i n } } + F _ { \operatorname* { m a x } } ) / 2$ 。中心频率（定义为 $F _ { c e n t e r }$ ）的可设置范围为 $F _ { \mathrm { m i n } }$ 至 $F _ { \mathrm { m a x } }$ ， 频率跨度（定义为 $F _ { s p a n }$ ）的范围受中心频率影响。当中心频率小于 $F _ { m }$ 时，频率跨度的范围为 $\pm 2 \times ( F _ { c e n t e r } - F _ { \mathrm { { m i n } } } )$ ；当中心频率大于 $F _ { m }$ 时，频率跨度的范围为 $\pm 2 \times ( { F _ { \mathrm { m a x } } } - { F _ { c e n t e r } } )$ 。 

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

起始频率、终止频率、中心频率和频率跨度满足如下关系式 

$$
F _ {c e n t e r} = \left(\left| F _ {s t a r t} + F _ {s t o p} \right|\right); \quad F _ {s p a n} = \left(\left| F _ {s t o p} - F _ {s t a r t} \right|\right)
$$

其中， 

Fcenter $F _ { c e n t e r }$ 中心频率； 

$F _ { s p a n }$ Fspan 频率跨度； 

Fstart $F _ { s t a r t }$ 起始频率； 

Fstop $F _ { s t o p }$ 终止频率。 

修改“频率跨度”后，信号发生器将重新从指定的“起始频率”开始扫频输出。大范围扫频时，输出信 号的幅度特性可能会有变化。 

# 返回格式

以科学计数形式返回频率跨度，有效位数为 7位，如 8.000000E+02，表示频率跨度为 800Hz。 

# 举例

:SOUR1:FREQ:SPAN 800 /*设置 CH1的扫频功能的频率跨度为 $8 0 0 \mathsf { H z } ^ { \star } /$ 

:SOUR1:FREQ:SPAN? /*查询 CH1的扫频功能的频率跨度，返回 $8 . 0 0 0 0 0 0 0 \mathsf { E } + 0 2 ^ { \star } /$ 

# [:SOURce[<n>]]:FREQuency:STARt

# 命令格式

[:SOURce[<n>]]:FREQuency:STARt {<frequency>|MINimum|MAXimum} 

[:SOURce[<n>]]:FREQuency:STARt? [MINimum|MAXimum] 

# 功能描述

设置指定通道扫频功能的起始频率。 

查询指定通道扫频功能的起始频率。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;frequency&gt;</td><td>实型</td><td>指定通道当前波形的频率范围</td><td>100Hz</td></tr></table>

# 说明

起始频率和终止频率（[:SOURce[<n>]]:FREQuency:STOP）是频率扫描的频率上限和下限。信号发生 器总是从起始频率扫频到终止频率，然后又回到起始频率。当起始频率小于终止频率时，信号发生器从 低频向高频扫描；当起始频率大于终止频率时，信号发生器从高频向低频扫描；当起始频率等于终止频 率时，信号发生器以固定频率输出。 

省略[:SOURce[<n>]]或[ $\cdot < n > ]$ 时，默认设置 CH1 的相关参数。 

正弦波、方波、锯齿波和任意波可以产生扫频输出，不同的扫频波形对应的起始频率<frequency>的范 围不同。 

起始频率、终止频率、中心频率和频率跨度满足如下关系式 

$$
F _ {c e n t e r} = \left(\left| F _ {s t a r t} + F _ {s t o p} \right|\right); \quad F _ {s p a n} = \left(\left| F _ {s t o p} - F _ {s t a r t} \right|\right)
$$

其中， 

Fcenter $F _ { c e n t e r }$ ——中心频率； 

$F _ { s p a n }$ Fspan 频率跨度； 

$F _ { s t a r t }$ Fstart 起始频率； 

Fstop $F _ { s t o p }$ 终止频率。 

修改“起始频率“后，信号发生器将重新从指定的“起始频率”开始扫频输出。大范围扫频时，输出信 号的幅度特性可能会有变化。 

# 返回格式

以科学计数形式返回起始频率，有效位数为 7位，如 1.000000E+02，表示起始频率为 100Hz。 

# 举例

:SOUR1:FREQ:STAR 100 /*设置 CH1的扫频功能的起始频率为 $1 0 0 \mathsf { H z } ^ { \star } /$ 

:SOUR1:FREQ:STAR? /*查询 CH1的扫频功能的起始频率，返回 $1 . 0 0 0 0 0 0 0 \mathsf { E } + 0 2 ^ { \star } /$ 

# [:SOURce[<n>]]:FREQuency:STOP

# 命令格式

[:SOURce[<n>]]:FREQuency:STOP {<frequency>|MINimum|MAXimum} 

[:SOURce[<n>]]:FREQuency:STOP? [MINimum|MAXimum] 

# 功能描述

设置指定通道扫频功能的终止频率。 

查询指定通道扫频功能的终止频率。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;frequency&gt;</td><td>实型</td><td>指定通道当前波形的频率范围</td><td>1kHz</td></tr></table>

# 说明

起始频率（[:SOURce[<n>]]:FREQuency:STARt）和终止频率是频率扫描的频率上限和下限。信号发生 器总是从起始频率扫频到终止频率，然后又回到起始频率。当起始频率小于终止频率时，信号发生器从 低频向高频扫描；当起始频率大于终止频率时，信号发生器从高频向低频扫描；当起始频率等于终止频 率时，信号发生器以固定频率输出。 

省略[:SOURce[ $< n > ]$ ]]或[<n>]时，默认设置 CH1 的相关参数。 

正弦波、方波、锯齿波和任意波可以产生扫频输出，不同的扫频波形对应的终止频率<frequency>的范 围不同。 

起始频率、终止频率、中心频率和频率跨度满足如下关系式 

$$
F _ {c e n t e r} = \left(\left| F _ {s t a r t} + F _ {s t o p} \right|\right); \quad F _ {s p a n} = \left(\left| F _ {s t o p} - F _ {s t a r t} \right|\right)
$$

其中， 

Fcenter $F _ { c e n t e r }$ ——中心频率； 

$F _ { s p a n }$ Fspan 频率跨度； 

Fstart $F _ { s t a r t }$ 起始频率； 

Fstop $F _ { s t o p }$ 终止频率。 

修改“终止频率”后，信号发生器将重新从指定的“起始频率”开始扫频输出。大范围扫频时，输出信 号的幅度特性可能会有变化。 

# 返回格式

以科学计数形式返回终止频率，有效位数为 7位，如 9.000000E+02，表示终止频率为 900Hz。 

# 举例

:SOUR1:FREQ:STOP 900 /*设置 CH1的扫频功能的终止频率为 $9 0 0 \mathsf { H z } ^ { \star } /$ :SOUR1:FREQ:STOP? /*查询 CH1的扫频功能的终止频率，返回 $9 . 0 0 0 0 0 0 0 \mathsf { E } + 0 2 ^ { \star } /$ 

# :SOURce:FUNCtion 命令

# 命令列表：

$\spadesuit$ [:SOURce[<n>]]:FUNCtion:DUALTone:CENTERFreq 

 [:SOURce[<n>]]:FUNCtion:DUALTone:FREQ1 

 [:SOURce[<n>]]:FUNCtion:DUALTone:FREQ2 

 [:SOURce[<n>]]:FUNCtion:DUALTone:OFFSETFreq 

 [:SOURce[<n>]]:FUNCtion:PRBS:BRATe 

 [:SOURce[<n>]]:FUNCtion:PRBS:DATA 

 [:SOURce[<n>]]:FUNCtion:PULSe:DCYCle 

 [:SOURce[<n>]]:FUNCtion:PULSe:PERiod 

[:SOURce[<n>]]:FUNCtion:PULSe:TRANsition[:BOTH] 

[:SOURce[<n>]]:FUNCtion:PULSe:TRANsition:LEADing 

[:SOURce[<n>]]:FUNCtion:PULSe:TRANsition:TRAiling 

 [:SOURce[<n>]]:FUNCtion:PULSe:WIDTh 

[:SOURce[<n>]]:FUNCtion:RAMP:SYMMetry 

[:SOURce[<n>]]:FUNCtion:RS232:BAUDrate 

 [:SOURce[<n>]]:FUNCtion:RS232:CHECKBit 

[:SOURce[<n>]]:FUNCtion:RS232:DATA 

[:SOURce[<n>]]:FUNCtion:RS232:DATABit 

 [:SOURce[<n>]]:FUNCtion:RS232:STOPBit 

[:SOURce[<n>]]:FUNCtion:SEQuence:FILTer 

[:SOURce[<n>]]:FUNCtion:SEQuence:PERiod 

[:SOURce[<n>]]:FUNCtion:SEQuence:SRATe 

 [:SOURce[<n>]]:FUNCtion:SEQuence[:STATe] 

 [:SOURce[<n>]]:FUNCtion:SEQuence:WAVE 

 [:SOURce[<n>]]:FUNCtion[:SHAPe] 

[:SOURce[<n>]]:FUNCtion:SQUare:DCYCle 

[:SOURce[<n>]]:FUNCtion:SQUare:PERiod 

# [:SOURce[<n>]]:FUNCtion:DUALTone:CENTERFreq

# 命令格式

[:SOURce[<n>]]:FUNCtion:DUALTone:CENTERFreq {<frequency $>$ |MINimum|MAXimum} 

[:SOURce[<n>]]:FUNCtion:DUALTone:CENTERFreq? 

# 功能描述

设置指定通道的双音信号的中心频率。 

查询指定通道的双音信号的中心频率。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;frequency&gt;</td><td>实型</td><td>见下文“说明”</td><td>1kHz</td></tr></table>

# 说明

省略[:SOURce[<n>]]或[ $\cdot < n > ]$ ]时，默认设置 CH1的相关参数。 

中心频率和频率 1、频率 2 满足如下关系式 

$$
F _ {c e n t e r} = \left(F _ {I} + F _ {2}\right) / 2;
$$

其中， 

Fcenter $F _ { c e n t e r }$ 中心频率； 

$F _ { I }$ -频率1; 

$F _ { 2 }$ 频率 2。 

# 返回格式

以科学计数形式返回双音信号的中心频率，有效位数为 7位，如 5.000000E+02，表示中心频率为 500Hz。 

# 举例

:SOUR1:FUNC:DUALT:CENTERF 500 /*设置 CH1的双音信号的中心频率为 500Hz */ 

:SOUR1:FUNC:DUALT:CENTERF? /*查询 CH1的双音信号的中心频率，返回 $5 . 0 0 0 0 0 0 0 \mathsf { E } { + } 0 2 ^ { \star } /$ 

# [:SOURce[<n>]]:FUNCtion:DUALTone:FREQ1

# 命令格式

[:SOURce[<n>]]:FUNCtion:DUALTone:FREQ1 {<frequency>|MINimum|MAXimum} 

[:SOURce[<n>]]:FUNCtion:DUALTone:FREQ1? 

# 功能描述

设置指定通道的双音信号的频率 1。 

查询指定通道的双音信号的频率 1。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;frequency&gt;</td><td>实型</td><td>1μHz至20MHz</td><td>1kHz</td></tr></table>

# 说明

省略[:SOURce[<n>]]或 $[ < n >$ ]时，默认设置 CH1 的相关参数。 

# 返回格式

以科学计数形式返回频率 1，有效位数为 7 位，如 5.000000E $+ 0 2$ ，表示频率 1为 500Hz。 

# 举例

:SOUR1:FUNC:DUALT:FREQ1 500 /*设置 CH1 的双音信号的频率 1 为 $5 0 0 \mathsf { H z } ^ { \star } /$ 

:SOUR1:FUNC:DUALT:FREQ1? /*查询 CH1的双音信号的频率 1，返回 $5 . 0 0 0 0 0 0 0 \mathsf { E } { + } 0 2 ^ { \star } /$ 

# [:SOURce[<n>]]:FUNCtion:DUALTone:FREQ2

# 命令格式

[:SOURce[<n>]]:FUNCtion:DUALTone:FREQ2 {<frequency>|MINimum|MAXimum} 

[:SOURce[<n>]]:FUNCtion:DUALTone:FREQ2? 

# 功能描述

设置指定通道的双音信号的频率 2。 

查询指定通道的双音信号的频率 2。 

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;frequency&gt;</td><td>实型</td><td>1μHz至20MHz</td><td>1kHz</td></tr></table>

# 说明

省略[:SOURce[<n>]]或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

# 返回格式

以科学计数形式返回频率 2，有效位数为 7 位，如 $5 . 0 0 0 0 0 0 0 \mathsf { E } + 0 2$ ，表示频率 2为 500Hz。 

# 举例

:SOUR1:FUNC:DUALT:FREQ2 500 /*设置 CH1 的双音信号的频率 2 为 $5 0 0 \mathsf { H z } ^ { \star } /$ 

:SOUR1:FUNC:DUALT:FREQ2? /*查询 CH1 的双音信号的频率 2，返回 5.000000E+02*/ 

# [:SOURce[<n>]]:FUNCtion:DUALTone:OFFSETFreq

# 命令格式

[:SOURce[<n>]]:FUNCtion:DUALTone:OFFSETFreq {<frequency>|MINimum|MAXimum} 

[:SOURce[<n>]]:FUNCtion:DUALTone:OFFSETFreq? 

# 功能描述

设置指定通道的双音信号的偏移频率。 

查询指定通道的双音信号的偏移频率。 

# 参数

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;frequency&gt;</td><td>实型</td><td>见下文“说明”</td><td>0Hz</td></tr></table>

# 说明

省略[:SOURce[<n>]]或[<n>]时，默认设置 CH1 的相关参数。 

偏移频率和频率 1、频率 2 满足如下关系式 

$$
F _ {\text {o f f s e t}} = F _ {2} - F _ {1};
$$

其中， 

Foffset 偏移频率； 

$F _ { I }$ 频率1; 

$F _ { 2 }$ 2 频率 2； 

# 返回格式

以科学计数形式返回偏移频率，有效位数为 7位，如 $2 . 0 0 0 0 0 0 0 \mathsf { E } + 0 3$ ，表示偏移频率为 2kHz。 

# 举例

:SOUR1:FUNC:DUALT:OFFSETF 2000 

/*设置 CH1 的双音信号的偏移频率为 2kHz*/ 

:SOUR1:FUNC:DUALT:OFFSETF? 

/*查询 CH1 的双音信号的偏移频率，返回 2.000000E+03*/ 

# [:SOURce[<n>]]:FUNCtion:PRBS:BRATe

# 命令格式

[:SOURce[<n>]]:FUNCtion:PRBS:BRATe {<bit_rate>|MINimum|MAXimum} 

[:SOURce[<n>]]:FUNCtion:PRBS:BRATe? [MINimum|MAXimum] 

# 功能描述

设置指定通道的 PRBS 比特率。 

查询指定通道的 PRBS 比特率。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;srate&gt;</td><td>实型</td><td>2kbps至60Mbps</td><td>2kbps</td></tr></table>

# 说明

省略[:SOURce[<n>]]或[ $\cdot < n > ]$ 时，默认设置 CH1 的相关参数。 

# 返回格式

以科学计数形式返回 PRBS 比特率，有效位数为 7 位，如 3.000000E $+ 0 3$ ，表示 PRBS 比特率为 3kbps。 

# 举例

:SOUR1:FUNC:PRBS:BRAT 3000 /*设置 CH1 的 PRBS 比特率为 3kbps*/ 

:SOUR1:FUNC:PRBS:BRAT? /*查询 CH1 的 PRBS 比特率，返回 3.000000E+03*/ 

# [:SOURce[<n>]]:FUNCtion:PRBS:DATA

# 命令格式

[:SOURce[<n>]]:FUNCtion:PRBS:DATA {PN7|PN9|PN11} 

[:SOURce[<n>]]:FUNCtion:PRBS:DATA? 

# 功能描述

设置指定通道的 PRBS 数据类型。 

查询指定通道的 PRBS 数据类型。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{PN7|PN9|PN11}</td><td>离散型</td><td>PN7|PN9|PN11</td><td>PN7</td></tr></table>

# 说明

省略[:SOURce $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

# 返回格式

返回 PN7、PN9 或 PN11。 

# 举例

:SOUR1:FUNC:PRBS:DATA PN9 

/*设置 CH1 的 PRBS 的数据类型为 PRBS9*/ 

:SOUR1:FUNC:PRBS:DATA? 

/*查询 CH1的 PRBS 的数据类型，返回 $\mathsf { P N } 9 ^ { \star } /$ 

# [:SOURce[<n>]]:FUNCtion:PULSe:DCYCle

# 命令格式

[:SOURce[<n>]]:FUNCtion:PULSe:DCYCle {<percent>|MINimum|MAXimum} 

[:SOURce[<n>]]:FUNCtion:PULSe:DCYCle? [MINimum|MAXimum] 

# 功能描述

设置指定通道的脉冲占空比。 

查询指定通道的脉冲占空比。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;percent&gt;</td><td>离散型</td><td>0.001%至99.999%</td><td>50%</td></tr></table>

# 说明

脉冲占空比定义为脉宽（[:SOURce[<n>]]:FUNCtion:PULSe:WIDTh）占脉冲周期 （[:SOURce[<n>]]:FUNCtion:PULSe:PERiod）的百分比。 

. 脉冲占空比的可设范围受“最小脉冲宽度”和“脉冲周期”的限制（关于“最小脉冲宽度”和“脉冲周 期”的范围，请参考《DG2000 数据手册》“性能指标”中“信号特性”的说明）。脉冲占空比的实际取 值范围为 

$$
1 0 0 \times P _ {w \min } \div P _ {\text {p u l s e}} \leq P _ {\text {d c y c l e}} <   1 0 0 \times (1 - 2 \times P _ {w \min } \div P _ {\text {p u l s e}})
$$

其中， 

$P _ { d c y c l e }$ 脉冲占空比； 

$P _ { w \mathrm { m i n } }$ Pwmin 最小脉冲宽度； 

$P _ { p u l s e }$ 脉冲周期。 

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1 的相关参数。 

# 返回格式

以科学计数形式返回脉冲占空比，有效位数为 7位，如 $4 . 5 0 0 0 0 0 0 \mathsf { E } + 0 1$ ，表示脉冲占空比为 $45 \%$ 。 

# 举例

:SOUR1:FUNC:PULS:DCYC 45 /*设置 CH1 的脉冲占空比为 $4 5 \% ^ { \star } /$ 

:SOUR1:FUNC:PULS:DCYC? /*查询 CH1的脉冲占空比，返回 $4 . 5 0 0 0 0 0 0 \mathsf { E } { + } 0 1 ^ { \star } /$ 

# [:SOURce[<n>]]:FUNCtion:PULSe:PERiod

# 命令格式

[:SOURce[<n>]]:FUNCtion:PULSe:PERiod {<seconds $>$ |MINimum|MAXimum} 

[:SOURce[<n>]]:FUNCtion:PULSe:PERiod? [MINimum|MAXimum] 

# 功能描述

设置指定通道的脉冲周期。 

查询指定通道的脉冲周期。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;seconds&gt;</td><td>实型</td><td>40ns至1Ms</td><td>1ms</td></tr></table>

# 说明

省略[:SOURce[<n>]]或 $[ < n > ]$ ]时，默认设置 CH1 的相关参数。 

当指定通道波形类型改变（[:SOURce[<n>]]:APPLy?）时，若该周期在新的波形类型下有效，则仪器依 然使用该周期；若该周期在新的波形类型下无效，仪器则弹出提示消息，并自动将周期设置为新的波形 类型的周期下限值。 

# 返回格式

以科学计数形式返回脉冲周期，有效位数为 7位，如 1.000000E-01，表示脉冲周期为 0.1s。 

# 举例

:SOUR1:FUNC:PULS:PER 0.1 /*设置 CH1的脉冲周期为 $0 . 1 \mathsf { s } ^ { \star } /$ 

:SOUR1:FUNC:PULS:PER? /*查询 CH1 的脉冲周期，返回 1.000000E-01*/ 

# [:SOURce[<n>]]:FUNCtion:PULSe:TRANsition[:BOTH]

# 命令格式

[:SOURce[<n>]]:FUNCtion:PULSe:TRANsition[:BOTH] {<seconds>|MINimum|MAXimum} 

# 功能描述

设置指定通道的脉冲上升沿和下降沿时间为同一指定值。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;seconds&gt;</td><td>实型</td><td>10ns至0.625×脉宽</td><td>20ns</td></tr></table>

# 说明

上升沿时间定义为脉冲幅度从 $10 \%$ 上升至 $90 \%$ 所持续的时间；下降沿时间定义为脉冲幅度从 $90 \%$ 下降 至 $10 \%$ 所持续的时间。 

省略[:SOURce[<n>]]或 $\cdot < n > ]$ ]时，默认设置 CH1 的相关参数。 

上升沿和下降沿时间的可设范围受当前的波形频率和脉宽限制，当所设置的数值超出限定值，仪器将自 动调整边沿时间以适应指定的脉宽。 

# 举例

:SOUR1:FUNC:PULS:TRAN 0.000000035 /*设置 CH1的脉冲上升沿和下降沿时间均为 35ns*/ 

# [:SOURce[<n>]]:FUNCtion:PULSe:TRANsition:LEADing

# 命令格式

[:SOURce[<n>]]:FUNCtion:PULSe:TRANsition:LEADing {<seconds>|MINimum|MAXimum} [:SOURce[<n>]]:FUNCtion:PULSe:TRANsition:LEADing? [MINimum|MAXimum] 

# 功能描述

设置指定通道的脉冲上升沿时间。 

查询指定通道的脉冲上升沿时间。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;seconds&gt;</td><td>实型</td><td>10ns至0.625×脉宽</td><td>20ns</td></tr></table>

# 说明

上升沿时间定义为脉冲幅度从 $10 \%$ 上升至 $90 \%$ 所持续的时间。 

省略[:SOURce[ $< n > ] ]$ 或[<n>]时，默认设置 CH1的相关参数。 

上升沿时间的可设范围受当前的波形频率和脉宽限制，当所设置的数值超出限定值，DG2000将自动调 整边沿时间以适应指定的脉宽。 

# 返回格式

以科学计数形式返回脉冲上升沿时间，有效位数为 7位，如 3.500000E-08，表示脉冲上升沿时间为 35ns。 

# 举例

:SOUR1:FUNC:PULS:TRAN:LEAD 0.000000035 /*设置 CH1 的脉冲上升沿时间为 35ns*/ 

:SOUR1:FUNC:PULS:TRAN:LEAD? /*查询 CH1 的脉冲上升沿时间，返回 3.500000E-08*/ 

# [:SOURce[<n>]]:FUNCtion:PULSe:TRANsition:TRAiling

# 命令格式

[:SOURce[<n>]]:FUNCtion:PULSe:TRANsition:TRAiling {<seconds>|MINimum|MAXimum} 

[:SOURce[<n>]]:FUNCtion:PULSe:TRANsition:TRAiling? [MINimum|MAXimum] 

# 功能描述

设置指定通道的脉冲下降沿时间。 

查询指定通道的脉冲下降沿时间。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;seconds&gt;</td><td>实型</td><td>10ns至0.625×脉宽</td><td>20ns</td></tr></table>

# 说明

下降沿时间定义为脉冲幅度从 $90 \%$ 下降至 $10 \%$ 所持续的时间。 

省略[:SOURce[ $< n > ] ]$ 或[ $\cdot < n > ]$ 时，默认设置 CH1 的相关参数。 

下降沿时间的可设范围受当前的波形频率和脉宽限制，当所设置的数值超出限定值，DG2000将自动调 整边沿时间以适应指定的脉宽。 

# 返回格式

以科学计数形式返回脉冲下降沿时间，有效位数为 7位，如 3.500000E-08，表示脉冲下降沿时间为 35ns。 

# 举例

:SOUR1:FUNC:PULS:TRAN:TRA 0.000000035 /*设置 CH1 的脉冲下降沿时间为 35ns*/ 

:SOUR1:FUNC:PULS:TRAN:TRA? /*查询 CH1 的脉冲下降沿时间，返回 3.500000E-08*/ 

# [:SOURce[<n>]]:FUNCtion:PULSe:WIDTh

# 命令格式

[:SOURce[<n>]]:FUNCtion:PULSe:WIDTh {<seconds $>$ |MINimum|MAXimum} 

[:SOURce[<n>]]:FUNCtion:PULSe:WIDTh? [MINimum|MAXimum] 

# 功能描述

设置指定通道的脉宽。 

查询指定通道的脉宽。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;seconds&gt;</td><td>实型</td><td>16ns至999.999 982 118 590 6ks</td><td>500us</td></tr></table>

# 说明

脉宽定义为从脉冲上升沿幅度的 $50 \%$ 处到下一个下降沿幅度的 $50 \%$ 处之间的时间间隔。 

脉宽的可设范围受“最小脉冲宽度”和“脉冲周期”的限制（关于“最小脉冲宽度”和“脉冲周期”的 范围，请参考《DG2000 数据手册》“性能指标”中“信号特性”的说明）。脉宽的实际取值范围为 

$$
P _ {w \min } \leq P _ {\text {w i d t h}} <   P _ {\text {p u l s e}} - 2 \times P _ {w \min }
$$

其中， 

Pwidth $P _ { w i d t h }$ 脉宽； 

Pwmin $P _ { w \mathrm { m i n } }$ —最小脉冲宽度； 

Ppulse $P _ { p u l s e }$ 脉冲周期。 

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1 的相关参数。 

# 返回格式

以科学计数形式返回脉宽，有效位数为 7位，如 1.000000E-02，表示脉宽为 10ms（即 0.01s）。 

# 举例

:SOUR1:FUNC:PULS:WIDT 0.01 /*设置 CH1 的脉宽为 10ms（即 0.01s）*/ 

:SOUR1:FUNC:PULS:WIDT? /*查询 CH1 的脉宽，返回 1.000000E-02*/ 

# [:SOURce[<n>]]:FUNCtion:RAMP:SYMMetry

# 命令格式

[:SOURce[<n>]]:FUNCtion:RAMP:SYMMetry {<symmetry>|MINimum|MAXimum} 

[:SOURce[<n>]]:FUNCtion:RAMP:SYMMetry? [MINimum|MAXimum] 

# 功能描述

设置指定通道的锯齿波对称性。 

查询指定通道的锯齿波对称性。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;symmetry&gt;</td><td>实型</td><td>0%至100%</td><td>50%</td></tr></table>

# 说明

对称性定义为锯齿波波形处于上升期间所占周期的百分比。 

省略[:SOURce[<n>]]或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

# 返回格式

以科学计数形式返回对称性，有效位数为 7 位，如 $5 . 5 0 0 0 0 0 0 \mathsf { E } + 0 1$ ，表示锯齿波对称性为 $5 5 \%$ 。 

# 举例

:SOUR1:FUNC:RAMP:SYMM 55 /*设置 CH1 的锯齿波对称性为 $5 5 \% ^ { \star } /$ 

:SOUR1:FUNC:RAMP:SYMM? /*查询 CH1的锯齿波对称性，返回 $5 . 5 0 0 0 0 0 0 \mathsf { E } { + } 0 1 ^ { \star } /$ 

# [:SOURce[<n>]]:FUNCtion:RS232:BAUDrate

# 命令格式

$$
\begin{array}{l} [: S O U R c e [ <   n > ]: F U N C t i o n: R S 2 3 2: B A U D r a t e \{9 6 0 0 | 1 4 4 0 0 | 1 9 2 0 0 | 3 8 4 0 0 | 5 7 6 0 0 | 1 1 5 2 0 0 | 1 2 8 0 0 0 | 2 3 0 4 0 0 \} \\ [: S O U R c e [ <   n > ]: F U N C t i o n: R S 2 3 2: B A U D r a t e? \\ \end{array}
$$

# 功能描述

设置指定通道的 RS232 波形的波特率。 

查询指定通道的 RS232 波形的波特率。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{9600|14400|19200|38400|57600|115200|128000|230400}</td><td>离散型</td><td>9600|14400|19200|38400|57600|115200|128000|230400</td><td>9600</td></tr></table>

# 说明

省略[:SOURce[<n>]]或 $[ < n > ]$ 时，默认设置 CH1 的相关参数。 

# 返回格式

以整数形式返回 RS232 波形的波特率。 

# 举例

:SOUR1:FUNC:RS232:BAUD 9600 /*设置 CH1 的 RS232 波形的波特率为 $9 6 0 0 ^ { \star } /$ 

:SOUR1:FUNC:RS232:BAUD? /*查询 CH1的 RS232波形的波特率，返回 $9 6 0 0 ^ { \star } /$ 

# [:SOURce[<n>]]:FUNCtion:RS232:CHECKBit

# 命令格式

$$
[: S O U R c e [ <   n > ]: F U N C t i o n: R S 2 3 2: C H E C K B i t \{N O N E | O D D | E V E N \}
$$

$$
[: S O U R c e [ <   n > ]: F U N C t i o n: R S 2 3 2: C H E C K B i t?
$$

# 功能描述

设置指定通道的 RS232波形的校验位。 

查询指定通道的 RS232 波形的校验位。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{NONE|ODD|EVEN}</td><td>离散型</td><td>NONE|ODD|EVEN</td><td>NONE</td></tr></table>

# 说明

省略[:SOURce $\cdot < n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1 的相关参数。 

# 返回格式

返回 NONE、ODD 或 EVEN。 

# 举例

:SOUR1:FUNC:RS232:CHECKB ODD 

/*设置 CH1 的 RS232 波形的校验位为奇校验*/ 

:SOUR1:FUNC:RS232:CHECKB? 

/*查询 CH1 的 RS232 波形的校验位，返回 ODD*/ 

# [:SOURce[<n>]]:FUNCtion:RS232:DATA

# 命令格式

$$
\begin{array}{l} [: S O U R c e [ <   n > ]: F U N C t i o n: R S 2 3 2: D A T A \{<   v a l u e > | M I N i m u m | M A X i m u m \} \\ [: S O U R c e [ <   n > ]: F U N C t i o n: R S 2 3 2: D A T A? \\ \end{array}
$$

# 功能描述

设置指定通道的 RS232波形数据位的数据。 

查询指定通道的 RS232 波形数据位的数据。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;value&gt;</td><td>整型</td><td>0至255</td><td>0</td></tr></table>

# 说明

省略[:SOURce $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1 的相关参数。 

# 返回格式

以整数形式返回 RS232波形数据位的数据。 

# 举例

$$
: S O U R 1: F U N C: R S 2 3 2: D A T A 2 5 5
$$

/*设置 CH1的 RS232波形数据位的数据为 $2 5 5 ^ { \star } /$ 

$$
: S O U R 1: F U N C: R S 2 3 2: D A T A?
$$

/*查询 CH1的 RS232波形数据位的数据，返回 $2 5 5 ^ { \star } /$ 

# [:SOURce[<n>]]:FUNCtion:RS232:DATABit

# 命令格式

$$
[: S O U R c e [ <   n > ]: F u n c t i o n: R S 2 3 2: D A T A B i t \{7 | 8 \}
$$

$$
[: S O U R c e [ <   n > ]]: F U N C t i o n: R S 2 3 2: D A T A B i t?
$$

# 功能描述

设置指定通道的 RS232波形的数据位。 

查询指定通道的 RS232 波形的数据位。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{7|8}</td><td>离散型</td><td>7|8</td><td>7</td></tr></table>

# 说明

省略[:SOURce[<n>]]或 $\cdot < n > ]$ 时，默认设置 CH1 的相关参数。 

# 返回格式

返回 7或 8。 

# 举例

:SOUR1:FUNC:RS232:DATAB 7 /*设置 CH1 的 RS232 波形的数据位为 7 位*/ :SOUR1:FUNC:RS232:DATAB? /*查询 CH1的 RS232 波形的数据位，返回 $7 ^ { \star } /$ 

# [:SOURce[<n>]]:FUNCtion:RS232:STOPBit

# 命令格式

[:SOURce[<n>]]:FUNCtion:RS232:STOPBit {1|1.5|2} [:SOURce[<n>]]:FUNCtion:RS232:STOPBit? 

# 功能描述

设置指定通道的 RS232波形的停止位。 查询指定通道的 RS232 波形的停止位。 

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{1|1.5|2}</td><td>离散型</td><td>1|1.5|2</td><td>1</td></tr></table>

# 说明

省略[:SOURce[<n>]]或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

# 返回格式

返回 1、1.5 或 2。 

# 举例

:SOUR1:FUNC:RS232:STOPB 2 /*设置 CH1 的 RS232 波形的停止位为 2 位*/ :SOUR1:FUNC:RS232:STOPB? /*查询 CH1的 RS232 波形的停止位，返回 ${ 2 ^ { \star } } /$ 

# [:SOURce[<n>]]:FUNCtion:SEQuence:EDGETime

# 命令格式

[:SOURce[<n>]]:FUNCtion:SEQuence:EDGETime <seconds> [:SOURce[<n>]]:FUNCtion:SEQuence:EDGETime? 

# 功能描述

设置指定通道的序列波形的边沿时间。 查询指定通道的序列波形的边沿时间。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;seconds&gt;</td><td>实型</td><td>8ns至(1/采样率)/1.25</td><td>7ns</td></tr></table>

# 说明

省略[:SOURce[<n>]]或[<n>]时，默认设置 CH1 的相关参数。 

该命令仅当序列波形滤波器为插值模式时才有效。 

# 返回格式

以科学计数形式返回序列波形的边沿时间，有效位数为 7位，如 5.000000E-07，表示边沿时间为 0.5us。 

# 举例

:SOUR1:FUNC:SEQ:EDGET 0.0000005 

/*设置 CH1的序列波形边沿时间为 $0 . 5 \mathrm { u s ^ { \star } } /$ 

:SOUR1:FUNC:SEQ:EDGET? 

/*查询 CH1 的序列波形边沿时间，返回 5.000000E-07*/ 

# [:SOURce[<n>]]:FUNCtion:SEQuence:FILTer

# 命令格式

[:SOURce[<n>]]:FUNCtion:SEQuence:FILTer {SMOOth|STEP|INSErt} 

[:SOURce[<n>]]:FUNCtion:SEQuence:FILTer? 

# 功能描述

设置指定通道的序列波形的滤波器模式。 

查询指定通道的序列波形的滤波器模式。 

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{SMOOth|STEP|INSERT}</td><td>离散型</td><td>SMOOth|STEP|INSERT</td><td>INSERT</td></tr></table>

# 说明

省略[:SOURce[<n>]]或 $[ < n > ]$ ]时，默认设置 CH1的相关参数。 

# 返回格式

返回 SMOO、STEP 或 INSE。 

# 举例

:SOUR1:FUNC:SEQ:FILT STEP /*设置 CH1的序列波形的滤波器模式为步进*/ 

:SOUR1:FUNC:SEQ:FILT? /*查询 CH1的序列波形的滤波器模式，返回 STEP*/ 

# [:SOURce[<n>]]:FUNCtion:SEQuence:PERiod

# 命令格式

[:SOURce[<n>]]:FUNCtion:SEQuence:PERiod <num>|1|2|3|4|5|6|7|8 <value>|MINimum|MAXimum 

[:SOURce[<n>]]:FUNCtion:SEQuence:PERiod? {1|2|3|4|5|6|7|8} 

# 功能描述

设置指定通道的序列波形中指定序号波形的周期数。 

查询指定通道的序列波形中指定序号波形的周期数。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[n]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>[num]</td><td>离散型</td><td>1|2|3|4|5|6|7|8</td><td>1</td></tr><tr><td>=value&gt;</td><td>整型</td><td>1至256</td><td>0</td></tr></table>

# 说明

省略[:SOURce $\cdot < n > ] ]$ 或 $[ < n > ]$ ]时，默认设置 CH1的相关参数。 

# 返回格式

以整数形式返回序列波形中指定序号波形的周期数。 

# 举例

:SOUR1:FUNC:SEQ:PER 1 2 /*设置 CH1的序列波形中序号 1 波形的周期数为 ${ 2 ^ { \star } } /$ :SOUR1:FUNC:SEQ:PER? /*查询 CH1的序列波形中序号 1 波形的周期数，返回 ${ 2 ^ { \star } } /$ 

# [:SOURce[<n>]]:FUNCtion:SEQuence:SRATe

# 命令格式

[:SOURce[<n>]]:FUNCtion:SEQuence:SRATe {<sample_rate>|MINimum|MAXimum} [:SOURce[<n>]]:FUNCtion:SEQuence:SRATe? 

# 功能描述

设置指定通道的序列波形的采样率。 查询指定通道的序列波形的采样率。 

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;sample_rate&gt;</td><td>实型</td><td>2kSa/s至60MSa/s</td><td>1MSa/s</td></tr></table>

# 说明

采样率是指每秒输出的点数。 

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1 的相关参数。 

# 返回格式

以科学计数形式返回序列波采样率，有效位数为 7 位，如 3.000000E+03，表示采样率为 3kSa/s。 

# 举例

:SOUR1:FUNC:SEQ:SRAT 3000 /*设置 CH1 的序列波形的采样率为 3kSa/s*/ 

:SOUR1:FUNC:SEQ:SRAT? /*查询 CH1 的序列波形的采样率，返回 3.000000E+03*/ 

# [:SOURce[<n>]]:FUNCtion:SEQuence[:STATe]

# 命令格式

[:SOURce[<n>]]:FUNCtion:SEQuence[:STATe] {ON|1|OFF|0} [:SOURce[<n>]]:FUNCtion:SEQuence[:STATe]? 

# 功能描述

打开或关闭指定通道的序列波功能。 查询指定通道的序列波形的开关状态 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 说明

省略[:SOURce[<n>]]或 $[ < n > ]$ 时，默认设置 CH1 的相关参数。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:SOUR1:FUNC:SEQ ON /*打开 CH1的序列波功能*/ 

:SOUR1:FUNC:SEQ? /*查询 CH1的序列波功能的开关状态，返回 $\mathsf { O N } ^ { \star } /$ 

# [:SOURce[<n>]]:FUNCtion:SEQuence:WAVE

# 命令格式

[:SOURce[<n>]]:FUNCtion:SEQuence:WAVE <num>,<wavename> 

[:SOURce[<n>]]:FUNCtion:SEQuence:WAVE? {1|2|3|4|5|6|7|8} 

# 功能描述

设置指定通道的序列波形中指定序号的波形。 

查询指定通道的序列波形中指定序号的波形。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;num&gt;</td><td>离散型</td><td>1|2|3|4|5|6|7|8</td><td>1</td></tr><tr><td>&lt;wavename&gt;</td><td>离散型</td><td>见下文“说明”</td><td>SINusoid</td></tr></table>

# 说明

省略[:SOURce[<n>]]或 $[ < n > ]$ ]时，默认设置 CH1 的相关参数。 

参数<name>可以为各种基本波形、谐波以及任意波，其范围为 SINusoid|SQUare |RAMP|PULSe|NOISe|USER|HARMonic|CUSTom|DC|KAISER|ROUNDPM|SINC|NEGRAMP|ATTALT|AMP ALT|STAIRDN|STAIRUP|STAIRUD|CPULSE|PPULSE|NPULSE|TRAPEZIA|ROUNDHALF|ABSSINE|ABSSI NEHALF|SINETRA|SINEVER|EXPRISE|EXPFALL|TAN|COT|SQRT|X2DATA|GAUSS|HAVERSINE|LORENT Z|DIRICHLET|GAUSSPULSE|AIRY|CARDIAC|QUAKE|GAMMA|VOICE|TV|COMBIN|BANDLIMITED|STEP RESP|BUTTERWORTH|CHEBYSHEV1|CHEBYSHEV2|BOXCAR|BARLETT|TRIANG|BLACKMAN|HAMMIN G|HANNING|DUALTONE|ACOS|ACOSH|ACOTCON|ACOTPRO|ACOTHCON|ACOTHPRO|ACSCCON|ACS CPRO|ACSCHCON|ACSCHPRO|ASECCON|ASECPRO|ASECH|ASIN|ASINH|ATAN|ATANH|BESSELJ|BESS ELY|CAUCHY|COSH|COSINT|COTHCON|COTHPRO|CSCCON|CSCPRO|CSCHCON|CSCHPRO|CUBIC|ER F|ERFC|ERFCINV|ERFINV|LAGUERRE|LAPLACE|LEGEND|LOG|LOGNORMAL|MAXWELL|RAYLEIGH|RE CIPCON|RECIPPRO|SECCON|SECPRO|SECH|SINH|SININT|TANH|VERSIERA|WEIBULL|BARTHANN|BL ACKMANH|BOHMANWIN|CHEBWIN|FLATTOPWIN|NUTTALLWIN|PARZENWIN|TAYLORWIN|TUKEYWI N|CWPUSLE|LFPULSE|LFMPULSE|EOG|EEG|EMG|PULSILOGRAM|TENS1|TENS2|TENS3|SURGE|DAMP EDOSC|SWINGOSC|RADAR|THREEAM|THREEFM|THREEPM|THREEPWM|THREEPFM|RESSPEED|MCN OSIE|PAHCUR|RIPPLE|ISO76372TP1|ISO76372TP2A|ISO76372TP2B|ISO76372TP3A|ISO76372TP3B |ISO76372TP4|ISO76372TP5A|ISO76372TP5B|ISO167502SP|ISO167502VR|SRC|IGNITION|NIMHDI SCHARGE|GATEVIBR。 

# 返回格式

返回一个字符串，如 SQU。 

# 举例

:SOUR1:FUNC:SEQ:WAVE 1,SQU /*设置 CH1 的序列波形中序号 1 的波形为方波*/ 

:SOUR1:FUNC:SEQ:WAVE? 1 /*查询 CH1的序列波形中序号 1 的波形，返回 SQU*/ 

# [:SOURce[<n>]]:FUNCtion[:SHAPe]

# 命令格式

[:SOURce[<n>]]:FUNCtion[:SHAPe] <name> 

[:SOURce[<n>]]:FUNCtion[:SHAPe]? 

# 功能描述

设置指定通道的波形类型。 

查询指定通道的波形类型。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{name&gt;</td><td>离散型</td><td>见下文“说明”</td><td>无</td></tr></table>

# 说明

省略[:SOURce[<n>]]或[<n>]时，默认设置 CH1 的相关参数。 

参数<name>可以为各种基本波形、谐波以及任意波，其范围为 SINusoid|SQUare|RAMP| PULSe|NOISe|USER|HARMonic|DC|KAISER|ROUNDPM|SINC|NEGRAMP| ATTALT|AMPALT|STAIRDN|STAIRUP|STAIRUD|CPULSE|PPULSE|NPULSE|TRAPEZIA| ROUNDHALF|ABSSINE|ABSSINEHALF|SINETRA|SINEVER|EXPRISE|EXPFALL|TAN|COT| SQRT|X2DATA|GAUSS|HAVERSINE|LORENTZ|DIRICHLET|GAUSSPULSE|AIRY| CARDIAC|QUAKE|GAMMA|VOICE|TV|COMBIN|BANDLIMITED|STEPRESP| BUTTERWORTH|CHEBYSHEV1|CHEBYSHEV2|BOXCAR|BARLETT|TRIANG|BLACKMAN| HAMMING|HANNING|DUALTONE|ACOS|ACOSH|ACOTCON|ACOTPRO|ACOTHCON| ACOTHPRO|ACSCCON|ACSCPRO|ACSCHCON|ACSCHPRO|ASECCON|ASECPRO|ASECH| ASIN|ASINH|ATAN|ATANH|BESSELJ|BESSELY|CAUCHY|COSH|COSINT|COTHCON| COTHPRO|CSCCON|CSCPRO|CSCHCON|CSCHPRO|CUBIC|ERF|ERFC|ERFCINV|ERFINV| LAGUERRE|LAPLACE|LEGEND|LOG|LOGNORMAL|MAXWELL|RAYLEIGH|RECIPCON| RECIPPRO|SECCON|SECPRO|SECH|SINH|SININT|TANH|VERSIERA|WEIBULL| BARTHANN|BLACKMANH|BOHMANWIN|CHEBWIN|FLATTOPWIN|NUTTALLWIN| PARZENWIN|TAYLORWIN|TUKEYWIN|CWPUSLE|LFPULSE|LFMPULSE|EOG|EEG|EMG| PULSILOGRAM|TENS1|TENS2|TENS3|SURGE|DAMPEDOSC|SWINGOSC|RADAR| THREEAM|THREEFM|THREEPM|THREEPWM|THREEPFM|RESSPEED|MCNOSIE| PAHCUR|RIPPLE|ISO76372TP1|ISO76372TP2A|ISO76372TP2B|ISO76372TP3A| ISO76372TP3B|ISO76372TP4|ISO76372TP5A|ISO76372TP5B|ISO167502SP| ISO167502VR|SCR|IGNITION|NIMHDISCHARGE|GATEVIBR。 

# 返回格式

返回一个字符串，如 SQU。 

# 举例

:SOUR1:FUNC SQU /*设置 CH1 的波形类型为方波*/ 

:SOUR1:FUNC? /*查询 CH1的波形类型，返回 $\mathsf { S O U } ^ { \star } /$ 

# [:SOURce[<n>]]:FUNCtion:SQUare:DCYCle

# 命令格式

[:SOURce[<n>]]:FUNCtion:SQUare:DCYCle {<percent $>$ |MINimum|MAXimum} 

[:SOURce[<n>]]:FUNCtion:SQUare:DCYCle? [MINimum|MAXimum] 

# 功能描述

设置指定通道的方波占空比。 

查询指定通道的方波占空比。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;percent&gt;</td><td>实型</td><td>受波形频率限制</td><td>50%</td></tr></table>

# 说明

占空比定义为方波波形高电平持续的时间所占周期的百分比。 

省略[:SOURce[ $< n > ]$ ]]或 $[ < n > ]$ ]时，默认设置 CH1 的相关参数。 

# 返回格式

以科学计数形式返回方波占空比，有效位数为 7位，如 $4 . 5 0 0 0 0 0 0 \mathsf { E } + 0 1$ ，表示方波占空比为 $45 \%$ 。 

# 举例

:SOUR1:FUNC:SQU:DCYC 45 /*设置 CH1的方波占空比为 $45 \% ^ { \star } /$ 

:SOUR1:FUNC:SQU:DCYC? /*查询 CH1 的方波占空比，返回 4.500000E+01*/ 

# [:SOURce[<n>]]:FUNCtion:SQUare:PERiod

# 命令格式

[:SOURce[<n>]]:FUNCtion:SQUare:PERiod {<seconds>|MINimum|MAXimum} [:SOURce[<n>]]:FUNCtion:SQUare:PERiod? [{MINimum|MAXimum}] 

# 功能描述

设置指定通道的方波周期。 

查询指定通道的方波周期。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;seconds&gt;</td><td>实型</td><td>40ns至1Ms</td><td>1ms</td></tr></table>

# 说明

省略[:SOURce[<n>]]或 $\cdot < n > ]$ ]时，默认设置 CH1的相关参数。 

当指定通道波形类型改变（[:SOURce[<n>]]:APPLy?）时，若该周期在新的波形类型下有效，则仪器依 然使用该周期；若该周期在新的波形类型下无效，仪器则弹出提示消息，并自动将周期设置为新的波形 类型的周期下限值。 

# 返回格式

以科学计数形式返回方波周期，有效位数为 7位，如 $1 . 0 0 0 0 0 0 0 \mathsf { E } + 0 0$ ，表示方波周期为 1s。 

# 举例

:SOUR1:FUNC:SQU:PER 1 /*设置 CH1 的方波周期为 1s*/ 

:SOUR1:FUNC:SQU:PER? /*查询 CH1 的方波周期，返回 1.000000E+00*/ 

# :SOURce:HARMonic 命令

# 命令列表：

$\spadesuit$  [:SOURce[<n>]]:HARMonic:AMPL 

$\spadesuit$ [:SOURce[<n>]]:HARMonic:ORDEr 

 [:SOURce[<n>]]:HARMonic:PHASe 

 [:SOURce[<n>]]:HARMonic[:STATe] 

[:SOURce[<n>]]:HARMonic:TYPe 

? [:SOURce[<n>]]:HARMonic:USER 

# [:SOURce[<n>]]:HARMonic:AMPL

# 命令格式

[:SOURce[<n>]]:HARMonic:AMPL <sn>,{<value>|MINimum|MAXimum} 

[:SOURce[<n>]]:HARMonic:AMPL? <sn>[,MINimum|MAXimum] 

# 功能描述

设置指定通道谐波功能中指定次谐波的幅度。 

查询指定通道谐波功能中指定次谐波的幅度。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;sn&gt;</td><td>整型</td><td>2至8</td><td>2</td></tr><tr><td>营养价值&gt;</td><td>实型</td><td>0Vpp至指定通道可达到的幅度上限</td><td>1.264 7Vpp</td></tr></table>

# 说明

省略[:SOURce[<n>]]或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

指定通道可达到的幅度上限受“阻抗”（:OUTPut[<n>]:IMPedance 或:OUTPut[<n>]:LOAD）和“频率 /周期”（[:SOURce[<n>]]:FREQuency[:FIXed]或[:SOURce[<n>]]:PERiod[:FIXed]）设置的限制。 

# 返回格式

以科学计数形式返回谐波幅度，有效位数为 7位，如 1.000000E $+ 0 0$ ，表示谐波幅度为 1Vpp。 

# 举例

:SOUR1:HARM:AMPL 5,1 /*设置 CH1谐波功能中 5次谐波的幅度为 ${ 1 } \mathsf { V } \mathsf { p } \mathsf { p } ^ { \star } /$ 

:SOUR1:HARM:AMPL? 5 /*查询 CH1 谐波功能中 5 次谐波的幅度，返回 1.000000E+00*/ 

# [:SOURce[<n>]]:HARMonic:ORDEr

# 命令格式

[:SOURce[<n>]]:HARMonic:ORDEr {<value $>$ |MINimum|MAXimum} 

[:SOURce[<n>]]:HARMonic:ORDEr? [MINimum|MAXimum] 

# 功能描述

设置指定通道谐波功能中可输出的最高谐波次数。 

查询指定通道谐波功能中可输出的最高谐波次数。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;value&gt;</td><td>整型</td><td>2至8</td><td>2</td></tr></table>

# 说明

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

最高谐波次数的可设置范围受仪器最大输出频率（定义为 $F _ { o u t \operatorname* { m a x } }$ ）和当前的基波频率（定义为 $F _ { f u n d }$ ） 限制，实际范围为 2 至( $F _ { o u t \operatorname* { m a x } } \div F _ { f u n d }$ )且为整数。 

# 返回格式

以科学计数形式返回最高谐波次数，有效位数为 7 位，如 3.000000E+00，表示最高谐波次数为 3。 

# 举例

:SOUR1:HARM:ORDE 3 /*设置 CH1可输出的最高谐波次数为 $3 ^ { \star } /$ 

:SOUR1:HARM:ORDE? /*查询 CH1 可输出的最高谐波次数，返回 $3 . 0 0 0 0 0 0 0 \mathsf { E } + 0 0 ^ { \star } /$ 

# [:SOURce[<n>]]:HARMonic:PHASe

# 命令格式

[:SOURce[<n>]]:HARMonic:PHASe <sn>,{<value>|MINimum|MAXimum} 

[:SOURce[<n>]]:HARMonic:PHASe? <sn>[,MINimum|MAXimum] 

# 功能描述

设置指定通道谐波功能中指定次谐波的相位。 

查询指定通道谐波功能中指定次谐波的相位。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;sn&gt;</td><td>整型</td><td>2至8</td><td>2</td></tr><tr><td>营养价值</td><td>实型</td><td>0°至360°</td><td>0.000°</td></tr></table>

# 说明

省略[:SOURce[<n>]]或[ $\cdot < n > ]$ 时，默认设置 CH1 的相关参数。 

# 返回格式

以科学计数形式返回谐波相位，有效位数为 7位，如 1.000000E+01，表示谐波相位为 $ { 1 0 ^ { \circ } }$ 。 

# 举例

:SOUR1:HARM:PHAS 5,10 /*设置 CH1 谐波功能中 5 次谐波的相位为 $1 0 ^ { \circ \star } /$ 

:SOUR1:HARM:PHAS? 5 /*查询 CH1谐波功能中 5次谐波的相位，返回 $1 . 0 0 0 0 0 0 0 \mathsf { E } { + } 0 1 ^ { \star } /$ 

# [:SOURce[<n>]]:HARMonic[:STATe]

# 命令格式

[:SOURce[<n>]]:HARMonic[:STATe] {ON|1|OFF|0} 

[:SOURce[<n>]]:HARMonic[:STATe]? 

# 功能描述

打开或关闭指定通道的谐波功能。 

查询指定通道谐波功能的开关状态。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 说明

DG2000 可作为一款谐波发生器，可以输出具有指定次数（[:SOURce[<n>]]:HARMonic:ORDEr）、幅度 （[:SOURce[<n>]]:HARMonic:AMPL）和相位（[:SOURce[<n>]]:HARMonic:PHASe）的谐波。 

省略[:SOURce[<n>]]或 $[ < n > ]$ ]时，默认设置 CH1的相关参数。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:SOUR1:HARM ON /*打开 CH1 的谐波功能*/ 

:SOUR1:HARM? /*查询 CH1谐波功能的开关状态，返回 $\mathsf { O N } ^ { \star } /$ 

# [:SOURce[<n>]]:HARMonic:TYPe

# 命令格式

[:SOURce[<n>]]:HARMonic:TYPe {EVEN|ODD|ALL|USER} 

[:SOURce[<n>]]:HARMonic:TYPe? 

# 功能描述

设置指定通道的谐波类型为偶次谐波（EVEN）、奇次谐波（ODD）、顺序谐波（ALL）或自定义谐波（USER）。 查询指定通道的谐波类型。 

# 参数

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{EVEN|ODD|ALL|USER}</td><td>离散型</td><td>EVEN|ODD|ALL|USER</td><td>EVEN</td></tr></table>

# 说明

偶次谐波（EVEN）：仪器输出基波和偶次谐波。 

奇次谐波（ODD）：仪器输出基波和奇次谐波。 

顺序谐波（ALL）：仪器按顺序输出基波和各次谐波。 

自定义谐波（USER）：用户可自定义输出谐波的次数，最高次数为 8。 使用 8位二进制数据分别代表 8次谐波的输出状态，最左侧的位表示基波，固定为 X，不允许修改，后 面的 7位从左到右依次对应 2次谐波到 8次谐波。1 表示打开相应次谐波的输出，0表示关闭相应次谐 波的输出。例如：将 8 位数据设置为 X0010001，表示输出基波和 4次、8次谐波 

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1 的相关参数。 

实际输出的谐波受当前指定的最高谐波次数（[:SOURce[<n>]]:HARMonic:ORDEr）和谐波类型共同限 制。 

# 返回格式

返回 EVEN、ODD、ALL 或 USER。 

# 举例

:SOUR1:HARM:TYP ODD /*设置 CH1的谐波类型为奇次谐波*/ 

:SOUR1:HARM:TYP? /*查询 CH1的谐波类型，返回 $\mathrm { O D D ^ { \star } } /$ 

# [:SOURce[<n>]]:HARMonic:USER

# 命令格式

[:SOURce[<n>]]:HARMonic:USER <user> 

[:SOURce[<n>]]:HARMonic:USER? 

# 功能描述

设置指定通道的自定义谐波输出。 

查询指定通道的自定义谐波输出。 

# 参数

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;user&gt;</td><td>ASCII字符串</td><td>X0000000至X11111111</td><td>X0000000</td></tr></table>

# 说明

在自定义谐波（[:SOURce[<n>]]:HARMonic:TYPe）中，用户可自定义输出谐波的次数，最高次数为 8。 使用 8位二进制数据分别代表 8次谐波的输出状态，最左侧的位表示基波，固定为 X，不允许修改，后 面的 7位从左到右依次对应 2次谐波到 8次谐波。1 表示打开相应次谐波的输出，0表示关闭相应次谐 

波的输出。例如：将 8 位数据设置为 X0010001，表示输出基波和 4次、8次谐波。 

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

# 返回格式

返回 X0000000 至 X11111111 之间的一个字符串，如 X0010001。 

# 举例

:SOUR1:HARM:USER X0010001 /*设置 CH1 的自定义谐波输出基波和 4 次、8 次谐波*/ 

:SOUR1:HARM:USER? /*查询 CH1 的自定义谐波输出，返回 X0010001*/ 

# :SOURce:MARKer 命令

# 命令列表：

$\spadesuit$ [:SOURce[<n>]]:MARKer:FREQuency 

$\spadesuit$  [:SOURce[<n>]]:MARKer[:STATe] 

# [:SOURce[<n>]]:MARKer:FREQuency

# 命令格式

[:SOURce[<n>]]:MARKer:FREQuency {<frequency $>$ |MINimum|MAXimum} 

[:SOURce[<n>]]:MARKer:FREQuency? [MINimum|MAXimum] 

# 功能描述

设置指定通道的标记频率。 

查询指定通道的标记频率。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;frequency&gt;</td><td>实型</td><td>见下文“说明”</td><td>550Hz</td></tr></table>

# 说明

. 对于步进扫描（由起始频率、终止频率和步进数决定的扫频点分别为 f1， $\mathsf { f } _ { 2 }$ ，……，fn， $\mathbf { f } _ { \mathsf { n } + 1 } \bullet \cdots )$ ），若 设置的标记频率为扫频点的值，在扫描开始时，同步信号为 TTL高电平，在标记频率处变为低电平。若 设置的标记频率不等于扫频点的值，同步信号则在距离该频率最近的扫频点处变为低电平。 

省略[:SOURce[ $\angle n > ]$ ]或 $[ < n > ]$ ]时，默认设置 CH1的相关参数。 

参数<frequency $>$ 的可设范围受“起始频率”（[:SOURce[<n>]]:FREQuency:STARt）和“终止频率” （[:SOURce[<n>]]:FREQuency:STOP）限制，必须在起始频率和终止频率之间。 

修改“标记频率”后，信号发生器将重新从指定的“起始频率”开始扫频输出。 

# 返回格式

以科学计数形式返回标记频率，有效位数为 7位，如 $5 . 0 0 0 0 0 0 0 \mathsf { E } + 0 2$ ，表示标记频率为 500Hz。 

# 举例

:SOUR1:MARK:FREQ 500 /*设置 CH1的标记频率为 $5 0 0 \mathsf { H z } ^ { \star } /$ 

:SOUR1:MARK:FREQ? /*查询 CH1 的标记频率，返回 5.000000E+02*/ 

# [:SOURce[<n>]]:MARKer[:STATe]

# 命令格式

[:SOURce[<n>]]:MARKer[:STATe] {ON|1|OFF|0} 

[:SOURce[<n>]]:MARKer[:STATe]? 

# 功能描述

启用或禁用指定通道的频率标记功能。 

查询指定通道频率标记功能的开关状态。 

# 参数

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 说明

后面板上与指定通道对应的 [Sync/Ext Mod/Trig/FSK] 连接器上的同步信号，总是在每次扫描的开 始处由低电平变为高电平。如果您禁用“标记”功能，同步信号将在到达中心频率时变为低电平。如果 您启用“标记”功能，同步信号将在到达指定的标记频率时，变为低电平。 

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:SOUR1:MARK ON /*启用 CH1的频率标记功能*/ 

:SOUR1:MARK? /*查询 CH1的频率标记功能的开关状态，返回 $\mathsf { O N } ^ { \star } /$ 

# :SOURce[:MOD]:AM 命令

# 命令列表：

$\spadesuit$ [:SOURce[<n>]][:MOD]:AM[:DEPTh] 

$\spadesuit$  [:SOURce[<n>]][:MOD]:AM:DSSC 

$\spadesuit$ [:SOURce[<n>]][:MOD]:AM:INTernal:FREQuency 

$\spadesuit$  [:SOURce[<n>]][:MOD]:AM:INTernal:FUNCtion 

$\spadesuit$  [:SOURce[<n>]][:MOD]:AM:SOURce 

[:SOURce[<n>]][:MOD]:AM:STATe 

# [:SOURce[<n>]][:MOD]:AM[:DEPTh]

# 命令格式

[:SOURce[<n>]][:MOD]:AM[:DEPTh] {<depth>|MINimum|MAXimum} 

[:SOURce[<n>]][:MOD]:AM[:DEPTh]? [MINimum|MAXimum] 

# 功能描述

设置指定通道的 AM 调制深度。 

查询指定通道的 AM 调制深度。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;depth&gt;</td><td>实型</td><td>0%至120%</td><td>100%</td></tr></table>

# 说明

省略[:SOURce[<n>]]或 $[ < n > ]$ ]时，默认设置 CH1 的相关参数。 

? 调制深度表示幅度变化的程度，以百分比表示。在调制深度为 $0 \%$ 时，输出幅度为载波幅度的二分之一； 在调制深度为 $100 \%$ 时，输出幅度等于载波幅度；在大于 $100 \%$ 调制时，仪器的输出幅度不会超过 10Vpp （负载为 50Ω）。 

选择外部调制源（[:SOURce[<n>]][:MOD]:AM:SOURce）时，仪器的输出幅度受后面板相应通道的 [Sync/Ext Mod/Trig/FSK] 连接器上的 $\pm 5 \mathsf { V }$ 信号电平控制，例如：将调制深度设置为 $100 \%$ ，则在 调制信号为 $+ 5 V$ 时输出为最大振幅，在调制信号为-5V 时输出为最小振幅。 

# 返回格式

以科学计数形式返回 AM 调制深度，有效位数为 7 位，如 5.000000E+01，表示 AM 调制深度为 $50 \%$ 。 

# 举例

:SOUR1:AM 50 /*设置 CH1的 AM 调制深度为 $5 0 \% ^ { \star } /$ 

:SOUR1:AM? /*查询 CH1 的 AM 调制深度，返回 5.000000E+01*/ 

# [:SOURce[<n>]][:MOD]:AM:DSSC

# 命令格式

[:SOURce[<n>]][:MOD]:AM:DSSC {ON|1|OFF|0} 

[:SOURce[<n>]][:MOD]:AM:DSSC? 

# 功能描述

打开或关闭指定通道的 AM 载波抑制功能。 

查询指定通道 AM 载波抑制功能的开关状态。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 说明

. DG2000 支持两种类型的幅度调制：常规的幅度调制和双边带抑制载波（Double Sideband Suppressed Carrier, DSB-SC）的幅度调制。在常规的幅度调制中，已调波中含有载波分量。由于载波分量不携带信 息，因此，调制效率较低。为了提高调制效率，在常规的幅度调制的基础上将载波分量抑制。此时，已 调波全部携带信息。这种方式称为抑制载波双边带调制。 

省略[:SOURce[ $\angle n > ]$ ]或 $[ < n > ]$ ]时，默认设置 CH1 的相关参数。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:SOUR1:AM:DSSC ON /*打开 CH1 的 AM 载波抑制功能*/ 

:SOUR1:AM:DSSC? /*查询 CH1的 AM 载波抑制功能的开关状态，返回 $\mathsf { O N } ^ { \star } /$ 

# [:SOURce[<n>]][:MOD]:AM:INTernal:FREQuency

# 命令格式

[:SOURce[<n>]][:MOD]:AM:INTernal:FREQuency {<frequency $>$ |MINimum|MAXimum} 

[:SOURce[<n>]][:MOD]:AM:INTernal:FREQuency? [MINimum|MAXimum] 

# 功能描述

设置指定通道 AM 调制波的频率。 

查询指定通道 AM 调制波的频率。 

# 参数

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;frequency&gt;</td><td>实型</td><td>2mHz至1MHz</td><td>100Hz</td></tr></table>

# 说明

该命令仅适用于内部调制源（[:SOURce[<n>]][:MOD]:AM:SOURce）。 

省略[:SOURce[<n>]]或[<n>]时，默认设置 CH1 的相关参数。 

# 返回格式

以科学计数形式返回AM调制波的频率，有效位数为7位，如1.500000E $+ 0 2$ ，表示AM调制波的频率为150Hz。 

# 举例

:SOUR1:AM:INT:FREQ 150 /*设置 CH1的 AM 调制波的频率为 $1 5 0 \mathsf { H z } ^ { \star } /$ 

:SOUR1:AM:INT:FREQ? /*查询 CH1 的 AM 调制波的频率，返回 1.500000E+02*/ 

# [:SOURce[<n>]][:MOD]:AM:INTernal:FUNCtion

# 命令格式

[:SOURce[<n>]][:MOD]:AM:INTernal:FUNCtion {SINusoid|SQUare|TRIangle|RAMP|NRAMp|NOISe|USER} 

[:SOURce[<n>]][:MOD]:AM:INTernal:FUNCtion? 

# 功能描述

设置指定通道的 AM 调制波形。 

查询指定通道的 AM 调制波形。 

# 参数

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{SINusoid|SQUare|TRIangle|RAMP|NRAMp|NOISE|USER}</td><td>离散型</td><td>SINusoid|SQUare|TRIangle|RA MP|NRAMp|NOISE|USER</td><td>SINusoid</td></tr></table>

# 说明

该命令仅适用于内部调制源。 

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1 的相关参数。 

SQUare：占空比为 $50 \%$ ；TRIangle：对称性为 $50 \%$ ；RAMP：对称性为 $100 \%$ ；NRAMp：对称性为 $0 \%$ ； USER：指定通道选择的任意波。 

# 返回格式

返回 SIN、SQU、TRI、RAMP、NRAM、NOIS 或 USER。 

# 举例

:SOUR1:AM:INT:FUNC SQU /*设置 CH1的 AM 调制波形为方波*/ 

:SOUR1:AM:INT:FUNC? 

/*查询 CH1的 AM 调制波形，返回 $\mathsf { S O U } ^ { \star } /$ 

# [:SOURce[<n>]][:MOD]:AM:SOURce

# 命令格式

[:SOURce[<n>]][:MOD]:AM:SOURce {INTernal|EXTernal} 

[:SOURce[<n>]][:MOD]:AM:SOURce? 

# 功能描述

设置指定通道的 AM 调制信号源为内部（INTernal）或外部（EXTernal）调制源。 

查询指定通道的 AM 调制信号源类型。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{INTERNAL|EXTERNAL}</td><td>离散型</td><td>INTERNAL|EXTERNAL</td><td>INTERNAL</td></tr></table>

# 说明

DG2000可以接收来自内部或外部调制源的调制波形。 

选择内部调制源后，可选择 SINusoid、SQUare、TRIangle、RAMP、NRAMp、NOISe 或 USER 作为调 制波形，默认为 SINusoid。NOISe 可以作为调制波，但不能作为载波。 

? 选择外部调制源后，信号发生器接收从后面板相应通道的 [Sync/Ext Mod/Trig/FSK] 连接器输入的 外部调制信号。此时，已调信号的幅度受该连接器上的 $\pm 5 \mathsf { V }$ 信号电平控制。例如：调制深度为 $100 \%$ 时， 则在调制信号为 $+ 5 V$ 时输出为最大幅度，在调制信号为-5V 时输出为最小幅度。 

省略[:SOURce[ $< n > ] ]$ 或 $\cdot < n > ]$ 时，默认设置 CH1的相关参数。 

# 返回格式

返回 INT 或 EXT。 

# 举例

:SOUR1:AM:SOUR EXT /*设置 CH1的 AM 调制信号源为外部调制源*/ 

:SOUR1:AM:SOUR? /*查询 CH1 的 AM 调制信号源类型，返回 EXT*/ 

# [:SOURce[<n>]][:MOD]:AM:STATe

# 命令格式

[:SOURce[<n>]][:MOD]:AM:STATe {ON|1|OFF|0} 

[:SOURce[<n>]][:MOD]:AM:STATe? 

# 功能描述

打开或关闭指定通道的 AM 调制功能。 

查询指定通道 AM 调制功能的开关状态。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 说明

AM：幅度调制（Amplitude Modulation），载波的幅度随着调制波瞬时电压的变化而变化。 

AM 载波波形可以是正弦波、方波、锯齿波或任意波，默认为正弦波。脉冲、噪声和直流不能作为载波。 载波波形的多个参数（如频率、幅度、偏移和起始相位等）的不同设置都会影响输出的 AM 已调制波形。 

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

若当前已打开扫频功能（[:SOURce[<n>]]:SWEep:STATe）或脉冲串功能 

（[:SOURce[<n>]]:BURSt[:STATe]），则打开调制功能时，扫频功能或脉冲串功能将自动关闭。 

若当前已打开谐波功能（[:SOURce[<n>]]:HARMonic[:STATe]），则不能打开调制功能，即不能调制谐 波。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:SOUR1:AM:STAT ON /*打开 CH1 的 AM 调制功能*/ 

:SOUR1:AM:STAT? /*查询 CH1的 AM 调制功能的开关状态，返回 $\mathsf { O N } ^ { \star } /$ 

# :SOURce[:MOD]:ASKey 命令

# 命令列表：

$\spadesuit$ [:SOURce[<n>]][:MOD]:ASKey:AMPLitude 

 [:SOURce[<n>]][:MOD]:ASKey:INTernal[:RATE] 

$\spadesuit$ [:SOURce[<n>]][:MOD]:ASKey:POLarity 

 [:SOURce[<n>]][:MOD]:ASKey:SOURce 

$\spadesuit$  [:SOURce[<n>]][:MOD]:ASKey:STATe 

# [:SOURce[<n>]][:MOD]:ASKey:AMPLitude

# 命令格式

[:SOURce[ $< \mathsf { n } >$ ]][:MOD]:ASKey:AMPLitude {<amplitude $>$ |MINimum|MAXimum} 

[:SOURce[<n>]][:MOD]:ASKey:AMPLitude? [MINimum|MAXimum] 

# 功能描述

设置指定通道的 ASK 调制幅度。 

查询指定通道的 ASK 调制幅度。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;amplitude&gt;</td><td>实型</td><td>0Vpp至10Vpp（高阻）</td><td>2Vpp</td></tr></table>

# 说明

 ASK 调制时，信号发生器在两个预设的幅度（载波幅度和调制幅度）间移动其输出幅度。 

省略[:SOURce[<n>]]或 $[ < n > ]$ 时，默认设置 CH1 的相关参数。 

# 返回格式

以科学计数形式返回 ASK 调制幅度，有效位数为 7 位，如 $1 . 0 0 0 0 0 0 0 \mathsf { E } + 0 0$ ，表示 ASK 调制幅度为 1Vpp。 

# 举例

:SOUR1:ASK:AMPL 1 /*设置 CH1 的 ASK 调制幅度为 ${ 1 } \mathsf { V p p } ^ { \star } /$ 

:SOUR1:ASK:AMPL? /*查询 CH1 的 ASK 调制幅度，返回 1.000000E+00*/ 

# [:SOURce[<n>]][:MOD]:ASKey:INTernal[:RATE]

# 命令格式

[:SOURce[<n>]][:MOD]:ASKey:INTernal[:RATE] {<frequency $>$ |MINimum|MAXimum} 

[:SOURce[<n>]][:MOD]:ASKey:INTernal[:RATE]? [MINimum|MAXimum] 

# 功能描述

设置指定通道的 ASK 调制速率。 

查询指定通道的 ASK 调制速率。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;frequency&gt;</td><td>实型</td><td>2mHz至1MHz</td><td>100Hz</td></tr></table>

# 说明

该命令仅适用于内部调制源，ASK 调制速率是指输出幅度在载波幅度和调制幅度之间“移动”的频率 

省略[:SOURce[<n>]]或 $[ < n > ]$ ]时，默认设置 CH1的相关参数。 

# 返回格式

以科学计数形式返回 ASK 调制速率，有效位数为 7 位，如 1.500000E+02，表示 ASK 调制速率为 150Hz。 

# 举例

:SOUR1:ASK:INT 150 /*设置 CH1 的 ASK 调制速率为 $1 5 0 \mathsf { H z } ^ { \star } /$ 

:SOUR1:ASK:INT? /*查询 CH1 的 ASK 调制速率，返回 1.500000E+02*/ 

# [:SOURce[<n>]][:MOD]:ASKey:POLarity

# 命令格式

[:SOURce[<n>]][:MOD]:ASKey:POLarity {POSitive|NEGative} 

[:SOURce[<n>]][:MOD]:ASKey:POLarity? 

# 功能描述

设置指定通道的 ASK 调制极性为正极性（POSitive）或负极性（NEGative）。 

查询指定通道的 ASK 调制极性。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{POSitive|NEGative}</td><td>离散型</td><td>POSitive|NEGative</td><td>POSitive</td></tr></table>

# 说明

省略[:SOURce[<n>]]或 $[ < n > ]$ ]时，默认设置 CH1的相关参数。 

内部调制（[:SOURce[<n>]][:MOD]:ASKey:SOURce）时，若设定极性为“正极性”，则在调制波为逻 辑低电平时输出载波幅度和调制幅度（[:SOURce[<n>]][:MOD]:ASKey:AMPLitude）之间较小的幅度； 在调制波为逻辑高电平时输出载波幅度和调制幅度之间较大的幅度。极性为“负极性”时，情况相反。 

外部调制（[:SOURce[<n>]][:MOD]:ASKey:SOURce）时，若设定极性为“正极性”，则在外部输入信 号为逻辑低电平时输出载波幅度和调制幅度（[:SOURce[<n>]][:MOD]:ASKey:AMPLitude）之间较小的 幅度；在外部输入信号为逻辑高电平时输出载波幅度和调制幅度之间较大的幅度。极性为“负极性”时， 情况相反。 

# 返回格式

返回 POS 或 NEG。 

# 举例

:SOUR1:ASK:POL POS /*设置 CH1 的 ASK 调制极性为正极性*/ 

:SOUR1:ASK:POL? /*查询 CH1的 ASK 调制极性，返回 $\mathsf { P O S } ^ { \star } /$ 

# [:SOURce[<n>]][:MOD]:ASKey:SOURce

# 命令格式

[:SOURce[<n>]][:MOD]:ASKey:SOURce {INTernal|EXTernal} 

[:SOURce[<n>]][:MOD]:ASKey:SOURce? 

# 功能描述

设置指定通道的 ASK 调制信号源为内部（INTernal）或外部（EXTernal）调制源。 

查询指定通道的 ASK 调制信号源类型。 

# 参数

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{INTERNAL|EXTERNAL}</td><td>离散型</td><td>INTERNAL|EXTERNAL</td><td>INTERNAL</td></tr></table>

# 说明

DG2000可以接收来自内部或外部调制源的调制波形。 

选择内部调制源，即选择占空比为 $50 \%$ 的方波为调制波形。此时，输出幅度在载波幅度和调制幅度 （[:SOURce[<n>]][:MOD]:ASKey:AMPLitude）之间移动的频率由调制速率决定。 

选择外部调制源时，信号发生器接收从后面板相应通道的 [Sync/Ext Mod/Trig/FSK] 连接器输入的 外调制信号。通过该连接器从外部控制 ASK 调制和控制 AM/FM/PM 调制时不同。在控制 ASK 调制时， 您可以设置极性（[:SOURce[<n>]][:MOD]:ASKey:POLarity） 

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1 的相关参数。 

# 返回格式

返回 INT 或 EXT。 

# 举例

:SOUR1:ASK:SOUR EXT /*设置 CH1 的 ASK 调制信号源为外部调制源*/ 

:SOUR1:ASK:SOUR? /*查询 CH1 的 ASK 调制信号源类型，返回 EXT*/ 

# [:SOURce[<n>]][:MOD]:ASKey:STATe

# 命令格式

[:SOURce[<n>]][:MOD]:ASKey:STATe { ON|1|OFF|0} 

[:SOURce[<n>]][:MOD]:ASKey:STATe? 

# 功能描述

打开或关闭指定通道的 ASK 调制功能。 

查询指定通道 ASK 调制功能的开关状态。 

# 参数

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 说明

ASK：幅移键控（Amplitude Shift Keying）调制，信号发生器在两个预设的幅度（载波幅度和调制幅度） 

间移动其输出幅度。 

. ASK 载波波形可以是正弦波、方波、锯齿波或任意波，默认为正弦波。脉冲、噪声和直流不能作为载波。 载波波形的多个参数（如频率、幅度、偏移和起始相位等）的不同设置都会影响输出的 ASK 已调制波 形。 

省略[:SOURce[<n>]]或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

若当前已打开扫频功能（[:SOURce[<n>]]:SWEep:STATe）或脉冲串功能 （[:SOURce[<n>]]:BURSt[:STATe]），则打开调制功能时，扫频功能或脉冲串功能将自动关闭。 

若当前已打开谐波功能（[:SOURce[<n>]]:HARMonic[:STATe]），则不能打开调制功能，即不能调制谐 波。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:SOUR1:ASK:STAT ON /*打开 CH1 的 ASK 调制功能*/ 

:SOUR1:ASK:STAT? /*查询 CH1的 ASK 调制功能的开关状态，返回 $\mathsf { O N } ^ { \star } /$ 

# :SOURce[:MOD]:FM 命令

# 命令列表：

$\spadesuit$ [:SOURce[<n>]][:MOD]:FM[:DEViation] 

$\spadesuit$ [:SOURce[<n>]][:MOD]:FM:INTernal:FREQuency 

$\spadesuit$ [:SOURce[<n>]][:MOD]:FM:INTernal:FUNCtion 

$\spadesuit$ [:SOURce[<n>]][:MOD]:FM:SOURce 

[:SOURce[<n>]][:MOD]:FM:STATe 

# [:SOURce[<n>]][:MOD]:FM[:DEViation]

# 命令格式

[:SOURce[<n>]][:MOD]:FM[:DEViation] {<deviation $>$ |MINimum|MAXimum} 

[:SOURce[<n>]][:MOD]:FM[:DEViation]? [MINimum|MAXimum] 

# 功能描述

设置指定通道的 FM 频率偏移。 

查询指定通道的 FM 频率偏移。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;deviation&gt;</td><td>实型</td><td>见下文“说明”</td><td>1kHz</td></tr></table>

# 说明

省略[:SOURce[<n>]]或[<n>]时，默认设置 CH1 的相关参数。 

频率偏移是指调制波形的频率（[:SOURce[<n>]][:MOD]:FM:INTernal:FREQuency）相对于载波频率的 偏差。频率偏移必须小于或等于载波频率，且频率偏移与载波频率之和必须小于或等于当前载波频率上 限与 1kHz 之和。 

. 若当前载波为正弦波，则当频率偏移与载波频率之和大于当前载波的频率上限时，载波幅度被限制在 2Vpp。 

选择外部调制源（[:SOURce[<n>]][:MOD]:FM:SOURce）时，频率偏移受后面板相应通道的 [Sync/Ext Mod/Trig/FSK] 连接器上的 $\pm 5 \mathsf { V }$ 信号电平控制。正信号电平对应频率增加，负信号电平对应于频率 

降低，较低的电平产生较少的偏移。例如：将频率偏移设置为 1kHz，则 $+ 5 V$ 信号电平对应于频率增加 1kHz，-5V 信号电平对应于频率降低 1kHz。 

# 返回格式

以科学计数形式返回频率偏移，有效位数为 7位，如 1.000000E $+ 0 2$ ，表示频率偏移为 100Hz。 

# 举例

:SOUR1:FM 100 /*设置 CH1的 FM 频率偏移为 $1 0 0 \mathsf { H z } ^ { \star } /$ 

:SOUR1:FM? /*查询 CH1 的 FM 频率偏移，返回 1.000000E+02*/ 

# [:SOURce[<n>]][:MOD]:FM:INTernal:FREQuency

# 命令格式

[:SOURce[<n>]][:MOD]:FM:INTernal:FREQuency {<frequency>|MINimum|MAXimum} 

[:SOURce[<n>]][:MOD]:FM:INTernal:FREQuency? [MINimum|MAXimum] 

# 功能描述

设置指定通道 FM 调制波的频率。 

查询指定通道 FM 调制波的频率。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;frequency&gt;</td><td>实型</td><td>2mHz至1MHz</td><td>100Hz</td></tr></table>

# 说明

该命令仅适用于内部调制源（[:SOURce[<n>]][:MOD]:FM:SOURce）。 

省略[:SOURce[<n>]]或[ $\cdot < n > ]$ 时，默认设置 CH1 的相关参数。 

# 返回格式

以科学计数形式返回FM调制波的频率，有效位数为7位，如1.500000E $+ 0 2$ ，表示FM调制波的频率为150Hz。 

# 举例

:SOUR1:FM:INT:FREQ 150 /*设置 CH1的 FM 调制波的频率为 $1 5 0 \mathsf { H z } ^ { \star } /$ 

:SOUR1:FM:INT:FREQ? /*查询 CH1的 FM 调制波的频率，返回 $1 . 5 0 0 0 0 0 0 \mathsf { E } { + } 0 2 ^ { \star } /$ 

# [:SOURce[<n>]][:MOD]:FM:INTernal:FUNCtion

# 命令格式

[:SOURce[<n>]][:MOD]:FM:INTernal:FUNCtion {SINusoid|SQUare|TRIangle|RAMP|NRAMp|NOISe|USER} [:SOURce[<n>]][:MOD]:FM:INTernal:FUNCtion? 

# 功能描述

设置指定通道的 FM 调制波形。 

查询指定通道的 FM 调制波形。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{SINusoid|SQUare|TRIangle|RAMP|NRAMp|NOISE|USER}</td><td>离散型</td><td>SINusoid|SQUare|TRIangle|RAMP|NRAMp|NOISE|USER</td><td>SINusoid</td></tr></table>

# 说明

该命令仅适用于内部调制源（[:SOURce[<n>]][:MOD]:FM:SOURce）。 

省略[:SOURce[<n>]]或 $[ < n > ]$ ]时，默认设置 CH1 的相关参数。 

SQUare：占空比为 $50 \%$ ；TRIangle：对称性为 $50 \%$ ；RAMP：对称性为 $100 \%$ ；NRAMp：对称性为 $0 \%$ USER：指定通道选择的任意波。 

# 返回格式

返回 SIN、SQU、TRI、RAMP、NRAM、NOIS 或 USER。 

# 举例

:SOUR1:FM:INT:FUNC SQU /*设置 CH1的 FM 调制波形为方波*/ 

:SOUR1:FM:INT:FUNC? /*查询 CH1的 FM 调制波形，返回 $\mathsf { S O U } ^ { \star } /$ 

# [:SOURce[<n>]][:MOD]:FM:SOURce

# 命令格式

[:SOURce[<n>]][:MOD]:FM:SOURce {INTernal|EXTernal} 

[:SOURce[<n>]][:MOD]:FM:SOURce? 

# 功能描述

设置指定通道的 FM 调制信号源为内部（INTernal）或外部（EXTernal）调制源。 

查询指定通道的 FM 调制信号源类型。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{INTERNAL|EXTERNAL}</td><td>离散型</td><td>INTERNAL|EXTERNAL</td><td>INTERNAL</td></tr></table>

# 说明

DG2000可以接收来自内部或外部调制源的调制波形。 

选择内部调制源后，可选择 SINusoid、SQUare、TRIangle、RAMP、NRAMp、NOISe 或 USER 作为调 制波形，默认为 SINusoid。NOISe 可以作为调制波，但不能作为载波。 

. 选择外部调制源后，信号发生器接收从后面板相应通道的 [Sync/Ext Mod/Trig/FSK] 连接器输入的 外部调制信号。此时，已调信号的频率偏移由该连接器上的 $\pm 5 \mathsf { V }$ 信号电平控制。例如：将频率偏移设置 为 1kHz，则 $+ 5 V$ 信号电平对应于频率增加 1kHz，-5V 信号电平对应于频率降低 1kHz。 

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1 的相关参数。 

# 返回格式

返回 INT 或 EXT。 

# 举例

:SOUR1:FM:SOUR EXT /*设置 CH1的 FM 调制信号源为外部调制源*/ 

:SOUR1:FM:SOUR? /*查询 CH1的 FM 调制信号源类型，返回 EXT*/ 

# [:SOURce[<n>]][:MOD]:FM:STATe

# 命令格式

[:SOURce[<n>]][:MOD]:FM:STATe {ON|1|OFF|0} 

[:SOURce[<n>]][:MOD]:FM:STATe? 

# 功能描述

打开或关闭指定通道的 FM 调制功能。 

查询指定通道 FM 调制功能的开关状态。 

# 参数

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 说明

. FM：频率调制（Frequency Modulation），载波的频率随调制波的瞬时电压的变化而变化。 

FM 载波波形可以是正弦波、方波、锯齿波或任意波，默认为正弦波。脉冲、噪声和直流不能作为载波。 载波波形的多个参数（如频率、幅度、偏移和起始相位等）的不同设置都会影响输出的 FM 已调制波形。 

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

若当前已打开扫频功能（[:SOURce[<n>]]:SWEep:STATe）或脉冲串功能 （[:SOURce[<n>]]:BURSt[:STATe]），则打开调制功能时，扫频功能或脉冲串功能将自动关闭。 

若当前已打开谐波功能（[:SOURce[<n>]]:HARMonic[:STATe]），则不能打开调制功能，即不能调制谐 波。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:SOUR1:FM:STAT ON /*打开 CH1 的 FM 调制功能*/ 

:SOUR1:FM:STAT? /*查询 CH1的 FM 调制功能的开关状态，返回 $\mathsf { O N } ^ { \star } /$ 

# :SOURce[:MOD]:FSKey 命令

# 命令列表：

$\spadesuit$  [:SOURce[<n>]][:MOD]:FSKey[:FREQuency] 

[:SOURce[<n>]][:MOD]:FSKey:INTernal:RATE 

$\spadesuit$ [:SOURce[<n>]][:MOD]:FSKey:POLarity 

 [:SOURce[<n>]][:MOD]:FSKey:SOURce 

[:SOURce[<n>]][:MOD]:FSKey:STATe 

# [:SOURce[<n>]][:MOD]:FSKey[:FREQuency]

# 命令格式

[:SOURce[<n>]][:MOD]:FSKey[:FREQuency] {<frequency $>$ |MINimum|MAXimum} 

[:SOURce[<n>]][:MOD]:FSKey[:FREQuency]? [MINimum|MAXimum] 

# 功能描述

设置指定通道的 FSK 跳跃频率。 

查询指定通道的 FSK 跳跃频率。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;frequency&gt;</td><td>实型</td><td>指定通道的频率范围</td><td>10kHz</td></tr></table>

# 说明

 FSK 调制时，信号发生器在两个预设频率（载波频率和跳跃频率）间“移动”其输出频率。 

省略[:SOURce[ $< n > ] ]$ 或 $\cdot < n > ]$ 时，默认设置 CH1的相关参数。 

# 返回格式

以科学计数形式返回 FSK 跳跃频率，有效位数为 7 位，如 5.000000E+03，表示 FSK 调制幅度为 5kHz。 

# 举例

:SOUR1:FSK 5000 /*设置 CH1 的 FSK 跳跃频率为 5kHz*/ 

:SOUR1:FSK? /*查询 CH1 的 FSK 跳跃频率，返回 5.000000E+03*/ 

# [:SOURce[<n>]][:MOD]:FSKey:INTernal:RATE

# 命令格式

[:SOURce[<n>]][:MOD]:FSKey:INTernal:RATE {<rate>|MINimum|MAXimum} 

[:SOURce[<n>]][:MOD]:FSKey:INTernal:RATE? [MINimum|MAXimum] 

# 功能描述

设置指定通道的 FSK 调制速率。 

查询指定通道的 FSK 调制速率。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>率达</td><td>实型</td><td>2mHz至1MHz</td><td>100Hz</td></tr></table>

# 说明

该命令仅适用于内部调制源（[:SOURce[<n>]][:MOD]:FSKey:SOURce），FSK 调制速率是指输出频率在 载波频率和跳跃频率（[:SOURce[<n>]][:MOD]:FSKey[:FREQuency]）之间“移动”的频率。 

省略[:SOURce[ $< n > ]$ ]或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

# 返回格式

以科学计数形式返回 FSK 调制速率，有效位数为 7 位，如 $1 . 5 0 0 0 0 0 0 \mathsf { E } + 0 2$ ，表示 FSK 调制速率为 150Hz。 

# 举例

:SOUR1:FSK:INT:RATE 150 /*设置 CH1 的 FSK 调制速率为 $1 5 0 \mathsf { H z } ^ { \star } /$ 

:SOUR1:FSK:INT:RATE? /*查询 CH1 的 FSK 调制速率，返回 1.500000E+02*/ 

# [:SOURce[<n>]][:MOD]:FSKey:POLarity

# 命令格式

[:SOURce[<n>]][:MOD]:FSKey:POLarity {POSitive|NEGative} 

[:SOURce[<n>]][:MOD]:FSKey:POLarity? 

# 功能描述

设置指定通道的 FSK 调制极性为正极性（POSitive）或负极性（NEGative）。 

查询指定通道的 FSK 调制极性。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{POSitive|NEGative}</td><td>离散型</td><td>POSitive|NEGative</td><td>POSitive</td></tr></table>

# 说明

省略[:SOURce[ $\cdot < n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

内部调制（[:SOURce[<n>]][:MOD]:FSKey:SOURce）时，若设定极性为“正极性”，则在调制波幅度为 逻辑低电平时输出载波频率；在调制波幅度为逻辑高电平时输出跳跃频率 （[:SOURce[<n>]][:MOD]:FSKey[:FREQuency]）。极性为“负极性”时，情况相反。 

外部调制（[:SOURce[<n>]][:MOD]:FSKey:SOURce）时，若设定极性为“正极性”，则在外部输入信号 为逻辑低电平时输出载波频率；在外部输入信号为逻辑高电平时输出跳跃频率 （[:SOURce[<n>]][:MOD]:FSKey[:FREQuency]）。极性为“负极性”时，情况相反。 

# 返回格式

返回 POS 和 NEG。 

# 举例

:SOUR1:FSK:POL POS /*设置 CH1的 FSK 调制极性为正极性*/ 

:SOUR1:FSK:POL? /*查询 CH1 的 FSK 调制极性，返回 POS*/ 

# [:SOURce[<n>]][:MOD]:FSKey:SOURce

# 命令格式

[:SOURce[<n>]][:MOD]:FSKey:SOURce {INTernal|EXTernal} 

[:SOURce[<n>]][:MOD]:FSKey:SOURce? 

# 功能描述

设置指定通道的 FSK 调制信号源为内部（INTernal）或外部（EXTernal）调制源。 查询指定通道的 FSK 调制信号源类型。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{INTERNAL|EXTernal}</td><td>离散型</td><td>INTERNAL|EXTernal</td><td>INTERNAL</td></tr></table>

# 说明

DG2000可以接收来自内部或外部调制源的调制波形。 

选择内部调制源，即选择占空比为 $50 \%$ 的方波。此时，输出频率在载波频率和跳跃频率 （[:SOURce[<n>]][:MOD]:FSKey[:FREQuency]）之间“移动”的频率由调制速率 （[:SOURce[<n>]][:MOD]:FSKey:INTernal:RATE）决定。 

选择外部调制源时，信号发生器接收从后面板相应通道的 [Sync/Ext Mod/Trig/FSK] 连接器输入的 外调制信号。通过该连接器从外部控制 FSK 调制和控制 AM/FM/PM 调制时不同。在控制 FSK 调制时， 您可以设置极性（[:SOURce[<n>]][:MOD]:FSKey:POLarity）。 

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1 的相关参数。 

# 返回格式

返回 INT 或 EXT。 

# 举例

:SOUR1:FSK:SOUR EXT /*设置 CH1 的 FSK 调制信号源为外部调制源*/ 

:SOUR1:FSK:SOUR? /*查询 CH1 的 FSK 调制信号源类型，返回 EXT*/ 

# [:SOURce[<n>]][:MOD]:FSKey:STATe

# 命令格式

[:SOURce[<n>]][:MOD]:FSKey:STATe {ON|1|OFF|0} 

[:SOURce[<n>]][:MOD]:FSKey:STATe? 

# 功能描述

打开或关闭指定通道的 FSK 调制功能。 

查询指定通道 FSK 调制功能的开关状态。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 说明

FSK：频移键控（Frequency Shift Keying）调制，信号发生器在两个预设频率（载波频率和跳跃频率） 间“移动”其输出频率。 

FSK 载波波形可以是正弦波、方波、锯齿波或任意波，默认为正弦波。脉冲、噪声和直流不能作为载波。 载波波形的多个参数（如频率、幅度、偏移和起始相位等）的不同设置都会影响输出的 FSK 已调制波形。 

省略[:SOURce[ $< n > ]$ ]]或 $\cdot < n > .$ ]时，默认设置 CH1的相关参数。 

若当前已打开扫频功能（[:SOURce[<n>]]:SWEep:STATe）或脉冲串功能 

（[:SOURce[<n>]]:BURSt[:STATe]），则打开调制功能时，扫频功能或脉冲串功能将自动关闭。 

若当前已打开谐波功能（[:SOURce[<n>]]:HARMonic[:STATe]），则不能打开调制功能，即不能调制谐 波。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:SOUR1:FSK:STAT ON /*打开 CH1 的 FSK 调制功能*/ 

:SOUR1:FSK:STAT? /*查询 CH1的 FSK 调制功能的开关状态，返回 $\mathsf { O N } ^ { \star } /$ 

# :SOURce[:MOD]:PM 命令

# 命令列表：

$\spadesuit$ [:SOURce[<n>]][:MOD]:PM[:DEViation] 

 [:SOURce[<n>]][:MOD]:PM:INTernal:FREQuency 

$\spadesuit$  [:SOURce[<n>]][:MOD]:PM:INTernal:FUNCtion 

 [:SOURce[<n>]][:MOD]:PM:SOURce 

 [:SOURce[<n>]][:MOD]:PM:STATe 

# [:SOURce[<n>]][:MOD]:PM[:DEViation]

# 命令格式

[:SOURce[<n>]][:MOD]:PM[:DEViation] {<deviation $>$ |MINimum|MAXimum} 

[:SOURce[<n>]][:MOD]:PM[:DEViation]? [MINimum|MAXimum] 

# 功能描述

设置指定通道的 PM 相位偏差。 

查询指定通道的 PM 相位偏差。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;deviation&gt;</td><td>实型</td><td>0°至360°</td><td>90°</td></tr></table>

# 说明

省略[:SOURce[ $\angle n > ]$ ]或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

相位偏差指调制波形的相位相对于载波相位的变化。 

选择外部调制源（[:SOURce[<n>]][:MOD]:PM:SOURce）时，相位偏差受后面板相应的 [Sync/Ext Mod/Trig/FSK] 连接器上的 $\pm 5 \mathsf { V }$ 信号电平控制。例如，将相位偏差设置为 $ 1 8 0 ^ { \circ }$ ，则 $+ 5 V$ 信号电平对 应于相位改变 $1 8 0 ^ { \circ }$ 。较低的外部信号电平产生较少的偏差。 

# 返回格式

以科学计数形式返回 PM 相位偏差，有效位数为 7 位，如 5.000000E $+ 0 1$ ，表示 PM 相位偏差为 $5 0 ^ { \circ }$ 。 

# 举例

:SOUR1:PM 50 /*设置 CH1的 PM 相位偏差为 $5 0 ^ { \circ \star } /$ 

:SOUR1:PM? /*查询 CH1的 PM 相位偏差，返回 $5 . 0 0 0 0 0 0 0 \mathsf { E } { + } 0 1 ^ { \star } /$ 

# [:SOURce[<n>]][:MOD]:PM:INTernal:FREQuency

# 命令格式

[:SOURce[<n>]][:MOD]:PM:INTernal:FREQuency {<frequency $>$ |MINimum|MAXimum} 

[:SOURce[<n>]][:MOD]:PM:INTernal:FREQuency? [MINimum|MAXimum] 

# 功能描述

设置指定通道 PM 调制波的频率。 

查询指定通道 PM 调制波的频率。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;frequency&gt;</td><td>实型</td><td>2mHz至1MHz</td><td>100Hz</td></tr></table>

# 说明

该命令仅适用于内部调制源（[:SOURce[<n>]][:MOD]:PM:SOURce）。 

省略[:SOURce[<n>]]或[<n>]时，默认设置 CH1 的相关参数。 

# 返回格式

以科学计数形式返回PM调制波的频率，有效位数为7位，如1.500000E $^ { + 0 2 }$ ，表示PM调制波的频率为150Hz。 

# 举例

:SOUR1:PM:INT:FREQ 150 /*设置 CH1的 PM 调制波的频率为 $1 5 0 \mathsf { H z } ^ { \star } /$ 

:SOUR1:PM:INT:FREQ? /*查询 CH1 的 PM 调制波的频率，返回 1.500000E+02*/ 

# [:SOURce[<n>]][:MOD]:PM:INTernal:FUNCtion

# 命令格式

[:SOURce[<n>]][:MOD]:PM:INTernal:FUNCtion {SINusoid|SQUare|TRIangle|RAMP|NRAMp|NOISe|USER} 

[:SOURce[<n>]][:MOD]:PM:INTernal:FUNCtion? 

# 功能描述

设置指定通道的 PM 调制波形。 

查询指定通道的 PM 调制波形。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{SINusoid|SQUare|TRIangle|RAMP|NRAMp|NOISE|USER}</td><td>离散型</td><td>SINusoid|SQUare|TRIangle|RAMP|NRAMp|NOISE|USER</td><td>SINusoid</td></tr></table>

# 说明

该命令仅适用于内部调制源（[:SOURce[<n>]][:MOD]:PM:SOURce）。 

省略[:SOURce[<n>]]或 $[ < n > ]$ ]时，默认设置 CH1的相关参数。 

SQUare：占空比为 $50 \%$ ；TRIangle：对称性为 $50 \%$ ；RAMP：对称性为 $100 \%$ ；NRAMp：对称性为 $0 \%$ USER：指定通道选择的任意波。 

# 返回格式

返回 SIN、SQU、TRI、RAMP、NRAM、NOIS 或 USER。 

# 举例

:SOUR1:PM:INT:FUNC SQU /*设置 CH1的 PM 调制波形为方波*/ 

:SOUR1:PM:INT:FUNC? /*查询 CH1的 PM 调制波形，返回 $\mathsf { S O U } ^ { \star } /$ 

# [:SOURce[<n>]][:MOD]:PM:SOURce

# 命令格式

[:SOURce[<n>]][:MOD]:PM:SOURce {INTernal|EXTernal} 

[:SOURce[<n>]][:MOD]:PM:SOURce? 

# 功能描述

设置指定通道的 PM 调制信号源为内部（INTernal）或外部（EXTernal）调制源。 

查询指定通道的 PM 调制信号源类型。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{INTERNAL|EXTERNAL}</td><td>离散型</td><td>INTERNAL|EXTERNAL</td><td>INTERNAL</td></tr></table>

# 说明

DG2000可以接收来自内部或外部调制源的调制波形。 

选择内部调制源后，可选择 SINusoid、SQUare、TRIangle、RAMP、NRAMp、NOISe 或 USER 作为调 制波形，默认为 SINusoid。NOISe 可以作为调制波，但不能作为载波。 

选择外部调制源后，信号发生器接收从后面板相应 [Sync/Ext Mod/Trig/FSK] 连接器输入的外部调 制信号。此时，已调信号的相位偏差由该连接器上的 $\pm 5 \mathsf { V }$ 信号电平控制。例如：将相位偏差设置为 $\boldsymbol { 1 8 0 ^ { \circ } }$ ， 则 $+ 5 V$ 信号电平对应于相位改变 $1 8 0 ^ { \circ }$ 。较低的外部信号电平产生较少的偏差。 

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1 的相关参数。 

# 返回格式

返回 INT 或 EXT。 

# 举例

:SOUR1:PM:SOUR EXT /*设置 CH1的 PM 调制信号源为外部调制源*/ 

:SOUR1:PM:SOUR? /*查询 CH1的 PM 调制信号源类型，返回 EXT*/ 

# [:SOURce[<n>]][:MOD]:PM:STATe

# 命令格式

$$
\begin{array}{l} [: S O U R c e [ <   n > ] [ : M O D ]: P M: S T A t e \{O N | 1 | O F F | 0 \} \\ [: S O U R c e [ <   n > ] [ : M O D ]: P M: S T A t e? \\ \end{array}
$$

# 功能描述

打开或关闭指定通道的 PM 调制功能。 

查询指定通道 PM 调制功能的开关状态。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 说明

PM：相位调制（Phase Modulation），载波的相位随调制波形的瞬时电压的变化而变化。 

. PM 载波波形可以是正弦波、方波、锯齿波或任意波，默认为正弦波。脉冲、噪声和直流不能作为载波。 载波波形的多个参数（如频率、幅度和偏移）的不同设置都会影响输出的 PM 已调制波形。 

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1 的相关参数。 

若当前已打开扫频功能（[:SOURce[<n>]]:SWEep:STATe）或脉冲串功能 

（[:SOURce[<n>]]:BURSt[:STATe]），则打开调制功能时，扫频功能或脉冲串功能将自动关闭。 

若当前已打开谐波功能（[:SOURce[<n>]]:HARMonic[:STATe]），则不能打开调制功能，即不能调制谐 波。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:SOUR1:PM:STAT ON /*打开 CH1 的 PM 调制功能*/ 

:SOUR1:PM:STAT? /*查询 CH1的 PM 调制功能的开关状态，返回 $\mathsf { O N } ^ { \star } /$ 

# :SOURce[:MOD]:PSKey 命令

# 命令列表：

 [:SOURce[<n>]][:MOD]:PSKey:INTernal:RATE 

[:SOURce[<n>]][:MOD]:PSKey:PHASe 

 [:SOURce[<n>]][:MOD]:PSKey:POLarity 

[:SOURce[<n>]][:MOD]:PSKey:SOURce 

 [:SOURce[<n>]][:MOD]:PSKey:STATe 

# [:SOURce[<n>]][:MOD]:PSKey:INTernal:RATE

# 命令格式

[:SOURce[<n>]][:MOD]:PSKey:INTernal:RATE {<rate>|MINimum|MAXimum} 

[:SOURce[<n>]][:MOD]:PSKey:INTernal:RATE? [MINimum|MAXimum] 

# 功能描述

设置指定通道的 PSK 调制速率。 

查询指定通道的 PSK 调制速率。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;frequency&gt;</td><td>实型</td><td>2mHz至1MHz</td><td>100Hz</td></tr></table>

# 说明

该命令仅适用于内部调制源（[:SOURce[<n>]][:MOD]:PSKey:SOURce），PSK 调制速率是指输出相位在 载波相位和调制相位（[:SOURce[<n>]][:MOD]:PSKey:PHASe）之间“移动”的频率。 

省略[:SOURce[<n>]]或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

# 返回格式

以科学计数形式返回 PSK 调制速率，有效位数为 7 位，如 1.500000E $+ 0 2$ ，表示 PSK 调制速率为 150Hz。 

# 举例

:SOUR1:PSK:INT:RATE 150 /*设置 CH1 的 PSK 调制速率为 $1 5 0 \mathsf { H z } ^ { \star } /$ 

:SOUR1:PSK:INT:RATE? /*查询 CH1 的 PSK 调制速率，返回 1.500000E+02*/ 

# [:SOURce[<n>]][:MOD]:PSKey:PHASe

# 命令格式

[:SOURce[<n>]][:MOD]:PSKey:PHASe {<phase>|MINimum|MAXimum} 

[:SOURce[<n>]][:MOD]:PSKey:PHASe? [MINimum|MAXimum] 

# 功能描述

设置指定通道的 PSK 调制相位。 

查询指定通道的 PSK 调制相位。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;phase&gt;</td><td>实型</td><td>0°至360°</td><td>180°</td></tr></table>

# 说明

 PSK 调制时，信号发生器在两个预置相位（载波相位和调制相位）间“移动”其输出相位。 

省略[:SOURce[<n>]]或 $[ < n > ]$ ]时，默认设置 CH1的相关参数。 

# 返回格式

以科学计数形式返回 PSK 调制相位，有效位数为 7 位，如 $9 . 0 0 0 0 0 0 0 \mathsf { E } + 0 1$ ，表示 PSK 调制相位为 $9 0 ^ { \circ }$ 。 

# 举例

:SOUR1:PSK:PHAS 90 /*设置 CH1 的 PSK 调制相位为 $9 0 ^ { \circ \star } /$ 

:SOUR1:PSK:PHAS? /*查询 CH1的 PSK 调制相位，返回 $9 . 0 0 0 0 0 0 0 \mathsf { E } { + } 0 1 ^ { \star } /$ 

# [:SOURce[<n>]][:MOD]:PSKey:POLarity

# 命令格式

[:SOURce[<n>]][:MOD]:PSKey:POLarity {POSitive|NEGative} 

[:SOURce[<n>]][:MOD]:PSKey:POLarity? 

# 功能描述

设置指定通道的 PSK 调制极性为正极性（POSitive）或负极性（NEGative）。 

查询指定通道的 PSK 调制极性。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{POSitive|NEGative}</td><td>离散型</td><td>POSitive|NEGative</td><td>POSitive</td></tr></table>

# 说明

省略[:SOURce[<n>]]或[<n>]时，默认设置 CH1 的相关参数。 

内部调制（[:SOURce[<n>]][:MOD]:PSKey:SOURce）时，若设定极性为“正极性”，则在调制波幅度为 逻辑低电平时输出载波相位；在调制波幅度为逻辑高电平时输出调制相位 （[:SOURce[<n>]][:MOD]:PSKey:PHASe）。极性为“负极性”时，情况相反。 

外部调制（[:SOURce[<n>]][:MOD]:PSKey:SOURce）时，若设定极性为“正极性”，则在外部输入信号 为逻辑低电平时输出载波相位；在外部输入信号为逻辑高电平时输出调制相位 （[:SOURce[<n>]][:MOD]:PSKey:PHASe）。极性为“负极性”时，情况相反。 

# 返回格式

返回 POS 和 NEG。 

# 举例

:SOUR1:PSK:POL POS /*设置 CH1的 PSK 调制极性为正极性*/ 

:SOUR1:PSK:POL? /*查询 CH1的 PSK 调制极性，返回 $\mathsf { P O S } ^ { \star } /$ 

# [:SOURce[<n>]][:MOD]:PSKey:SOURce

# 命令格式

[:SOURce[<n>]][:MOD]:PSKey:SOURce {INTernal|EXTernal} 

[:SOURce[<n>]][:MOD]:PSKey:SOURce? 

# 功能描述

设置指定通道的 PSK 调制信号源为内部（INTernal）或外部（EXTernal）调制源。 

查询指定通道的 PSK 调制信号源类型。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{INTERNAL|EXTERNAL}</td><td>离散型</td><td>INTERNAL|EXTERNAL</td><td>INTERNAL</td></tr></table>

# 说明

DG2000可以接收来自内部或外部调制源的调制波形。 

选择内部调制源，即选择占空比为 $50 \%$ 的方波。此时，输出相位在载波相位和调制相位 （[:SOURce[<n>]][:MOD]:PSKey:PHASe）之间“移动”的频率由调制速率 （[:SOURce[<n>]][:MOD]:PSKey:INTernal:RATE）决定。 

选择外部调制源时，信号发生器接收从后面板相应 [Sync/Ext Mod/Trig/FSK] 连接器输入的外调制 信号。通过该连接器从外部控制 PSK 调制和控制 AM/FM/PM 调制时不同。在控制 PSK 调制时，您可以 设置极性（[:SOURce[<n>]][:MOD]:PSKey:POLarity）。 

省略[:SOURce $\cdot < n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1 的相关参数。 

# 返回格式

返回 INT 或 EXT。 

# 举例

:SOUR1:PSK:SOUR EXT /*设置 CH1的 PSK 调制信号源为外部调制源*/ :SOUR1:PSK:SOUR? /*查询 CH1 的 PSK 调制信号源类型，返回 EXT*/ 

# [:SOURce[<n>]][:MOD]:PSKey:STATe

# 命令格式

[:SOURce[<n>]][:MOD]:PSKey:STATe {ON|1|OFF|0} [:SOURce[<n>]][:MOD]:PSKey:STATe? 

# 功能描述

打开或关闭指定通道的 PSK 调制功能。 查询指定通道 PSK 调制功能的开关状态。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 说明

PSK：相移键控（Phase Shift Keying）调制，信号发生器在两个预置相位（载波相位和调制相位）间“移 动”其输出相位。 

. PSK 载波波形可以是正弦波、方波、锯齿波或任意波，默认为正弦波。脉冲、噪声和直流不能作为载波。 载波波形的多个参数（如频率、幅度、偏移和起始相位等）的不同设置都会影响输出的 PSK 已调制波 形。 

省略[:SOURce[<n>]]或 $[ < n > ]$ ]时，默认设置 CH1的相关参数。 

若当前已打开扫频功能（[:SOURce[<n>]]:SWEep:STATe）或脉冲串功能 （[:SOURce[<n>]]:BURSt[:STATe]），则打开调制功能时，扫频功能或脉冲串功能将自动关闭。 

若当前已打开谐波功能（[:SOURce[<n>]]:HARMonic[:STATe]），则不能打开调制功能，即不能调制谐 波。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:SOUR1:PSK:STAT ON /*打开 CH1 的 PSK 调制功能*/ 

:SOUR1:PSK:STAT? /*查询 CH1的 PSK 调制功能的开关状态，返回 $\mathsf { O N } ^ { \star } /$ 

# :SOURce[:MOD]:PWM 命令

# 命令列表：

$\spadesuit$  [:SOURce[<n>]][:MOD]:PWM[:DEViation]:DCYCle 

$\spadesuit$ [:SOURce[<n>]][:MOD]:PWM[:DEViation][:WIDTh] 

$\spadesuit$ [:SOURce[<n>]][:MOD]:PWM:INTernal:FREQuency 

[:SOURce[<n>]][:MOD]:PWM:INTernal:FUNCtion 

[:SOURce[<n>]][:MOD]:PWM:SOURce 

 [:SOURce[<n>]][:MOD]:PWM:STATe 

# [:SOURce[<n>]][:MOD]:PWM[:DEViation]:DCYCle

# 命令格式

[:SOURce[<n>]][:MOD]:PWM[:DEViation]:DCYCle {<percent>|MINimum|MAXimum} 

[:SOURce[<n>]][:MOD]:PWM[:DEViation]:DCYCle? [MINimum|MAXimum] 

# 功能描述

设置指定通道的 PWM 调制占空比偏差。 

查询指定通道的 PWM 调制占空比偏差。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;percent&gt;</td><td>实型</td><td>见下文“说明”</td><td>20%</td></tr></table>

# 说明

占空比偏差表示已调制波形相对于原始脉冲波形的占空比的变化（以%表示）。 

省略[:SOURce[<n>]]或 $[ < n > ]$ 时，默认设置 CH1 的相关参数。 

占空比偏差受到最小占空比和边沿时间的限制，且不能超过脉冲的占空比。 

如果当前指定通道的脉冲波选择的是“占空比”，则启用 PWM 调制功能后，界面上显示“占空比偏差”； 如果当前指定通道的脉冲波选择的是“脉宽”，则启用 PWM 调制功能后，界面上显示“宽度偏差”。 

# 返回格式

以科学计数形式返回 PWM 调制占空比偏差，有效位数为 7位，如 $1 . 5 0 0 0 0 0 0 \mathsf { E } + 0 1$ ，表示 PWM 调制占空比偏 差为 $1 5 \%$ 。 

# 举例

:SOUR1:PWM:DCYC 15 /*设置 CH1的 PWM 调制占空比偏差为 $1 5 \% ^ { \star } /$ 

:SOUR1:PWM:DCYC? /*查询 CH1的 PWM 调制占空比偏差，返回 $1 . 5 0 0 0 0 0 0 \mathsf { E } { + } 0 1 ^ { \star } /$ 

# [:SOURce[<n>]][:MOD]:PWM[:DEViation][:WIDTh]

# 命令格式

[:SOURce[<n>]][:MOD]:PWM[:DEViation][:WIDTh] {<deviation>|MINimum|MAXimum} 

[:SOURce[<n>]][:MOD]:PWM[:DEViation][:WIDTh]? [MINimum|MAXimum] 

# 功能描述

设置指定通道的 PWM 调制宽度偏差。 

查询指定通道的 PWM 调制宽度偏差。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;deviation&gt;</td><td>实型</td><td>见下文“说明”</td><td>200us</td></tr></table>

# 说明

宽度偏差表示已调波形相对于原始脉冲波形的脉冲宽度的变化。 

省略[:SOURce[<n>]]或[<n>]时，默认设置 CH1 的相关参数。 

宽度偏差受到最小脉冲宽度和边沿时间设置的限制，且不能超过脉冲宽度。 

如果当前指定通道的脉冲波选择的是“占空比”，则启用 PWM 调制功能后，界面上显示“占空比偏差”； 如果当前指定通道的脉冲波选择的是“脉宽”，则启用 PWM 调制功能后，界面上显示“宽度偏差”。 

# 返回格式

以科学计数形式返回 PWM 调制宽度偏差，有效位数为 7位，如 1.000000E-04，表示 PWM 调制宽度偏差为 100us（即 0.0001s）。 

# 举例

:SOUR1:PWM 0.0001 /*设置 CH1 的 PWM 调制宽度偏差为 100us（即 0.0001s）*/ 

:SOUR1:PWM? /*查询 CH1 的 PWM 调制宽度偏差，返回 1.000000E-04*/ 

# [:SOURce[<n>]][:MOD]:PWM:INTernal:FREQuency

# 命令格式

[:SOURce[<n>]][:MOD]:PWM:INTernal:FREQuency {<frequency>|MINimum|MAXimum} 

[:SOURce[<n>]][:MOD]:PWM:INTernal:FREQuency? [MINimum|MAXimum] 

# 功能描述

设置指定通道 PWM 调制波的频率。 

查询指定通道 PWM 调制波的频率。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;frequency&gt;</td><td>实型</td><td>2mHz至1MHz</td><td>100Hz</td></tr></table>

# 说明

该命令仅适用于内部调制源（[:SOURce[<n>]][:MOD]:PWM:SOURce）。 

省略[:SOURce[<n>]]或[<n>]时，默认设置 CH1 的相关参数。 

# 返回格式

以科学计数形式返回 PWM 调制波的频率，有效位数为 7位，如 1.500000E+02，表示 PWM 调制波的频率为 150Hz。 

# 举例

:SOUR1:PWM:INT:FREQ 150 /*设置 CH1 的 PWM 调制波的频率为 $1 5 0 \mathsf { H z } ^ { \star } /$ 

:SOUR1:PWM:INT:FREQ? /*查询 CH1的 PWM 调制波的频率，返回 $1 . 5 0 0 0 0 0 0 \mathsf { E } { + } 0 2 ^ { \star } /$ 

# [:SOURce[<n>]][:MOD]:PWM:INTernal:FUNCtion

# 命令格式

[:SOURce[<n>]][:MOD]:PWM:INTernal:FUNCtion 

{SINusoid|SQUare|TRIangle|RAMP|NRAMp|NOISe|USER} 

[:SOURce[<n>]][:MOD]:PWM:INTernal:FUNCtion? 

# 功能描述

设置指定通道的 PWM 调制波形。 

查询指定通道的 PWM 调制波形。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{SINusoid|SQUare|TRIangle|RAMP|NRAMp|NOISE|USER}</td><td>离散型</td><td>SINusoid|SQUare|TRIangle|RAMP|NRAMp|NOISE|USER</td><td>SINusoid</td></tr></table>

# 说明

该命令仅适用于内部调制源（[:SOURce[<n>]][:MOD]:PWM:SOURce）。 

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

SQUare：占空比为 $50 \%$ ；TRIangle：对称性为 $50 \%$ ；RAMP：对称性为 $100 \%$ ；NRAMp：对称性为 $0 \%$ USER：指定通道选择的任意波。 

# 返回格式

返回 SIN、SQU、TRI、RAMP、NRAM、NOIS 或 USER。 

# 举例

:SOUR1:PWM:INT:FUNC SQU /*设置 CH1 的 PWM 调制波形为方波*/ 

:SOUR1:PWM:INT:FUNC? /*查询 CH1 的 PWM 调制波形，返回 SQU*/ 

# [:SOURce[<n>]][:MOD]:PWM:SOURce

# 命令格式

[:SOURce[<n>]][:MOD]:PWM:SOURce {INTernal|EXTernal} 

[:SOURce[<n>]][:MOD]:PWM:SOURce? 

# 功能描述

设置指定通道的 PWM 调制信号源为内部（INTernal）或外部（EXTernal）调制源。 

查询指定通道的 PWM 调制信号源类型。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{INTERNAL|EXTERNAL}</td><td>离散型</td><td>INTERNAL|EXTERNAL</td><td>INTERNAL</td></tr></table>

# 说明

DG2000可以接收来自内部或外部调制源的调制波形。 

选择内部调制源后，可选择 SINusoid、SQUare、TRIangle、RAMP、NRAMp、NOISe 或 USER 作为调 

制波形，默认为 SINusoid。NOISe 可以作为调制波，但不能作为载波。 

选择外部调制源后，信号发生器接收从后面板相应通道的 [Sync/Ext Mod/Trig/FSK] 连接器输入的 外部调制信号。此时，已调信号的宽度偏差（[:SOURce[<n>]][:MOD]:PWM[:DEViation][:WIDTh]）或 占空比偏差（[:SOURce[<n>]][:MOD]:PWM[:DEViation]:DCYCle）由该连接器上的 $\pm 5 \mathsf { V }$ 信号电平控制。 例如，将宽度偏差设置为 10s，则 $+ 5 V$ 信号电平对应于宽度改变 10s。 

省略[:SOURce[ $\cdot < n > ] ]$ ]或 $[ < n > ]$ ]时，默认设置 CH1的相关参数。 

# 返回格式

返回 INT 或 EXT。 

# 举例

:SOUR1:PWM:SOUR EXT /*设置 CH1的 PWM 调制信号源为外部调制源*/ :SOUR1:PWM:SOUR? /*查询 CH1 的 PWM 调制信号源类型，返回 EXT*/ 

# [:SOURce[<n>]][:MOD]:PWM:STATe

# 命令格式

[:SOURce[<n>]][:MOD]:PWM:STATe {ON|1|OFF|0} [:SOURce[<n>]][:MOD]:PWM:STATe? 

# 功能描述

打开或关闭指定通道的 PWM 调制功能。 查询指定通道 PWM 调制功能的开关状态。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 说明

PWM：脉宽（Pulse Width Modulation）调制，载波的脉宽随调制波形的瞬时电压的变化而变化。 

? PWM 的载波波形只可以是脉冲波，且只有当指定通道的当前波形为脉冲波时，才能打开 PWM 调制功 能。脉冲波的多个参数（如频率、幅度、偏移、脉宽、占空比等）的不同设置都会影响输出的 PWM 已 调制波形。 

省略[:SOURce[ $< n > ] ]$ 或[ $< n > ]$ 时，默认设置 CH1的相关参数。 

若当前已打开扫频功能（[:SOURce[<n>]]:SWEep:STATe）或脉冲串功能 （[:SOURce[<n>]]:BURSt[:STATe]），则打开调制功能时，扫频功能或脉冲串功能将自动关闭。 

# 返回格式

返回 ON 或 OFF。 

# 举例

假设 CH1 的当前波形为脉冲， 

:SOUR1:PWM:STAT ON /*打开 CH1 的 PWM 调制功能*/ 

:SOUR1:PWM:STAT? /*查询 CH1的 PWM 调制功能的开关状态，返回 $\mathsf { O N } ^ { \star } /$ 

# :SOURce:MOD 命令

# 命令列表：

$\spadesuit$  [:SOURce[<n>]]:MOD[:STATe] 

$\spadesuit$  [:SOURce[<n>]]:MOD:TYPe 

# [:SOURce[<n>]]:MOD[:STATe]

# 命令格式

$$
\begin{array}{l} [: S O U R c e <   n > ]: M O D [ : S T A t e ] \{O N | 1 | O F F | 0 \} \\ [: S O U R c e [ <   n > ] ]: M O D [: S T A t e ]? \\ \end{array}
$$

# 功能描述

打开或关闭指定通道的调制功能。 

查询指定通道调制功能的开关状态。 

# 参数

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 说明

省略[:SOURce[ $< n > ] ]$ 或[ $\cdot < n > ]$ 时，默认设置 CH1 的相关参数。 

若当前已打开扫频功能（[:SOURce[<n>]]:SWEep:STATe）或脉冲串功能 （[:SOURce[<n>]]:BURSt[:STATe]），则打开调制功能时，扫频功能或脉冲串功能将自动关闭。 

若当前已打开谐波功能（[:SOURce[<n>]]:HARMonic[:STATe]），则不能打开调制功能，即不能调制谐 波。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:SOUR1:MOD ON /*打开 CH1 的调制功能*/ 

:SOUR1:MOD? /*查询 CH1调制功能的开关状态，返回 ON*/ 

# [:SOURce[<n>]]:MOD:TYPe

# 命令格式

[:SOURce[<n>]]:MOD:TYPe {AM|FM|PM|ASK|FSK|PSK|PWM} 

[:SOURce[<n>]]:MOD:TYPe? 

# 功能描述

设置指定通道的调制类型。 

查询指定通道的调制类型。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{AM|FM|PM|ASK|FSK|PSK|PWM}</td><td>离散型</td><td>AM|FM|PM|ASK|FSK|PSK|PWM</td><td>AM</td></tr></table>

# 说明

省略[:SOURce[ $< n > ] ]$ ]或 $\cdot < n > ]$ 时，默认设置 CH1的相关参数。 

? AM：幅度调制（Amplitude Modulation），载波的幅度随着调制波瞬时电压的变化而变化。 

FM：频率调制（Frequency Modulation），载波的频率随调制波的瞬时电压的变化而变化。 

PM：相位调制（Phase Modulation），载波的相位随调制波形的瞬时电压的变化而变化。 

ASK：幅移键控（Amplitude Shift Keying）调制，信号发生器在两个预设的幅度（载波幅度和调制幅度） 间移动其输出幅度。 

FSK：频移键控（Frequency Shift Keying）调制，信号发生器在两个预设频率（载波频率和跳跃频率） 间“移动”其输出频率。 

PSK：相移键控（Phase Shift Keying）调制，信号发生器在两个预置相位（载波相位和调制相位）间“移 动”其输出相位。 

. PWM：脉宽（Pulse Width Modulation）调制，载波的脉宽随调制波形的瞬时电压的变化而变化。 

# 返回格式

返回 AM、FM、PM、ASK、FSK、PSK 或 PWM。 

# 举例

:SOUR1:MOD:TYPE FM /*设置 CH1的调制类型为频率调制*/ 

:SOUR1:MOD:TYPE? /*查询 CH1 的调制类型，返回 $\mathsf { F M } ^ { \star } /$ 

# :SOURce:PERiod 命令

# 命令列表：

[:SOURce[<n>]]:PERiod[:FIXed] 

# [:SOURce[<n>]]:PERiod[:FIXed]

# 命令格式

$$
\begin{array}{l} [: S O U R c e [ <   n > ]: P E R i o d [ : F I X e d ] \{\langle p e r i o d > | M I N i m u m | M A X i m u m \} \\ [: S O U R c e <   n > ]: P E R i o d [ : F I X e d ]? [ M I N i m u m | M A X i m u m ] \\ \end{array}
$$

# 功能描述

设置指定通道的波形（基本波形和任意波）周期。 

查询指定通道的波形（基本波形和任意波）周期。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;period&gt;</td><td>实型</td><td>见下文“说明”</td><td>1ms</td></tr></table>

# 说明

省略[:SOURce[<n>]]或[<n>]时，默认设置 CH1 的相关参数。 

周期与频率互为倒数关系，有关 DG2000 系列不同型号和不同波形的频率可设范围请参考表 2-1。 

. 若实际发送的命令中的周期值低于相应的周期下限，则设置指定通道的波形周期为其周期下限。 

指定通道波形类型改变（[:SOURce[<n>]]:APPLy?）时，若该周期在新的波形类型下有效，则仪器依然 使用该周期；若该周期在新的波形类型下无效，仪器则弹出提示消息，并自动将周期设置为新的波形类 型的周期下限值。 

# 返回格式

以科学计数形式返回波形周期，有效位数为 7位，如 1.000000E-01，表示波形周期为 0.1s。 

# 举例

:SOUR1:PER 0.1 /*设置 CH1的波形周期为 $0 . 1 \mathsf { s } ^ { \star } /$ 

:SOUR1:PER? /*查询 CH1 的波形周期，返回 1.000000E-01*/ 

# :SOURce:PHASe 命令

# 命令列表：

$\spadesuit$ [:SOURce[<n>]]:PHASe[:ADJust] 

$\spadesuit$ [:SOURce[<n>]]:PHASe:INITiate 

$\spadesuit$  [:SOURce[<n>]]:PHASe:SYNChronize 

# [:SOURce[<n>]]:PHASe[:ADJust]

# 命令格式

[:SOURce[<n>]]:PHASe[:ADJust] {<phase $>$ |MINimum|MAXimum} 

[:SOURce[<n>]]:PHASe[:ADJust]? [MINimum|MAXimum] 

# 功能描述

设置指定通道的波形（基本波形和任意波形）起始相位。 

查询指定通道的波形（基本波形和任意波形）起始相位。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;phase&gt;</td><td>实型</td><td>0°至360°</td><td>0°</td></tr></table>

# 说明

省略[:SOURce[<n>]]或[<n>]时，默认设置 CH1 的相关参数。 

若实际发送的命令中的起始相位值低于相应的起始相位下限，则设置指定通道的波形起始相位为其起始 相位下限。 

# 返回格式

以科学计数形式返回波形起始相位，有效位数为 7 位，如 $1 . 0 0 0 0 0 0 0 \mathsf { E } + 0 1$ ，表示波形起始相位为 $ { 1 0 ^ { \circ } }$ 。 

# 举例

:SOUR1:PHAS 10 /*设置 CH1的起始相位为 $1 0 ^ { \circ \star } /$ 

:SOUR1:PHAS? /*查询 CH1 的起始相位，返回 1.000000E+01*/ 

[:SOURce[<n>]]:PHASe:INITiate 

[:SOURce[<n>]]:PHASe:SYNChronize 

# 命令格式

[:SOURce[<n>]]:PHASe:INITiate 

[:SOURce[<n>]]:PHASe:SYNChronize 

# 功能描述

在指定通道执行一次同相位操作。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr></table>

# 说明

DG2000系列双通道函数/任意波形发生器提供同相位功能。执行同相位操作后，仪器将重新配置两个通 道，使其按照设定的频率和相位输出。 

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1 的相关参数。 

# 举例

:SOUR1:PHAS:INIT /*在 CH1执行一次同相位操作*/ 

:SOUR2:PHAS:SYNC /*在 CH2 执行一次同相位操作*/ 

# :SOURce:PULSe 命令

# 命令列表：

$\spadesuit$  [:SOURce[<n>]]:PULSe:DCYCle 

 [:SOURce[<n>]]:PULSe:TRANsition[:LEADing] 

 [:SOURce[<n>]]:PULSe:TRANsition:TRAiling 

$\spadesuit$ [:SOURce[<n>]]:PULSe:WIDTh 

# [:SOURce[<n>]]:PULSe:DCYCle

# 命令格式

[:SOURce[<n>]]:PULSe:DCYCle {<percent $>$ |MINimum|MAXimum} 

[:SOURce[<n>]]:PULSe:DCYCle? [MINimum|MAXimum] 

# 功能描述

设置指定通道的脉冲占空比。 

查询指定通道的脉冲占空比。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;percent&gt;</td><td>实型</td><td>0.001%至99.999%</td><td>50%</td></tr></table>

# 说明

脉冲占空比定义为脉宽（[:SOURce[<n>]]:FUNCtion:PULSe:WIDTh）占脉冲周期 （[:SOURce[<n>]]:FUNCtion:PULSe:PERiod）的百分比。脉冲占空比与脉宽相关联，修改其中一个参 数将自动修改另一个参数。 

. 脉冲占空比的可设范围受“最小脉冲宽度”和“脉冲周期”的限制（关于“最小脉冲宽度”和“脉冲周 期”的范围，请参考《DG2000 数据手册》“性能指标”中“信号特性”的说明）。脉冲占空比的实际取 值范围为 

$$
1 0 0 \times P _ {w \min } \div P _ {p u l s e} \leq P _ {d c y c l e} <   1 0 0 \times (1 - 2 \times P _ {w \min } \div P _ {p u l s e})
$$

其中， 

$P _ { d c y c l e }$ 脉冲占空比； 

Pwmin $P _ { w \mathrm { m i n } }$ 最小脉冲宽度； 

$P _ { p u l s e }$ 脉冲周期。 

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1 的相关参数。 

# 返回格式

以科学计数形式返回脉冲占空比，有效位数为 7位，如 4.500000E $+ 0 1$ ，表示脉冲占空比为 $45 \%$ 。 

# 举例

:SOUR1:PULS:DCYC 45 /*设置 CH1的脉冲占空比为 $45 \% ^ { \star } /$ 

:SOUR1:PULS:DCYC? /*查询 CH1 的脉冲占空比，返回 $4 . 5 0 0 0 0 0 0 \mathsf { E } { + } 0 1 ^ { \star } /$ 

# [:SOURce[<n>]]:PULSe:TRANsition[:LEADing]

# 命令格式

[:SOURce[<n>]]:PULSe:TRANsition[:LEADing] {<seconds $>$ |MINimum|MAXimum} 

[:SOURce[<n>]]:PULSe:TRANsition[:LEADing]? [MINimum|MAXimum] 

# 功能描述

设置指定通道的脉冲上升沿时间。 

查询指定通道的脉冲上升沿时间。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;seconds&gt;</td><td>实型</td><td>8ns至(0.625×脉宽)</td><td>20ns</td></tr></table>

# 说明

上升沿时间定义为脉冲幅度从 $10 \%$ 上升至 $90 \%$ 所持续的时间。 

省略[:SOURce[<n>]]或 $[ < n > ]$ ]时，默认设置 CH1 的相关参数。 

上升沿时间的可设范围受波形频率和脉宽限制，当所设置的数值超出限定值，仪器将自动调整边沿时间 以适应指定的脉宽。 

# 返回格式

以科学计数形式返回脉冲上升沿时间，有效位数为 7位，如 3.500000E-08，表示脉冲上升沿时间为 35ns。 

# 举例

:SOUR1:PULS:TRAN 0.000000035 /*设置 CH1 的脉冲上升沿时间为 35ns*/ 

:SOUR1:PULS:TRAN? /*查询 CH1 的脉冲上升沿时间，返回 3.500000E-08*/ 

# [:SOURce[<n>]]:PULSe:TRANsition:TRAiling

# 命令格式

[:SOURce[<n>]]:PULSe:TRANsition:TRAiling {<seconds>|MINimum|MAXimum} 

[:SOURce[<n>]]:PULSe:TRANsition:TRAiling? [MINimum|MAXimum] 

# 功能描述

设置指定通道的脉冲下降沿时间。 

查询指定通道的脉冲下降沿时间。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;seconds&gt;</td><td>实型</td><td>8ns至(0.625×脉宽)</td><td>20ns</td></tr></table>

# 说明

下降沿时间定义为脉冲幅度从 $90 \%$ 下降至 $10 \%$ 所持续的时间。 

省略[:SOURce[<n>]]或 $\cdot < n >$ ]时，默认设置 CH1 的相关参数。 

下降沿时间的可设范围受波形频率和脉宽限制，当所设置的数值超出限定值，仪器将自动调整边沿时间 以适应指定的脉宽。 

# 返回格式

以科学计数形式返回脉冲下降沿时间，有效位数为 7位，如 3.500000E-08，表示脉冲下降沿时间为 35ns。 

# 举例

:SOUR1:PULS:TRAN:TRA 0.000000035 /*设置 CH1 的脉冲下降沿时间为 35ns*/ 

:SOUR1:PULS:TRAN:TRA? /*查询 CH1 的脉冲下降沿时间，返回 3.500000E-08*/ 

# [:SOURce[<n>]]:PULSe:WIDTh

# 命令格式

[:SOURce[<n>]]:PULSe:WIDTh {<seconds>|MINimum|MAXimum} 

[:SOURce[<n>]]:PULSe:WIDTh? [MINimum|MAXimum] 

# 功能描述

设置指定通道的脉宽。 

查询指定通道的脉宽。 

# 参数

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;seconds&gt;</td><td>实型</td><td>16ns至999.999 982 118 590 6ks</td><td>500us</td></tr></table>

# 说明

 脉宽定义为从脉冲上升沿幅度的 $50 \%$ 处到下一个下降沿幅度的 $50 \%$ 处之间的时间间隔。 

 脉宽的可设范围受“最小脉冲宽度”和“脉冲周期”的限制（关于“最小脉冲宽度”和“脉冲周期”的 范围，请参考《DG2000 数据手册》“性能指标”中“信号特性”的说明）。脉宽的实际取值范围为 

$$
P _ {w \min } \leq P _ {\text {w i d t h}} <   P _ {\text {p u l s e}} - 2 \times P _ {w \min }
$$

其中， 

Pwidth $P _ { w i d t h }$ 脉宽； 

Pwmin $P _ { w \mathrm { m i n } }$ —最小脉冲宽度； 

Ppulse $P _ { p u l s e }$ 脉冲周期。 

省略[:SOURce $\cdot < n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1 的相关参数。 

# 返回格式

以科学计数形式返回脉宽，有效位数为 7位，如 1.000000E-02，表示脉宽为 10ms（即 0.01s）。 

# 举例

:SOUR1:FUNC:PULS:WIDT 0.01 /*设置 CH1 的脉宽为 10ms（即 0.01s）*/ 

:SOUR1:FUNC:PULS:WIDT? /*查询 CH1 的脉宽，返回 1.000000E-02*/ 

# :SOURce:SUM 命令

# 命令列表：

$\spadesuit$  [:SOURce[<n>]]:SUM:AMPLitude 

$\spadesuit$ [:SOURce[<n>]]:SUM:INTernal:FREQuency 

$\spadesuit$ [:SOURce[<n>]]:SUM:INTernal:FUNCtion 

[:SOURce[<n>]]:SUM[:STATe] 

# [:SOURce[<n>]]:SUM:AMPLitude

# 命令格式

[:SOURce[<n>]]:SUM:AMPLitude {<amplitude $>$ |MINimum|MAXimum} 

[:SOURce[<n>]]:SUM:AMPLitude? [MINimum|MAXimum] 

# 功能描述

设置指定通道波形叠加功能的叠加比例。 

查询指定通道波形叠加功能的叠加比例。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;amplitude&gt;</td><td>实型</td><td>0%至100%</td><td>10%</td></tr></table>

# 说明

叠加比例是指叠加在基本波上的波形与基本波幅度的百分比。 

省略[:SOURce[<n>]]或 $[ < n > ]$ ]时，默认设置 CH1 的相关参数。 

# 返回格式

以科学计数形式返回叠加比例，有效位数为 7位，如 1.000000E+01，表示叠加比例为 $10 \%$ 。 

# 举例

:SOUR1:SUM:AMPL 10 /*设置 CH1 波形叠加功能的叠加比例为 $1 0 \% ^ { \star } /$ 

:SOUR1:SUM:AMPL? /*查询 CH1波形叠加功能的叠加比例，返回 $1 . 0 0 0 0 0 0 0 \mathsf { E } { + } 0 1 ^ { \star } /$ 

# [:SOURce[<n>]]:SUM:INTernal:FREQuency

# 命令格式

[:SOURce[<n>]]:SUM:INTernal:FREQuency {<frequency $>$ |MAXimum|MINimum} 

[:SOURce[<n>]]:SUM:INTernal:FREQuency? [MINimum|MAXimum] 

# 功能描述

设置指定通道波形叠加功能的叠加频率。 

查询指定通道波形叠加功能的叠加频率。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;frequency&gt;</td><td>实型</td><td>1uHz至100MHz</td><td>1kHz</td></tr></table>

# 说明

叠加频率是指叠加到基本波上的波形的频率。 

省略[:SOURce[<n>]]或 $\cdot < n > ]$ 时，默认设置 CH1的相关参数。 

# 返回格式

以科学计数形式返回叠加频率，有效位数为 7位，如 $1 . 0 0 0 0 0 0 0 \mathsf { E } + 0 2$ ，表示叠加频率为 100Hz。 

# 举例

:SOUR1:SUM:INT:FREQ 100 /*设置 CH1 波形叠加功能的叠加频率为 $1 0 0 \mathsf { H z } ^ { \star } /$ 

:SOUR1:SUM:INT:FREQ? /*查询 CH1 波形叠加功能的叠加频率，返回 1.000000E+02*/ 

# [:SOURce[<n>]]:SUM:INTernal:FUNCtion

# 命令格式

[:SOURce[<n>]]:SUM:INTernal:FUNCtion {SIN|SQU|RAMP|NOISe|ARB} 

[:SOURce[<n>]]:SUM:INTernal:FUNCtion? 

# 功能描述

设置指定通道波形叠加功能的叠加源。 

查询指定通道波形叠加功能的叠加源。 

# 参数

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{SIN|SQU|RAMP|NOISE|ARB}</td><td>离散型</td><td>SIN|SQU|RAMP|NOISE|ARB</td><td>SIN</td></tr></table>

# 说明

叠加源是指要叠加到基本波上的波形，可以为正弦波（SIN）、方波（SQU）、锯齿波（RAMP）、噪声（NOISe） 或任意波（ARB）。 

省略[:SOURce[<n>]]或 $[ < n > ]$ 时，默认设置 CH1 的相关参数。 

# 返回格式

返回 SIN、SQU、RAMP、NOISE 或 ARB。 

# 举例

:SOUR1:SUM:INT:FUNC SQU /*设置 CH1波形叠加功能的叠加源为方波*/ :SOUR1:SUM:INT:FUNC? /*查询 CH1波形叠加功能的叠加源，返回 SQ 

# [:SOURce[<n>]]:SUM[:STATe]

# 命令格式

[:SOURce[<n>]]:SUM[:STATe] {ON|1|OFF|0} [:SOURce[<n>]]:SUM[:STATe]? 

# 功能描述

打开或关闭指定通道的波形叠加功能。 

查询指定通道波形叠加功能的开关状态。 

# 参数

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 说明

波形叠加是指在基本波上叠加指定的波形后再输出。该功能仅对基本波形有效。 

省略[:SOURce[<n>]]或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:SOUR1:SUM ON /*打开 CH1的波形叠加功能*/ 

:SOUR1:SUM? /*查询 CH1波形叠加功能的开关状态，返回 $\mathsf { O N } ^ { \star } /$ 

# :SOURce:SWEep 命令

# 命令列表：

$\spadesuit$ [:SOURce[<n>]]:SWEep:HTIMe:STARt 

$\spadesuit$  [:SOURce[<n>]]:SWEep:HTIMe[:STOP] 

$\spadesuit$ [:SOURce[<n>]]:SWEep:RTIMe 

[:SOURce[<n>]]:SWEep:SPACing 

[:SOURce[<n>]]:SWEep:STATe 

 [:SOURce[<n>]]:SWEep:STEP 

 [:SOURce[<n>]]:SWEep:TIME 

[:SOURce[<n>]]:SWEep:TRIGger[:IMMediate] 

$\spadesuit$ [:SOURce[<n>]]:SWEep:TRIGger:SLOPe 

 $\spadesuit$ [:SOURce[<n>]]:SWEep:TRIGger:SOURce 

# [:SOURce[<n>]]:SWEep:HTIMe:STARt

# 命令格式

[:SOURce[<n>]]:SWEep:HTIMe:STARt {<seconds>|MINimum|MAXimum} [:SOURce[<n>]]:SWEep:HTIMe:STARt? [MINimum|MAXimum] 

# 功能描述

设置指定通道扫频功能的起始保持时间。 查询指定通道扫频功能的起始保持时间。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;seconds&gt;</td><td>实型</td><td>0s至500s</td><td>0s</td></tr></table>

# 说明

起始保持是指扫频开始后，输出信号保持以“起始频率”（[:SOURce[<n>]]:FREQuency:STARt）输出 的时间。起始保持时间结束后，信号发生器将按当前的扫描类型改变频率继续输出。 

省略[:SOURce[<n>]]或[<n>]时，默认设置 CH1 的相关参数。 

 修改“起始保持”时间后，信号发生器将重新从指定的“起始频率”开始扫频输出。 

# 返回格式

以科学计数形式返回起始保持时间，有效位数为 7 位，如 1.000000E $+ 0 0$ ，表示起始保持时间为 1s。 

# 举例

:SOUR1:SWE:HTIM:STAR 1 /*设置 CH1 扫频功能的起始保持时间为 ${ { \bar { 1 } } { \mathsf { S } } ^ { \star } } /$ 

:SOUR1:SWE:HTIM:STAR? /*查询 CH1 扫频功能的起始保持时间，返回 1.000000E+00*/ 

# [:SOURce[<n>]]:SWEep:HTIMe[:STOP]

# 命令格式

[:SOURce[<n>]]:SWEep:HTIMe[:STOP] {<seconds $>$ |MINimum|MAXimum} 

[:SOURce[<n>]]:SWEep:HTIMe[:STOP]? [MINimum|MAXimum] 

# 功能描述

设置指定通道扫频功能的终止保持时间。 

查询指定通道扫频功能的终止保持时间。 

# 参数

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;seconds&gt;</td><td>实型</td><td>0s至500s</td><td>0s</td></tr></table>

# 说明

终止保持是指信号发生器从“起始频率”（[:SOURce[<n>]]:FREQuency:STARt）扫描到“终止频率” （[:SOURce[<n>]]:FREQuency:STOP）后，输出信号继续保持“终止频率”输出的时间。 

省略[:SOURce[<n>]]或[<n>]时，默认设置 CH1 的相关参数。 

 修改“终止保持”时间后，信号发生器将重新从指定的“起始频率”开始扫频输出。 

# 返回格式

以科学计数形式返回终止保持时间，有效位数为 7 位，如 $1 . 0 0 0 0 0 0 0 \mathsf { E } + 0 0$ ，表示终止保持时间为 1s。 

# 举例

:SOUR1:SWE:HTIM 1 /*设置 CH1扫频功能的终止保持时间为 ${ { \sf 1 } { \sf s } ^ { \star } } /$ 

:SOUR1:SWE:HTIM? /*查询 CH1 扫频功能的终止保持时间，返回 1.000000E+00*/ 

# [:SOURce[<n>]]:SWEep:RTIMe

# 命令格式

[:SOURce[<n>]]:SWEep:RTIMe {<seconds>|MINimum|MAXimum} 

[:SOURce[<n>]]:SWEep:RTIMe? [MINimum|MAXimum] 

# 功能描述

设置指定通道扫频功能的返回时间。 

查询指定通道扫频功能的返回时间。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;seconds&gt;</td><td>实型</td><td>0s至500s</td><td>0s</td></tr></table>

# 说明

返回时间是指信号发生器从“起始频率”（[:SOURce[<n>]]:FREQuency:STARt）扫描到“终止频率” （[:SOURce[<n>]]:FREQuency:STOP）并且经过“终止保持” （[:SOURce[<n>]]:SWEep:HTIMe[:STOP]）时间后，输出信号从“终止频率”复位至“起始频率”的 时间。 

省略[:SOURce[<n>]]或[<n>]时，默认设置 CH1 的相关参数。 

修改返回时间后，信号发生器将重新从指定的“起始频率”开始扫频输出。 

# 返回格式

以科学计数形式返回返回时间，有效位数为 7位，如 1.000000E $+ 0 0$ ，表示返回时间为 1s。 

# 举例

:SOUR1:SWE:RTIM 1 /*设置 CH1 扫频功能的返回时间为 ${ { \bar { 1 } } { \mathsf { S } } ^ { \star } } /$ 

:SOUR1:SWE:RTIM? /*查询 CH1扫频功能的返回时间，返回 $1 . 0 0 0 0 0 0 0 \mathsf { E } + 0 0 ^ { \star } /$ 

# [:SOURce[<n>]]:SWEep:SPACing

# 命令格式

[:SOURce[<n>]]:SWEep:SPACing {LINear|LOGarithmic|STEp} 

[:SOURce[<n>]]:SWEep:SPACing? 

# 功能描述

设置指定通道的扫频类型为线性（LINear）、对数（LOGarithmic）或步进（STEp）扫频。 查询指定通道的扫频类型。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{LINear|LOGarithmic|STEp}</td><td>离散型</td><td>LINear|LOGarithmic|STEp</td><td>LINear</td></tr></table>

# 说明

DG2000提供线性、对数和步进三种扫频类型。 

在线性扫频方式下，仪器输出信号的频率以线性方式变化，即以每秒若干赫兹的方式改变输出频率，该 变化由“起始频率”（[:SOURce[<n>]]:FREQuency:STARt）、“终止频率” 

（[:SOURce[<n>]]:FREQuency:STOP）和“扫描时间”（[:SOURce[<n>]]:SWEep:TIME）控制。在屏 幕的波形上，可以看到一条直线，表明输出频率以线性方式变化。 

在对数扫频方式下，仪器输出信号的频率以对数方式变化，即以每秒倍频程或每秒十倍的方式改变输出 频率，该变化由“起始频率”、“终止频率”和“扫描时间”控制。在屏幕的波形上，可以看到一条指数 函数的曲线，表明输出频率以对数方式变化。 

在步进扫频方式下，仪器输出信号的频率从“起始频率”到“终止频率”之间以阶梯式“步进”，输出 信号在每个频点上停留的时间长短由“扫描时间”和“步进数”控制。在屏幕的波形上，可以看到一条 阶梯波，表明输出频率以阶梯式“步进”。 

省略[:SOURce[ $< n > ] ]$ ]或 $[ < n > ]$ ]时，默认设置 CH1 的相关参数。 

# 返回格式

返回 LIN、LOG 或 STE。 

# 举例

:SOUR1:SWE:SPAC LIN /*设置 CH1 的扫频类型为线性扫频*/ 

:SOUR1:SWE:SPAC? /*查询 CH1的扫频类型，返回 ${ \mathsf { L } } { \mathsf { I N } } ^ { \star } /$ 

# [:SOURce[<n>]]:SWEep:STATe

# 命令格式

[:SOURce[<n>]]:SWEep:STATe {ON|1|OFF|0} 

[:SOURce[<n>]]:SWEep:STATe? 

# 功能描述

打开或关闭指定通道的扫频功能。 

查询指定通道扫频功能的开关状态。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 说明

 DG2000可从单通道或同时从双通道输出扫频波形。在扫频模式下，信号发生器在指定的扫描时间内从 起始频率到终止频率变化输出。 

 DG2000支持线性、对数和步进三种扫频方式；允许用户设定“标记”频率；允许用户设置起始保持、 终止保持和返回时间；支持内部、外部或手动触发源；对于正弦波、方波、锯齿波和任意波，均可以产 生扫频输出（不允许基本波脉冲和噪声产生扫频信号）。 

省略[:SOURce[<n>]]或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

若当前已打开调制（[:SOURce[<n>]]:MOD[:STATe]）或脉冲串（[:SOURce[<n>]]:BURSt[:STATe]）功 能，则打开扫频功能时，调制或脉冲串功能将自动关闭。 

. 若当前已打开谐波（[:SOURce[<n>]]:HARMonic[:STATe]）功能，则不能打开扫频功能。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:SOUR1:SWE:STAT ON /*打开 CH1 的扫频功能*/ 

:SOUR1:SWE:STAT? /*查询 CH1扫频功能的开关状态，返回 $\mathsf { O N } ^ { \star } /$ 

# [:SOURce[<n>]]:SWEep:STEP

# 命令格式

[:SOURce[<n>]]:SWEep:STEP {<n>|MINimum|MAXimum} 

[:SOURce[<n>]]:SWEep:STEP? [MINimum|MAXimum] 

# 功能描述

设置指定通道的扫频步进数。 

查询指定通道的扫频步进数。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;n&gt;</td><td>整型</td><td>2至1024</td><td>2</td></tr></table>

# 说明

步进数是指从“起始频率”（[:SOURce[<n>]]:FREQuency:STARt）变化至“终止频率” （[:SOURce[<n>]]:FREQuency:STOP）所需的步数，仅适用于步进扫描 （[:SOURce[<n>]]:SWEep:SPACing）。 

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1 的相关参数。 

# 返回格式

以科学计数形式返回扫频步进数，有效位数为 7位，如 5.000000E+00，表示扫频步进数为 5。 

# 举例

:SOUR1:SWE:STEP 5 /*设置 CH1 的扫频步进数为 $5 ^ { \star } /$ 

:SOUR1:SWE:STEP? /*查询 CH1的扫频步进数，返回 $5 . 0 0 0 0 0 0 0 \mathsf { E } + 0 0 ^ { \star } /$ 

# [:SOURce[<n>]]:SWEep:TIME

# 命令格式

[:SOURce[<n>]]:SWEep:TIME {<seconds $>$ |MINimum|MAXimum} 

[:SOURce[<n>]]:SWEep:TIME? [MINimum|MAXimum] 

# 功能描述

设置指定通道的扫频时间。 

查询指定通道的扫频时间。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;seconds&gt;</td><td>实型</td><td>1ms至500s</td><td>1s</td></tr></table>

# 说明

扫频时间是指完成从“起始频率”（[:SOURce[<n>]]:FREQuency:STARt）变化至“终止频率” （[:SOURce[<n>]]:FREQuency:STOP）扫描所需要的时间。 

省略[:SOURce[<n>]]或[<n>]时，默认设置 CH1 的相关参数。 

修改“扫频时间”后，信号发生器将重新从指定的“起始频率”开始扫频输出。 

# 返回格式

以科学计数形式返回扫频时间，有效位数为 7位，如 $5 . 0 0 0 0 0 0 0 \mathsf { E } + 0 0$ ，表示扫频时间为 5s。 

# 举例

:SOUR1:SWE:TIME 5 /*设置 CH1 的扫频时间为 $5 s ^ { \star } /$ 

:SOUR1:SWE:TIME? /*查询 CH1 的扫频时间，返回 5.000000E+00*/ 

# [:SOURce[<n>]]:SWEep:TRIGger[:IMMediate]

# 命令格式

[:SOURce[<n>]]:SWEep:TRIGger[:IMMediate] 

# 功能描述

在指定通道立即触发一次扫频。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr></table>

# 说明

该命令仅适用于手动触发（[:SOURce[<n>]]:SWEep:TRIGger:SOURce），且仅当打开相应通道的输出 （:OUTPut[<n>][:STATe]）时，该命令有效。 

省略[:SOURce $\cdot < n > ] ]$ 或 $[ < n > ]$ ]时，默认设置 CH1 的相关参数。 

# 举例

:SOUR1:SWE:TRIG /*在 CH1立即触发一次扫频*/ 

# [:SOURce[<n>]]:SWEep:TRIGger:SLOPe

# 命令格式

[:SOURce[<n>]]:SWEep:TRIGger:SLOPe {POSitive|NEGative} 

[:SOURce[<n>]]:SWEep:TRIGger:SLOPe? 

# 功能描述

设置指定通道触发输入信号的边沿类型为上升沿（POSitive）或下降沿（NEGative）。 

查询指定通道触发输入信号的边沿类型。 

# 参数

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{POSitive|NEGative}</td><td>离散型</td><td>POSitive|NEGative</td><td>POSitive</td></tr></table>

# 说明

 设置触发输入信号的边沿类型，即选择在触发输入信号的上升沿或下降沿进行触发。 

该命令仅适用于外部触发（[:SOURce[<n>]]:SWEep:TRIGger:SOURce）。外部触发时，信号发生器接 收从后面板相应通道的 [Sync/Ext Mod/Trig/FSK] 连接器输入的触发信号，每次接收到一个具有指 定极性的 TTL脉冲时，就启动一次扫频。 

省略[:SOURce[ $\angle n > ]$ ]或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

# 返回格式

返回 POS 或 NEG。 

# 举例

:SOUR1:SWE:TRIG:SLOP POS /*设置 CH1 触发输入信号的边沿类型为上升沿*/ 

:SOUR1:SWE:TRIG:SLOP? /*查询 CH1 触发输入信号的边沿类型，返回 $\mathsf { P O S } ^ { \star } /$ 

# [:SOURce[<n>]]:SWEep:TRIGger:SOURce

# 命令格式

[:SOURce[<n>]]:SWEep:TRIGger:SOURce {INTernal|EXTernal|MANual} 

[:SOURce[<n>]]:SWEep:TRIGger:SOURce? 

# 功能描述

设置指定通道的扫频触发源为内部源（INTernal）、外部源（EXTernal）或手动源（MANual）。 查询指定通道的扫频触发源类型。 

# 参数

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{INTERNAL|EXTERNAL|MANual}</td><td>离散型</td><td>INTERNAL|EXTERNAL|MANual</td><td>INTERNAL</td></tr></table>

# 说明

内部触发时，信号发生器输出连续的扫频波形。触发周期由指定的扫描时间 （[:SOURce[<n>]]:SWEep:TIME）、返回时间（[:SOURce[<n>]]:SWEep:RTIMe）、起始保持 （[:SOURce[<n>]]:SWEep:HTIMe:STARt）和终止保持（[:SOURce[<n>]]:SWEep:HTIMe[:STOP]）时 间决定。 

外部触发时，信号发生器接收从后面板相应通道的 [Sync/Ext Mod/Trig/FSK] 连接器输入的触发信 号，每次接收到一个具有指定极性的 TTL 脉冲（[:SOURce[<n>]]:SWEep:TRIGger:SLOPe）时，就启 动一次扫频。 

手动触发时，每发送一次触发命令（[:SOURce[<n>]]:SWEep:TRIGger[:IMMediate]）立即在相应通道 

启动一次扫频（仅当指定通道的输出打开时，触发命令有效）。 

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

# 返回格式

返回 INT、EXT 或 MAN。 

# 举例

:SOUR1:SWE:TRIG:SOUR INT /*设置 CH1的扫频触发源为内部源*/ :SOUR1:SWE:TRIG:SOUR? /*查询 CH1的扫频触发源类型，返回 INT*/ 

# :SOURce:TRACe 命令

# 命令列表：

 [:SOURce[<n>]][:TRACe]:DATA:DAC16 

# [:SOURce[<n>]][:TRACe]:DATA:DAC16

# 命令格式

[:SOURce[<n>]][:TRACe]:DATA:DAC16 VOLATILE,<flag>,<data> 

# 功能描述

下载大波表到 DDRIII 内存中。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;flag&gt;</td><td rowspan="2">ASCII字符串</td><td rowspan="2">见下文“说明”</td><td rowspan="2">无</td></tr><tr><td>&lt;data&gt;</td></tr></table>

# 说明

省略[:SOURce[<n>]]或[<n>]时，默认设置 CH1 的相关参数。 

该命令由两部分构成，一部分为命令字符串，包括“[:SOURce[<n>]][:TRACe]:DATA:DAC16 VOLATILE,<flag>,”，另一部分为二进制数据，包括“<data>”。<flag $>$ 表示数据传输的状态，可设置 为 CON或 END。CON表示本数据包后还有数据包；END 表示本数据包为最后一个数据包，数据发送结 束。<data>为要下载的二进制数据，数据长度为 8pts（16Bytes）至 16kpts（32kBytes）。 

<data $>$ 为要下载的二进制数据，数据长度范围为 16Bytes（8pts）至 32kBytes（16kpts）。<data>是以 #号开头的二进制数据块，例如：“#516384 二进制数据”，“#”号之后的“5”表示数据长度信息（即 16384）共占 5个字符；“16384”表示后续二进制数据的字节数。每个波形点对应两个字节的二进制数 （可设范围均为 0000至 3FFF），所以字节数必须为偶数。 

发送的命令中的<flag>为 END 时，仪器自动切换到任意波输出。 

# :SOURce:TRACK 命令

# 命令列表：

[:SOURce[<n>]]:TRACK 

# [:SOURce[<n>]]:TRACK

# 命令格式

[:SOURce[<n>]]:TRACK {ON|OFF|INVerted} 

[:SOURce[<n>]]:TRACK? 

# 功能描述

设置指定通道跟踪功能的状态为打开（ON）、关闭（OFF）或反转（INVerted）。 

查询指定通道跟踪功能的状态。 

# 参数

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{ON|OFF|INVerted}</td><td>离散型</td><td>ON|OFF|INVerted</td><td>OFF</td></tr></table>

# 说明

. 打开：开启跟踪功能。仪器自动将 CH1的各种参数和状态（除通道输出开关状态）复制到 CH2，并且 调整 CH1 的参数或状态时，CH2的相应参数或状态（除通道输出开关状态）自动调整为与 CH1相同的 参数或状态。此时，双通道可输出相同的信号（通道输出已打开）。 

关闭：关闭跟踪功能。 

. 反转：跟踪功能处于开启状态。仪器自动将 CH1 的各种参数和状态（除通道输出开关状态）复制到 CH2， 并且调整 CH1的参数或状态时，CH2的相应参数或状态（除通道输出开关状态）自动调整为与 CH1相 同的参数或状态。此时，CH2（通道输出已打开）输出将 CH1的输出信号反转后的信号。 

省略[:SOURce[<n>]]或[<n>]时，默认设置 CH1 的相关参数。 

跟踪功能打开时，耦合功能和通道复制功能被禁用。 

# 返回格式

返回 ON、OFF 或 INV。 

# 举例

:SOUR1:TRACK ON /*设置 CH1 跟踪功能的状态为打开*/ 

:SOUR1:TRACK? /*查询 CH1跟踪功能的状态，返回 $\mathsf { O N } ^ { \star } /$ 

# :SOURce:VOLTage 命令

# 命令列表：

$\spadesuit$ [:SOURce[<n>]]:VOLTage:COUPle[:STATe] 

 $\spadesuit$ [:SOURce[<n>]]:VOLTage[:LEVel][:IMMediate][:AMPLitude] 

$\spadesuit$ [:SOURce[<n>]]:VOLTage[:LEVel][:IMMediate]:HIGH 

$\spadesuit$  [:SOURce[<n>]]:VOLTage[:LEVel][:IMMediate]:LOW 

 [:SOURce[<n>]]:VOLTage[:LEVel][:IMMediate]:OFFSet 

[:SOURce[<n>]]:VOLTage:UNIT 

# [:SOURce[<n>]]:VOLTage:COUPle[:STATe]

# 命令格式

[:SOURce[<n>]]:VOLTage:COUPle[:STATe] {ON|1|OFF|0} 

[:SOURce[<n>]]:VOLTage:COUPle[:STATe]? 

# 功能描述

打开或关闭幅度耦合功能。 

查询幅度耦合功能的开关状态。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 说明

打开幅度耦合功能后，CH1 和 CH2两个通道互为基准源，当改变其中一个通道（该通道作为基准源） 的幅度时，另一通道的幅度将自动调整，并总是与基准通道保持指定的幅度差值或比例。 

. 您也可以发送:COUPling[<n>]:AMPL[:STATe]命令设置和查询幅度耦合功能的开关状态。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:SOUR1:VOLT:COUP ON /*打开幅度耦合功能*/ 

:SOUR1:VOLT:COUP? /*查询幅度耦合功能的开关状态，返回 $\mathsf { O N } ^ { \star } /$ 

# [:SOURce[<n>]]:VOLTage[:LEVel][:IMMediate][:AMPLitude]

# 命令格式

[:SOURce[<n>]]:VOLTage[:LEVel][:IMMediate][:AMPLitude] {<amplitude>|MINimum|MAXimum} 

[:SOURce[<n>]]:VOLTage[:LEVel][:IMMediate][:AMPLitude]? [MINimum|MAXimum] 

# 功能描述

设置指定通道的波形幅度。 

查询指定通道的波形幅度。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;amplitude&gt;</td><td>实型</td><td>见下文“说明”</td><td>5Vpp</td></tr></table>

# 说明

省略[:SOURce $\cdot < n > ]$ ]或[ $\cdot < n > ]$ 时，默认设置 CH1的相关参数。 

幅度<amplitude>的最小值为 2mVpp，最大值受“阻抗”（:OUTPut[<n>]:IMPedance 或:OUTPut[<n>]:LOAD）和“频率/周期”（[:SOURce[<n>]]:FREQuency[:FIXed]或 [:SOURce[<n>]]:PERiod[:FIXed]）设置的限制。若实际发送的命令中的幅度值大于相应的幅度上限或 者低于相应的幅度下限，则设置指定通道的波形幅度为其幅度上限或幅度下限。 

 仪器当前的幅度为其默认值或之前设置的幅度。当仪器配置改变时（如频率），若该幅度有效，则仪器 依然使用该幅度。若该幅度无效，仪器则弹出提示消息，并自动将幅度设置为新配置的幅度上限值。 

您也可以使用“高电平”或“低电平”设置幅度和偏移： 

幅度 $=$ 高电平-低电平 

偏移 $=$ (高电平 $^ +$ 低电平)/2 

# 返回格式

以科学计数形式返回波形幅度，有效位数为 7 位，如 $5 . 0 0 0 0 0 0 0 \mathsf { E } + 0 0$ ，表示波形幅度为 5Vpp。 

# 举例

:SOUR1:VOLT 5 /*设置 CH1 的波形幅度为 5Vpp*/ 

:SOUR1:VOLT? /*查询 CH1的波形幅度，返回 $5 . 0 0 0 0 0 0 0 \mathsf { E } + 0 0 ^ { \star } /$ 

# [:SOURce[<n>]]:VOLTage[:LEVel][:IMMediate]:HIGH

# 命令格式

$$
\begin{array}{l} [: S O U R c e [ <   n > ]: V O L T a g e [ : L E V e l ] [ : I M M e d i a t e ]: H I G H \{<   v o l t a g e > | M I N i m u m | M A X i m u m \} \\ [: S O U R c e [ <   n > ]: V O L T a g e [: L E V e l ] [: I M M e d i a t e]: H I G H? [ M I N i m u m | M A X i m u m ] \\ \end{array}
$$

# 功能描述

设置指定通道的波形高电平值。 

查询指定通道的波形高电平值。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;voltage&gt;</td><td>实型</td><td>见下文“说明”</td><td>2.5Vpp</td></tr></table>

# 说明

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

您也可以使用“幅度”（[:SOURce[<n>]]:VOLTage[:LEVel][:IMMediate][:AMPLitude]）和“偏移” （[:SOURce[<n>]]:VOLTage[:LEVel][:IMMediate]:OFFSet）来设置高电平和低电平： 

高电平 $=$ 偏移 $^ +$ 幅度/2 

低电平 $=$ 偏移-幅度/2 

# 返回格式

以科学计数形式返回波形高电平值，有效位数为 7 位，如 3.500000E+00，表示波形高电平值为 $3 . 5 \mathsf { V } \mathsf { p } \mathsf { p }$ 。 

# 举例

:SOUR1:VOLT:HIGH 3.5 /*设置 CH1 的波形高电平值为 3.5Vpp*/ 

:SOUR1:VOLT:HIGH? /*查询 CH1 的波形高电平值，返回 3.500000E+00*/ 

# [:SOURce[<n>]]:VOLTage[:LEVel][:IMMediate]:LOW

# 命令格式

$$
\begin{array}{l} [: S O U R c e [ <   n > ] ]: V O L T a g e [ : L E V e l ] [ : I M M e d i a t e ]: L O W \{\langle v o l t a g e > | M I N i m u m | M A X i m u m \} \\ [: S O U R c e <   n > ]: V O L T a g e [ : L E V e l ] [ : I M M e d i a t e ]: L O W? [ M I N i m u m | M A X i m u m ] \\ \end{array}
$$

# 功能描述

设置指定通道的波形低电平值。 

查询指定通道的波形低电平值。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;voltage&gt;</td><td>实型</td><td>见下文“说明”</td><td>-2.5Vpp</td></tr></table>

# 说明

省略[:SOURce[ $< n > ] ]$ 或 $\cdot < n > ]$ 时，默认设置 CH1的相关参数。 

您也可以使用“幅度”（[:SOURce[<n>]]:VOLTage[:LEVel][:IMMediate][:AMPLitude]）和“偏移” （[:SOURce[<n>]]:VOLTage[:LEVel][:IMMediate]:OFFSet）来设置高电平和低电平： 

高电平 $=$ 偏移 $^ +$ 幅度/2 

低电平 $=$ 偏移-幅度/2 

# 返回格式

以科学计数形式返回波形低电平值，有效位数为 7 位，如-1.500000E $+ 0 0$ ，表示波形低电平值为-1.5Vpp。 

# 举例

:SOUR1:VOLT:LOW -1.5 /*设置 CH1 的波形低电平值为-1.5Vpp*/ 

:SOUR1:VOLT:LOW? /*查询 CH1 的波形低电平值，返回-1.500000E+00*/ 

# [:SOURce[<n>]]:VOLTage[:LEVel][:IMMediate]:OFFSet

# 命令格式

[:SOURce[<n>]]:VOLTage[:LEVel][:IMMediate]:OFFSet {<voltage>|MINimum|MAXimum} 

[:SOURce[<n>]]:VOLTage[:LEVel][:IMMediate]:OFFSet? [MINimum|MAXimum] 

# 功能描述

设置指定通道的波形偏移电压。 

查询指定通道的波形偏移电压。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;voltage&gt;</td><td>实型</td><td>见下文“说明”</td><td>0Vdc</td></tr></table>

# 说明

省略[:SOURce[<n>]]或 $[ < n > ]$ ]时，默认设置 CH1 的相关参数。 

直流偏移电压的可设置范围受“阻抗”（:OUTPut[<n>]:IMPedance 或:OUTPut[<n>]:LOAD）、“频率” （[:SOURce[<n>]]:FREQuency[:FIXed]）和“幅度” 

（[:SOURce[<n>]]:VOLTage[:LEVel][:IMMediate][:AMPLitude]）设置的限制。若实际发送的命令中的 偏移值大于相应的偏移上限或者低于相应的偏移下限，则设置指定通道的波形偏移为其偏移上限或偏移 下限。 

 仪器当前的 DC 偏移电压为默认值或之前设置的偏移。当仪器配置改变时（如阻抗），若该偏移有效， 则仪器依然使用该偏移。若该偏移无效，仪器则弹出提示消息，并自动将偏移设置为新配置的偏移上限 值。 

# 返回格式

以科学计数形式返回波形偏移电压值，有效位数为 7 位，如 $1 . 0 0 0 0 0 0 0 \mathsf { E } + 0 0$ $+ 0 0$ ，表示波形偏移电压值为 $\mathsf { 1 V _ { \mathrm { d c } } }$ 

# 举例

:SOUR1:VOLT:OFFS 1 /*设置 CH1的偏移电压为 ${ \mathsf { 1 } } { \mathsf { V } } _ { \mathrm { d c } } { } ^ { \star } /$ 

:SOUR1:VOLT:OFFS? /*查询 CH1的偏移电压，返回 $1 . 0 0 0 0 0 0 0 \mathsf { E } + 0 0 ^ { \star } /$ 

# [:SOURce[<n>]]:VOLTage:UNIT

# 命令格式

[:SOURce[<n>]]:VOLTage:UNIT {VPP|VRMS|DBM} 

[:SOURce[<n>]]:VOLTage:UNIT? 

# 功能描述

设置指定通道的幅度单位为 Vpp（VPP）、Vrms（VRMS）或 dBm(DBM)。 

查询指定通道的幅度单位。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{VPP|VRMS|DBM}</td><td>离散型</td><td>VPP|VRMS|DBM</td><td>VPP</td></tr></table>

# 说明

省略[:SOURce[ $< n > ] ]$ 或 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

Vpp 是表示信号峰峰值的单位，Vrms 是表示信号有效值的单位，dBm 是表示信号功率绝对值的单位。 对于不同的波形，Vpp 与 Vrms 之间的关系不同。 

以正弦波为例，Vpp与Vrms之间的换算关系满足关系式： $V _ { P P } = 2 \sqrt { 2 } V r m s$ 。 

dBm 与Vrms 之间满足如下关系式： $d B m = 1 0 1 \mathrm { g } ( \frac { V r m s ^ { 2 } } { R } \times \frac { 1 } { 0 . 0 0 1 W } )$ 2Vrms 

其中， $R$ 表示通道的输出阻抗值，必须为确定的数值，因此，输出阻抗为高阻时，不可使用单位 dBm。 

# 返回格式

返回 VPP、VRMS 或 DBM。 

# 举例

:SOUR1:VOLT:UNIT VPP /*设置 CH1 的幅度单位为 $\mathsf { V p p } ^ { \star } /$ 

:SOUR1:VOLT:UNIT? /*查询 CH1 的幅度单位，返回 $\mathsf { V P P ^ { \star } } /$ 

# :SYSTem 命令

:SYSTem 命令用来设置蜂鸣器状态，查询仪器的通道个数及当前通道，设置各种接口（GPIB、LAN和 USB） 参数和状态，执行通道复制，查询错误队列，锁定前面板，设置系统语言和开机状态，设置时钟源以及查询 系统版本。 

# 命令列表：

:SYSTem:BEEPer[:IMMediate] 

:SYSTem:BEEPer:STATe 

:SYSTem:CHANnel:CURrent 

 :SYSTem:CHANnel:NUMber? 

 :SYSTem:COMMunicate:GPIB[:SELF]:ADDRess 

:SYSTem:COMMunicate:LAN:APPLy 

 :SYSTem:COMMunicate:LAN:AUTOip[:STATe] 

:SYSTem:COMMunicate:LAN:CONTrol? 

 :SYSTem:COMMunicate:LAN:DHCP[:STATe] 

 :SYSTem:COMMunicate:LAN:DNS 

:SYSTem:COMMunicate:LAN:DOMain 

 :SYSTem:COMMunicate:LAN:GATEway 

:SYSTem:COMMunicate:LAN:HOSTname 

:SYSTem:COMMunicate:LAN:IPADdress 

:SYSTem:COMMunicate:LAN:MAC? 

:SYSTem:COMMunicate:LAN:SMASk 

 :SYSTem:COMMunicate:LAN:STATic[:STATe] 

 :SYSTem:COMMunicate:LAN:UPDate 

 :SYSTem:COMMunicate:USB:INFormation? 

:SYSTem:CSCopy 

 :SYSTem:ERRor? 

:SYSTem:KLOCk 

:SYSTem:LANGuage 

:SYSTem:LOG:[:STATE] 

:SYSTem:POWeron 

 :SYSTem:PRESet:DELete:SYSTem:PRESet:RECall 

 :SYSTem:PRESet:SAVe:SYSTem:PRESet[:STATe]? 

:SYSTem:ROSCillator:SOURce 

# :SYSTem:BEEPer[:IMMediate]

# 命令格式

:SYSTem:BEEPer[:IMMediate] 

# 功能描述

蜂鸣器立即蜂鸣一次。 

# 说明

该命令不考虑蜂鸣器当前的开关状态。即使当前已关闭蜂鸣器，发送该命令，蜂鸣器也将立即蜂鸣一次。 

# :SYSTem:BEEPer:STATe

# 命令格式

:SYSTem:BEEPer:STATe {ON|1|OFF|0} 

:SYSTem:BEEPer:STATe? 

# 功能描述

打开或关闭蜂鸣器。 

查询蜂鸣器的状态。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>ON</td></tr></table>

# 说明

蜂鸣器打开时，当前面板或远程操作产生错误时会发出提示声音。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:SYST:BEEP:STAT 1 /*打开蜂鸣器*/ 

:SYST:BEEP:STAT? /*查询蜂鸣器的状态，返回 $\mathsf { O N } ^ { \star } /$ 

# :SYSTem:CHANnel:CURrent

# 命令格式

:SYSTem:CHANnel:CURrent {CH1|CH2} 

:SYSTem:CHANnel:CURrent? 

# 功能描述

选择当前通道。 

查询当前通道。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{CH1|CH2}</td><td>离散型</td><td>CH1|CH2</td><td>CH1</td></tr></table>

# 返回格式

返回 CH1 或 CH2。 

# 举例

:SYST:CHAN:CUR CH2 /*选择 CH2 为当前通道*/ 

:SYST:CHAN:CUR? /*查询当前通道，返回 $\mathsf { C H 2 ^ { \star } } /$ 

# :SYSTem:CHANnel:NUMber?

# 命令格式

:SYSTem:CHANnel:NUMber? 

# 功能描述

查询仪器输出通道的个数。 

# 返回格式

返回一个整数。 

# 举例

:SYST:CHAN:NUM? /*查询仪器输出通道的个数，返回 ${ 2 ^ { \star } } /$ 

# :SYSTem:COMMunicate:GPIB[:SELF]:ADDRess

# 命令格式

:SYSTem:COMMunicate:GPIB[:SELF]:ADDRess <integer> 

:SYSTem:COMMunicate:GPIB[:SELF]:ADDRess? 

# 功能描述

设置仪器的 GPIB 地址。 

查询仪器的 GPIB 地址。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>&lt;integer&gt;</td><td>整型</td><td>0至30</td><td>2</td></tr></table>

# 说明

如需使用 GPIB 接口，请确保您的计算机已安装 GPIB 卡，然后将 USB-GPIB 模块的 USB 端连接至信号源后 面板的 USB HOST 接口，USB-GPIB 模块的 GPIB 端连接至计算机的 GPIB 卡端口。 

# 返回格式

以整数形式返回 GPIB 地址。 

# 举例

:SYST:COMM:GPIB:ADDR 7 /*设置仪器的 GPIB 地址为 $7 ^ { \star } /$ 

:SYST:COMM:GPIB:ADDR? /*查询仪器的 GPIB 地址，返回 $7 ^ { \star } /$ 

# :SYSTem:COMMunicate:LAN:APPLy

# 命令格式

:SYSTem:COMMunicate:LAN:APPLy 

# 功能描述

应用当前设置的网络参数。 

# 说明

设置完 LAN参数后，必须执行此条命令，新的设置才会生效。 

# :SYSTem:COMMunicate:LAN:AUTOip[:STATe]

# 命令格式

:SYSTem:COMMunicate:LAN:AUTOip[:STATe] {ON|1|OFF|0} 

:SYSTem:COMMunicate:LAN:AUTOip[:STATe]? 

# 功能描述

打开或关闭 AutoIP（自动 IP）配置模式。 

查询 AutoIP（自动 IP）配置模式的状态。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>ON</td></tr></table>

# 说明

使用 LAN接口前，请使用网线将仪器连接至计算机或计算机所在的网络。 

. 仪器提供 3种 IP 配置模式：DHCP（动态配置）、Auto IP（自动配置）和 Manual IP（手动配置）。 

自动 IP 配置模式下，仪器根据当前网络配置自动获取从 169.254.0.1 到 169.254.255.254 的 IP 地址和 子网掩码 255.255.0.0。 

三种 IP 配置模式均设为“打开”时，参数配置的优先级从高到低依次为“动态配置”、“自动设置”、“手 动设置”，因此，欲启用自动配置模式，需将“动态配置”设为“关闭”。 

三种 IP 配置模式不能同时设为“关闭”。 

发送该命令后，必须执行:SYSTem:COMMunicate:LAN:APPLy 命令应用当前设置的网络参数，新的设置 才会生效。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:SYST:COMM:LAN:AUTO OFF /*关闭 AutoIP（自动 IP）配置模式*/ 

:SYST:COMM:LAN:AUTO? /*查询 AutoIP（自动 IP）配置模式的状态，返回 $\tt O F F ^ { \star } /$ 

# :SYSTem:COMMunicate:LAN:CONTrol?

# 命令格式

:SYSTem:COMMunicate:LAN:CONTrol? 

# 功能描述

读取用于套接字通信的初始控制连接端口号。 

# 返回格式

返回 5555，若接口不支持套接字，则返回 0。 

# :SYSTem:COMMunicate:LAN:DHCP[:STATe]

# 命令格式

:SYSTem:COMMunicate:LAN:DHCP[:STATe] {ON|1|OFF|0} 

:SYSTem:COMMunicate:LAN:DHCP[:STATe]? 

# 功能描述

打开或关闭 DHCP（动态配置）模式。 

查询 DHCP（动态配置）模式的状态。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>ON</td></tr></table>

# 说明

 DHCP 模式下，由当前网络中的 DHCP 服务器自动向仪器分配 IP 地址等网络参数。 

三种 IP 配置模式均设为“打开”时，参数配置的优先级从高到低依次为“动态配置”、“自动设置”、“手 动设置”。 

三种 IP 配置模式不能同时设为“关闭”。 

发送该命令后，必须执行:SYSTem:COMMunicate:LAN:APPLy 命令应用当前设置的网络参数，新的设置 才会生效。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:SYST:COMM:LAN:DHCP OFF /*关闭 DHCP（动态配置）模式*/ 

:SYST:COMM:LAN:DHCP? /*查询 DHCP（动态配置）模式的状态，返回 OFF*/ 

# :SYSTem:COMMunicate:LAN:DNS

# 命令格式

:SYSTem:COMMunicate:LAN:DNS <address> 

:SYSTem:COMMunicate:LAN:DNS? 

# 功能描述

设置 DNS（Domain Name Service，域名服务器）地址。 

查询 DNS地址。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>&lt;address&gt;</td><td>ASCII字符串</td><td>见下文“说明”</td><td>无</td></tr></table>

# 说明

仅当手动 IP 配置模式打开时（:SYSTem:COMMunicate:LAN:STATic[:STATe]），该命令有效。 

参数<address $>$ 格式为 nnn.nnn.nnn.nnn，第一个 nnn 的范围为 1 至 223（127 除外），其他三个 nnn 的范围为 0至 255。建议向您的网络管理员咨询一个可用的地址。 

发送该命令后，必须执行:SYSTem:COMMunicate:LAN:APPLy 命令应用当前设置的网络参数，新的设置 才会生效。 

# 返回格式

返回一个字符串，如 202.106.46.151。 

# 举例

:SYST:COMM:LAN:DNS 202.106.46.151 /*设置 DNS 地址为 202.106.46.151*/ 

:SYST:COMM:LAN:DNS? /*查询 DNS 地址，返回 202.106.46.151*/ 

# :SYSTem:COMMunicate:LAN:DOMain

# 命令格式

:SYSTem:COMMunicate:LAN:DOMain <name> 

:SYSTem:COMMunicate:LAN:DOMain? 

# 功能描述

设置域名。 

查询域名。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{name&gt;</td><td>ASCII字符串</td><td>见下文“说明”</td><td>YYYYRigollan</td></tr></table>

# 说明

参数<name>为指定的域名，长度不超过 99 个字符，可以为英文字符和数字。 

# 返回格式

返回一个字符串。 

# 举例

:SYST:COMM:LAN:DOM RIGOL /*设置域名为 RIGOL*/ 

:SYST:COMM:LAN:DOM? /*查询域名，返回 RIGOL*/ 

# :SYSTem:COMMunicate:LAN:GATEway

# 命令格式

:SYSTem:COMMunicate:LAN:GATEway <address> 

:SYSTem:COMMunicate:LAN:GATEway? 

# 功能描述

设置默认网关。 

查询默认网关。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>&lt;address&gt;</td><td>ASCII字符串</td><td>见下文“说明”</td><td>无</td></tr></table>

# 说明

仅当手动 IP 配置模式打开时（:SYSTem:COMMunicate:LAN:STATic[:STATe]），该命令有效。 

参数<address>的格式为 nnn.nnn.nnn.nnn，第一个 nnn 的范围为 1 至 223（127 除外），其他三个 nnn 的范围为 0至 255。建议向您的网络管理员咨询一个可用的网关地址。 

发送该命令后，必须执行:SYSTem:COMMunicate:LAN:APPLy 命令应用当前设置的网络参数，新的设置 才会生效。 

# 返回格式

返回一个字符串，如 192.168.1.1。 

# 举例

:SYST:COMM:LAN:GATE 192.168.1.1 /*设置默认网关为 192.168.1.1*/ 

:SYST:COMM:LAN:GATE? /*查询默认网关，返回 192.168.1.1*/ 

# :SYSTem:COMMunicate:LAN:HOSTname

# 命令格式

:SYSTem:COMMunicate:LAN:HOSTname <name> 

:SYSTem:COMMunicate:LAN:HOSTname? 

# 功能描述

设置主机名。 

查询主机名。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>&lt;name&gt;</td><td>ASCII字符串</td><td>见下文“说明”</td><td>YYYYrigollan</td></tr></table>

# 说明

参数<name>为指定的主机名，长度不超过 99个字符，可以为英文字符和数字。 

# 返回格式

返回一个字符串。 

# 举例

:SYST:COMM:LAN:HOST RIGOL123 /*设置主机名为 RIGOL123*/ 

:SYST:COMM:LAN:HOST? /*查询主机名，返回 RIGOL123*/ 

# :SYSTem:COMMunicate:LAN:IPADdress

# 命令格式

:SYSTem:COMMunicate:LAN:IPADdress <ip_address> 

:SYSTem:COMMunicate:LAN:IPADdress? 

# 功能描述

设置 IP 地址。 

查询 IP 地址。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>&lt;ip_address&gt;</td><td>ASCII字符串</td><td>见下文“说明”</td><td>无</td></tr></table>

# 说明

， 仅当手动 IP 配置模式打开时（:SYSTem:COMMunicate:LAN:STATic[:STATe]），该命令有效。 

参数<ip_address>的格式为 nnn.nnn.nnn.nnn，第一个 nnn 的范围为 1 至 223（127 除外），其他三个 nnn 的范围为 0至 255。建议向您的网络管理员咨询一个可用的地址。 

. 发送该命令后，必须执行:SYSTem:COMMunicate:LAN:APPLy 命令应用当前设置的网络参数，新的设置 才会生效。 

# 返回格式

返回一个字符串，如 192.168.1.88。 

# 举例

:SYST:COMM:LAN:IPAD 192.168.1.88 /*设置 IP 地址为 192.168.1.88*/ 

:SYST:COMM:LAN:IPAD? /*查询 IP 地址，返回 192.168.1.88*/ 

# :SYSTem:COMMunicate:LAN:MAC?

# 命令格式

:SYSTem:COMMunicate:LAN:MAC? 

# 功能描述

查询仪器的 MAC 地址。 

# 说明

MAC（Media Access Control）地址，也称为硬件地址，用于定义网络设备的位置。对于一台信号发生器， MAC 地址总是唯一的。为仪器分配 IP 地址时，总是通过 MAC 地址来识别仪器。MAC 地址（48位，即 6个 字节）通常以十六进制表示，如：00-14-0E-42-12-CF。 

# 返回格式

返回一个字符串，如 00-14-0E-42-12-CF。 

# :SYSTem:COMMunicate:LAN:SMASk

# 命令格式

:SYSTem:COMMunicate:LAN:SMASk <mask> 

:SYSTem:COMMunicate:LAN:SMASk? 

# 功能描述

设置子网掩码。 

查询子网掩码。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>&lt;mask&gt;</td><td>ASCII字符串</td><td>见下文“说明”</td><td>无</td></tr></table>

# 说明

. 仅当手动 IP 配置模式打开时（:SYSTem:COMMunicate:LAN:STATic[:STATe]），该命令有效。 

参数<mask>的格式为 nnn.nnn.nnn.nnn，其中 nnn 的范围为 0 至 255。建议向您的网络管理员咨询一 个可用的子网掩码。 

发送该命令后，必须执行:SYSTem:COMMunicate:LAN:APPLy 命令应用当前设置的网络参数，新的设置 才会生效。 

子网掩码必须是连续的，即 1和 0必须是连续的。 

# 返回格式

返回一个字符串，如 255.255.255.0。 

# 举例

:SYST:COMM:LAN:SMAS 255.255.255.0 /*设置子网掩码为 255.255.255.0*/ 

:SYST:COMM:LAN:SMAS? /*设置子网掩码，返回 255.255.255.0*/ 

# :SYSTem:COMMunicate:LAN:STATic[:STATe]

# 命令格式

:SYSTem:COMMunicate:LAN:STATic[:STATe] {ON|1|OFF|0} 

:SYSTem:COMMunicate:LAN:STATic[:STATe]? 

# 功能描述

打开或关闭手动 IP 配置模式。 

查询手动 IP 配置模式的状态。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 说明

手动 IP 配置模式下，由用户自定义 IP 地址等网络参数。 

. 三种 IP 配置模式均设为“打开”时，参数配置的优先级从高到低依次为“动态配置”、“自动设置”、“手 动设置”，因此，欲启用手动配置模式，需将“动态配置”和“自动设置”设为“关闭”。 

三种 IP 配置模式不能同时设为“关闭”。 

发送该命令后，必须执行:SYSTem:COMMunicate:LAN:APPLy 命令应用当前设置的网络参数，新的设置 才会生效。 

# 返回格式

返回 ON 或 OFF。 

# 举例

:SYST:COMM:LAN:STAT ON /*打开手动 IP 配置模式*/ 

:SYST:COMM:LAN:STAT? /*查询手动 IP 配置模式的状态，返回 $\mathsf { O N } ^ { \star } /$ 

# :SYSTem:COMMunicate:LAN:UPDate

# 命令格式

:SYSTem:COMMunicate:LAN:UPDate 

# 功能描述

将对 LAN 设置所做的所有更改都存储到非易失性存储器中，并用已更新的设置重新启动 LAN 驱动程序。 

# 说明

更改 DHCP、DNS、网关、主机名、IP 地址和子网掩码的设置后，必须发送该命令。 

请在发送该命令之前，完成对 LAN设置的所有更改。 

# :SYSTem:COMMunicate:USB:INFormation?

# 命令格式

:SYSTem:COMMunicate:USB:INFormation? 

# 功能描述

查询仪器的 USB 信息。 

# 返回格式

返回一个字符串，如:USB0::0x1AB1::0x0642::DG80000000001::INSTR。 

# :SYSTem:CSCopy

# 命令格式

:SYSTem:CSCopy <name>,<name> 

# 功能描述

将其中一个通道的所有参数和状态（不包括通道输出开关状态）以及任意波形数据复制到另一个通道。 

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{name&gt;</td><td>离散型</td><td>CH1|CH2</td><td>无</td></tr></table>

# 说明

两个<name>参数不可相同，即参数<name>,<name>可取 CH1,CH2 或 CH2,CH1。 

CH1,CH2：将 CH1的所有参数和状态（不包括通道输出开关状态）以及任意波形数据复制到通道 2。 

CH2,CH1：将 CH2的所有参数和状态（不包括通道输出开关状态）以及任意波形数据复制到 CH1。 

# 举例

:SYST:CSC CH1,CH2 /*将 CH1的所有参数和状态（不包括通道输出开关状态）以及任意波形数据复制到 CH2*/ 

# :SYSTem:ERRor?

# 命令格式

:SYSTem:ERRor? 

# 功能描述

查询并清除错误队列中的一条错误消息。 

# 说明

当您读取错误队列时，错误会被清除。您也可以使用清除状态命令*CLS，或仪器复位命令*RST，或开关仪 器来清除错误队列。 

# 返回格式

返回一个字符串，由两部分组成，这两部分之间以逗号隔开，依次是错误消息的编号和内容；其中，内容部 分是一个带双引号的字符串。如-113,"Undefined header; keyword cannot be found"，-113 是错误消息的编 号，Undefined header; keyword cannot be found（即双引号中的内容）是错误消息的内容。 

# :SYSTem:KLOCk

# 命令格式

:SYSTem:KLOCk <key $>$ ,{ON|1|OFF|0} 

:SYSTem:KLOCk? <key> 

# 功能描述

锁定或解锁指定的按键或旋钮。 

查询指定的按键或旋钮是否被锁定。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>&lt;key&gt;</td><td>离散型</td><td>见下文“说明”</td><td>无</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>OFF</td></tr></table>

# 说明

<key>用于指定按键，取值范围为： 

```txt
HOME|SHIFT|SINE|SQUARE|RAMP|PULSE| /*功能键*/  
NOISE|ARB|ALIGN|  
LEFT|RIGHT|KNOB| /*方向键和旋钮*/  
OUTPUT1|OUTPUT2| /*输出控制键*/  
COUNTER| /*频率计按键*/  
ALL /*前面板全部按键和旋钮*/ 
```

{ON|OFF|0|1}用于锁定或解锁按键，取值为 ON|1 时表示锁定指定的按键，取值为 OFF|0 时表示解除 锁定指定的按键。 

 DG2000允许用户锁定前面板上指定的按键或旋钮，以避免由于误操作而引起的危险。 

# 返回格式

返回 1或 0。 

# 举例

:SYST:KLOC HOME,1 /*锁定前面板上的 Home 键*/ 

:SYST:KLOC? HOME /*返回 ${ 1 ^ { \star } } /$ 

:SYST:KLOC HOME,OFF /*解锁前面板上的 Home 键*/ 

:SYST:KLOC? HOME /*返回 $0 ^ { \star } /$ 

# :SYSTem:LANGuage

# 命令格式

:SYSTem:LANGuage {ENGLish|SCHinese} 

:SYSTem:LANGuage? 

# 功能描述

设置系统语言为英文（ENGLish）或简体中文（SCHinese）。 

查询系统语言的类型。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{ENGLISH|SCHinese}</td><td>离散型</td><td>ENGLISH|SCHinese</td><td>SCHinese</td></tr></table>

# 返回格式

返回 ENGL 或 SCH。 

# 举例

:SYST:LANG SCH /*设置系统语言为简体中文*/ 

:SYST:LANG? /*查询系统语言的类型，返回 $\mathsf { S C H } ^ { \star } /$ 

# :SYSTem:LOG:[:STATE]

# 命令格式

:SYSTem:LOG:[:STATE] {ON|1|OFF|0} 

:SYSTem:LOG:[:STATE]? 

# 功能描述

打开或关闭系统日志。 

查询系统日志的开关状态。 

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{ON|1|OFF|0}</td><td>布尔型</td><td>ON|1|OFF|0</td><td>ON</td></tr></table>

# 返回格式

返回 ON 或 OFF。 

# 举例

:SYST:LOG 1 /*打开系统日志*/ 

:SYST:LOG? /*查询系统日志开关状态，返回 $\mathsf { O N } ^ { \star } /$ 

# :SYSTem:POWeron

# 命令格式

:SYSTem:POWeron {DEFault|LAST} 

:SYSTem:POWeron? 

# 功能描述

设置开机状态为默认值（DEFault）或上次值（LAST）。 

查询开机状态。 

# 参数

<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{DEFault|LAST}</td><td>离散型</td><td>DEFault|LAST</td><td>DEFault</td></tr></table>

# 说明

默认值（DEFault）：出厂默认值，某些不受恢复出厂值影响的参数（如：语言）除外，见“出厂设置”。 

上次值（LAST）：包括所有的系统参数和状态（除通道输出开关状态和时钟源）。 

# 返回格式

返回 DEFAULT 或 LAST。 

# 举例

:SYST:POW LAST /*设置开机状态为上次值*/ 

:SYST:POW? /*查询开机状态，返回 LAST*/ 

# :SYSTem:PRESet:DELete

# 命令格式

:SYSTem:PRESet:DELete {USER1|USER2|USER3|USER4|USER5|USER6|USER7|USER8|USER9|USER10} 

# 功能描述

删除仪器内部存储器中指定的用户已存储的状态文件（USER1 至 USER10）。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{USER1|USER2|USER3|USER4|USER5|USER6|USER7|USER8|USER9|USER10}</td><td>离散型</td><td>USER1|USER2|USER3|USER4|USER5|USER6|USER7|USER8|USER9|USER10</td><td>无</td></tr></table>

# 说明

USER1 至 USER10 分别表示存储在仪器内部存储器状态文件存储位置 1至 10 的文件，仅当内部存储器中指 定位置已存有状态文件时，可以删除该状态文件。 

# 举例

假设仪器内部存储器中状态文件存储位置 1 已存有状态文件， 

:SYSTem:PRESet:DELete USER1 /*删除仪器内部存储器中状态文件存储位置 1 已存的状态文件*/ 

# :SYSTem:PRESet:RECall

# 命令格式

:SYSTem:PRESet:RECall 

{DEFault|USER1|USER2|USER3|USER4|USER5|USER6|USER7|USER8|USER9|USER10} 

# 功能描述

将仪器恢复至默认状态（DEFault）或调用仪器内部存储器中指定的用户已存储的状态文件（USER1 至 USER10）。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{DEFault|USER1|USER2|USER3|USER4|USER5|USER6|USER7|USER8|USER9|USER10}</td><td>离散型</td><td>DEFault|USER1|USER2|USER3|USER4|USER5|USER6|USER7|USER8|USER9|USER10</td><td>无</td></tr></table>

# 说明

USER1 至 USER10 分别表示存储在仪器内部存储器状态文件存储位置 1至 10 的文件，仅当内部存储器中指 定位置已存有状态文件时，可以调用该状态文件。 

假设仪器内部存储器中状态文件存储位置 1 已存有状态文件， 

:SYSTem:PRESet:RECall USER1 /*调用仪器内部存储器中状态文件存储位置 1 已存的状态文件*/ 

# :SYSTem:PRESet:SAVe

# 命令格式

:SYSTem:PRESet:SAVe {USER1|USER2|USER3|USER4|USER5|USER6|USER7|USER8|USER9|USER10} 

# 功能描述

保存当前系统状态至仪器内部存储器中指定的用户存储位置（USER1至 USER10）。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{USER1|USER2|USER3|USER4|USER5|USER6|USER7|USER8|USER9|USER10}</td><td>离散型</td><td>USER1|USER2|USER3|USER4|USER5|USER6|USER7|USER8|USER9|USER10</td><td>无</td></tr></table>

# 举例

:SYSTem:PRESet:SAVe USER1 /*保存系统状态至仪器内部存储器中状态文件存储位置 ${ 1 ^ { \star } } /$ 

# :SYSTem:PRESet[:STATe]?

# 命令格式

:SYSTem:PRESet[:STATe]? 

# 功能描述

查询用户自定义的十组系统状态名称。 

# 返回格式

返回十组系统状态名称。若在 User n 中保存了当前系统状态，则显示其名称，如 "Default","","User2","","","","","","","",""。 

# :SYSTem:ROSCillator:SOURce

# 命令格式

:SYSTem:ROSCillator:SOURce {INTernal|EXTernal} 

:SYSTem:ROSCillator:SOURce? 

# 功能描述

选择系统时钟源为内部源（INTernal）或外部源（EXTernal）。 

查询系统时钟源的类型。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>{INTERNAL|EXTERNAL}</td><td>离散型</td><td>INTERNAL|EXTERNAL</td><td>INTERNAL</td></tr></table>

# 说明

DG2000提供内部 10MHz 的时钟源，也接收从后面板 [10MHz In/Out] 连接器输入的外部时钟源， 还可以从 [10MHz In/Out] 连接器输出时钟源，供其他设备使用。 

若选择外部源，系统将检测后面板 [10MHz In/Out] 连接器是否有有效的外部时钟信号输入。若没 有检测到有效的时钟源，则弹出相应提示消息，并将时钟源切换成内部。 

您可以通过时钟源的设置使两台仪器或多台仪器之间同步。 

两台仪器的同步： 

将仪器 A（时钟源设为“INTernal”）后面板 [10MHz In/Out] 连接器的输出连接到仪器 B（时钟源 设为“EXTernal”）的 [10MHz In/Out] 连接器，然后将两台仪器设置相同的输出频率，即可实现两 

台仪器的同步。 

多台仪器的同步： 

将一台仪器（时钟源设为“INTernal”）的 10MHz 时钟源分成多路，然后分别连接至多台仪器（时钟 源设为“EXTernal”）后面板的 [10MHz In/Out] 连接器，最后将每台仪器设置相同的输出频率，即 可实现多台仪器的同步。 

# 返回格式

返回 INT 或 EXT。 

# 举例

:SYST:ROSC:SOUR INT /*选择系统时钟源为内部源*/ 

:SYST:ROSC:SOUR? /*查询系统时钟源的类型，返回 INT*/ 

# :TRIGger 命令

:TRIGger 命令用于设置触发源类型、触发输入边沿类型和触发延时以及产生一次触发事件。 

# 命令列表：

:TRIGger[<n>]:DELay 

:TRIGger[<n>][:IMMediate] 

:TRIGger[<n>]:SLOPe 

$\spadesuit$ :TRIGger[<n>]:SOURce 

# :TRIGger[<n>]:DELay

# 命令格式

:TRIGger[ $\mathsf { < n > j }$ ]:DELay {<seconds $>$ |MINimum|MAXimum} 

:TRIGger[ $\cdot < n > ]$ ]:DELay? [MINimum|MAXimum] 

# 功能描述

设置指定通道的脉冲串（Burst）延时。 

查询指定通道的脉冲串（Burst）延时。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>整型</td><td>1|2</td><td>1</td></tr><tr><td>&lt;seconds&gt;</td><td>实型</td><td>见下文“说明”</td><td>0s</td></tr></table>

# 说明

脉冲串延时是指信号发生器从接收到触发信号到开始输出 N循环或无限脉冲串之间的时间，仅适用于 N 循环和无限脉冲串模式。 

对于外部触发或手动触发（[:SOURce[<n>]]:BURSt:TRIGger:SOURce）的 N 循环或无限脉冲串模式， <delay $>$ 的范围为 0s 至 100s。 

对于内部触发 N 循环脉冲串模式，<delay $>$ 的范围为 0s 至 $ { ' } P _ { b u r s t } - P _ { w a v e f o r m } \times N _ { c y c l e } - 2  { \mathrm { u s } }$ )且小于等于 100s。 

其中， 

Pburst $P _ { b u r s t }$ 猝发周期； 

Pwaveform 波形周期（即脉冲串函数（正弦波、方波等）的周期）； 

$N _ { c y c l e }$ 循环数。 

省略参数 $[ < n > ]$ 时，默认设置 CH1的脉冲串延时。 

# 返回格式

以科学计数形式返回脉冲串延时，有效位数为 7位，如 1.000000E $+ 0 0$ ，表示脉冲串延时为 1s。 

# 举例

:TRIG:DEL 1 /*设置 CH1的脉冲串延时为 ${ 1 s ^ { \star } } /$ 

:TRIG:DEL? /*查询 CH1 的脉冲串延时，返回 1.000000E+00*/ 

# :TRIGger[<n>][:IMMediate]

# 命令格式

:TRIGger $\angle 1 = 1 7 .$ ] [:IMMediate] 

# 功能描述

在指定通道产生一次触发。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr></table>

# 说明

该命令仅适用于手动触发（:TRIGger[<n>]:SOURce）脉冲串输出（[:SOURce[<n>]]:BURSt[:STATe]） 或扫频输出（[:SOURce[<n>]]:SWEep:STATe）。 

省略参数[<n>]时，默认在 CH1产生一个触发事件。 

如果对应通道的输出没有打开，触发将被忽略。 

# 举例

:TRIG1 /*在 CH1 产生一次触发*/ 

# :TRIGger[<n>]:SLOPe

# 命令格式

:TRIGger[ $\tt { < n > }$ ]:SLOPe {POSitive|NEGative} 

:TRIGger[<n>]:SLOPe? 

# 功能描述

设置指定通道触发输入信号的边沿类型为上升沿（POSitive）或下降沿（NEGative）。 

查询指定通道触发输入信号的边沿类型。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{POSitive|NEGative}</td><td>离散型</td><td>POSitive|NEGative</td><td>POSitive</td></tr></table>

# 说明

该命令仅适用于选择外部触发（:TRIGger[<n>]:SOURce）的脉冲串（N 循环、无限或门控）输出 （[:SOURce[<n>]]:BURSt[:STATe]）或扫频输出（[:SOURce[<n>]]:SWEep:STATe）。选择外部触发时， 信号发生器接收从后面板相应通道的 [Sync/Ext Mod/Trig/FSK] 连接器输入的触发信号，每次接收 到一个具有指定极性的 TTL 脉冲时，就启动一次脉冲串（N循环、无限或门控）输出或扫频输出。 

省略参数 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

# 返回格式

返回 POS 或 NEG。 

# 举例

:TRIG1:SLOP NEG /*设置 CH1触发输入信号的边沿类型为下降沿*/ :TRIG1:SLOP? /*查询 CH1触发输入信号的边沿类型，返回 NEG*/ 

# :TRIGger[<n>]:SOURce

# 命令格式

:TRIGger[ $\cdot < n >$ ]:SOURce {INTernal|EXTernal|BUS} :TRIGger[ $< n >$ ]:SOURce? 

# 功能描述

选择指定通道的触发源为内部（INTernal）、外部（EXTernal）或手动（BUS）。 查询指定通道的触发源类型。 


参数


<table><tr><td>名称</td><td>类型</td><td>范围</td><td>默认值</td></tr><tr><td>[&lt;n&gt;]</td><td>离散型</td><td>1|2</td><td>1</td></tr><tr><td>{INTERNAL|EXTERNAL|BUS}</td><td>离散型</td><td>INTERNAL|EXTERNAL|BUS</td><td>INTERNAL</td></tr></table>

# 说明

该命令仅适用于脉冲串（N 循环、无限或门控）输出或扫频输出。 

 N循环脉冲串和扫频模式支持内部触发。选择内部触发时，N循环脉冲串的频率由“猝发周期”（脉冲 串周期）决定；扫频波形的触发周期由指定的扫描时间、返回时间、起始保持和终止保持时间决定。您 还可以设置后面板相应通道的 [Sync/Ext Mod/Trig/FSK] 连接器输出具有指定边沿（上升沿或下降 沿）的触发信号或关闭触发输出信号。 

N循环、无限和门控脉冲串以及扫频模式均支持外部触发。选择外部触发时，信号发生器接收从后面板 相应通道的 [Sync/Ext Mod/Trig/FSK] 连接器输入的触发信号，每次接收到一个具有指定极性的 TTL脉冲时，就启动一次脉冲串（N循环、无限或门控）输出或扫频输出。您可以指定触发输入信号的 边沿类型（:TRIGger[<n>]:SLOPe）。 

N循环和无限脉冲串以及扫频模式均支持手动触发。选择手动触发时且对应通道的输出打开时，发送 *TRG、:TRIGger[<n>][:IMMediate]或[:SOURce[<n>]]:BURSt:TRIGger[:IMMediate]命令可输出 N 循 环或无限脉冲串；每发送一次*TRG、:TRIGger[<n>][:IMMediate]或 [:SOURce[<n>]]:SWEep:TRIGger[:IMMediate]命令立即在相应通道启动一次扫频。如果对应通道的输 出没有打开，触发将被忽略。您还可以设置后面板相应通道的 [Sync/Ext Mod/Trig/FSK] 连接器输 出具有指定边沿（上升沿或下降沿）的触发信号或关闭触发输出信号。 

省略参数 $[ < n > ]$ 时，默认设置 CH1的相关参数。 

# 返回格式

返回 INT、EXT 或 BUS。 

# 举例

:TRIG1:SOUR INT /*选择 CH1的触发源为内部*/ :TRIG1:SOUR? /*查询 CH1的触发源类型，返回 INT*/ 

# 第3章 应用实例

本章给出 SCPI 命令的应用实例，通过将一系列 SCPI 命令组合实现信号源的主要功能。 

# 注意：

1. 本章所列实例以 DG2102 为例。对于其它型号，某些参数的范围可能不同，使用时，请根据您所使用的 仪器型号进行相应调整。 

2. 使用本章所列实例之前，请选择通信接口（USB、LAN 或 GPIB）并进行正确的连接，参考“建立远程 通信”中的介绍。并且，您的计算机需要安装 Ultra Sigma 或其它可用于发送命令的 PC 软件。 

3. 本章所列实例每行命令之后由“/*”和“*/”包括的内容为注释部分，用于帮助用户理解，并非命令内 容。 

# 本章内容如下：

$\spadesuit$ 输出基本波 

$\spadesuit$ 输出任意波 

$\spadesuit$  输出谐波 

$\spadesuit$ 输出 AM 调制波形 

$\spadesuit$ 输出 FSK 调制波形 

$\spadesuit$ 输出 Sweep 波形 

$\spadesuit$ 输出 Burst 波形 

$\spadesuit$ 使用频率计功能 

# 输出基本波

# 要求

使用 SCPI 命令实现如下功能： 

从 CH1前面板输出连接器输出一个正弦波，频率为 500Hz，幅度为 $2 . 5 \mathsf { V p p }$ ，偏移电压为 1Vdc，起始相位为 $9 0 ^ { \circ }$ 。 

# 实现方法 1

1. *IDN? /*查询信号源 ID 字符串以检测远程通信是否正常*/ 

2. :SOUR1:APPL:SIN 500,2.5,1,90 $/ ^ { \star }$ 设置 CH1 的波形为正弦波且频率为 500Hz，幅度为 $2 . 5 \mathsf { V } \mathsf { p } \mathsf { p }$ 偏移为 $\mathsf { 1 V _ { d c } }$ ，起始相位为 $9 0 ^ { \circ \star } /$ 

3. :OUTP1 ON /*打开 CH1 的输出*/ 

# 实现方法 2

1. *IDN? /*查询信号源 ID 字符串以检测远程通信是否正常*/ 

2. :SOUR1:FUNC SIN $/ ^ { \star }$ 设置 CH1的波形为正弦波*/ 

3. :SOUR1:FREQ 500 /*设置 CH1的波形频率为 $5 0 0 \mathsf { H z } ^ { \star } /$ 

4. :SOUR1:VOLT 2.5 /*设置 CH1 的波形幅度为 $2 . 5 \mathsf { V p p } ^ { \star } /$ 

5. :SOUR1:VOLT:OFFS 1 /*设置 CH1的偏移电压为 ${ 1 } \mathsf { V } _ { \mathrm { d c } } { } ^ { \star } /$ 

6. :SOUR1:PHAS 90 /*设置 CH1的起始相位为 $9 0 ^ { \circ \star } /$ 

7. :OUTP1 ON /*打开 CH1 的输出*/ 

# 输出任意波

# 要求

使用 SCPI 命令实现如下功能： 

从 CH1前面板输出连接器输出任意波，频率设为 100Hz，幅度为 1Vpp，偏移为 $2 V _ { \mathrm { d c } }$ ，起始相位为 $3 ^ { \circ }$ 。 

# 实现方法

1. *IDN? /*查询信号源 ID 字符串以检测远程通信是否正常*/ 

2. :SOUR1:APPL:USER 100,1,2,3 /*设置 CH1的波形为任意波且频率为 $1 0 0 \mathsf { H z }$ ，幅度为 ${ 1 } \mathsf { V } \mathsf { p } \mathsf { p }$ ，偏 移为 $2 V _ { \mathrm { d c } }$ ，起始相位为 $3 ^ { \circ \star } /$ 

3. :OUTP1 ON /*打开 CH1 的输出*/ 

# 输出谐波

# 要求

使用 SCPI 命令实现如下功能： 

从 CH1前面板输出连接器输出谐波，基波（正弦波）参数为频率 1kHz、幅度 5Vpp、偏移电压 0Vdc、起始 相位 $0 ^ { \circ }$ ，最高谐波次数为 4 次，谐波类型为偶次谐波，2次谐波的谐波幅度和谐波相位分别为 2Vpp 和 $3 0 ^ { \circ }$ ， 4次谐波的谐波幅度和谐波相位分别为 1Vpp 和 $5 0 ^ { \circ }$ 。 

# 实现方法

1. *IDN? /*查询信号源 ID 字符串以检测远程通信是否正常*/ 

2. :SOUR1:APPL:SIN 1000,5,0,0 /*设置 CH1的波形为正弦波且频率为 1kHz，幅度为 5Vpp，偏 移为 $0 \mathsf { V } _ { \mathrm { d c } }$ ，起始相位为 $0 ^ { \circ \star } /$ 

3. :SOUR1:HARM ON /*打开 CH1 的谐波功能*/ 

4. :SOUR1:HARM:ORDE 4 /*设置 CH1可输出的最高谐波次数为 4次*/ 

5. :SOUR1:HARM:TYP EVEN $/ ^ { \star }$ 设置 CH1的谐波类型为偶次谐波*/ 

6. :SOUR1:HARM:AMPL 2,2 $/ ^ { \star }$ 设置 CH1 的 2 次谐波的谐波幅度为 ${ 2 \mathsf { V } \mathsf { p } \mathsf { p } ^ { \star } } /$ 

7. :SOUR1:HARM:PHAS 2,30 /*设置 CH1的 2次谐波的谐波相位为 $3 0 ^ { \circ \star } /$ 

8. :SOUR1:HARM:AMPL 4,1 /*设置 CH1的 4次谐波的谐波幅度为 ${ 1 } \mathsf { V p p } ^ { \star } /$ 

9. :SOUR1:HARM:PHAS 4,50 /*设置 CH1的 4次谐波的谐波相位为 $5 0 ^ { \circ } { } ^ { \star } /$ 

10. :OUTP1 ON /*打开 CH1 的输出*/ 

# 输出 AM 调制波形

# 要求

使用 SCPI 命令实现如下功能： 

从 CH1前面板输出连接器输出 AM 调制波形，选择载波波形为正弦波（频率为 1kHz，幅度为 5Vpp，偏移电 压为 0Vdc，起始相位为 $0 ^ { \circ }$ ），选择内部调制源且调制波形选择正弦波，调制深度为 $80 \%$ ，调制频率为 200Hz， 打开载波抑制功能。 

# 实现方法

1. *IDN? /*查询信号源 ID 字符串以检测远程通信是否正常*/ 

2. :SOUR1:APPL:SIN 1000,5,0,0 /*设置 CH1 的波形为正弦波且频率为 1kHz，幅度为 5Vpp，偏 移为 $0 \mathsf { V } _ { \mathrm { d c } }$ ，起始相位为 $0 ^ { \circ \star } /$ 

3. :SOUR1:AM:STAT ON /*打开 CH1 的 AM 调制功能*/ 

4. :SOUR1:AM:SOUR INT /*设置 CH1的 AM 调制信号源为内部调制源*/ 

5. :SOUR1:AM:INT:FUNC SIN $/ ^ { \star }$ 设置 CH1的 AM 调制波形为正弦波*/ 

6. :SOUR1:AM 80 $/ ^ { \star }$ 设置 CH1的 AM 调制深度为 $8 0 \% ^ { \star } /$ 

7. :SOUR1:AM:INT:FREQ 200 $/ ^ { \star }$ 设置 CH1的 AM 调制频率为 $2 0 0 \mathsf { H z } ^ { \star } /$ 

8. :SOUR1:AM:DSSC ON /*打开 CH1 的 AM 载波抑制功能*/ 

9. :OUTP1 ON /*打开 CH1 的输出*/ 

# 输出 FSK 调制波形

# 要求

使用 SCPI 命令实现如下功能： 

从 CH1前面板输出连接器输出 FSK 调制波形，选择载波波形为正弦波（频率为 1kHz，幅度为 5Vpp，偏移 电压为 0Vdc，起始相位为 $0 ^ { \circ }$ ），选择外部调制源，跳跃频率为 2kHz，调制极性为正极性。 

# 实现方法

1. *IDN? /*查询信号源 ID 字符串以检测远程通信是否正常*/ 

2. :SOUR1:APPL:SIN 1000,5,0,0 $/ ^ { \star }$ 设置 CH1 的波形为正弦波且频率为 1kHz，幅度为 5Vpp，偏 移为 $0 \mathsf { V } _ { \mathrm { d c } }$ ，起始相位为 $0 ^ { \circ \star } /$ 

3. :SOUR1:FSK:STAT ON /*打开 CH1 的 FSK 调制功能*/ 

4. :SOUR1:FSK:SOUR EXT /*设置 CH1的 FSK 调制信号源为外部调制源*/ 

5. :SOUR1:FSK 2000 $/ ^ { \star }$ 设置 CH1的 FSK 跳跃频率为 $2 \mathsf { k H z } ^ { \star } /$ 

6. :SOUR1:FSK:POL POS /*设置 CH1的 FSK 调制极性为正极性*/ 

7. :OUTP1 ON /*打开 CH1 的输出*/ 

# 输出 Sweep 波形

# 要求

使用 SCPI 命令实现如下功能： 

从 CH1前面板输出连接器输出扫频波形，选择扫频波形为正弦波（幅度为 5Vpp，偏移电压为 0Vdc），扫频 类型为线性扫频，扫频时间为 3s，返回时间为 0.1s，起始频率为 100Hz，终止频率为 1kHz，打开频率标记 功能且标记频率设为 500Hz，起始保持时间为 0.1s，终止保持时间为 0.1s，触发源选择手动触发，触发输出 信号选择上升沿。 

# 实现方法

1. *IDN? /*查询信号源 ID 字符串以检测远程通信是否正常*/ 

2. :SOUR1:FUNC SIN /*设置 CH1的波形为正弦波*/ 

3. :SOUR1:VOLT 5 /*设置 CH1的波形幅度为 $5 \mathsf { V p p } ^ { \star } /$ 

4. :SOUR1:VOLT:OFFS 0 /*设置 CH1的偏移电压为 $0 \mathsf { V } _ { \mathrm { d c } } { } ^ { \star } /$ 

5. :SOUR1:SWE:STAT ON /*打开 CH1 的扫频功能*/ 

6. :SOUR1:SWE:SPAC LIN /*设置 CH1的扫频类型为线性扫频*/ 

7. :SOUR1:SWE:TIME 3 /*设置 CH1的扫频时间为 $3 \mathsf { s } ^ { \star } /$ 

8. :SOUR1:SWE:RTIM 0.1 /*设置 CH1扫频功能的返回时间为 $0 . 1 \mathsf { s } ^ { \star } /$ 

9. :SOUR1:FREQ:STAR 100 /*设置 CH1的扫频功能的起始频率为 $1 0 0 \mathsf { H z } ^ { \star } /$ 

10. :SOUR1:FREQ:STOP 1000 /*设置 CH1的扫频功能的终止频率为 $1 \mathsf { k H z } ^ { \star } /$ 

11. :SOUR1:MARK ON /*启用 CH1扫频功能的频率标记功能*/ 

12. :SOUR1:MARK:FREQ 500 /*设置 CH1扫频功能的标记频率为 $5 0 0 \mathsf { H z } ^ { \star } /$ 

13. :SOUR1:SWE:HTIM:STAR 0.1 /*设置 CH1扫频功能的起始保持时间为 $0 . 1 \mathsf { s } ^ { \star } /$ 

14. :SOUR1:SWE:HTIM 0.1 /*设置 CH1扫频功能的终止保持时间为 $0 . 1 \mathsf { s } ^ { \star } /$ 

15. :SOUR1:SWE:TRIG:SOUR MAN /*设置 CH1的扫频触发源为手动源*/ 

16. :SOUR1:SWE:TRIG:TRIGO POS /*设置 CH1触发输出信号的边沿类型为上升沿*/ 

17. :OUTP1 ON /*打开 CH1 的输出*/ 

18. :SOUR1:SWE:TRIG /*在 CH1 立即触发一次扫频*/ 

# 输出 Burst 波形

# 要求

使用 SCPI 命令实现如下功能： 

从 CH1前面板输出连接器输出脉冲串波形，选择脉冲串波形为正弦波（频率为 1kHz，幅度为 5Vpp，偏移电 压为 0Vdc，起始相位为 $0 ^ { \circ }$ ），脉冲串类型为 N循环且循环数为 10，猝发时间为 0.1s，触发源选择内部触发， 触发输出信号选择下降沿，触发延时为 0.01s。 

# 实现方法

1. *IDN? /*查询信号源 ID 字符串以检测远程通信是否正常*/ 

2. :SOUR1:APPL:SIN 1000,5,0,0 /*设置 CH1的波形为正弦波且频率为 1kHz，幅度为 5Vpp，偏 移为 $0 \mathsf { V } _ { \mathrm { d c } }$ ，起始相位为 $0 ^ { \circ \star } /$ 

3. :SOUR1:BURS ON /*打开 CH1的脉冲串功能*/ 

4. :SOUR1:BURS:MODE TRIG /*设置 CH1的脉冲串类型为 N循环*/ 

5. :SOUR1:BURS:NCYC 10 $/ ^ { \star }$ 设置 CH1的 N 循环脉冲串的循环数为 ${ 1 0 ^ { \star } } /$ 

6. :SOUR1:BURS:INT:PER 0.1 $/ ^ { \star }$ 设置 CH1的 N 循环脉冲串的内部猝发周期为 $0 . 1 \mathsf { s } ^ { \star } /$ 

7. :SOUR1:BURS:TRIG:SOUR INT /*设置 CH1脉冲串模式的触发源类型为内部源*/ 

8. :SOUR1:BURS:TRIG:TRIGO NEG /*设置 CH1脉冲串模式中触发输出信号的边沿类型为下降沿*/ 

9. :SOUR1:BURS:TDEL 0.01 /*设置 CH1的 N 循环脉冲串的触发延时为 $0 . 0 1 \mathrm { s } ^ { \star } /$ 

10. :OUTP1 ON /*打开 CH1 的输出*/ 

11. :SOUR1:BURS:TRIG /*在 CH1 立即触发一次脉冲串输出*/ 

# 使用频率计功能

# 要求

使用 SCPI 命令实现如下功能： 

启用频率计功能，设置仪器根据被测信号的特征自动选择合适的闸门时间，打开统计功能，灵敏度为高，触 发电平为 0.1V，耦合方式为 AC 耦合，打开高频抑制功能，运行状态为运行。 

# 实现方法

1. *IDN? /*查询信号源 ID 字符串以检测远程通信是否正常*/ 

2. :COUN ON /*启用频率计功能*/ 

3. :COUN:AUTO /*设置仪器根据被测信号的特征自动选择合适的闸门时间*/ 

4. :COUN:STATI ON /*打开频率计的测量结果统计功能*/ 

5. :COUN:SENS HIG /*设置频率计的触发灵敏度为高*/ 

6. :COUN:LEVE 0.1 /*设置频率计的触发电平为 $0 . 1 \lor ^ { \star } /$ 

7. :COUN:COUP AC /*设置输入信号的耦合方式为 AC 耦合*/ 

8. :COUN:HF ON /*打开频率计的高频抑制功能*/ 

9. :COUN RUN /*设置频率计的运行状态为运行*/ 

# 第4章 编程实例

本章列出在 Excel、Matlab、LabVIEW、Visual Basic 和 Visual $\complement + +$ 等环境下基于 NI-VISA 使用 SCPI 命令编 程控制信号源的实例。 

NI-VISA（National Instrument-Virtual Instrument Software Architecture）是美国国家仪器 NI（National Instrument）公司开发的一种用来与各种仪器总线进行通信的高级应用编程接口，它以相同的方法与仪器通 信而不考虑仪器的接口类型（GPIB、USB、LAN/以太网或者 RS232）。 

它将通过各种接口与之通信的仪器称为“资源”，使用 VISA 描述符（即“资源名称”）描述 VISA 资源的准确 名称与位置。进行编程之前，请获取正确的 VISA 描述符。 

# 本章内容如下：

 编程准备 

$\spadesuit$  Excel 编程实例 

 Matlab 编程实例 

$\spadesuit$  LabVIEW 编程实例 

$\spadesuit$  Visual Basic 编程实例 

 Visual $\underline { { \mathsf { C } + + } }$ 编程实例 

# 编程准备

编程之前，您需要做如下准备工作： 

1. 安装 Ultra Sigma 通用 PC 软件。请登陆 RIGOL 官网（www.rigol.com）下载该软件，然后按照指导进 行安装。安装 Ultra Sigma 后，NI-VISA 库已自动安装完成。本文默认安装路径为 C:\Program Files\IVI Foundation\VISA。 

2. 本文应用信号源的 USB DEVICE 接口与计算机通信。请使用 USB 数据线将信号源后面板的 USB DEVICE 接口与计算机相连。您也可以使用 LAN或 GPIB 等远程接口与 PC 通信。 

3. 信号源与计算机正确连接后，请给信号源上电并开机。 

4. 此时，计算机上将弹出“硬件更新向导”对话框，请按照向导的提示安装“USB Test and Measurement Device (IVI)”（请参考《DG2000用户手册》第 3章“远程控制”中的“通过 USB 控制”一节）。 

![](images/d9d15dd25261b2c8637f46f2d049e1359bfc4774c5e221439b2218052ffd94c1.jpg)


5. 获取信号源的 USB VISA 描述符：在 Shift 键背灯变亮状态，按 Pulse/Utility 接口设置 USB ， USB ID 显示在界面上部。本实例使用的信号源的 USB ID 为 USB0::0x1AB1::0x0642::DG20000000001::INSTR。 

至此，编程准备工作结束。 

# Excel 编程实例

本例使用的程序：Microsoft Excel 2007 

本例实现的功能：发送*IDN?命令，读取设备信息。 

1. 新建一个启用宏的 Excel 文件，本实例命名为 DG2000_Demo_Excel.xlsm。 

2. 运行 DG2000_Demo_Excel.xlsm 文件，单击 Excel 文件左上角的 Office 按钮，点击“Excel 选项(I)”， 打开如下图所示界面，勾选“在功能区显示“开发工具”选项卡(D)”，点击“确定”。此时，Excel 的菜单栏将显示“开发工具”菜单。 

![](images/7536427ccefe85465827c390df70253b4287a61c22c596e2046d2e5b926c5cd9.jpg)


3. 将 USB ID 填入 Excel 文件的一个单元格中。单击“开发工具”菜单，选择“Visual Basic”选项，打开 Microsoft Visual Basic。 

4. 在 Microsoft Visual Basic 的菜单栏选择“工具(T)”并点击“引用(R)”。 

在弹出的对话框中选中“VISA Library”，单击“确定”按钮即可引用 VISA Library。 

![](images/3542818279a23b9ea3f96139a71d8b1100e26148a4ad05051864cd88fa93e9c8.jpg)


# 说明：

如果您在上图左侧的列表中无法找到 VISA Library，请按照如下方法查找： 

(1) 请确保您的计算机已经安装 NI-VISA 库。 

(2) 点击右侧的“浏览（B）…”进行查找，查找范围为 C:\WINDOWS\system32，文件名为 visa32.dll， 如下图所示。 

![](images/64f996e681d75eb47b6e1cfa25e8b255b05e92bfb8a568ee4310bdbfb7b8906c.jpg)


5. 在 Excel 文件的“开发工具”菜单下点击“查看代码”，进入 Microsoft Visual Basic 页面，添加如下代 码（字体颜色为绿色的部分为注释）到 DG2000_Demo_Excel.xlsm – Sheet1（代码）窗口并保存。 

Sub QueryIdn() 

Dim viDefRm As Long 

Dim viDevice As Long 

Dim viErr As Long 

Dim cmdStr As String 

Dim idnStr As String * 128 

Dim ret As Long 

‘打开设备，设备资源描述符在 SHEET1 的 CELLS(1,2)中’ 

viErr $=$ visa.viOpenDefaultRM(viDefRm) 

viErr $=$ visa.viOpen(viDefRm, Sheet1.Cells(1, 2), 0, 5000, viDevice) 

‘发送请求，读取数据，返回值在 SHEET1 的 CELLS(2,2)中’ 

cmdStr $=$ "*IDN?" 

viErr $=$ visa.viWrite(viDevice, cmdStr, Len(cmdStr), ret) 

viErr $=$ visa.viRead(viDevice, idnStr, 128, ret) 

Sheet1.Cells(2, 2) $=$ idnStr 

‘关闭设备’ 

visa.viClose (viDevice) 

visa.viClose (viDefRm) 

# End Sub

注意：若第 2步新建的 Excel 文件不是启用宏的文件，此时，将弹出“无法在未启用宏的工作薄中保存 以下功能”的提示消息，此时，请根据提示将工作薄保存为启用宏的文件即可。 

6. 添加按钮控件：在 Excel 文件中“开发工具”菜单下点击“插入”，在“表单控件”下选择所需的按钮 后点击一个 Excel 单元格将按钮放在其中。此时，弹出“指定宏”界面，选中“Sheet1.QueryIdn”， 单击“确定”即可。 

![](images/2f8dcd6ee50786824350a8bc0a36382f0e5a664975191514e5fcddc32ad14cfe.jpg)


按钮默认的名称为“按钮 1”。右击按钮，在弹出的菜单中选择“编辑文字(X)”，将按钮名称改为“*IDN?”。 

7. 点击上一步在 Excel 文件中插入的“*IDN?”按钮运行程序，返回设备信息。 

![](images/139a7ae6a075fef2c26db06a8f9d04b9f84c43c8b40d8af6450927eae2dde3a2.jpg)


# Matlab 编程实例

本例使用的程序：MATLAB R2009a 

本例实现的功能：查询 CH1的当前波形类型及其频率、幅度、偏移和相位值。 

1. 运行 Matlab 软件并修改当前路径（即修改软件上方的 Current Directory）。本实例将当前路径修改为 E:\DG2000_Demo_Matlab。 

![](images/9c8a499985a628fb9e925416fef62164aed3fe4d5d487d918cb1a21332e8f648.jpg)


2. 点击 Matlab 界面的 File New Blank M-File 创建一个空白的 M 文件。 

![](images/d79ef7b12798efe0bee9c49511a7e84d864c927a5a259f7e7ba57937eb5d7539.jpg)


3. 在 M 文件中添加如下代码： 

```txt
DG2000 = visa('ni','USB0::0x1AB1::0x0642::DG80000000001::INSTR'); %创建VISA对象 
```

fopen(DG2000); %打开已创建的VISA对象 

fprintf(DG2000, ':SOURce1:APPLy?' ); %发送请求 

query_CH1 $=$ fscanf(DG2000); %查询数据 

fclose(DG2000); %关闭VISA对象 

display(query_CH1) %显示已读取的设备信息 

4. 将 M 文件保存在当前路径下。本实例的 M 文件命名为 DG2000_Demo_MATLAB.m。 

5. 运行 M 文件。命令窗口显示如下运行结果： 

![](images/82fdea2dc0cd87e45a6042811c7792f1bfccc4a691f40d837e0fa42e491f3275.jpg)


# LabVIEW 编程实例

本例使用的程序：LabVIEW 2009 

本例实现的功能：查找仪器地址、连接仪器、发送命令并读取返回值。 

1. 运行 LabVIEW 2009，新建一个 VI 文件，命名为 DG2000_Demo_LABVIEW。 

2. 在前面板界面添加控件，包括地址栏、命令栏和返回值栏以及连接、写入、读取和退出按钮。 

![](images/19de931c3b6aa651ede0cf20d164c2baa9201cccf0a6a72ae7dcb8bca9ea0955.jpg)


3. 点击 Window 菜单下的“Show Block Diagram”，创建事件结构。 

![](images/35fc3deed40ea84265e5d0335a13bef7b07c355ec9057994ac8855ee95056482.jpg)


![](images/ba650fc05edcecddc25c554cf65b8e0ff5c7835e68dac4042c4adbef8e16234f.jpg)


4. 添加事件，包括连接仪器、写操作、读操作和退出。 

# (1) 连接仪器（包括出错处理）：

![](images/b8ff82526fabfc8267e1031d0eec3c9bf5c9b63a28f6aa0efda85440c93c800b.jpg)


![](images/c92a6cc0a090405ec18deea3a4cc8db74b13cd1c49128e727acf663d3dc2af0f.jpg)


![](images/539fc073ce0c0a5303371ecac22a65cb3c672cc8097e0e113885e5322a4fec95.jpg)


![](images/3821c8d1ce5c65ff3db4ada9946e6e57ff69a72bf211eb92500ddd18468bd0de.jpg)


# (2) 写操作（包括出错判断）：

![](images/4a6c11fc06250dae4fd3febf527c715170d8722a32a1c050e8adc68e843ae6e0.jpg)


![](images/4024842e1b3a070ae3f3362ad8969cd010d3e47699393f6f0f9a88c66c7232b3.jpg)


# (3) 读操作（包括出错处理）：

![](images/268eb1fa92bd73c49f0655c6c8cbfe897769e55aff7f1967f79ca1323a89acd4.jpg)


![](images/365bb837a4d3463f5e11cccc5ae7eff036c92c12d73f2552520aaea202768bd9.jpg)


(4) 退出： 

![](images/bcadd55bcc2f8a08b3d2e10ee4ee7492fd42c844543d1d1abfdd46da67d394db.jpg)


5. 运行程序，出现如下图所示界面。点击“Address”下拉框选择 VISA 资源名称，点击“Connect”按钮 连接仪器，在“Command”文本框中输入命令，点击“Write”按钮写入仪器。若为查询命令，点击“Read” 按钮，“Return”文本框显示返回值。 

![](images/5414b2ce65f05137f425e88b68e4176c619203810197a7fb8126161773baf0f8.jpg)


# Visual Basic 编程实例

本例使用的程序：Visual Basic 6.0 

本例实现的功能：打开信号源的两个通道并显示通道对应的颜色。 

1. 运行 Visual Basic 6.0，新建一个标准应用程序工程（Standard EXE），命名为 DG2000_Demo_VB。 

2. 点击 ProjectAdd Module 的 Existing 选项卡，在 NI-VISA 安装路径下的 include 文件夹中查找 visa32.bas 文件并添加。 

![](images/4ca5b5ed73b9b6b16382d9ccb74fa9452926a556f0acd8710d0b2c3c703f9266.jpg)


3. 添加两个 Command Button 控件分别表示 CH1 和 CH2，添加两个 Label 控件分别表示两个通道的状态 （默认显示灰色，通道打开时显示通道对应的颜色），分别为 Label1(0)、Label1(1)。布局如下图所示。 

![](images/0c84930912b6a4d40ae8d52caf5a24a3e9412d5301fcd61651fe4abb854653d6.jpg)


4. 打开 ProjectProject1 Properties 中的“General”选项卡，在“Startup Object”下拉框中选择“Form1”。 

![](images/0cf4794f207d21193a821c9fef4f82299176b6697f96e6a79bd52f65ba558ff8.jpg)


5. 双击 CH1 按钮进入编程环境，添加如下代码，即可实现对 CH1 和 CH2 的控制。以下为 CH1 的代码， CH2代码类似。 

```txt
Dim defrm As Long  
Dim vi As Long  
Dim strRes As String * 200  
Dim list As Long  
Dim nmatches As Long  
Dim matches As String * 200 
```

```txt
获得 visa 的 usb 资源  
Call viOpenDefaultRM(defrm)  
Call viFindRsrc(defrm, "USB?*, list, nmatches, matches) 
```

```txt
打开设备 Call viOpen.defrm, matches, 0, 0, vi) 
```

```txt
发送询问CH1状态命令Call viVPrintf(vi,":OUTP1?"+Chr$(10),0) 
```

```txt
获取CH1状态  
Call viVScanf(vi, "%t", strRes)  
If strRes = "ON" Then 
```

```txt
发送设置命令  
Call viVPrintf(vi,":OUTPUT1 OFF" + Chr$(10), 0)  
Label1(0).ForeColor = &H808080 '灰色 
```

```txt
Else
Call viVPrintf(vi, ':OUTPUT1 ON" + Chr$(10), 0)
Label1(0).ForColor = &HFFFF& '黄色
End If 
```

```txt
关闭资源  
Call viClose(vi)  
Call viClose.defrm) 
```

6. 运行并查看结果，如下图所示。 

![](images/5331e00dbc01e561d62dc7d164b3c39ab4b57c97909d9087a7a3c2e092f04739.jpg)


![](images/facb96c2327f4c8d746388ae3f8aa939b55ecab0f92779840e2f27aa065761c6.jpg)


1) 点击 CH1 按钮打开 CH1，CH1按钮上方显示红色； 

2) 点击 CH2 按钮打开 CH2，CH2按钮上方显示蓝色。 

运行结果如下图所示： 

![](images/fe26f796ff392c3c3a85b31da70582985243e2203665025594d29eed9ead80c1.jpg)


# Visual $\mathbb { C } + +$ 编程实例

本例使用的程序：Microsoft Visual $\mathsf { C } + + 6 . 0$ 

本例实现的功能：查找仪器地址、连接仪器、发送命令并读取返回值。 

1. 运行 Microsoft Visual $\mathsf { C } + + 6 . 0$ ，新建一个基于对话框的 MFC 工程，命名为 DG2000_Demo_VC。 

2. 点击 Project Settings，在弹出界面的“Link”选项卡下手动添加 visa32.lib。 

![](images/eb6d7dc72f447bc1d951fcac480517cbe2d0183242a8bba2c46efc7c65642af9.jpg)


![](images/d4c22d38095107da1e86a3ecb92c7b9cd1cc727a81309733fbc18476a428ed73.jpg)


# 3. 点击 Tools Options，

![](images/f599329ab8a6f8904996cbe8d42145a2203f15087e4ebcf81024cac40eb38204.jpg)


在弹出界面的“Directories”选项卡中添加 Include 和 Lib 路径： 

# 注意：

此处添加的两个路径与您计算机上 NI-VISA 的安装路径相关。此处默认为 NI-VISA 安装在 C:\Program Files\IVI Foundation\VISA 路径下。 

在“Show directories for”中选择 Include files，双击“Directories”选框中的空白处添加 Include 的路 径：C:\Program Files\IVI Foundation\VISA\WinNT\include。 

![](images/3caa8f0173849d505abb4679047da002fc26b073ae125cbea231c995ecd83329.jpg)


在 Show directories for 中选择 Library files，双击 Directories 选框中的空白处添加 Lib 的路径：C:\Program Files\IVI Foundation\VISA\WinNT\lib\msc。 

![](images/6e6e0c51b13de5afec7369db0aeb84fabddd99e137e787f06b7410688ee27a11.jpg)


4. 添加 Text、Edit 和 Button 控件，布局如下图所示，其中 Address、Command 和 Return 是 Text 控件， Connect、Send 和 Read 是 Button 控件，3 个 Edit 均为 Edit 控件，且第 3 个 Edit 控件为只读（Read-only） 控件。 

![](images/d9beb8a8da030610abcafbeb49a02bfdbff41ae4a178be4202a0f24a0743afcf.jpg)


5. 点击 ViewClassWizard，在弹出界面的“Member Variables”选项卡中添加控件变量： 

仪器地址 CString m_strInstrAddr 命令 CString m_strCommand 返回值 CString m_strResult 

![](images/3899bd723038245c1bc8db4c3c96fd3c949044bb16db504d0d70791e064a8864.jpg)


6. 封装 VISA 的读和写操作。 

1) 对 VISA 的写操作进行封装便于操作。 

bool CDG2000_Demo_VCDlg::InstrWrite(CString strAddr, CString strContent) //write function { 

ViSession defaultRM,instr;   
ViStatus status;   
ViUInt32 retCount;   
char \* SendBuf $=$ NULL;   
char \* SendAddr $=$ NULL;   
bool bWriteOK $=$ false;   
CString str;   
//Change the address's data style from CString to char\*   
SendAddr $=$ strtok.GetBuffer(strAddr-length());   
strcpy(SendAddr,strAddr);   
strAddrReleaseBuffer();   
//Change the command's data style from CString to char\*   
SendBuf $=$ strtok.GetBuffer(strContent-Length());   
strcpy(SendBuf,strContent);   
strContent_ReleaseBuffer(); 

```txt
//open the VISA instrument  
status = viOpenDefaultRM(&defaultRM);  
if (status < VI_SUCCESS)  
{  
    AfxMessageBox("No VISA instrument was opened!");
    return false; 
```

}   
status $=$ viOpen(defaultRM, SendAddr, VI_NULL, VI_NULL, &instr); //write command to the instrument status $=$ viWrite(instr, (unsigned char \*)SendBuf, strlen(SendBuf), &retCount); //close the instrument status $=$ viClose(instr); status $=$ viClose(defaultRM); return bWriteOK; 

2) 对 VISA 的读操作进行封装便于操作。 

```cpp
bool CDG2000_Demo_VCDlg::InstrRead(CString strAddr, CString *pstrResult) //Read from the instrument  
{ ViSession defaultRM,instr; ViStatus status; ViUInt32 retCount; char * SendAddr = NULL; unsigned char RecBuf[MAX_REC_SIZE]; bool bReadOK = false; CString str; 
```

//Change the address's data style from CString to char\*   
Addr $=$ strAddr.GetBuffer(strAddr lengths));   
strcpy SendAddr,strAddr);   
strAddr releasingBuffer();   
memset(RecBuf,0,MAX_REC_SIZE); 

```txt
//open the VISA instrument  
status = viOpenDefaultRM(&defaultRM);  
if (status < VI_SUCCESS)  
{ // Error Initializing VISA... exiting  
AfxMessageBox("No VISA instrument was opened!")  
return false;  
} 
```

//open the instrument status $=$ viOpen(defaultRM, SendAddr, VI_NULL, VI_NULL, &instr); 

```c
//read from the instrument  
status = viRead(instr, RecBuf, MAX_REC_SIZE, &retCount);  
//close the instrument  
status = viClose(instr);  
status = viClose(defaultRM); 
```

```txt
(*pstrResult).Format("%s",RecBuf); return bReadOK; } 
```

7. 增加控件消息响应代码。 

1) 连接仪器 

void CDG2000_Demo_VCDlg::OnConnect() 

// TODO: Add your control notification handler code here 

ViStatus status; 

ViSession defaultRM; 

ViString expr = "?*"; 

ViPFindList findList $=$ new unsigned long; 

ViPUInt32 retcnt $=$ new unsigned long; 

ViChar instrDesc[1000]; 

CString strSrc $=$ ""; 

CString strInstr $\mathbf { \mu } = \mathbf { \mu } ^ { \mathsf { m m } }$ 

unsigned long $\mathrm { ~ i ~ } = 0$ 

bool bFindDG $=$ false; 

status $=$ viOpenDefaultRM(&defaultRM); 

if (status $<$ VI_SUCCESS) 

```txt
{ // Error Initializing VISA... exiting MessageBox("No VISA instrument was opened!"); return;   
}   
memset(instrDesc,0,1000); 
```

// Find resource 

status $=$ viFindRsrc(defaultRM,expr,findList, retcnt, instrDesc); 

for $(\mathrm{i} = 0;\mathrm{i} <   (\text{串})$ retcnt);i++)   
{ //Getinstrument name strSrc.Format("%s",inst InstrWrite(strSrc,]*IDN ::Sleep(200); InstrRead(strSrc,&strIn 

// If the instrument(resource) belongs to the DG series then jump out from the loop 

```txt
strInstr.MakeUpper();
if (strInstr.Find("DG") >= 0)
{
    bFindDG = true;
    m_strInstrAddr = strSrc;
    break;
}
//Find next instrument
status = viFindNext(*findList,InstrDesc);
}
if (bFindDG == false)
{
    MessageBox("Didn't find any DG!");
}
UpdateData(false); 
```

2) 写操作 

```cpp
void CDG2000_Demo_VCDlg::OnSend()
{
    //Todo: Add your control notification handler code here
    UpdateData(true);
    if (m_strInstrAddr.IsEmpty())
        {
            MessageBox("Please connect to the instrument first!");
        }
        InstrWrite(m_strInstrAddr, m_strCommand);
        m_strResult.Free();
    UpdateData(false);
} 
```

```cpp
3）读操作  
void CDG2000_Demo_VCDlg::OnRead()  
{ //Todo:Add your control notification handler code here UpdateData(true); InstrRead(m_strInstrAddr,&m_strResult); UpdateData(false); } 
```

8. 运行程序将进入如下操作界面。 

![](images/08d009e06fced8acf8468c30c64855e3e57cbe64f9517cc99cfe21d6b9847dad.jpg)


执行以下步骤： 

1) 点击 Connect 按钮查找并连接信号源； 

2) 在 Command 编辑框中输入命令，如“*IDN?”； 

3) 点击 Send 按钮发送命令； 

4) 点击 Read 按钮读取返回值。 

运行结果如下图所示。 

![](images/2cb66d3403dfe1c2abe8b1ff9c99b2e107fc9f93f4f2e316e1bb27364ea3062a.jpg)


# 第5章 附录

# 附录 A：出厂设置

出厂设置如下表所示。注意，带“*”的项目由仪器出厂时设置，并且使用过程中和用户的设置有关，不受 恢复出厂值操作的影响。 

<table><tr><td>参数</td><td>出厂值</td></tr><tr><td colspan="2">通道参数</td></tr><tr><td>当前载波</td><td>Sine</td></tr><tr><td>输出阻抗</td><td>高阻</td></tr><tr><td>输出负载</td><td>50Ω</td></tr><tr><td>通道输出</td><td>关闭</td></tr><tr><td>输出反相</td><td>关闭</td></tr><tr><td>电平限制</td><td>关闭</td></tr><tr><td>高电平限制</td><td>0V</td></tr><tr><td>低电平限制</td><td>0V</td></tr><tr><td>同步输出</td><td>关闭</td></tr><tr><td>同步极性</td><td>负</td></tr><tr><td>频率耦合</td><td>关闭</td></tr><tr><td>频率耦合模式</td><td>差值</td></tr><tr><td>频率差值</td><td>0μHz</td></tr><tr><td>频率比例</td><td>1</td></tr><tr><td>幅度耦合</td><td>关闭</td></tr><tr><td>幅度耦合模式</td><td>差值</td></tr><tr><td>幅度差值</td><td>0Vpp</td></tr><tr><td>幅度比例</td><td>1</td></tr><tr><td>相位耦合</td><td>关闭</td></tr><tr><td>相位耦合模式</td><td>差值</td></tr><tr><td>相位差值</td><td>0°</td></tr><tr><td>相位比例</td><td>1</td></tr><tr><td>触发耦合</td><td>关闭</td></tr><tr><td>跟踪模式</td><td>关闭</td></tr><tr><td>波形叠加开关</td><td>关闭</td></tr><tr><td>叠加波形</td><td>Sine</td></tr><tr><td>叠加频率</td><td>1kHz</td></tr><tr><td>叠加比例</td><td>10%</td></tr><tr><td colspan="2"></td></tr><tr><td colspan="2">基本波形</td></tr><tr><td>频率</td><td>1kHz</td></tr><tr><td>幅度</td><td>5Vpp</td></tr><tr><td>幅度单位</td><td>Vpp</td></tr><tr><td>偏移</td><td>0Vdc</td></tr><tr><td>相位</td><td>0°</td></tr><tr><td>方波占空比</td><td>50%</td></tr><tr><td>锯齿波对称性</td><td>50%</td></tr><tr><td>脉冲占空比</td><td>50%</td></tr><tr><td>脉冲宽度</td><td>500μs</td></tr><tr><td>脉冲上升沿</td><td>10ns</td></tr><tr><td>脉冲下降沿</td><td>10ns</td></tr><tr><td>谐波类型</td><td>偶次谐波</td></tr><tr><td>谐波次数</td><td>2</td></tr><tr><td>谐波相位(7个)</td><td>0°</td></tr><tr><td>谐波序号</td><td>2</td></tr><tr><td>谐波幅度(7个)</td><td>1.2647Vpp</td></tr><tr><td>自定义</td><td>X0000000</td></tr><tr><td>DC偏移</td><td>0Vdc</td></tr><tr><td>内建任意波</td><td>Sinc</td></tr><tr><td colspan="2"></td></tr><tr><td colspan="2">高级波形</td></tr><tr><td>幅度</td><td>5Vpp</td></tr><tr><td>偏移</td><td>0Vdc</td></tr><tr><td>PRBS比特率</td><td>2kbps</td></tr><tr><td>PRBS数据</td><td>PRBS7</td></tr><tr><td>RS232波特率</td><td>9600</td></tr><tr><td>RS232数据位</td><td>8</td></tr><tr><td>RS232停止位</td><td>1</td></tr><tr><td>RS232奇偶位</td><td>无</td></tr><tr><td>RS232数据</td><td>85</td></tr><tr><td>任意序列滤波模式</td><td>插值</td></tr><tr><td>任意序列采样率</td><td>1MSa/s</td></tr><tr><td>任意序列相位</td><td>0°</td></tr><tr><td colspan="2"></td></tr><tr><td colspan="2">调制</td></tr><tr><td colspan="2">AM调制</td></tr><tr><td>信号源</td><td>内部</td></tr><tr><td>调制波形</td><td>正弦波</td></tr><tr><td>调制频率</td><td>100Hz</td></tr><tr><td>调制深度</td><td>100%</td></tr><tr><td>载波抑制</td><td>关闭</td></tr><tr><td colspan="2">FM调制</td></tr><tr><td>信号源</td><td>内部</td></tr><tr><td>调制波形</td><td>正弦波</td></tr><tr><td>调制频率</td><td>100Hz</td></tr><tr><td>频率偏差</td><td>1kHz</td></tr><tr><td colspan="2">PM调制</td></tr><tr><td>信号源</td><td>内部</td></tr><tr><td>调制波形</td><td>正弦波</td></tr><tr><td>调制频率</td><td>100Hz</td></tr><tr><td>相位偏差</td><td>90°</td></tr><tr><td colspan="2">ASK调制</td></tr><tr><td>信号源</td><td>内部</td></tr><tr><td>调制速率</td><td>100Hz</td></tr><tr><td>调制幅度</td><td>2Vpp</td></tr><tr><td>极性</td><td>正</td></tr><tr><td colspan="2">FSK调制</td></tr><tr><td>信号源</td><td>内部</td></tr><tr><td>调制速率</td><td>100Hz</td></tr><tr><td>跳跃频率</td><td>10kHz</td></tr><tr><td>极性</td><td>正</td></tr><tr><td colspan="2">PSK调制</td></tr><tr><td>信号源</td><td>内部</td></tr><tr><td>调制速率</td><td>100Hz</td></tr><tr><td>相位</td><td>180°</td></tr><tr><td>极性</td><td>正</td></tr><tr><td colspan="2">PWM调制</td></tr><tr><td>信号源</td><td>内部</td></tr><tr><td>调制波形</td><td>正弦波</td></tr><tr><td>调制频率</td><td>100Hz</td></tr><tr><td>宽度偏差</td><td>200μs</td></tr><tr><td>占空比偏差</td><td>20%</td></tr><tr><td colspan="2"></td></tr><tr><td colspan="2">扫频</td></tr><tr><td>扫频时间</td><td>1s</td></tr><tr><td>返回时间</td><td>0ms</td></tr><tr><td>起始频率</td><td>100Hz</td></tr><tr><td>终止频率</td><td>1kHz</td></tr><tr><td>中心频率</td><td>550Hz</td></tr><tr><td>频率跨度</td><td>900Hz</td></tr><tr><td>起始保持时间</td><td>0 ms</td></tr><tr><td>终止保持时间</td><td>0 ms</td></tr><tr><td>标记频率状态</td><td>关闭</td></tr><tr><td>标记频率</td><td>550Hz</td></tr><tr><td>触发源</td><td>内部</td></tr><tr><td>触发输入</td><td>上升沿</td></tr><tr><td>步进数</td><td>2</td></tr><tr><td colspan="2"></td></tr><tr><td colspan="2">脉冲串</td></tr><tr><td>循环数</td><td>1</td></tr><tr><td>猝发周期</td><td>10ms</td></tr><tr><td>门控极性</td><td>正</td></tr><tr><td>空闲电平</td><td>第一个点</td></tr><tr><td>触发源</td><td>内部</td></tr><tr><td>触发输出</td><td>关闭</td></tr><tr><td>触发输入</td><td>上升沿</td></tr><tr><td>延时</td><td>0ns</td></tr><tr><td colspan="2"></td></tr><tr><td colspan="2">界面焦点项</td></tr><tr><td>频率/周期</td><td>频率</td></tr><tr><td>幅度/高电平</td><td>幅度</td></tr><tr><td>偏移/低电平</td><td>偏移</td></tr><tr><td>脉宽/占空比</td><td>占空比</td></tr><tr><td>起始/中心</td><td>起始</td></tr><tr><td>终止/跨度</td><td>终止</td></tr><tr><td>默认通道</td><td>CH1</td></tr><tr><td colspan="2"></td></tr><tr><td colspan="2">频率计</td></tr><tr><td>测量参数</td><td>频率</td></tr><tr><td>匣门时间</td><td>100ms</td></tr><tr><td>统计</td><td>关闭</td></tr><tr><td>灵敏度</td><td>低</td></tr><tr><td>触发电平</td><td>0V</td></tr><tr><td>耦合类型</td><td>DC</td></tr><tr><td>高频抑制</td><td>关闭</td></tr><tr><td colspan="2">系统参数</td></tr><tr><td colspan="2">系统设置</td></tr><tr><td>语言*</td><td>取决于出厂时的设置</td></tr><tr><td>上电值</td><td>默认值</td></tr><tr><td>时钟源</td><td>内部</td></tr><tr><td>蜂鸣器</td><td>打开</td></tr><tr><td>小数点</td><td>点号</td></tr><tr><td>分隔符</td><td>逗号</td></tr><tr><td>系统日志</td><td>关闭</td></tr><tr><td colspan="2">显示设置</td></tr><tr><td>屏幕保护</td><td>关闭</td></tr><tr><td>亮度*</td><td>100%</td></tr><tr><td colspan="2">打印设置</td></tr><tr><td>打印路径</td><td>U盘</td></tr><tr><td>打印格式*</td><td>PNG</td></tr><tr><td colspan="2">接口设置</td></tr><tr><td>GPIO*</td><td>2</td></tr><tr><td>DHCP*</td><td>打开（LAN中的默认设置）</td></tr><tr><td>自动IP*</td><td>打开（LAN中的默认设置）</td></tr><tr><td>手动IP*</td><td>关闭（LAN中的默认设置）</td></tr></table>

# 附录 B：保修概要

苏州普源精电科技有限公司（RIGOL (SUZHOU) TECHNOLOGIES INC.，以下简称 RIGOL）承诺其产品在 保修期内无任何材料和工艺缺陷。在保修期内，若产品被证明有缺陷，RIGOL 将为用户免费维修或更换。 

详细保修条例请参见 RIGOL 官方网站或产品保修卡的说明。欲获得维修服务或保修说明全文，请与 RIGOL 维修中心或当地办事处联系。 

除本概要或其他适用的保修卡所提供的保证以外，RIGOL 公司不提供其他任何明示或暗示的保证，包括但 不局限于对产品可交易性和特殊用途适用性之任何暗示保证。在任何情况下，RIGOL 公司对间接的、特殊 的或继起的损失不承担任何责任。 