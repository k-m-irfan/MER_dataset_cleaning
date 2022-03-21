# looks for same file in target folder (even with different name)
# file is copied if any duplicate is not present in the target folder
import os
import filecmp
import shutil
sourceDir = 'D:\MER\Dataset\Expressions\Downloaded_from_google_images\Happiness' # Source folder
targetDir = 'D:\MER\Dataset\Expressions\duplicate_deleted\Happiness' # Target Folder
duplicates = 0
for sRoot,sDirs,sFiles in os.walk(sourceDir):
    break
for sourceName in sFiles:
    sourceFile = sourceDir+'\\'+sourceName
    for tRoot,tDirs,tFiles in os.walk(targetDir):
        break
    if tFiles == []:
        shutil.copy(sourceFile, targetDir)
    if tFiles != []:
        for targetName in tFiles:
            targetFile = targetDir+'\\'+targetName
            compare = filecmp.cmp(sourceFile,targetFile)
            if compare == True:
                duplicates+=1
        if duplicates == 0: # only copy if there is no duplicate file in the target folder
            shutil.copy(sourceFile, targetDir)
        duplicates = 0








        
