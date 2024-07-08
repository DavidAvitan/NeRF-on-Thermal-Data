import cv2
import numpy as np

def ssim(image1, image2, k1=0.01, k2=0.03):
    """
    Computes the Structural Similarity Index Measure (SSIM) between two images.

    Args:
        image1 (numpy.ndarray): The first image.
        image2 (numpy.ndarray): The second image.
        k1 (float, optional): The first Gaussian weight parameter. Defaults to 0.01.
        k2 (float, optional): The second Gaussian weight parameter. Defaults to 0.03.

    Returns:
        float: The SSIM value.
    """

    # Check if the images are empty.
    if image1.size == (0, 0) or image2.size == (0, 0):
        raise ValueError("One of the images is empty.")

    # Check if the images have the same dimensions.
    if image1.shape != image2.shape:
        raise ValueError("The images must have the same dimensions.")

    # Convert the images to grayscale.
    image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Compute the mean and standard deviation of each image.
    mu1 = np.mean(image1)
    mu2 = np.mean(image2)
    sigma1 = np.std(image1)
    sigma2 = np.std(image2)

    # Compute the covariance between the two images.
    c1 = np.sum((image1 - mu1) * (image2 - mu2)) / image1.size
    c2 = np.sum((image1 - mu1) ** 2) / image1.size
    c3 = np.sum((image2 - mu2) ** 2) / image1.size

    # Compute the SSIM value.
    ssim = (2 * mu1 * mu2 + k1) * (2 * c1 + k2) / ((mu1 ** 2 + k1) * (mu2 ** 2 + k2) + c2 * c3 + k1 * k2)

    return ssim

if __name__ == "__main__":
    # Load the images.
    source = "C:\\Users\\97252\\Pictures\\source333.jpg"
    #MVS = "D:\\Project\\NeRF\\Code\\Tools\\PSNR\\MVS.jpg"
    NeRF = "C:\\Users\\97252\\Pictures\\NeRF333.jpg"
    source_img = cv2.imread(source)
    #mvs_img = cv2.imread(MVS)
    nerf_img = cv2.imread(NeRF)

    # Compute the SSIM.
    ssim_NeRF = ssim(source_img, nerf_img)
    #ssim_MVS = ssim(source_img, mvs_img)

    #print("SSIM MVS is:", ssim_MVS)
    print("SSIM NeRF is:", ssim_NeRF)

