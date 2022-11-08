from importlib.resources import contents
import requests
from email.mime import image
from heapq import nsmallest
from pyexpat import ExpatError
from cv2 import VideoCapture, imdecode
import numpy as np
import cv2
import json
from PIL import Image
import requests
import os
import urllib.request
from flask import Flask, request, Response
from datetime import datetime
import face_recognition
from pathlib import Path
# import functions
# import urllib.request
# # import webbrowser
from PIL import Image
import cv2
# import os.path

# im = Image.open(requests.get("http://64.227.130.2:5000/profile/6295f81f9a52ac315fefa6a9.jpeg", stream=True).raw)
# print (im)

# with open ('naem.jpeg', 'wb') as f:
# #     f.write(im)
# app = Flask(__name__)
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=3000)


# @app.route('/id', methods=['GET'])

# def id():
# #   data = request.get_json()
#             id = np.fromstring(request.files['id'].read(), np.uint8)
#             print(id)
#             login = "http://64.227.130.2:5000/api/v1/userTimeEntry/logTime/"+id
#             result =  requests.post(login)
# #   print('result')
#             print(result, 'resukt')
#             print(id , 'id')

            
#             return Response(response=json.dumps, status=200, mimetype="application/json") #return json string

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)






# import urllib.request
# imgURL = "http://64.227.130.2:5000/profile/6295f81f9a52ac315fefa6a9.jpeg"
# urllib.request.urlretrieve(imgURL, r"C:\Users\arceu\Desktop\AwesomeProject\backend\profile_pics\local-filename.jpg")


# r = requests.get("http://64.227.130.2:5000/api/v1/user/allUser")

# d = r.json()

# for employee in d['data']:
#     # firstname = data['firstname']
#     id = employee['id']
#     firstname = employee['firstname']
#     profile = employee['profile']

#     print(firstname)
#     print(id)


    # if id == '6295f81f9a52ac315fefa6a9':
    #     login = "http://64.227.130.2:5000/api/v1/userTimeEntry/logTime/"
    #     result =  requests.post(login)
    #     print (login)

    # else :
    #     print('failed')
    # if profile is None:
    #     print ('No Pic')
    # else:
    #     # pic = 'http://64.227.130.2:5000'+ profile
    #     None

    # # im = Image.open(requests.get(pic, stream = True).raw)




    #     path_file = 'profile_pics/'
    # with open(firstname+".jpeg", "wb") as f:
    #     f.write((requests.get(pic).content), )


    # print(firstname, id)
    
    # print (profile)
    # print(pic)
    # print(data)



# url = ('http://64.227.130.2:5000/profile/6295f81f9a52ac315fefa6a9.jpeg')

# a = requests.get(url)
# with Image.open('name.jpeg', 'wb') as f:
#     response = requests.get(url, stream=True )
#     print(response)
#     for block in response.iter_content(1024):
    
#         f.write(block)
        # print(block)
    # print(a)















# print(r.status_code)
# print(r, "1")
# headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MjRlZjIxYWM5ZmNiMjkzNzU5ODBlYWIiLCJpYXQiOjE2NjIzODYwNjMsImV4cCI6MTY2MjY0NTI2M30.iZl4mtitmHrJPC5Y76CmiKqDvR4NTMrhxEhNjRGaYSI"}
# result =  requests.post("http://64.227.130.2:5000/api/v1/userTimeEntry/logTime", headers=headers).json()
# print(result, "2")
# x = requests.get("http://64.227.130.2:5000/profile/624ef21ac9fcb29375980eab.jpeg")
# print(x, "3")


# im = Image.open(requests.get("http://64.227.130.2:5000/profile/6295f81f9a52ac315fefa6a9.jpeg", stream=True).raw)

# # path = im
# images = []
# classNames = []





# import requests

# url = 'http://google.com/favicon.ico'
# filename = 'dp.jpeg'
# # path_file = r'C:\Users\arceu\Desktop\AwesomeProject\backend\profile_pics'
# r = requests.get(url)
# with open('filename',  'wb') as f:
#     f.write(requests.get(url).content)



# print(r, 'r')



#     url = 'http://google.com/favicon.ico'
#     r = requests.get(url, allow_redirects=True)
#     filename = 'felon.jpg'
#     with open('filename', 'wb') as f:
#         f.write(requests.get(url).content)
#     path_file = 'imgs/'+filename
#     # r = requests.get(url, allow_redirects=True)
#     cv2.imwrite(path_file,img)
#     print (r)
# # url = 'http://google.com/favicon.ico'
# # img = open(requests.get(url))
# # final = profilepic(img).replace("\"","")



# name = '6295f81f9a52ac315fefa6a9'

r = requests.get("http://64.227.130.2:5000/api/v1/user/allUser")

d = r.json()

for employee in d['data']:
            # firstname = data['firstname']
    id = employee['id']
    firstname = employee['firstname']
    print(firstname , id)
    
    
