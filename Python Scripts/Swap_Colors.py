import cv2
import os

folder_path = 'D:\Project\\NeRF\Code\Tools\\results\\termal'


# loop through each image file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
        # read the image file
        img_path = os.path.join(folder_path, filename)
        img = cv2.imread(img_path)

        # convert the image to grayscale
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # invert the grayscale image
        inv_img = cv2.bitwise_not(gray_img)

        # convert the inverted image back to BGR format
        inv_bgr_img = cv2.cvtColor(inv_img, cv2.COLOR_GRAY2BGR)

        # save the modified image to the same folder with the same filename

        output_path = os.path.join(folder_path, filename)
        cv2.imwrite(output_path, inv_bgr_img)

        print(f"{filename} processed successfully")
