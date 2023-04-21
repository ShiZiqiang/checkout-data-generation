from code.plot import contrast_plot,demo_viper_with_retinex
from code.retinex import retinex_FM,retinex_SSR,retinex_MSR,retinex_MSRCR,retinex_gimp,retinex_MSRCP,retinex_AMSR
from code.tools import cv2_heq
import os.path
import cv2


with open('./retinex/AIC23_Track4_Automated_Checkout_train_image_path.txt', 'r') as f:
    for l in f:
        l = l.strip()
        l_array = l.split("/")
        print(l)
        #print(l_array[-1])

        img=cv2.imread(l)
        img_MSRCR = retinex_MSRCR(img)
        cv2.imwrite(os.path.join('./data/AIC23_Track4_Automated_Checkout/train_MSRCR/', l_array[-1]), img_MSRCR)

