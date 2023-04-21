This repo is to prepare synthetic data for training classifiers and detectors used in https://github.com/ShiZiqiang/aicity-23/. Details on how to generate the data can be found in our paper "CheckSORT: Refined Synthetic Data Combination and Optimized SORT for Automatic Retail Checkout".

1. Generate synthesized background images (borrowed and adapted from https://github.com/cybercore-co-ltd/Track4_aicity_2022)

Run the following command to generate the backgrounds
```
cd generate_backgrounds
bash download.sh
cd  ../
```
The generated images are placed in ./generate_backgrounds/temp/

Then resize the background image from 256X256 to 381X491:
```
mkdir -p ./data/backgrounds/LSUN_256x256_N2M2S128/
mkdir -p ./data/backgrounds/CelebA_128x128_N2M2S64/
mkdir -p ./data/backgrounds/biggan_imagenet/
mkdir -p ./data/backgrounds/random_bg/
python ./tools/batch_resize.py
```

2. For objects of products (foreground products):

Put the original 116500 training images provided by the orginazer into ./data/AIC23_Track4_Automated_Checkout/train/.

Put segmentation labels of the original 116500  training images provided by the orginazer into
./data/AIC23_Track4_Automated_Checkout/segmentation_labels.

Do the MSRCR enhancement of training data 
use retinex (borrowed and adapted from https://github.com/muggledy/retinex)
```
mkdir ./data/AIC23_Track4_Automated_Checkout/train_MSRCR
python ./retinex/batch_MSRCR.py
```

Convert the RGB into RGBA png image
```
mkdir ./data/AIC23_Track4_Automated_Checkout/train_RGBA
python ./tools/batch_to_rgba.py
mv ./data/AIC23_Track4_Automated_Checkout/train_RGBA/ ./data/objects/
```

3. Synthesize image data for detectors (borrowed and adapted from https://github.com/a-nau/synthetic-dataset-generation/)

First to install the required packages.
```
pip install -r requirements.txt
```

Then do the opitimized synthesized training image generation (This program will generate images all the time without stopping, when it runs for 12 hours, it can be stopped manually).
```
python src/tools/generate_synthetic_data_train.py (Run 12 hours, then ctrl+c.)
```

Then combine the json files corresponding to all the images.
```
python src/tools/join_json.py
```

Generate part of the images for training classifiers (crop from the synthetic pictures just generated)
```
mkdir -p ./alladd2/train/
python src/tools/batch_mkdir.py
python src/tools/crop_117_class_objects.py
python src/tools/crop_classification_data.py
```

Comine with original 116500 training images for training classifiers
```
python batch_cp.py
```

Move the training data for detectors
```
mkdir coco_offline_MSRCR_GB_halfbackground_size100_no-ob_1
mv ./data/aicity23_train_scale0.4-0.8_iou0.5/train/ ./coco_offline_MSRCR_GB_halfbackground_size100_no-ob_1/
```
There is a instances_train.json in ./coco_offline_MSRCR_GB_halfbackground_size100_no-ob_1.
Change the last row of instances_train.json from "name": "box" to "name": "1".

So far we have completed the training data preparation for the classifier and detector, which are in folders ./alladd2 and ./coco_offline_MSRCR_GB_halfbackground_size100_no-ob_1/ respectively.


# Contact

If you have any questions, feel free to contact Ziqiang Shi (shiziqiang@fujitsu.com).
