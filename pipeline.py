import csv
import os
import json

# Get the list of classes for LISA
def getLabelsLISA():
    direct = "../Downloads/LISA/Annotations/Annotations/"
    sub_dir = os.listdir(direct)

    LISA_classes = set()

    for sdir in sub_dir:
        if sdir=='dayTrain' or sdir == "nightTrain":
            sub_sub_dir = os.listdir(direct+sdir)
            for ssdir in sub_sub_dir:
                for annotfile in os.listdir(direct+"/"+sdir+"/"+ssdir):
                    annot = open(direct+"/"+sdir+"/"+ssdir+"/"+annotfile)
                    annot_csv = csv.reader(annot, delimiter=';')
                    next(annot_csv)
                    for row in annot_csv:
                        LISA_classes.add(row[1])
        else:
            for annotfile in os.listdir(direct+"/"+sdir):
                annot = open(direct+"/"+sdir+"/"+annotfile)
                annot_csv = csv.reader(annot, delimiter=';')
                next(annot_csv)
                for row in annot_csv:
                    LISA_classes.add(row[1])

    
    print(LISA_classes)

# making raph directory where we store the data
"""
    mkdir raph
    mkdir raph/annotations
    mkdir raph/images
    mkdir raph/images/test2017
    mkdir raph/images/train2017
    mkdir raph/labels
    mkdir raph/labels/train2017
    mkdir raph/labels/val2017
"""

# filter out classes out of coco we will not use
def filterCOCO():

    coco_to_raph = {
        'person' : 0,
        'bicycle' : 1,
        'car' : 2,
        'motorcycle' : 3,
        'airplane': -1,
        'bus' : 4,
        'train': -1,
        'truck' : 5,
        'boat': -1,
        'traffic light' : 6,
        'fire hydrant' : 7,
        'stop sign' : 8,
        'parking meter' : 9,
        'bench' : 10,
        'bird': -1,
        'cat' : 11,
        'dog' : 12,
        'horse' : 13,
        'sheep': -1,
        'cow': -1,
        'elephant': -1,
        'bear': -1,
        'zebra': -1,
        'giraffe': -1,
        'backpack': -1,
        'umbrella': -1,
        'handbag': -1,
        'tie': -1,
        'suitcase': -1,
        'frisbee': -1,
        'skis': -1,
        'snowboard': -1,
        'sports ball': -1,
        'kite': -1,
        'baseball bat': -1,
        'baseball glove': -1,
        'skateboard': -1,
        'surfboard': -1,
        'tennis racket': -1,
        'bottle': -1,
        'wine glass': -1,
        'cup': -1,
        'fork': -1,
        'knife': -1,
        'spoon': -1,
        'bowl': -1,
        'banana': -1,
        'apple': -1,
        'sandwich': -1,
        'orange': -1,
        'broccoli': -1,
        'carrot': -1,
        'hot dog': -1,
        'pizza': -1,
        'donut': -1,
        'cake': -1,
        'chair': -1,
        'couch': -1,
        'potted plant': -1,
        'bed': -1,
        'dining table': -1,
        'toilet': -1,
        'tv': -1,
        'laptop': -1,
        'mouse': -1,
        'remote': -1,
        'keyboard': -1,
        'cell phone': -1,
        'microwave': -1,
        'oven': -1,
        'toaster': -1,
        'sink': -1,
        'refrigerator': -1,
        'book': -1,
        'clock': -1,
        'vase': -1,
        'scissors': -1,
        'teddy bear': -1,
        'hair drier': -1,
        'toothbrush': -1
    }

    path = "/home/autobike/yolov7/coco/labels/"
    for p in [path+"/"+"train2017", path+"/"+"val2017"]:
        all_files = os.listdir(p)
        for f in all_files:
            annot_file = open(p+"/"+f)
            annot_data = csv.reader(annot_file, delimiter = ' ')
            for row in annot_data:
                print(row)
                print()
            break
        break





filterCOCO()
