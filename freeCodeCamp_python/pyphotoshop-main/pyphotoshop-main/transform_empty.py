"""
Python Image Manipulation Empty Template by Kylie Ying (modified from MIT 6.865)

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

from image import Image
import numpy as np

def brighten(image, factor):
    # when we brighten, we just want to make each channel higher by some amount 
    # factor is a value > 0, how much you want to brighten the image by (< 1 = darken, > 1 = brighten)
    x_pixels, y_pixels, num_channels = image.array.shape
    new_image = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_image.array[x,y,c] = image.array[x,y,c] * factor

    #vectorized version
    #new_image.array = image.array * factor

    return new_image

def adjust_contrast(image, factor, mid=0.5):
    # adjust the contrast by increasing the difference from the user-defined midpoint by factor amount
    x_pixels, y_pixels, num_channels = image.array.shape
    new_image = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_image.array[x,y,c] = (image.array[x,y,c] - mid) * factor + mid

    #vectorized version
    #new_image.array = (image.array - mid) * factor + mid

    return new_image

def blur(image, kernel_size):
    # kernel size is the number of pixels to take into account when applying the blur
    # (ie kernel_size = 3 would be neighbors to the left/right, top/bottom, and diagonals)
    # kernel size should always be an *odd* number
    x_pixels, y_pixels, num_channels = image.array.shape
    new_image = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)

    neigh_range = kernel_size // 2
    

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):

                total = 0
                for xi in range(max(0, x-neigh_range), min(x+neigh_range, x_pixels-1)+1):
                    for yi in range(max(0, y-neigh_range), min(y+neigh_range, y_pixels-1)+1):
                        total += image.array[xi, yi, c]

                new_image.array[x,y,c] = total / (kernel_size ** 2)
    
    return new_image

def apply_kernel(image, kernel):
    # the kernel should be a 2D array that represents the kernel we'll use!
    # for the sake of simiplicity of this implementation, let's assume that the kernel is SQUARE
    # for example the sobel x kernel (detecting horizontal edges) is as follows:
    # [1 0 -1]
    # [2 0 -2]
    # [1 0 -1]
    pass

def combine_images(image1, image2):
    # let's combine two images using the squared sum of squares: value = sqrt(value_1**2, value_2**2)
    # size of image1 and image2 MUST be the same
    pass
    
if __name__ == '__main__':
    lake = Image(filename='lake.png')
    city = Image(filename='city.png')

    # brighten_image = brighten(lake, 1.9)
    # brighten_image.write_image('brighten.png')

    # dimmed_image = brighten(lake, 0.5)
    # dimmed_image.write_image('dimmed.png')

    # high_contrast = adjust_contrast(lake, 2)
    # high_contrast.write_image('high_conrast_vectorized.png')

    blured = blur(city, 5)
    blured.write_image('blured_skyline.png')

