import cv2

# create object VideoCapture to read input
cap = cv2.VideoCapture(0) # open camera ID=0 (get object cap)


# ไฟล์ข้อมูลตรวจจับใบหน้าที่ train เรียบร้อยแล้ว (ฐานความรู้ที่ทำให้คอมพิวเตอร์รู้จักใบหน้า)
casc_file = 'haarcascade_frontalface_default.xml' # ใช้ Haar

# สร้าง Haar cascade
frontal_face = cv2.CascadeClassifier(casc_file)

#ถ้าเชื่อมต่อหรือเปิดกล้อง(หรือไฟล์ VDO)ไม่ได้ ให้เเจ้งเตือน
if(cap.isOpened()==False):
    print('Could not open VDO source')

# ถ้าinputไม่มีปัญหา ทำการวนรอบ อ่านสัญญาณภาพและประมวล(Detect)
while( cap.isOpened() ):
    ret,frame=cap.read() # frame คือข้อมูลภาพinput

    if ret == True: # ถ้าอ่านข้อมูลภาพได้
        #เปลี่ยนเป็นภาพโทนเทา(ตรวจจับใบหน้าไม่จำเป็นต้องประมวลผลด้วยภาพสี)
        gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        #ตรวจจับใบหน้าในเฟรม
        bBoxes = frontal_face.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

        #จะได้ข้อมูลแบบ List ใน bBoxes กรณีมีหลายใบหน้า ก็ให้วนตีกรอบทุกใบหน้า
        for (x, y, w, h) in bBoxes:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # ตีกรอบสี RGB และขนาดเส้น line width

        cv2.imshow('Mywin',frame) #แสดงภาพและส่วนที่ตีกรอบรอบใบหน้า

        #หน่วงเวลาเฟรมถัดไป หรือ ถ้าผู้ใช้ กดEscให้ยุติการทำงาน
        if cv2.waitKey(10) & 0xFF == 27 :
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()