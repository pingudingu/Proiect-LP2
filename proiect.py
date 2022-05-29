# This program is written by Abubakr Shafique (abubakr.shafique@gmail.com)
import cv2
import numpy as np  # This is to deal with numbers and arrays
import cv2 as cv  # This is to deal with images
import os
from os import listdir


import skimage
from skimage.exposure import is_low_contrast

def Max(Current_Value, New_Value):
    if New_Value > Current_Value:
        return New_Value
    else:
        return Current_Value


def Min(Current_Value, New_Value):
    if New_Value < Current_Value:
        return New_Value
    else:
        return Current_Value


def Histogram_Computation(Image):
    print("Aici sunt")
    Image_Height = Image.shape[0]
    Image_Width = Image.shape[1]
    Image_Channels = Image.shape[2]

    Histogram = np.zeros([256, Image_Channels], np.int32)

    Max_Intensity = np.zeros([Image_Channels], np.int32)
    Min_Intensity = np.full([Image_Channels], 255, np.int32)

    for x in range(0, Image_Height):
        for y in range(0, Image_Width):
            for c in range(0, Image_Channels):
                Histogram[Image[x, y, c], c] += 1
                Max_Intensity[c] = Max(Max_Intensity[c], Image[x, y, c])
                Min_Intensity[c] = Min(Min_Intensity[c], Image[x, y, c])

    return Histogram, Min_Intensity, Max_Intensity


def New_Pixel_Value(Current_Value, Min, Max):
    Target_Max = 255
    Target_Min = 0
    return (Target_Min + (Current_Value - Min) * int(Target_Max - Target_Min) / (Max - Min))


def Histogram_Equalization(Image, Min, Max):
    print('Si aici HE')
    Image_Height = Image.shape[0]
    Image_Width = Image.shape[1]
    Image_Channels = Image.shape[2]
    Size = (Image_Height, Image_Width, Image_Channels)

    New_Image = np.zeros(Size, np.uint8)

    for x in range(0, Image_Height):
        for y in range(0, Image_Width):
            for c in range(0, Image_Channels):
                New_Image[x, y, c] = New_Pixel_Value(Image[x, y, c], Min[c], Max[c])

    return New_Image


def main():
    


if __name__ == '__main__':
    main()