import cv2 # import opencv
scale = 0.75 #reduced scale picture to 75%
cap = cv2.VideoCapture('testvdo.mp4') # create object to open VDO file

if(cap.isOpened() == False): # ตรวจสอบการเปิดไฟล์VDOถ้ามีปัญหา ให้แจ้งเตือน
    print('Could not open the VDO file')
frame_counter = 0 # ตัวนับเฟรม เริ่มต้นให้เท่ากับ 0

while(cap.isOpened()): # วนรอบอ่านภาพนิ่งจากVDO
    ret,frame = cap.read() # อ่านเฟรมภาพนิ่งทีละเฟรม(capture frame by frame)
    if ret == True: # ถ้าอ่านเฟรมได้ไม่มีปัญหา
        frame_counter += 1 # เพิ่มตัวนับในการอ่านเฟรมต่อไป
        if frame_counter >= cap.get(cv2.CAP_PROP_FRAME_COUNT): # cv2.CAP_PROP_FRAME_COUNT นับจำนวนเฟรมที่มีใน VDO
            frame_counter = 0 # ถ้าจบ VDO แล้ว ให้วนรอบเริ่มเฟรมแรกใหม่
            cap.set(cv2.CAP_PROP_POS_FRAMES,frame_counter)

        #ลดขนาดภาพเพื่อให้เเสดงหน้าต่างVDOตามสเกลที่ตั้งไว้
        frame = cv2.resize(frame,None,fx=scale,fy=scale,interpolation=cv2.INTER_AREA)
        cv2.imshow('Mechmat',frame) # หน้าต่างแสดงเฟรมภาพ

        #หน่วงเวลาแต่ละเฟรม หรือ กด Esc เพื่อยุติการทำงาน ออกจากโปรแกรม
        if cv2.waitKey(30) & 0xFF == 27 :
            break

    #ถ้าอ่านเฟรมไม่ได้ ให้หยุด loop และปิดหน้าต่าง
    else: #else ของการอ่านเฟรม if ret == True:
            break
cap.release() #คืนทรัพยากร video capture object
cv2.destroyAllWindows() # ปิดหน้าต่าง
