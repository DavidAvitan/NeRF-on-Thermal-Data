# NeRF-on-Thermal-Data
Reconstruction of 3D Objects Using Neural Radiance Field (NeRF) on Thermal Data

1. **Installing Required Software:**
   
   a. python:
   - Install Python 3.9.7 or later.
   - Recommended: Use Anaconda. Download and install from https://www.anaconda.com/products/distribution
   - **Important** : Ensure Python is added to your system PATH during installation.
     
    b. CUDA Toolkit :
    - Download and install CUDA Toolkit 11.5 or later from https://developer.nvidia.com/cuda-toolkit

    c. Vulkan SDK (Optional, for DLSS support):
     - Download and install from https://vulkan.lunarg.com/


2. **Downloading Instant-NGP Files** 

   a. Download the appropriate package for your GPU:
    - For RTX 3000 & 4000 series: Download Link
    - For RTX 2000 series: Download Link  
    - For GTX 1000 series: Download Link
    
   b. Extract the files
    - Extract the downloaded files to a folder on your computer.

3. **Installing Python Requirements**
   - Copy the install_requirements.bat file to the extracted Instant-NGP folder
   - Run the install_requirements.bat file by double-clicking it.

4. **Installing FFMPEG**
   - Navigate to the scripts subfolder in the Instant-NGP folder.
   - Run the download_ffmpeg.bat file by double-clicking it.
   - **Important**: Add the FFMPEG path to your system PATH.

5. **Installing COLMAP**
   - Navigate to the scripts subfolder in the Instant-NGP folder.
   - Run the download_colmap.bat file by double-clicking it.
   - **Important**: Add the COLMAP path to your system PATH.

6. **Preparing Batch Files**
   - Copy the nerf_photos.bat and nerf_video.bat files to the main Instant-NGP folder.

7. **Using the Software**
   
     **a. Creating a NeRF from Video:**
   - Drag a video file onto nerf_video.bat.
   - Choose an FPS extraction value (Recommended: Choose a value that results in 150-300 images).
  
     
   **b. Creating a NeRF from Video:**
   - Drag a folder containing images onto nerf_photos.bat.
  
* **Note**: Files and folders must not contain spaces or special characters in their names.
After preparation is complete, the Instant NGP GUI will automatically launch and begin training. A transforms.json file will be created in the same location as the source file or image folder.


8. **Additional Tips**
   * For more information on optimal capture and training methods, refer to NVIDIA's official document here.
   * Note that NeRF is designed for use with color files (RGB), so the recommendations should be taken with a grain of salt when working on thermal images or grayscale data.
   * At the same time, it is imperative to go deeper and understand how to use the tool, capabilities and data collection methods in order to succeed in reaching better results.

   
9. **Additional Tools**
    - There were additional scripts written during the research. The purpose of these tools is to prepare the data for the process in order to obtain optimal results (changing image sizes, turning shades from black to white, etc.).
    - Each script has an indicative name in the name of the file indicating the action it performs and within each script there is accompanying documentation about the tool and its various functions.

10. **Data**
    - All the data from the stage of the research proposal to the end of the research as well as the code written are in GIT(here)    
