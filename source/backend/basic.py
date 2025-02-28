import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
import time

model=YOLO('yolov8s.pt')


def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        colorsBGR = [x, y]
        print(colorsBGR)
        

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

cap=cv2.VideoCapture('parking1.mp4.mp4')
file_path = "source\\backend\\coco.txt"


my_file = open(file_path, "r")
data = my_file.read()
class_list = data.split("\n")
   



area1=[(888,375),(911,354),(870,316),(822,320)]
area2=[(881,377),(840,379),(770,318),(819,317)]
area3=[(785,377),(833,377),(765,316),(719,318)]
area4=[(736,380),(780,378),(714,318),(666,320)]
area5=[(682,377),(726,377),(660,318),(615,317)]
area6=[(676,377),(629,377),(599,317),(607,317)]
area7=[(624,377),(573,376),(507,319),(555,316)]
area8=[(570,378),(519,373),(456,317),(503,317)]
area9=[(516,377),(470,377),(403,316),(450,317)]
area10=[(422,377),(462,377),(399,316),(352,316)]
area11=[(365,377),(411,377),(348,316),(299,316)]
area12=[(315,377),(363,377),(298,317),(253,317)]
area13=[(309,377),(272,377),(203,316),(246,314)]
area14=[(218,377),(257,377),(198,316),(155,316)]
area15=[(209,377),(166,377),(104,312),(149,312)]
area16=[(158,369),(112,370),(60,310),(97,312)]
area17=[(68,372),(112,369),(52,313),(11,312)]
area18=[(1015,211),(982,212),(939,160),(974,162)]
area19=[(934,210),(976,214),(927,161),(886,159)]
area20=[(882,213),(924,211),(881,158),(850,160)]
area21=[(827,211),(870,211),(824,158),(783,158)]
area22=[(774,209),(815,211),(772,160),(729,163)]
area23=[(728,211),(765,211),(719,159),(672,158)]
area24=[(666,211),(711,211),(664,157),(621,157)]
area25=[(610,210),(656,213),(612,159),(563,160)]
area26=[(557,209),(601,212),(555,159),(510,158)]
area27=[(502,209),(544,209),(497,152),(455,154)]
area28=[(447,210),(493,212),(448,158),(402,156)]
area29=[(393,210),(437,210),(392,159),(350,160)]
area30=[(339,211),(384,209),(340,159),(297,156)]
area31=[(285,207),(331,210),(287,157),(242,158)]
area32=[(233,205),(277,206),(236,159),(190,159)]
area33=[(182,209),(224,206),(182,153),(139,157)]
area34=[(133,208),(172,209),(131,161),(91,160)]
area35=[(67,208),(122,209),(84,160),(41,162)]



while True:    
    ret,frame = cap.read()
    if not ret:
        break
    
    frame=cv2.resize(frame,(1020,500))

    results=model.predict(frame)
    print(results)
    a=results[0].boxes.data
    px=pd.DataFrame(a).astype("float")
    print(px)
    
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    list5=[]
    list6=[]
    list7=[]
    list8=[]
    list9=[]
    list10=[]
    list11=[]
    list12=[]
    list13=[]
    list14=[]
    list15=[]
    list16=[]
    list17=[]
    list18=[]
    list19=[]
    list20=[]
    list21=[]
    list22=[]
    list23=[]
    list24=[]
    list25=[]
    list26=[]
    list27=[]
    list28=[]
    list29=[]
    list30=[]
    list31=[]
    list32=[]
    list33=[]
    list34=[]
    list35=[]
    
    for index,row in px.iterrows():
