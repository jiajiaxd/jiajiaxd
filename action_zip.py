import os
import sys
import zipfile

root_folder=sys.argv[1]

def zipdir(path, ziph):
    # 打包指定路径下的所有文件和文件夹
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
        for dir in dirs:
            zipdir(os.path.join(root, dir), ziph)

for folder in os.listdir(root_folder):
    zipf=zipfile.ZipFile('{0}/{1}.zip'.format(sys.argv[2],folder),'w',zipfile.ZIP_DEFLATED)
    zipdir(os.path.join(root_folder,folder), zipf)
    zipf.close()
