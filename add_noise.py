# coding: utf-8
import argparse
from skimage import io, util

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, required=True)
parser.add_argument('--output', type=str, required=True)
args = parser.parse_args()

img = util.img_as_float(io.imread(args.input))
img_with_noise = util.random_noise(img, seed=1)
io.imsave(args.output, img_with_noise)
