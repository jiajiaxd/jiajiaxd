import requests
import sys
import os
import FileUtils
os.chdir(sys.path[0])

latest_trackers=requests.get('https://fastly.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ip.txt').text.replace('\n',r'\n')
print(latest_trackers)
# 他妈的我也不想这样写读写配置文件，奈何我一用configparser，qbittorrent就给我重新生成一个配置文件，气死我了，有缘人快帮我看看咋办啊我去
# 我TM测试了1个小时，也没搞明白。最终用了下面这个很SB的读写配置文件方法。呕！
original=FileUtils.readfile('qBittorrent.conf')
original_split=original.split('\n')
a=0
for i in original_split:
    if 'Session\AdditionalTrackers' in i:
        original_split[a]='Session\AdditionalTrackers='+latest_trackers
        r=False
        break
    a+=1
new=str()
for i in original_split:
    new+=i+'\n'
FileUtils.writefile('qBittorrent.conf',new)
