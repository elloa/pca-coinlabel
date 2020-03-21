import re
import glob
import json
import cv2 as cv
import numpy as np
from labelme_utils import circle2bbox as cb

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Circle, Polygon

src_dir = '/home/yonekura/Documents/pca-coinlabel/all/'

#Polygon_coins = [
#"10_1477289016.json",
#"130_1477862364.json",
#"10_1477186224.json",
#"25_1477149534.json",
#"5_1477145532.json",
#"75_1477849572.json"
#]

files = [i for i in glob.glob(src_dir+'/*.json') ]
#files = [src_dir+i for i in bruh ]
#files.sort()


for file in files:
    circles, img_path = cb.data_from_json(file)
    img = cv.imread(src_dir + img_path)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    mask = np.zeros((480,640))
    
    patches = []
    for circle in circles:
        if circle["shape_type"] == "circle":
            x,y,r = circle["coord"]
            patches.append(Circle((x,y),r))
        else:
            patches.append(Polygon(circle["coord"]))

    colors = 100*np.random.random(len(circles))

    ax = plt.gca()
    p = PatchCollection(patches, 
            cmap=matplotlib.cm.viridis, 
            linewidth=4, 
            facecolor="none",
            antialiased=True,
            alpha=0.7)
    p.set_array(colors)
    ax.add_collection(p)
    plt.imshow(img)
    plt.show()



