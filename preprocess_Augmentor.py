# -*- coding:utf-8 -*-
'''  
#====#====#====#====
# Project Name:     Image-Augmentor
# File Name:        preprocess_Augmentor 
# Date:             2/4/18 2:02 PM 
# Using IDE:        PyCharm Community Edition  
# From HomePage:    https://github.com/DuFanXin/Image-Augmentor
# Author:           DuFanXin 
# BlogPage:         http://blog.csdn.net/qq_30239975  
# E-mail:           18672969179@163.com
# Copyright (c) 2018, All Rights Reserved.
#====#====#====#==== 
'''
import Augmentor

p = Augmentor.Pipeline(
	source_directory='../inputdata/image',
	output_directory='/home/dufanxin/PycharmProjects/Image-Augmentor/outputdata'
)
p.rotate(probability=0.5, max_left_rotation=10, max_right_rotation=10)
p.zoom(probability=0.5, min_factor=1.1, max_factor=1.6)
p.skew(probability=0.5)
p.random_distortion(probability=0.5, grid_width=100, grid_height=100, magnitude=1)
p.shear(probability=0.5, max_shear_left=10, max_shear_right=10)
p.crop_random(probability=0.5, percentage_area=0.6)
p.flip_random(probability=0.5)
p.sample(n=12000)
