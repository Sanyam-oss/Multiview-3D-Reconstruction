import cv2
import numpy as np
import os
import sys
from scipy.optimize import least_squares
from tomlkit import boolean
from tqdm import tqdm
import matplotlib.pyplot as plt
from Image_loader import Image_loader
from sfm_algo import Sfm

if len(sys.argv) > 1:
    for i, arg in enumerate(sys.argv[1:], 1):
        sfm = Sfm("Datasets/"+arg)
        sfm()
else:
    print("Please provide dataset name!")
