# face detection 
# to remove multiple face images, non face images and corrupt/non convertible images
import os
import cv2
import mediapipe as mp

sourceDir = 'D:\MER\Dataset\Expressions\duplicate_deleted\Surprise' # Source folder
targetDir = 'D:\MER\Dataset\Expressions\Face_crop\Surprise' # Target Folder

imageCount = 0 # for file naming
errorCount = 0

findFace = mp.solutions.face_detection.FaceDetection()
def faceBox(frame):#face bounding box
    try:
        frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    except:
        return []
    results = findFace.process(frameRGB)
    myFaces = []
    if results.detections != None:
        for face in results.detections:
            bBox = face.location_data.relative_bounding_box
            myFaces.append(bBox)
    return myFaces

for sRoot,sDirs,sFiles in os.walk(sourceDir):
    break
for sourceName in sFiles:
    sourceFile = sourceDir+'\\'+sourceName
    image = cv2.imread(sourceFile)
    faceBoxes = faceBox(image)
    if len(faceBoxes) == 1:
        imageCount+=1
        fileName = 'surprise'+str(imageCount)+'.jpg' #change file name here
        height,width,channel = image.shape
        x,y,w,h = int(faceBoxes[0].xmin*width),int(faceBoxes[0].ymin*height),int(faceBoxes[0].width*width),int(faceBoxes[0].height*height)
        # cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),1)
        croppedImage = image[y:y+h,x:x+w]
        try:
            cv2.imwrite(targetDir+'\\'+fileName,croppedImage)
        except:
            errorCount+=1
            print(errorCount)
            continue