import cv2
scale = 0.5 # กำหนดscale เพื่อลดขนาดภาพ (50%)
image_file = 'testpic.jpg' # loadภาพที่ต้องการตรวจจับใบหน้า

# ไฟล์ข้อมูลตรวจจับใบหน้าที่ train เรียบร้อยแล้ว
casc_file = 'haarcascade_frontalface_default.xml' # ใช้ Haar

# สร้าง Haar cascade
frontal_face = cv2.CascadeClassifier(casc_file)
image = cv2.imread(image_file) # อ่านไฟล์ภาพ

# ลดขนาดภาพ
image = cv2.resize(image,None,fx=scale,fy=scale,interpolation=cv2.INTER_AREA)
gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #แปลงเป็นโทนเทา

#ตรวจจับใบหน้าในภาพ
bBoxes = frontal_face.detectMultiScale(gray_img,scaleFactor=1.3,minNeighbors=5,minSize=(30,30))

print('Found {} face'.format(len(bBoxes)))

# เขียนสี่เหลี่ยม/ตีกรอบ บริเวณที่พบใบหน้า
for (x,y,w,h) in bBoxes:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2) # ตีกรอบสี RGB และขนาดเส้น line width
cv2.imshow('Mywin',image)
cv2.waitKey(0)
cv2.destroyAllWindows()