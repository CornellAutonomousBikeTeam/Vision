import csv
import os
import json
import shutil

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
        '0' : 0,
        '1' : 1,
        '2' : 2,
        '3' : 3,
        '4': -1,
        '5' : 4,
        '6': -1,
        '7' : 5,
        '8': -1,
        '9' : 6,
        '10' : 7,
        '11' : 8,
        '12' : 9,
        '13' : 10,
        '14': -1,
        '15' : 11,
        '16' : 12,
        '17' : 13,
        '18': -1,
        '19': -1,
        '20': -1,
        '21': -1,
        '22': -1,
        '23': -1,
        '24': -1,
        '25': -1,
        '26': -1,
        '27': -1,
        '28': -1,
        '29': -1,
        '30': -1,
        '31': -1,
        '32': -1,
        '33': -1,
        '34': -1,
        '35': -1,
        '36': -1,
        '37': -1,
        '38': -1,
        '39': -1,
        '40': -1,
        '41': -1,
        '42': -1,
        '43': -1,
        '44': -1,
        '45': -1,
        '46': -1,
        '47': -1,
        '48': -1,
        '49': -1,
        '50': -1,
        '51': -1,
        '52': -1,
        '53': -1,
        '54': -1,
        '55': -1,
        '56': -1,
        '57': -1,
        '58': -1,
        '59': -1,
        '60': -1,
        '61': -1,
        '62': -1,
        '63': -1,
        '64': -1,
        '65': -1,
        '66': -1,
        '67': -1,
        '68': -1,
        '69': -1,
        '70': -1,
        '71': -1,
        '72': -1,
        '73': -1,
        '74': -1,
        '75': -1,
        '76': -1,
        '77': -1,
        '78': -1,
        '79': -1
    }

    for p in ["train2017", "val2017"]:
        
        path = coco_path + "/" + p
        keepers = dict()

        all_files = os.listdir(path)

        c = 0

        for f in all_files:
            to_keep = []
            annot_file = open(path+"/"+f)
            annot_data = csv.reader(annot_file, delimiter = ' ')
            for row in annot_data:
                if coco_to_raph[row[0]] != -1:
                    row[0] = str(coco_to_raph[row[0]])
                    to_keep.append(" ".join(row))
            
            if to_keep!=[]:
                keepers[f] = "\n".join(to_keep)

        #dump content of keepers in dict
        with open(raph_path+"/"+p+".json", "w") as f:
            json.dump(keepers, f)

# Read json dumped file and copying images to the right location in raph
def moveImages():

    raph_path = "/home/autobike/yolov7/raph/labels/"

    for p in ["train2017", "val2017"]:
        
        path = raph_path + p+".json"

        json_file = open(path)

        data = json.load(json_file)

        l = list(data.keys())

        images_path = "/home/autobike/yolov7/raph/images/"

        for filename in l:
            imagename = filename.replace(".txt", ".jpg")
            shutil.copy("/home/autobike/yolov7/coco/images/" + p + "/" + imagename , images_path + p)
            shutil.copy("/home/autobike/yolov7/coco/labels/" + p + "/" + filename , raph_path + p)
