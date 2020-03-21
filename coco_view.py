import argparse
from pycocotools.coco import COCO 
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Script for COCO annotation format visualization')

parser.add_argument('PATH', type=str,
                    help='path of annotation files')
parser.add_argument('--show_imgs', action='store_true',)
parser.add_argument('--show_masks', action='store_true',help='')
parser.add_argument('--show_labels', action='store_true',help='')
parser.add_argument('--ids', type=int, nargs='+',help='defines which images will be loaded')

parser.add_argument('--ids_range', type=int, nargs=2,
        help='defines an range of images to load, if specified, IDS are ignored')

args = parser.parse_args()
coco = COCO(args.PATH)

if args.ids == None:
    ids = list(range(len(coco.imgs)))
else:
    ids = args.ids

if args.ids_range != None:
    ids = list(range(args.ids_range[0], args.ids_range[1]+1))

    

cats = coco.loadCats([0,1,2,3,4,5])
img_ids = coco.getImgIds(imgIds=ids)
img_dict = coco.loadImgs(img_ids)

coco.info()
for img in img_dict:
    I = mpimg.imread("./coco_anns/"+img["file_name"])
    annIds = coco.getAnnIds(imgIds=[img['id']])
    anns = coco.loadAnns(annIds)

    if args.show_labels:
        for ann in anns:
            print("class: {},".format(cats[ann['category_id']]['name']),"bbox",ann['bbox'])

    if args.show_imgs:
        plt.imshow(I);
        coco.showAnns(anns)
        plt.show()

    if args.show_masks:
        mask = coco.annToMask(anns[0])
        for i in anns[1:]:
            mask = mask | coco.annToMask(i)
        plt.imshow(mask)
        plt.show()
