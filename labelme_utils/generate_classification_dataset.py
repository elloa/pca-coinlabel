import re
import io
import glob
import json
import base64
import PIL.Image
import cv2 as cv
import numpy as np
import circle2bbox as cb
import matplotlib.pyplot as plt

def decode_base64_image(filename):
    img = 0
    with open(filename, 'r') as f: 
        data = json.load(f) 
        if data['imageData'] is not None: 
            imageData = base64.b64decode(data['imageData']) 
            with io.BytesIO() as f:
                f.write(imageData)
                img = np.array(PIL.Image.open(f))
    return img

src_dir = '/home/yonekura/Documents/pca-coinlabel/all/'
dst_dir  = '/home/yonekura/Documents/seg_coins/'

json_pattern = re.compile('(\d*)_\d*.json')
json_labels = [i for i in glob.glob(src_dir+"/*.json")]

count = 0
for filename in json_labels:
    circles, img_path = cb.data_from_json(filename)
    img_id = filename.split('/')[-1][:-5]
    img = decode_base64_image(filename)
    img = cv.cvtColor(img,cv.COLOR_RGB2BGR)

    segmented_coins = cb.segment(img,circles) 
    for i, coin in enumerate(segmented_coins):
        label = circles[i]['label']
        count+=1
        #cv.imwrite(dst_dir + label + '/' + "{}_{}_{}.jpg".format(label,img_id,i),coin)
        #plt.imshow(coin)
        #plt.show()
    print(count)
