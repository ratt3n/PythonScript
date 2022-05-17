import os
import urllib.parse

path = ""
files = os.listdir(path)
files.sort()
for file in files:
    if os.path.isdir(path+file):
        continue
    urlpath=urllib.parse.unquote(file)
    if "/" in urlpath:
        tmp=file.replace("%2F","/")
        try:
            os.makedirs(path+os.path.dirname(tmp))
        except FileExistsError:
            pass
        os.renames(path+file,path+tmp)
    else:
        os.rename(path+file,path+urlpath)
