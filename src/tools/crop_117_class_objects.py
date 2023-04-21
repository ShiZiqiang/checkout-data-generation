
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
from PIL import Image


def crop(frame, tray):
    frame = frame[int(tray[1]):int(tray[3])][:][:]
    frame = np.transpose(frame, (1, 0, 2))
    frame = frame[int(tray[0]):int(tray[2])][:][:]
    frame = np.transpose(frame, (1, 0, 2))

    return frame

if __name__ == "__main__":
    
    img_cnt = 1
    loop_cnt = 1
    with open("./background_image_paths.txt") as f:
        for l in f:
            loop_cnt = loop_cnt + 1

            # if loop_cnt > 5000:
            #     break

            l = l.strip()
            if l[-3:] == "png":
                print(l)
                frame = cv2.imread(l)
                w, h, _ = frame.shape
                print('w h {} {}'.format(w, h))
                for i in range(2):
                    rndw = random.randint(3, w)
                    rndh = random.randint(3, h)
                    rndx = random.randint(0, w-rndw)
                    rndy = random.randint(0, h-rndh)

                    bbox = [rndx, rndy, rndx+rndw, rndy+rndh]
                    print(bbox)
                    #if l[-3:] == "png":

                    mask_frame=crop(frame, bbox)
                    # else:
                    #     #mask_frame = frame
                    #
                    #     frame1 = frame.copy()
                    #
                    #     mask_frame = frame1.crop((rndx, rndy, rndx+rndw, rndy+rndh))


                    print(mask_frame.shape)
                    savename1="./alladd2/train/class117/00117_"+str(img_cnt)+".jpg"
                    cv2.imwrite(savename1, mask_frame)
                    img_cnt = img_cnt + 1


                for i in range(1):
                    if loop_cnt % 5 == 0:
                        rndw = random.randint(3, w)
                        rndh = random.randint(3, h)
                        rndx = random.randint(0, w-rndw)
                        rndy = random.randint(0, h-rndh)

                        bbox = [rndx, rndy, rndx+rndw, rndy+rndh]
                        # if l[-3:] == "png":
                        mask_frame=crop(frame, bbox)
                        # else:
                        #     frame1 = frame.copy()
                        #
                        #     mask_frame = frame1.crop((rndx, rndy, rndx+rndw, rndy+rndh))
                        savename1="./alladd2/val/class117/00117_"+str(img_cnt)+".jpg"
                        cv2.imwrite(savename1, mask_frame)
                        img_cnt = img_cnt + 1

            else:

                print(l)
                #frame = cv2.imread(l)
                frame = Image.open(l)
                #w, h, _ = frame.shape
                w, h = frame.size
                print('w h {} {}'.format(w, h))
                for i in range(2):
                    rndw = random.randint(3, int(w/1))
                    rndh = random.randint(3, int(h/1))
                    rndx = random.randint(0, w - rndw)
                    rndy = random.randint(0, h - rndh)

                    bbox = [rndx, rndy, rndx + rndw, rndy + rndh]
                    print(bbox)

                    frame1 = frame.copy()
                    mask_frame = frame1.crop((rndx, rndy, rndx+rndw, rndy+rndh))

                    print(mask_frame.size)
                    savename1 = "./alladd2/train/class117/00117_" + str(img_cnt) + ".jpg"
                    #savename1 = "./data4classification/train/class117/00117_" + str(img_cnt) + ".jpg"
                    #cv2.imwrite(savename1, mask_frame)
                    mask_frame.save(savename1, 'JPEG')
                    img_cnt = img_cnt + 1

                for i in range(1):
                    if loop_cnt % 5 == 0:
                        rndw = random.randint(3, w)
                        rndh = random.randint(3, h)
                        rndx = random.randint(0, w - rndw)
                        rndy = random.randint(0, h - rndh)

                        bbox = [rndx, rndy, rndx + rndw, rndy + rndh]

                        frame1 = frame.copy()
                        mask_frame = frame1.crop((rndx, rndy, rndx+rndw, rndy+rndh))

                        savename1 = "./alladd2/val/class117/00117_" + str(img_cnt) + ".jpg"
                        #savename1 = "./data4classification/val/class117/00117_" + str(img_cnt) + ".jpg"
                        #cv2.imwrite(savename1, mask_frame)
                        mask_frame.save(savename1, 'JPEG')
                        img_cnt = img_cnt + 1

            #print(annotations[i]['bbox'])
            #bbox = [annotations[i]['bbox'][0], annotations[i]['bbox'][1], annotations[i]['bbox'][0]+annotations[i]['bbox'][2], annotations[i]['bbox'][1] + annotations[i]['bbox'][3]]
                #print(bbox)
            #mask_frame=crop(frame, bbox)
            #rndint = random.randint(0, 10)
            #savename1="./data4classification/train/class"+str(prod_id)+"/"+image_name[0:-4]+"_"+str(rndint)+".jpg"
                #print(savename1)
            #cv2.imwrite(savename1, mask_frame)
 

