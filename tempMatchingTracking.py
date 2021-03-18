# ! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import sys
import time
import cv2
import numpy as np
from math import *
from skimage.feature import local_binary_pattern


def normalizeImage(v):
    v = (v - v.min()) / (v.max() - v.min() + 1)
    result = (v * 255).astype(np.uint8)
    return result


cap = cv2.VideoCapture('Taiwan.mp4')