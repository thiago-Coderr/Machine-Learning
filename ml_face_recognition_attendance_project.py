## importing important modules
import face_recognition as fr
import cv2
import numpy as np
import csv
from datetime import datetime
import os
import threading


### capturing videos
video_capture = cv2.VideoCapture(0)

Supayan_photo = fr.load_image_file('photos/Supayan.jpeg')
Supayan_encoding = fr.face_encodings(Supayan_photo)[0]

Subhannita_photo = fr.load_image_file('photos/Subhannita.jpeg')
Subhannita_encoding = fr.face_encodings(Subhannita_photo)[0]

hissein_photo = fr.load_image_file('photos/Hissein.jpeg')
hissein_encoding = fr.face_encodings(hissein_photo)[0]

tiago_photo = fr.load_image_file('photos/Thiago.jpeg')
tiago_encoding  = fr.face_encodings(tiago_photo)[0]





### encoding the photos

known_face_encoding = [
Supayan_encoding,
Subhannita_encoding,
hissein_encoding,
tiago_encoding,
]

known_faces_names = [
'Supayan Das',
'Subhannita Saha',
'Hissein',
'Thiago',
#'Shiwanshu'
]

students = known_faces_names.copy()

face_location = []
face_encoding = []
face_names = []
s = True


now = datetime.now()
curr_date = now.strftime('%y-%m-%d')


f = open(curr_date + '.csv', 'w+', newline = '')
lnwriter = csv.writer(f)


while True:
	a, frame = video_capture.read()
	small_frame = cv2.resize(frame, (0, 0), fx = 1, fy = 1)
	rgb_small_frame = small_frame ## converting bgr to rgb format
	if s:
		face_locations = fr.face_locations(rgb_small_frame)
		
		
		face_encodings = fr.face_encodings(rgb_small_frame, face_locations)
		face_names = []
		for face_encoding in face_encodings:
			matches = fr.face_distance(known_face_encoding, face_encoding)
			name = ''
			face_distance = fr.face_distance(known_face_encoding, face_encoding)
			best_match_index = np.argmin(face_distance)
			if(min(face_distance) > 0.6):
				name = 'UNKNOWN'				
			elif matches[best_match_index]:
				name = known_faces_names[best_match_index]
			
			face_names.append(name)
			if name in known_faces_names:
				current_time = now.strftime('%H-%M-%S')
			
				if name in students:
					print(students)
					students.remove(name)
					lnwriter.writerow([name, current_time])
				
		
		for faces, nname in zip(face_locations, face_names):
		
			face_loc = np.array(faces)
			
			y1, x1, y2, x2 = face_loc
			cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 2)
			cv2.putText(frame, nname, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)	
		cv2.imshow('face_recg', frame)
		#cv2.waitKey(1)
		#cv2.waitKey(1) 0xFF == ord('q'):
		if cv2.waitKey(10) == ord('z'):
        		break
		
video_capture.release()
cv2.destroyAllWindows()
f.close()
