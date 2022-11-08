import numpy as np
import cv2
import json
import os
from flask import Flask, request, Response
from pathlib import Path
import face_recognition
import functions

#API
app = Flask(__name__)

#route http post to this method
# print ('abc')

@app.route('/', methods=['GET'])

def home():
   return 'Hello'

@app.route('/image', methods=['POST'])
def image():
            #retrieve image from client
            img = cv2.imdecode(np.fromstring(request.files['image'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
            imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
            print(img, 'img')
            print(imgS, 'imgS')
            

            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
            print(facesCurFrame,"hhhhhhhhh")
            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                print(faceDis,"dddddddd")
                matchIndex = np.argmin(faceDis)
                print('xyz now')
                if matches[matchIndex]:
                    name = classNames[matchIndex].upper()
                    # print(name)
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                    cv2.rectangle(img, (x1, y1), (x2,y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2-30), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 2)
                    functions.markAttendence(name)


            img_processed = functions.faceDetect(img).replace("\"","")
            #response
            data_response = {"image_processed": img_processed}
            data_json = json.dumps(data_response)
            print('jason', json.dumps(data_json) )
            
            return Response(response=json.dumps(data_json), status=200, mimetype="application/json") #return json string


path = "./image_attendence"
images = []
classNames = []
myList = os.listdir(path)

for cl in myList:
    curImg = cv2. imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

encodeListKnown = functions.findEncodings(images)
print('Encoding Complete')
# print(classNames, images)


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)

# http://64.227.130.2:5000/api/v1/auth/login
# post

# email: "dainik.bhuva@centillionsofttech.com"
# password: "Centi$@2019!"
