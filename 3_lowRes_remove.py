#removes small images (<80x80) and resize all remaining images to 80x80
import os
import cv2

sourceDir = 'D:\MER\Dataset\Expressions\\3. Face_crop\\Surprise' # Source folder
targetDir = 'D:\MER\Dataset\Expressions\\4. small_image_removed_resized\\Surprise' # Target Folder
imageCount = 0
for sRoot,sDirs,sFiles in os.walk(sourceDir):
    break
for sourceName in sFiles:
    sourceFile = sourceDir+'\\'+sourceName
    image = cv2.imread(sourceFile)
    if image.shape[0] >= 80:
        imageCount+=1
        fileName = 'surprise'+str(imageCount)+'.jpg' #change file name here
        imageResize = cv2.resize(image,(80,80)) # resize to 80x80 pixel
        cv2.imwrite(targetDir+'\\'+fileName,imageResize)
