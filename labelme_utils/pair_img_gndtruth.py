import shutil, random, os
import re
import glob

src_dir = '/home/yonekura/Documents/pca-coinlabel/all/'
dst_dir = '/home/yonekura/Documents/seg_coins_map/'

filename_pattern = re.compile(src_dir + '(\d*_\d*).json')
files = [filename_pattern.match(i).group(1) for i in glob.glob(src_dir+'*') if filename_pattern.match(i) is not None]

filenames = random.sample(files, 200)
for fname in filenames:
    if src_dir + fname + '.jpg' in glob.glob(src_dir+'*.jpg'):
        shutil.copyfile(src_dir + fname + '.jpg' , dst_dir + fname+ '.jpg')
        shutil.copyfile(src_dir + fname + '.json', dst_dir + fname+ '.json')

