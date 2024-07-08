import cv2

image1 = cv2.imread("C:\\Users\\97252\\Pictures\\NeRF333.jpg")
image2 = cv2.imread("C:\\Users\\97252\\Pictures\\source333.jpg")

psnr = cv2.PSNR(image1, image2)

print("PSNR is:", psnr)
