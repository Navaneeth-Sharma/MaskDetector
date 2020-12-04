import cv2
import sys,time
from pydub import AudioSegment
from pydub.playback import play


####################################   GIVE THE PATHS CORRECTLY #############################
mouthCascade = cv2.CascadeClassifier('OpenCV-detection-models-master/haarcascades/'+'haarcascade_mcs_mouth.xml')
eyesCascade = cv2.CascadeClassifier('OpenCV-detection-models-master/haarcascades/'+'haarcascade_mcs_eyepair_small.xml')

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
noseCascade = cv2.CascadeClassifier('OpenCV-detection-models-master/haarcascades/'+'haarcascade_mcs_nose.xml')
video_capture = cv2.VideoCapture(0)

############################ TO SAVE ###########################
frame_width = int(video_capture.get(3)) 
frame_height = int(video_capture.get(4)) 

size = (frame_width, frame_height) 
result = cv2.VideoWriter('test.avi',  
                         cv2.VideoWriter_fourcc(*'MJPG'), 
                         10, size) 
###################################################################

MaskWearing = 0
NotWearingMask = 0



######################################################################
#                                   MAIN CODE
######################################################################
while True:
    # Capture frame-by-frame
	ret, frame = video_capture.read()
	# time.sleep(1)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	mouth = mouthCascade.detectMultiScale(gray, 1.3, 5)
	nose = noseCascade.detectMultiScale(gray, 1.3, 5)
	faces = faceCascade.detectMultiScale(
	            gray,
	            scaleFactor=1.1,
	            minNeighbors=5,
	            minSize=(20, 20)
	        )
    # Draw a rectangle around the faces
	c = 0
	for (x, y, w, h) in faces:
		if x!=0 and y!=0:
		    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
		        # Draw a rectangle around the faces
		    roi_gray_mouth = gray[y+(int(h/2)):y+h, x:x+w]
		    roi_color_mouth = frame[y+(int(h/2)):y+h, x:x+w]

		    roi_gray_eye = gray[y-(int(h/2)):y+h, x:x+w]
		    roi_color_eye = frame[y-(int(h/2)):y+h, x:x+w]

		    roi_gray_nose = gray[y+(int(h/.5)):y+h, x:x+w]
		    roi_color_nose = frame[y+(int(h/.5)):y+h, x:x+w]

		    mouth = mouthCascade.detectMultiScale(roi_gray_mouth)
		    eyes = eyeCascade.detectMultiScale(roi_gray_eye)
		    nose = noseCascade.detectMultiScale(roi_gray_nose)

		    a = 0
		    for (ex,ey,ew,eh) in mouth:
		        # cv2.rectangle(roi_color_mouth, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
		        if ex !=0 and ey !=0 and ew !=0 and eh!=0:
		        	a = 1
		        	MaskWearing = 0
		        	NotWearingMask += 1
		    for (ex,ey,ew,eh) in nose:
		        cv2.rectangle(roi_color_mouth, (ex, ey), (ex+ew, ey+eh), (0, 255, 255), 2)


		    P = 0
		    for (eex,eey,eew,eeh) in eyes:
		        d = int(eew / 2)
		        # cv2.circle(roi_color_eye, (int(eex + eew / 4) + int(d / 2), int(eey + eeh / 4) + int(d / 2)), int(d) ,(0,0,255),2)
		        if eex !=0 and eey !=0 and eew !=0 and eeh!=0:
		        	P = 1
		    
		    if a==0 and P!=0:
		    	MaskWearing+=1
		    	NotWearingMask = 0

	# You can ADJUST THE FRAMES OF NOT WEARING MASK 
	if NotWearingMask>0 and NotWearingMask % 6 == 0:
		# print("Please Wear Mask ..... ")

		sound = AudioSegment.from_file('MaskWearing.wav')
		play(sound)
		NotWearingMask = 0
		# time.sleep(3)

	# You can ADJUST THE FRAMES OF WEARING MASK 
	if MaskWearing>=5:
		# print("Move On ......")
		sound = AudioSegment.from_file('MoveForward.wav')
		MaskWearing = 0
		play(sound)

 #    # Display the resulting frame
	cv2.imshow('Video', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
	    break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()


