import cv2
import matplotlib.pyplot as plt

path='test.tif'
img = cv2.imread(path)

print(img.shape)
# resize an image
resized_img_1st_way = cv2.resize(img,(200,100),interpolation=cv2.INTER_AREA)
resized_img_2nd_way = cv2.resize(img,None,fx=0.3,fy=0.4,interpolation=cv2.INTER_AREA)

print('Size of original image -> ',img.shape)
print('Size after resizing using 1st way -> ',resized_img_1st_way.shape)
print('Size after resizing using 2nd way -> ',resized_img_2nd_way.shape)

# Plotting our results in one place
plt.figure(figsize=(12,8))

plt.subplot(131)
plt.imshow(img)
plt.title('Original Image')

plt.subplot(132)
plt.imshow(resized_img_1st_way)
plt.title('Resized using 1st way')

plt.subplot(133)
plt.imshow(resized_img_2nd_way)
plt.title('Resized using 2nd way')

plt.show()
plt.tight_layout()
