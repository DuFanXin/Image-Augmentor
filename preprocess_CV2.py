# -*- coding:utf-8 -*-
'''  
#====#====#====#====
# Project Name:     Image-Augmentor
# File Name:        preprocess_CV2 
# Date:             2/5/18 11:17 AM 
# Using IDE:        PyCharm Community Edition  
# From HomePage:    https://github.com/DuFanXin/Image-Augmentor
# Author:           DuFanXin 
# BlogPage:         http://blog.csdn.net/qq_30239975  
# E-mail:           18672969179@163.com
# Copyright (c) 2018, All Rights Reserved.
#====#====#====#==== 
'''
import cv2
import numpy as np
import warnings


def convert_from_color_segmentation(image_3d=None):
	# import numpy as np
	patterns = {
		(0, 0, 0): 0,       # 边界
		(255, 255, 255): 1  # 细胞
	}
	with warnings.catch_warnings():
		warnings.simplefilter("ignore")
		# image_3d = img_as_ubyte(image_3d)
	image_2d = np.zeros((image_3d.shape[0], image_3d.shape[1]), dtype=np.uint8)
	for pattern, index in patterns.items():
		# print(pattern)
		# print(index)
		match = (image_3d == np.array(pattern).reshape(1, 1, 3)).all(axis=2)
		# print(m)
		image_2d[match] = index

	return image_2d


def read():
	im = cv2.imread('../outputdata/image_b9c8ec40-ba93-4f37-a472-8e9cc118d11f.JPEG')
	# im = cv2.imread('../inputdata/image/combine0.png')
	arr = im[:, :, 2]
	cv2.imshow('r', arr)
	cv2.waitKey(0)


def write():
	# image_arr = cv2.imread('../inputdata/image/0.tif', 0)
	# label_arr = cv2.imread('../inputdata/label/0.tif')
	# label = convert_from_color_segmentation(label_arr) * 10
	# arr = np.zeros(shape=label_arr.shape, dtype=np.uint8)
	# arr[:, :, 0] = image_arr
	# arr[:, :, 2] = label
	# cv2.imwrite('../inputdata/simdata2.png', arr)
	for index in range(30):
		image_arr = cv2.imread('../inputdata/image/%d.tif' % index, 0)
		label_arr = cv2.imread('../inputdata/label/%d.tif' % index)
		label = convert_from_color_segmentation(label_arr) * 200
		arr = np.zeros(shape=label_arr.shape, dtype=np.uint8)
		arr[:, :, 0] = image_arr
		arr[:, :, 2] = label
		cv2.imwrite('../inputdata/image/combine%d.png' % index, arr)

if __name__ == '__main__':
	# write()
	read()

