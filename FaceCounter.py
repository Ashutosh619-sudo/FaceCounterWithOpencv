import cv2
import face_recognition


video_capture = cv2.VideoCapture(0)

face_location=[]
faces = 0

while True:
    ret, frame = video_capture.read()

    rbg_frame = frame[:, :, ::-1]
    face_location = face_recognition.face_locations(rbg_frame)
    faces = len(face_location)
    people = "People: "+str(faces)
    for top,right,bottom,left in face_location:
        cv2.rectangle(frame, (left, top), (right,bottom),(0,255,0),2)
        
    cv2.putText(frame,people,(20,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)   

    cv2.imshow("face_recongition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(faces)
video_capture.release()
cv2.destroyAllWindows()
