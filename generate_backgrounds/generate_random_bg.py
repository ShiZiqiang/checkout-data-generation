import cv2
import numpy as np
import random
import os
import json
# Util methods for augmentation

path = os.path.abspath("./temp/random_bg")
if not os.path.exists(path):
    os.makedirs(path)

save_dict = {'images': [], 'annotations': []}
save_dict["categories"] = [
    {"supercategory": "person", "id": 0, "name": "person"}
]

img_id = 0
annotation_id = 0
for i in range(3200):
    R = random.randint(120, 200)
    #G = random.randint(120, 200)
    #B = random.randint(120, 200)
    img = np.zeros([381, 491, 3], dtype=np.uint8)
    #img = np.zeros([1080, 1920, 3], dtype=np.uint8)
    noise = np.random.normal(255./2, 255./10, img.shape)
    img[:,:,0] = R
    img[:,:,1] = R+random.randint(0, 10)
    img[:,:,2] = R+random.randint(0, 10)
    #print(value)
    H, W = img.shape[:2]
    #img[H-300:, ...] = noise[H-300:, ...]

    filename = str(i).zfill(6) + '.jpg'
    filepath = os.path.join('./temp/random_bg', filename)

    cv2.imwrite(filepath, img)
    '''
