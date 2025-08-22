import numpy as np
import pandas as pd
import sys
sys.path.append('/Users/mattgoldberg/Projects/CSEM/research/CRIOS/SMART/smart_cables/')
from utils import *
import matplotlib.pyplot as plt
import os

import pandas as pd
from plotting import express as px
from plotting import graph_objects as go

# Base directory relative to the notebook/post
base_dir = os.path.join(os.getcwd(), "assets", "data", "aste")   
nx, ny = (250, 150)
x = read_float32(os.path.join(base_dir, 'x.bin')).reshape((nx, ny))
y = read_float32(os.path.join(base_dir, 'y.bin')).reshape((nx, ny))
z = read_float32(os.path.join(base_dir, 'z.bin')).reshape((nx, ny))
df = pd.read_csv(os.path.join(base_dir, 'sc_aste.csv'))

# Normalize/filter z
#z_filtered = np.exp(z / (np.max(z) + 1e-10))
#z = z_filtered.copy()

# Build custom blue colorscale
blues = plt.cm.get_cmap('Blues')
blues_r = blues.reversed()
colorscale = []
for i in range(blues_r.N):
    rgba = blues_r(i / (blues_r.N - 1))
    colorscale.append([i / (blues_r.N - 1), f'rgba({rgba[0]*255}, {rgba[1]*255}, {rgba[2]*255}, {rgba[3]})'])
