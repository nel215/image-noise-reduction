# coding: utf-8
import argparse
from skimage import io, util, measure

parser = argparse.ArgumentParser()
parser.add_argument('--true', type=str, required=True)
parser.add_argument('--noise', type=str, required=True)
parser.add_argument('--reduced', type=str, required=True)
args = parser.parse_args()

true = io.imread(args.true)
noise = io.imread(args.noise)
reduced = io.imread(args.reduced)

print('noise: %.3f' % (measure.compare_psnr(true, noise)))
print('reduced: %.3f' % (measure.compare_psnr(true, reduced)))
