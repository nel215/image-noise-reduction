# coding: utf-8
from skimage import data, io

img = data.coffee()
io.imsave('coffee.png', img)
