import re
import glob
import json
import cv2 as cv
import circle2bbox as cb
import matplotlib.pyplot as plt

src_dir = '/home/yonekura/Documents/pca-coinlabel/'
dst_dir  = '/home/yonekura/Documents/seg_coins/'

matricula_pattern = re.compile(src_dir + '(\d{10})')
filename_pattern = re.compile('/(\d*)_\d*')

#Find folders and get registration number
matriculas = [matricula_pattern.match(i).group(1) for i in glob.glob(src_dir+'/*') if matricula_pattern.match(i) is not None]
matriculas.sort()

"""
Generated file format:
    {Digit}_{ImageID}_{Num}.jpg

    Digit:   [5,10,25,50,100]
    ImageID: Identificador da imagem original
    Num:     Diferencia as moedas, Ex: imagens com moedas repetidas 
"""


for matricula in matriculas:
    json_pattern = re.compile(src_dir + matricula + '(.*\.json)')
    files = [json_pattern.match(i).group(1) for i in glob.glob(src_dir+matricula+'/*') if json_pattern.match(i) is not None]
    files.sort()

    #print(matricula,'qtd:',len(files))

    for file in files:
        circles, img_path = cb.data_from_json(src_dir+matricula+'/'+file)
        image_id = file.split('_')[1][1:-5]
        img_path = src_dir+matricula+'/'+img_path
        img = cv.imread(img_path)
        segmented_coins = cb.segment(img,circles) 
        
        for i, coin in enumerate(segmented_coins):
            label = circles[i]['label']
            #cv.imwrite(dst_dir + label + '/' + "{}_{}_{}.jpg".format(label,image_id,i),coin)
            print(dst_dir + label + '/' + "{}_{}_{}.jpg".format(label,image_id,i))

