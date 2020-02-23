import cv2
import numpy as np 

net = cv2.dnn.readNet("yolov3.weights","yolov3.cfg")
classes = []
with open("coco.names","r") as coco:
    classes = [line.strip() for line in coco.readlines()]
layerNames = net.getLayerNames()
output = [layerNames[i[0]-1] for i in net.getUnconnectedOutLayers()]

cap = cv2.VideoCapture(0)
while(True):
    ret,img = cap.read()
    img = cv2.resize(img,None, fx=0.4,fy=0.3)
    h,w,c = img.shape
    # cv2.imshow("Window",img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows

    colors= np.random.uniform(0,255,size=(len(classes),3))


    #detecting objects
    blob = cv2.dnn.blobFromImage(img,0.00392,(416,416),(0,0,0),True,crop=False)

    net.setInput(blob)
    outs = net.forward(output)
    #print(outs[1])


    #get confidence score of algorithm in detecting an object in blob
    class_ids=[]
    confidences=[]
    boxes=[]
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                #onject detected
                center_x= int(detection[0]*w)
                center_y= int(detection[1]*h)
                w = int(detection[2]*w)
                h = int(detection[3]*h)
            
                #centering the boxes
                x=int(center_x - w/2)
                y=int(center_y - h/2)
                
                boxes.append([x,y,w,h]) 
                confidences.append(float(confidence)) #how confidence was that object detected and show that percentage
                class_ids.append(class_id) #name of the object tha was detected

    indexes = cv2.dnn.NMSBoxes(boxes,confidences,0.4,0.6)

    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x,y,w,h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[i]
            cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
            cv2.putText(img,label,(x,y+30),font,1,(255,255,255),2)
    
    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()