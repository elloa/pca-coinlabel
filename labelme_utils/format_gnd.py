import re
import glob
import json
import cv2 as cv
import circle2bbox as cb
import matplotlib.pyplot as plt

src_dir  = '/home/yonekura/Documents/seg_coins_map/'
dst_dir  = '/home/yonekura/Documents/seg_coins_map/ground_truth/'

json_pattern = re.compile(src_dir + '(.*)\.json')

files = [(i,json_pattern.match(i).group(1)) for i in glob.glob(src_dir+'/*') if json_pattern.match(i) is not None]
for path, filename in files:
    with open(dst_dir+filename+'.txt','w') as file:
        circles = cb.data_from_json(src_dir + filename + '.json')[0]
        for circle in circles:
            x,y,w,h = cb.circle_2_tuple(circle['coord'])
            file.write("{} {} {} {} {}\n".format(circle['label'] ,x,y,x+w,y+h))
