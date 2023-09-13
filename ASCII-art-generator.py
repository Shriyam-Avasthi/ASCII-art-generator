import os
import cv2
import numpy as np
from sys import argv
from skimage import exposure
from skimage import img_as_ubyte
from rgbprint import rgbprint 

def FindLeastDissimilarCharacter(image):
    minDissimilarityIndex = 1000
    imagePosition = -1
    for i in range(0 , len(characterImages)):
        dissimilarityArray = np.subtract( image ,characterImages[i] )
        dissimilarityArray = (dissimilarityArray)
        dissimilarityIndex = np.mean(dissimilarityArray)
        if( dissimilarityIndex < minDissimilarityIndex ):
            minDissimilarityIndex = dissimilarityIndex
            imagePosition = i
    return imagePosition

def FindBestColor( image_rgb ):
    
    red = int( np.mean(image_rgb[:,:,0]) )
    green = int( np.mean(image_rgb[:,:,1]) )
    blue = int( np.mean(image_rgb[:,:,2]) )
    
    return [red,green,blue]

characterImages= [];
asciiCodes = [];

# try:
#     image_path = argv[1]
# except IndexError:
#     raise Exception("You need to provide the path of an image, no path provided.")
image_path = "Gun3.png"
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

for filename in os.listdir("CharacterImages"):
    img = cv2.imread(os.path.join("CharacterImages",filename),0)
    if img is not None : 
        characterImages.append(img)
        asciiCodes.append( int(filename[:-4]) )

characterImages = np.array(characterImages)
kernelHeight = characterImages[0].shape[0]
kernelWidth = characterImages[0].shape[1]

newImageHeight = ( image.shape[0] // kernelHeight ) * kernelHeight
newImageWidth = ( image.shape[1] // kernelWidth ) * kernelWidth
image = cv2.resize(image , (newImageWidth , newImageHeight) )

image_gray = cv2.cvtColor( image, cv2.COLOR_BGR2GRAY)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

imgToBeDrawn = exposure.equalize_adapthist(image_gray, clip_limit=0.03)
imgToBeDrawn = exposure.adjust_log(imgToBeDrawn, 0.65)
imgToBeDrawn = img_as_ubyte(imgToBeDrawn)

for row in range(0 , image_gray.shape[0] - kernelHeight + 1, kernelHeight ):
    for column in range( 0, image_gray.shape[1] - kernelWidth + 1, kernelWidth ):
        color = FindBestColor(image[ row : row + kernelHeight , column : column + kernelWidth,:])
        rgbprint(chr(asciiCodes[FindLeastDissimilarCharacter ( imgToBeDrawn[ row : row + kernelHeight , column : column + kernelWidth ] ) ] )  , end = "", color = color );
    print()

cv2.imshow("Image" , cv2.cvtColor(image,cv2.COLOR_RGB2BGR) )
# cv2.waitKey(0)