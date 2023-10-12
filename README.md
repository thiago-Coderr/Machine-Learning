# Machine-Learning
Face recognition system for attendance

1) - It imports the necessary libraries, including face_recognition, cv2 (OpenCV), numpy, csv, datetime, and os.
2) - It captures video from the default camera (camera with index 0).
3) - It loads pre-defined images of faces (Supayan, Subhannita, Hissein, and Tiago), extracts their face encodings, and associates them with their names.
4) - It sets up variables and lists to store face location, encodings, names, and students' names.
5) - It opens a CSV file named with the current date in YY-MM-DD format for recording attendance.
6) - It enters into a loop for continuously capturing frames from the camera and processing them for face recognition.
7) - Within the loop:
     a) - It resizes the captured frame to a smaller size.
     b) - It identifies face locations in the resized frame.
     c) - It calculates face encodings for the detected faces.
     d) - It compares the encodings with the known encodings (the loaded images).
     e) - It assigns names to the recognized faces based on the best-matching encoding.
     f) - If a recognized face is a known student, it records their name and the current time in the CSV file, updating the list of students.
     g) - It draws rectangles around the detected faces and labels them with their names on the video frame.
     h) - It displays the video frame with recognized faces.
     i) - It breaks the loop if the 'z' key is pressed.
8) - After the loop ends, it releases the video capture and closes the OpenCV windows.
9) - It closes the CSV file, saving the attendance records for the day.