#        print(row)
 
        x1=int(row[0])
        y1=int(row[1])
        x2=int(row[2])
        y2=int(row[3])
        d=int(row[5])
        c=class_list[d]
        if 'car' in c:
            cx=int(x1+x2)//2
            cy=int(y1+y2)//2

            results1=cv2.pointPolygonTest(np.array(area1,np.int32),((cx,cy)),False)
            if results1>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list1.append(c)  
            
            results2=cv2.pointPolygonTest(np.array(area2,np.int32),((cx,cy)),False)
            if results2>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list2.append(c)  
             
            results3=cv2.pointPolygonTest(np.array(area3,np.int32),((cx,cy)),False)
            if results3>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list3.append(c)  
               
               
            results4=cv2.pointPolygonTest(np.array(area4,np.int32),((cx,cy)),False)
            if results4>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list4.append(c)    
               
            results5=cv2.pointPolygonTest(np.array(area5,np.int32),((cx,cy)),False)
            if results5>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list5.append(c) 
               
            results6=cv2.pointPolygonTest(np.array(area6,np.int32),((cx,cy)),False)
            if results6>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list6.append(c)      
               
            results7=cv2.pointPolygonTest(np.array(area7,np.int32),((cx,cy)),False)
            if results7>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list7.append(c)      
               
            results8=cv2.pointPolygonTest(np.array(area8,np.int32),((cx,cy)),False)
            if results8>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list8.append(c)     
               
            results9=cv2.pointPolygonTest(np.array(area9,np.int32),((cx,cy)),False)
            if results9>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list9.append(c)      
               
            results10=cv2.pointPolygonTest(np.array(area10,np.int32),((cx,cy)),False)
            if results10>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list10.append(c)     
               
            results11=cv2.pointPolygonTest(np.array(area11,np.int32),((cx,cy)),False)
            if results11>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list11.append(c)     
               
            results12=cv2.pointPolygonTest(np.array(area12,np.int32),((cx,cy)),False)
            if results12>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list12.append(c)      
               
            results13=cv2.pointPolygonTest(np.array(area13,np.int32),((cx,cy)),False)
            if results13>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list13.append(c)      
               
            results14=cv2.pointPolygonTest(np.array(area14,np.int32),((cx,cy)),False)
            if results14>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list14.append(c)     
               
            results15=cv2.pointPolygonTest(np.array(area15,np.int32),((cx,cy)),False)
            if results15>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list15.append(c)      
          
            results16=cv2.pointPolygonTest(np.array(area16,np.int32),((cx,cy)),False)
            if results16>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list16.append(c)  
        
            results17=cv2.pointPolygonTest(np.array(area17,np.int32),((cx,cy)),False)
            if results17>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list17.append(c)  
             
            results18=cv2.pointPolygonTest(np.array(area18,np.int32),((cx,cy)),False)
            if results18>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list18.append(c) 
               
               
               
               
               
            results19=cv2.pointPolygonTest(np.array(area19,np.int32),((cx,cy)),False)
            if results19>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list19.append(c)      
              
            results20=cv2.pointPolygonTest(np.array(area20,np.int32),((cx,cy)),False)
            if results20>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list20.append(c)  
    
            results21=cv2.pointPolygonTest(np.array(area21,np.int32),((cx,cy)),False)
            if results21>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list21.append(c)
            
            results22=cv2.pointPolygonTest(np.array(area22,np.int32),((cx,cy)),False)
            if results22>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list22.append(c)    
            
            results23=cv2.pointPolygonTest(np.array(area23,np.int32),((cx,cy)),False)
            if results23>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list23.append(c)      
               
            results24=cv2.pointPolygonTest(np.array(area24,np.int32),((cx,cy)),False)
            if results24>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list24.append(c)
               
            results25=cv2.pointPolygonTest(np.array(area25,np.int32),((cx,cy)),False)
            if results25>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list25.append(c)       
               
            results26=cv2.pointPolygonTest(np.array(area26,np.int32),((cx,cy)),False)
            if results26>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list26.append(c)     
            
            results27=cv2.pointPolygonTest(np.array(area27,np.int32),((cx,cy)),False)
            if results27>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list27.append(c)
               
            results28=cv2.pointPolygonTest(np.array(area28,np.int32),((cx,cy)),False)
            if results28>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list28.append(c)
               
               
            results29=cv2.pointPolygonTest(np.array(area29,np.int32),((cx,cy)),False)
            if results29>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list29.append(c) 
               
            results30=cv2.pointPolygonTest(np.array(area30,np.int32),((cx,cy)),False)
            if results30>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list30.append(c)
               
            results31=cv2.pointPolygonTest(np.array(area31,np.int32),((cx,cy)),False)
            if results31>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list31.append(c) 
               
            results32=cv2.pointPolygonTest(np.array(area32,np.int32),((cx,cy)),False)
            if results32>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list32.append(c)           
            
            results33=cv2.pointPolygonTest(np.array(area33,np.int32),((cx,cy)),False)
            if results33>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list33.append(c)
               
            results34=cv2.pointPolygonTest(np.array(area34,np.int32),((cx,cy)),False)
            if results34>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list34.append(c)
               
            results35=cv2.pointPolygonTest(np.array(area35,np.int32),((cx,cy)),False)
            if results35>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list35.append(c) 
        
              
           
    
    a1=(len(list1))
    a2=(len(list2))
    a3=(len(list3))
    a4=(len(list4))
    a5=(len(list5))
    a6=(len(list6))
    a7=(len(list7))
    a8=(len(list8))
    a9=(len(list9))
    a10=(len(list10))
    a11=(len(list11))
    a12=(len(list12))
    a13=(len(list13))
    a14=(len(list14))
    a15=(len(list15))
    a16=(len(list16))
    a17=(len(list17))
    a18=(len(list18))   
    a19=(len(list19))
    a20=(len(list20))
    a21=(len(list21))
    a22=(len(list22))
    a23=(len(list23))
    a24=(len(list24))
    a25=(len(list25))
    a26=(len(list26))
    a27=(len(list27))
    a28=(len(list28))
    a29=(len(list29))
    a30=(len(list30))
    a31=(len(list31))
    a32=(len(list32))
    a33=(len(list33))
    a34=(len(list34))
    a35=(len(list35))
    
    
    
    
    
    
    
    
    
    
    
    
    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print(a5)
    print(a6)
    print(a7)
    print(a8)
    print(a9)
    print(a10) 
    print(a11)
    print(a12)
    print(a13)
    print(a14)
    print(a15)
    print(a16)
    print(a17)
    print(a18)
    print(a19)
    print(a20)
    print(a21)
    print(a22)
    print(a23)
    print(a24)
    print(a25)
    print(a26)
    print(a27)
    print(a28)
    print(a29)
    print(a30)
    print(a31)
    print(a32)
    print(a33)
    print(a34)
    print(a35)
      
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    
    if a1==1:
        cv2.polylines(frame,[np.array(area1,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('1'),(911,374),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area1,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('1'),(911,374),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
    
    if a2==1:
        cv2.polylines(frame,[np.array(area2,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('2'),(869,388),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area2,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('2'),(869,388),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
    
    if a3==1:
        cv2.polylines(frame,[np.array(area3,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('3'),(811,387),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area3,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('3'),(811,387),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
        
    if a4==1:
        cv2.polylines(frame,[np.array(area4,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('4'),(762,384),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area4,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('4'),(762,384),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)    

    if a5==1:
        cv2.polylines(frame,[np.array(area5,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('5'),(702,386),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area5,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('5'),(702,386),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
    
    if a6==1:
        cv2.polylines(frame,[np.array(area6,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('6'),(653,382),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area6,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('6'),(653,382),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
    
 
    if a7==1:
        cv2.polylines(frame,[np.array(area7,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('7'),(606,390),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area7,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('7'),(606,390),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
   
    if a8==1:
        cv2.polylines(frame,[np.array(area8,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('8'),(550,385),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area8,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('8'),(550,385),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
   
    if a9==1:
        cv2.polylines(frame,[np.array(area9,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('9'),(496,382),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area9,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('9'),(496,382),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
   
    if a10==1:
        cv2.polylines(frame,[np.array(area10,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('10'),(443,385),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area10,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('10'),(443,385),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
   
    if a11==1:
        cv2.polylines(frame,[np.array(area11,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('11'),(392,381),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area11,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('11'),(392,381),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
   
    if a12==1:
        cv2.polylines(frame,[np.array(area12,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('12'),(337,382),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area12,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('12'),(337,382),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
   
    if a13==1:
        cv2.polylines(frame,[np.array(area13,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('13'),(287,385),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area13,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('13'),(287,385),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
   
    if a14==1:
        cv2.polylines(frame,[np.array(area14,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('14'),(238,378),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area14,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('14'),(238,378),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
   
    if a15==1:
        cv2.polylines(frame,[np.array(area15,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('15'),(184,379),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area15,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('15'),(184,379),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
   
    if a16==1:
        cv2.polylines(frame,[np.array(area16,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('16'),(139,379),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area16,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('16'),(139,379),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
   
    if a17==1:
        cv2.polylines(frame,[np.array(area17,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('17'),(94,381),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area17,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('17'),(94,381),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
   
    if a18==1:
        cv2.polylines(frame,[np.array(area18,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('18'),(952,139),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area18,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('18'),(952,139),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
        
    if a19==1:
        cv2.polylines(frame,[np.array(area19,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('19'),(904,138),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area19,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('19'),(904,138),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
        
    if a20==1:
        cv2.polylines(frame,[np.array(area20,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('20'),(850,137),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area20,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('20'),(850,137),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
        
    if a21==1:
        cv2.polylines(frame,[np.array(area21,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('21'),(794,138),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area21,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('21'),(794,138),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
    
    
    if a22==1:
        cv2.polylines(frame,[np.array(area22,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('22'),(747,138),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area22,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('22'),(747,138),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
    
    if a23==1:
        cv2.polylines(frame,[np.array(area23,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('23'),(694,138),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area23,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('23'),(694,138),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
    
    if a24==1:
        cv2.polylines(frame,[np.array(area24,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('24'),(634,140),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area24,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('24'),(634,140),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
    
    if a25==1:
        cv2.polylines(frame,[np.array(area25,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('25'),(582,136),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area25,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('25'),(582,136),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
    
    if a26==1:
        cv2.polylines(frame,[np.array(area26,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('26'),(525,134),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area26,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('26'),(525,134),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
    
    if a27==1:
        cv2.polylines(frame,[np.array(area27,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('27'),(474,137),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area27,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('27'),(474,137),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
    
    if a28==1:
        cv2.polylines(frame,[np.array(area28,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('28'),(416,135),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area28,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('28'),(416,135),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
    
    if a29==1:
        cv2.polylines(frame,[np.array(area29,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('29'),(365,137),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area29,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('29'),(365,137),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
    
    if a30==1:
        cv2.polylines(frame,[np.array(area30,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('30'),(314,132),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area30,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('30'),(314,132),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
    
    if a31==1:
        cv2.polylines(frame,[np.array(area31,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('31'),(262,138),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area31,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('31'),(262,138),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
    
    
    if a32==1:
        cv2.polylines(frame,[np.array(area32,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('32'),(212,140),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area32,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('32'),(212,140),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
    
    if a33==1:
        cv2.polylines(frame,[np.array(area33,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('33'),(154,137),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area33,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('33'),(154,137),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
    
    if a34==1:
        cv2.polylines(frame,[np.array(area34,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('34'),(109,141),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area34,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('34'),(109,141),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
    
    if a35==1:
        cv2.polylines(frame,[np.array(area35,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('35'),(56,139),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area35,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('35'),(56,139),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
       
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    cv2.imshow("RGB", frame)

































    if cv2.waitKey(0)&0xFF==27:
        break
cap.release()
#cv2.destroyAllWindows()
#stream.stop()


