import cv2
cap = cv2.VideoCapture(0) # open camera ID=0 (get object cap)
cap.set(3,640) # กำหนดขนาดความกว้าง
cap.set(4,480) # ความสูง

#ถ้าเชื่อมต่อหรือเปิดกล้องไม่ได้ ให้เเจ้งเตือน
if(cap.isOpened()==False):
    print('Could not open VDO source')

#วนรอบ อ่านสัญญาณภาพ แล้วแสดงที่หน้าต่าง Mywindow (แสดงภาพสดจากกล้อง)
while(cap.isOpened()):
    ret,frame = cap.read() # frame คือข้อมูลภาพจากกล้อง (ภาพเป็นเฟรมๆ)
    if ret == True:
        cv2.imshow('Mywindow',frame) # แสดงภาพนิ่งที่หน้าต่างpreview
        if cv2.waitKey(3) & 0xFF == 27 :#รอการกดEscเพื่อยุติการทำงาน
         break
    else: # else ของ if ret == True:
        break

cap.release() #ปิดกล้องและคืนทรัพยากร
cv2.destroyAllWindows() #ปิดหน้าต่าง