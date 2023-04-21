from pathlib import Path
import sys

ROOT = Path(__file__).parent.parent.parent
sys.path.append(ROOT.as_posix())
import shutil
import random
import numpy as np
import os
import json
import cv2
import random

seed = 42
random.seed(seed)
np.random.seed(seed)

DATA_DIR = ROOT / "data"

def crop(frame, tray):
    frame = frame[int(tray[1]):int(tray[3])][:][:]
    frame = np.transpose(frame, (1, 0, 2))
    frame = frame[int(tray[0]):int(tray[2])][:][:]
    frame = np.transpose(frame, (1, 0, 2))

    return frame


if __name__ == "__main__":


    for image_dir in os.listdir(ROOT / "data/aicity23_train_scale0.4-0.8_iou0.5/train"):
        #print('image_dir {}'.format(image_dir))
        #ROOT / "data/aicity23_dataset/train/" / image_dir
        #with open("./data/aicity23_dataset/train/00001/image_none00.json") as f:
        if os.path.exists("./data/aicity23_train_scale0.4-0.8_iou0.5/train/" + image_dir + "/image_none00.json"):
            with open("./data/aicity23_train_scale0.4-0.8_iou0.5/train/" + image_dir + "/image_none00.json") as f:
                instances_train = json.load(f)
                print(instances_train["render_config"]['objects'])
                annotations = instances_train["annotations"]
                nObjects = len(instances_train["render_config"]['objects'])
                objects = instances_train["render_config"]['objects']
                for i in range(nObjects):
                    image_name = objects[i]
                    prod_id, prod_cnt = image_name.split("_")
                    prod_id = int(prod_id)
                    frame = cv2.imread("./data/aicity23_train_scale0.4-0.8_iou0.5/train/" + image_dir + "/image_none00.jpg")
                    #print(annotations[i]['bbox'])
                    bbox = [annotations[i]['bbox'][0], annotations[i]['bbox'][1], annotations[i]['bbox'][0]+annotations[i]['bbox'][2], annotations[i]['bbox'][1] + annotations[i]['bbox'][3]]
                    #print(bbox)
                    mask_frame=crop(frame, bbox)
                    rndint = random.randint(0, 30)
                    #rndint = random.randint(0, 10000)
                    savename1="./alladd2/train/class"+str(prod_id)+"/"+image_name[0:-4]+"_"+str(rndint)+".jpg"
                    if annotations[i]['bbox'][2] > 2 and annotations[i]['bbox'][3] > 2:
                        cv2.imwrite(savename1, mask_frame)
                

