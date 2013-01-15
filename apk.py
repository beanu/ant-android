import os

for line in open("list.txt"):
    if not line.startswith("#"):
        if not line=="\n":
            if line.startswith("dir="):
                dirs=line[4:].strip('\n')
            else:
                value=line.split('|')
                num=value[0]
                filename=value[1]
                directory=dirs+'/'+value[2]
                name=value[3]
                print "%s %s %s %s" % (num,filename,directory,name)
                os.chdir('/home/beanu/resource/workspace/TradeClient')
                os.system('ant -f build.xml -Dappname='+filename+' -Dcopypath='+directory)
