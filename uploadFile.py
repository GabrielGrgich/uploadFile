from importlib.metadata import files
import os
from threading import local
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def uploadFile(self,fileFrom,fileTo):
        dbx = dropbox.Dropbox(self.access_token,scope=['files.content.read', 'files.metadata.read'])
        for root,dirs,files in os.walk(fileFrom):
            for fileName in files:
                localPath=os.path.join(root,fileName)
                relativePath=os.path.relpath(localPath,fileFrom)
                drobBoxPath=os.path.join(fileTo,relativePath)
                f=open(fileFrom, 'rb')
                dbx.files_upload(f.read(),drobBoxPath, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BJrz_kWpL_x3KuHUBNPgMev15dnNyUIrVpkVEeNyWqJTFn__K412qqbGd5z1SVLSpY_G1sF7PYQIh1XF2rFTEVGBH62oxI70ZXGsxMh7yhVNzbXX1FKSbY6wK5MQySYOQcrWuLvGoe0'
    transferData = TransferData(access_token)

    fileFrom=input("enter file path here: ")
    fileTo='/test/testFile.txt'

    transferData.uploadFile(fileFrom, fileTo)
    print("transfer was a success")

#if __name__ =='__main__':
main()

