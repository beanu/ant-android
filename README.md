ant-android
===========

Ant脚本，自动打包apk
注意:
1.<property environment="env" />
    这里的env是你的系统环境变量，如果是linux系统，键入命令env，检查一下有没有下面这两个变量
    ${env.ANDROID_SDK_HOME} ${env.JAVA_HOME} 前一个是android的sdk根目录，后一个是java home的根目录

2.<property file="build.properties" />
    加载build.properties文件

3.apk.py 和list.txt
    这两个文件是为了自动执行ant的python脚本，list.txt是存的变量
    例如<code>ant -f build.xml -Dappname="123"</code>
    ${appname}在build的任何地方都可以用了
