import PIL.Image
import json
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def circle_2_tuple(circle):
    """
    Takes a tuple representing a circle as (x,y,radius)
    and returns a tuple with the x,y coordinates and width,size (x,y,w,h)
    """
    assign_coord = lambda x,y: x - y if x > y else 0
    x = assign_coord(circle[0],circle[2])
    y = assign_coord(circle[1],circle[2])

    assign_size = lambda x,y : y*2 if x > y else y*2 - (y-x)  
    w = assign_size(circle[0],circle[2])
    h = assign_size(circle[1],circle[2])
    return (x,y,w,h)

def circle_2_bbox(circle):
    """
    Takes a tuple representing a circle as (x,y,radius)
    and returns a tuple represeting a bbox ((x,y),(x',y'))
    """
    x,y,w,h = circle_2_tuple(circle)
    return ((x,y),(x+w,y+h))

def fix_bbox(bbox,img_shape):
    """
    Takes a tuple of tuples represeting a bbox ((x,y),(x',y'))
    and returns 
    """
    x = min(bbox[1][0],img_shape[1])
    y = min(bbox[1][1],img_shape[0])
    return ((bbox[0]),(x,y))

def bbox_from_circle(img, circles):
    """
    Draws bboxes in a image given an array of circles [(x,y,radius)]
    """
    seg_imgs = []
    bboxes = []
    aux = img.copy()
    for i,el in enumerate(circles):
        bbox = circle_2_bbox(el['coord'])
        bbox = fix_bbox(bbox,aux.shape)
        cv.rectangle(aux,bbox[0],bbox[1],(0,255,0))
        bboxes.append(bbox)
    return bboxes

def segment(img, circles):
    seg_imgs = []
    meme = np.zeros_like(img)
    for i,el in enumerate(circles):
        x,y,w,h = circle_2_tuple(el['coord'])
        circle = el['coord']

        if x == y and x == 0:
            w=circle[2]*2
            h=circle[2]*2
        if w > h:
            h = w;
        else:
            w = h
        aux = np.zeros((h,w,3),dtype=np.uint8)

        mask = np.zeros_like(img)
        cv.circle(mask,(circle[0],circle[1]),circle[2],(255,255,255),-1)
        mask = cv.bitwise_and(img,mask)
        crop_img = mask[y:y+h, x:x+w]

        dim = crop_img.shape

        aux[:dim[0], :dim[1],:] = crop_img
        seg_imgs.append(aux)
    return seg_imgs

def data_from_json(filename):
    circles = []
    with open(filename) as json_file:
        data = json.load(json_file)
        for i, shape in enumerate(data['shapes']):
            if shape['label'] == 'finger':
                continue
            if shape['shape_type'] == 'circle':
                coord = shape['points']
                coord[0] = np.array(coord[0],dtype=np.int64)
                coord[1] = np.array(coord[1],dtype=np.int64)
                circle = (coord[0][0], coord[0][1],int(cv.norm(coord[0]-coord[1])))
                circles.append(dict(coord=circle,label=shape['label']))
    return circles,data['imagePath']


