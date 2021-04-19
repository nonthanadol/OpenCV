# install opencv by anaconda --> 1.open anaconda prompt --> conda install -c conda-forge opencv=3.4.2
# install opencv by pip --> pip install --upgrade pip --> pip install opencv-contrib-python
import cv2
img = cv2.imread('testpic.jpg',0) # open file (color mode) --> Gray tone ('name',0) or ('name',cv2.IMREAD_GRAYSCALE)
print(img.shape) # hight = 1706 x wide = 960 x 3 color(BGR)
cv2.imshow('image_non',img) # show image
cv2.waitKey(0) # รอการกดแป้นพิมพ์ใดๆ เพื่อปิดหน้าต่าง
cv2.destroyAllWindows() # ปิด.