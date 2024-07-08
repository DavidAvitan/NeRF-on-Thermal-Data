import os
import glob

# Input folder path containing image files
folder_path = r"D:\\NeRF\\instant-ngp-master\\Test\\images"

# Get a list of all image files in the folder
image_files = glob.glob(os.path.join(folder_path, "*.jpg")) + glob.glob(os.path.join(folder_path, "*.jpeg")) + glob.glob(os.path.join(folder_path, "*.png")) + glob.glob(os.path.join(folder_path, "*.gif")) + glob.glob(os.path.join(folder_path, "*.bmp"))

# Loop through each image file
for image_file in image_files:
    # Extract the file name and extension
    file_name, file_ext = os.path.splitext(image_file)
    # Extract the last 4 characters of the file name
    last_4_chars = file_name[-2:]
    # Create the new file name with 'image' prefix and last 4 characters
    new_file_name = 'image' + last_4_chars + file_ext
    # Create the new file path
    new_file_path = os.path.join(folder_path, new_file_name)
    # Rename the image file
    os.rename(image_file, new_file_path)
    print(f"Renamed {image_file} to {new_file_path}")
