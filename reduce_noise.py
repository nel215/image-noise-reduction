# coding: utf-8
import argparse
import numpy as np
from skimage import io, util
from sklearn.feature_extraction import image
from sklearn import preprocessing
from ksvd import ApproximateKSVD

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, required=True)
parser.add_argument('--output', type=str, required=True)
args = parser.parse_args()


def clip(img):
    img = np.minimum(np.ones(img.shape), img)
    img = np.maximum(np.zeros(img.shape), img)
    return img

img = util.img_as_float(io.imread(args.input))
patch_size = (5, 5)
patches = image.extract_patches_2d(img, patch_size)
signals = patches.reshape(patches.shape[0], -1)
mean = np.mean(signals, axis=1)[:, np.newaxis]
signals -= mean
aksvd = ApproximateKSVD(n_components=32)
dictionary = aksvd.fit(signals[:10000]).components_
gamma = aksvd.transform(signals)
reduced = gamma.dot(dictionary) + mean
reduced_img = image.reconstruct_from_patches_2d(
    reduced.reshape(patches.shape), img.shape)
io.imsave(args.output, clip(reduced_img))
