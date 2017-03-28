import cv2
import sys

# get paths for the image and haar cascade  
imagePath = sys.argv[1]
cascPath = sys.argv[2]

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image and convert to gray
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# now we can try to detect faces 
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)


# Draw a rectangle around the faces and display on screen
for (x, y, w, h) in faces:
    print x, y, w, h
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# TODO
# Get face points for eyes, ears, nose, mouth (l+r)
# get model points - use example from (http://www.morethantechnical.com/2010/03/19/quick-and-easy-head-pose-estimation-with-opencv-w-code/   OR   https://www.learnopencv.com/head-pose-estimation-using-opencv-and-dlib/ 	)
# get camera matrix ( use example in https://www.learnopencv.com/head-pose-estimation-using-opencv-and-dlib/ )



#for face in faces:
#	ret, rvec, tvec = cv2.solvePnP(face)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
