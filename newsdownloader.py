import requests
import json
from moviepy.editor import *
import os
from natsort import natsorted

videotitle = ''


def editvideo():
    L = []
    for root, dirs, files in os.walk("newsdownloader"):
        # 按文件名排序
        files = natsorted(files)
        # 遍历所有文件
        for file in files:
            # 如果后缀名为 .mp4
            if os.path.splitext(file)[1] == '.mp4':
                # 拼接成完整路径
                filePath = os.path.join(root, file)
                # 载入视频
                video = VideoFileClip(filePath)
                # 添加到数组
                L.append(video)

    # 拼接视频
    final_clip = concatenate_videoclips(L)

    # 生成目标视频文件
    final_clip.to_videofile("newsdownloader//targets//target.mp4",
                            fps=24, remove_temp=False)


if __name__ == '__main__':
    response = requests.get(
        "https://api.cntv.cn/lanmu/columnSearch?&fl=&fc=%E6%96%B0%E9%97%BB&cid=&p=1&n=20&serviceId=tvcctv&t=jsonp&cb"
        "=Callback")
    res = json.loads(response.text.removeprefix(
        'Callback(').removesuffix(');'))
    res = res.get('response').get("docs")[14].get('lastVIDE')
    videotitle = res.get('videoTitle')
    print("获取到", videotitle, res.get('videoUrl'))
    os.system("you-get -n -o newsdownloader "+res.get('videoUrl'))
    editvideo()
    os.rename("newsdownloader//targets//target.mp4","newsdownloader//targets//"+videotitle+".mp4")
