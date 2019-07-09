import numpy as np
import csv
import math

def convolution2d(image, kernel):
    m, n = kernel.shape
    if m == n:
        y, x = image.shape
        y = y - m + 1
        x = x - m + 1
        new_image = np.zeros((y,x))
        for i in range(y):
            for j in range(x):
                new_image[i][j] = np.sum(image[i:i+m, j:j+m]*kernel)
    return new_image


from numpy import genfromtxt
image = genfromtxt("channel2.csv", delimiter=",")
image = np.array(image)


edge_detection = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

sharpen = np.array([[-1, -1, -1], [-1, -8, -1], [-1, -1, -1]])

box_blur = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

gaussian_blur = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])

gaussian_blur_5 = np.array([[1, 4, 6, 4, 1], [4, 16, 24, 16, 4], [6, 24, -476, 24, 6],[4, 16, 24, 16, 4], [1, 4, 6, 4, 1]])

new_edge_image = convolution2d(image,edge_detection)
new_edge_image = convolution2d(image,edge_detection)

with open("edge.csv","w", newline = '') as f:
    writer = csv.writer(f)
    writer.writerows(new_edge_image)

new_sharpen_image = convolution2d(image,sharpen)
new_sharpen_image = convolution2d(image,sharpen)


with open("sharpen.csv","w", newline = '') as f:
    writer = csv.writer(f)
    writer.writerows(new_sharpen_image)


new_box_image = convolution2d(image,box_blur)
new_box_image = convolution2d(image,box_blur)

with open("box.csv","w", newline = '') as f:
    writer = csv.writer(f)
    writer.writerows(new_box_image)

new_gauss_image = convolution2d(image,gaussian_blur)
new_gauss_image = convolution2d(image,gaussian_blur)

with open("gauss.csv","w", newline = '') as f:
    writer = csv.writer(f)
    writer.writerows(new_gauss_image)


new_gauss_5_image = convolution2d(image,gaussian_blur_5)
new_gauss_5_image = convolution2d(image,gaussian_blur_5)

with open("gauss_5.csv","w", newline = '') as f:
    writer = csv.writer(f)
    writer.writerows(new_gauss_5_image)

new_unsharp_5_image = convolution2d(image,unsharp_mask_5)
new_unsharp_5_image = convolution2d(image,unsharp_mask_5)

with open("unsharp.csv","w", newline = '') as f:
    writer = csv.writer(f)
    writer.writerows(new_unsharp_5_image)
