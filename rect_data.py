# importing csv module
import csv
import matplotlib.pyplot as plt
import cv2
import numpy as np
import imutils
from PIL import Image
import os
import math
import glob


#blank_image=cv2.imread("/home/yogesh/Desktop/computer vision sub/abc.jpeg")

# csv file name
#filename = "/home/yogesh/Desktop/computer_vision_sub/rect.csv"
#cap=cv2.VideoCapture("/home/yogesh/Desktop/movidius-rpi-master/dl vision/mall.mp4")

filename = "csv_data/data1.csv"
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)



    # extracting each data row one by one
    for row in csvreader:
        #print(row)
        rows.append(row)

co = []
i=0
for j in rows:
    c=[]

    for k in j:
         c.append(''.join(i for i in k if i.isdigit()))
         #print(k)    
    co.append(c)


frame_no=0
x_all=[]
y_all=[]
old=[[150,250],[150,250]]
pair=[]
img_dir="/home/yogesh/Desktop/computer_vision_sub/project/UCSD_Anomaly_Dataset.v1p2/UCSDped1/Test/Test006"

#img_dir="/home/yogesh/Desktop/computer_vision_sub/UCSD_Anomaly_Dataset.v1p2/UCSDped1/Train/Train001"
data_path = os.path.join(img_dir,'*f')
files = sorted(glob.glob(data_path))
data = []
crop=[]

for f1 in files:
    img = Image.open(f1)
    img = np.array(img) 
    data.append(img)


for frame in co:
    frame_no=frame_no+1
    #print(frame)
   
   # cap.set(cv2.CAP_PROP_POS_FRAMES,frame_no)
    new=[]
    #(grabbed, frames) = cap.read()
    frames=data[frame_no]
    #frames=frames.resize([158,238])
    #ret, frames = cap.read()
    frames = imutils.resize(frames, width=158,height=238)
    if len(frame)>1:
        for i in range(int(len(frame)/2)):

           # x0=int(frame[0+i*4])
            #y0=int(frame[1+i*4])
            #x1=int(frame[2+i*4])
            #y1=int(frame[3+i*4])
            x=int(frame[0+i*2])
            y=int(frame[1+i*2])
            x_all.append(x)
            y_all.append(y)
            new.append([x,y])
            #y=0
            for q in old:
                #print(q[0],x,q[1],y)
                if abs(q[0]-x)<20 and abs(q[1]-y)<20:
                    pair.append([x,y,q[0],q[1]])
                    #cv2.line(frames,(x,y),(q[0],q[1]),(0,255,0), 4)

                #if (q[0]-x)<50 and (q[1]-y)<50:
                #print((min(q[2],x1)-min(q[0],x0))*(min(q[3],y1)-min(q[1],y0)))
                #print("area")
                #print((x1-x0)*(y1-y0))
                #if (min(q[2],x1)-min(q[0],x0))*(min(q[3],y1)-min(q[1],y0))<0.5*(x1-x0)*(y1-y0):
                #for ind in range(len(x_all)):
                #    cv2.circle(frames,(x_all[ind],y_all[ind]), 5, (0,255,0), -1)
                #else:
                #    cv2.circle(frames,(x,y), 5, (0,0,255), -1)
    old=new
            #cv2.rectangle(blank_image, (x0,y0), (x1,y1),(255, 0, 0), 2)
    #print(pair)
    if  True:
        if(frame_no%20==0):
            img = np.zeros([158,238])
            for line in pair:
                cv2.line(img,(line[0],line[1]),(line[2],line[3]),(255,255,255), 4)
                cv2.imwrite("data/img_%i.jpg"%(frame_no),img)
            pair=[]

        for line in pair:
            #print(frames.shape)
            cv2.line(frames,(line[0],line[1]),(line[2],line[3]),(0,255,0), 4)
        cv2.imshow("abvv",frames)
        if cv2.waitKey(3000) & 0xFF == ord('q'):
            
            break


# if the `q` key was pressed, break from the loop

