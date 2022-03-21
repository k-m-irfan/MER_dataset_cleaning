# Final Rename
import os

path = 'D:\MER\Dataset\Expressions\Micro_Expressions\\test\\surprise' # Source folder
for root,dirs,files in os.walk(path):
    break
count = 0
for file in files: #renaming to numbers to avoid FileExistError
    count+=1
    oldName = path+'\\'+file
    newName = path+'\\'+str(count)+'.jpg'
    os.rename(oldName,newName)
    # print(count)

count = 0
for root,dirs,files in os.walk(path):
    break
for file in files:
    count+=1
    oldName = path+'\\'+file
    newName = path+'\\'+'surprise'+str(count)+'.jpg'
    os.rename(oldName,newName)
print("No. of files renamed: ",count)
    
