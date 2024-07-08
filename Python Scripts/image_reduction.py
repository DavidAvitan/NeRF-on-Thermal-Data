import os
import sys
from PIL import Image

# Check if correct number of arguments are passed
if len(sys.argv) != 2:
    print("Usage: python image_reduction.py [folder_path]")
    sys.exit(1)

# Get folder path from command line argument
folder_path = sys.argv[1]

# Check if the provided path is a directory
if not os.path.isdir(folder_path):
    print("Error: Invalid folder path provided.")
    sys.exit(1)

# Create "Results" subfolder if not already present
results_folder_path = os.path.join(folder_path, "Results")
if not os.path.exists(results_folder_path):
    os.mkdir(results_folder_path)

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        try:
            # Open the image using PIL
            with Image.open(file_path) as img:
                # Reduce image size by 40%
                width, height = img.size
                new_width = int(width * 0.6)
                new_height = int(height * 0.6)
                reduced_img = img.resize((new_width, new_height))

                # Save the reduced image in the "Results" subfolder
                reduced_file_path = os.path.join(results_folder_path, filename)
                reduced_img.save(reduced_file_path)
                print(f"Reduced image saved as: {reduced_file_path}")
        except Exception as e:
            print(f"Error processing image: {filename} - {e}")

print("Image reduction completed.")
