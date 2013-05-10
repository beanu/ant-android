ant-android
===========

Ant脚本，自动打包apk

注意:
    
1.env系统变量

    property environment="env"
    这里的env是你的系统环境变量，如果是linux系统，键入命令env，检查一下有没有下面这两个变量
    env.ANDROID_SDK_HOME env.JAVA_HOME前一个是android的sdk根目录，后一个是java home的根目录
    在linux的/etc/profile中设置是
    export JAVA_HOM=E/opt/jdk1.6.0_45
    export JRE_HOME=/opt/jdk1.6.0_45/jre
    export CLASSPATH=.:$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
    export PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$PATH

    export ANDROID_HOME=/opt/android-sdks
    export PATH=$ANDROID_HOME/platform-tools:$ANDROID_HOME/tools:$PATH

2.加载build.properties文件

    <code>property file="build.properties"</code>

3.apk.py 和list.txt

    这两个文件是为了自动执行ant的python脚本，list.txt是存的变量
    例如<code>ant -f build.xml -Dappname="123"</code>
    ${appname}在build的任何地方都可以用了
    
Markdown语言还没学，所以写的很糟糕！
