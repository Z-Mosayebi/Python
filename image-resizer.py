import cv2

img=cv2.imread('gol.jpg')
print(img.shape)

width = int(img.shape[1]/5)
height = int(img.shape[0]/5)

scade_img = cv2.resize(img,(width,height), interpolation=cv2.INTER_AREA)
cv2.imwrite('scade_photo1.jpg',scade_img)