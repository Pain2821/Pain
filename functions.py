import cv2
import json
from datetime import datetime
import face_recognition
from pathlib import Path
import requests

def faceDetect(img):
        imgV = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        file_name = 'felon.jpg'
        path_file = 'imgs/'+file_name
        cv2.imwrite(path_file, imgV)
        return json.dumps(path_file)


def findEncodings(images):
    encodeList= []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def markAttendence(name):
    with open('./attendence.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        # print("nameList", nameList)
        lastentry=''
        entry = lastentry.strip()
        login = "http://64.227.130.2:5000/api/v1/userTimeEntry/logTime/"+name
        result =  requests.post(login) 
        d = result.json()
        print ('d', d)
        print ('result', result.json())  
        print('login', login)

        r = requests.get("http://64.227.130.2:5000/api/v1/auth/login_with_id")
        d = r.json()

        for employee in d['data']:
            # firstname = data['firstname']
            id = employee['id']
            firstname = employee['firstname']
            # print(id)
            # print(firstname)
            if id ==  name.lower() :
                name = firstname
                # print('name...', name)
            else :
                None

        for line in myDataList:
    
            data = line.split(",")
            x = data[0]
            if x == name:
                nameList.append(x)
                entry=data[3]
            
        if name not in nameList :
            now = datetime.now()
            dtstring = now.strftime('%b-%d-%Y, %H:%M:%S')
            f.writelines(f'\n{name}, {dtstring}, {"in"}')
            print('welcome', name)

        elif name in nameList :
        
            if  entry==" out\n" or entry==" out"  :
                now = datetime.now()
                dtstring = now.strftime('%b-%d-%Y, %H:%M:%S')
                f.writelines(f'\n{name}, {dtstring}, {"in"}')
                print(name,', lastentry =',entry)
                      
            elif entry==" in\n" or entry==" in":
                
                now = datetime.now()
                dtstring = now.strftime('%b-%d-%Y, %H:%M:%S')
                f.writelines(f'\n{name}, {dtstring}, {"out"}') 
                print(name,', lastentry =',entry)

            else :      
                    print(4)
                    print('error',entry, name)

        else :
            print('ERORRRR.....!!!')

# def login(name):
#             for id in name:
#                 # if id == name :
#                     login = "http://64.227.130.2:5000/api/v1/userTimeEntry/logTime/"+id
#                     result =  requests.post(login) 
#                     print ('result', result)



# def retrive(ids):
#     for id in ids:
#     # firstname = data['firstname']
#         id = ids['id']