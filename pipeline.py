# pipeline.py for yolov7, Spring 2023

import csv
import os
import json

def getLabelsLISA():
    direct = "../Downloads/LISA/Annotations/Annotations/dayTrain"
    sub_dir = os.listdir(direct)
    
    LISA_classes = set()

    for sdir in sub_dir:
        for annotfile in os.listdir(direct+"/"+sdir):
            annot = open(direct+"/"+sdir+"/"+annotfile)
            annot_csv = csv.reader(annot, delimiter=';')
            next(annot_csv)
            for row in annot_csv:
                LISA_classes.add(row[1])
    
    print(LISA_classes)


getLabelsLISA()
