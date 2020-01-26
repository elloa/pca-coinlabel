import re
import glob
import json
import cv2 as cv
import circle2bbox as cb
import matplotlib.pyplot as plt

src_dir  = '/home/yonekura/Documents/seg_coins_map/'
dst_dir  = '/home/yonekura/Documents/seg_coins_map/input/ground-truth/'

json_pattern = re.compile(src_dir + '(.*)\.json')

files = [i for i in glob.glob(src_dir+'/*.json')]
for filename in files:
    circles = cb.data_from_json(filename)[0]
    with open(filename[:-5]+'.txt','w') as file:
        for circle in circles:
            x,y,w,h = cb.circle_2_tuple(circle['coord'])
            file.write("{} {} {} {} {}\n".format(circle['label'] ,x,y,x+w,y+h))
