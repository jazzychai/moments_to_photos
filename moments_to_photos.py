import os
import shutil


def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
    return fsize
    
def listfiles(path):
    global conflict_index
    
    files= os.listdir(path)
    for v in files:
        if v != "@eaDir":
            if os.path.isdir((path+"/"+v)):
                listfiles(path+"/"+v)
            else:
                full_file_path = path+"/"+v #照片的完整路径
                # 获取年月
                ps = full_file_path.split('/') 
                date = ps[len(ps)-2]
                ps2 = date.split('-')
                y = ps2[0]
                m = ps2[1]
                # 创建文件夹
                if not os.path.isdir("/volume1/homes/jazzy/Photos/PhotoLibrary/"+y):
                    os.makedirs("/volume1/homes/jazzy/Photos/PhotoLibrary/"+y)
                if not os.path.isdir("/volume1/homes/jazzy/Photos/PhotoLibrary/"+y+"/"+m):
                    os.makedirs("/volume1/homes/jazzy/Photos/PhotoLibrary/"+y+"/"+m)
                # 移动文件
                if not os.path.exists("/volume1/homes/jazzy/Photos/PhotoLibrary/"+y+"/"+m+"/"+v):
                    shutil.move(full_file_path,"/volume1/homes/jazzy/Photos/PhotoLibrary/"+y+"/"+m+"/")
                else:
                    source_size = get_FileSize(full_file_path)
                    dist_size = get_FileSize("/volume1/homes/jazzy/Photos/PhotoLibrary/"+y+"/"+m+"/"+v)
                    print("--------------------",conflict_index,"--------------------")
                    conflict_index = conflict_index + 1
                    if(source_size == dist_size):
                        print("\033[0;32;40mconflict:\033[0m",full_file_path,"/volume1/homes/jazzy/Photos/PhotoLibrary/"+y+"/"+m+"/"+v)
                        print("\033[0;32;40msize same:\033[0m","source_size:",source_size,"dist_size:",dist_size)
                    else:
                        print("\033[0;31;40mconflict\033[0m",full_file_path,"/volume1/homes/jazzy/Photos/PhotoLibrary/"+y+"/"+m+"/"+v)
                        print("\033[0;31;40msize not same\033[0m","source_size:",source_size,"dist_size:",dist_size)
                    
                    
                    



conflict_index = 1
listfiles("/volume1/homes/jazzy/Moments")

