import os
from PIL import Image

# specify the path to the input folder
input_folder = "D:\Project\\NeRF\Code\Tools\\results"

# specify the path to the output folder
output_folder_vis = "D:\Project\\NeRF\Code\Tools\\results\\vis"
output_folder_termal = "D:\Project\\NeRF\Code\Tools\\results\\termal"

# loop through all the files in the input folder
for filename in os.listdir(input_folder):
    #if filename.endswith("_S.JPG"):  # check if the file ends with the letter S
    # open the image file
    img = Image.open(os.path.join(input_folder, filename))

    # get the size of the image
    width, height = img.size

    # split the image into two parts
    left = img.crop((0, 0, width / 2, height))
    right = img.crop((width / 2, 0, width, height))
    output_folder_vis
    # save the left and right parts as separate files
    #left.save(os.path.join(output_folder_termal, filename[:-4] + "L.jpg"))
    #right.save(os.path.join(output_folder_vis, filename[:-4] + "R.jpg")

    if not os.path.exists(output_folder_termal):
        os.makedirs(output_folder_termal)
    left.save(os.path.join(output_folder_termal, filename[:-4] + "L.jpg"))

    if not os.path.exists(output_folder_vis):
        os.makedirs(output_folder_vis)
    right.save(os.path.join(output_folder_vis, filename[:-4] + "R.jpg"))
