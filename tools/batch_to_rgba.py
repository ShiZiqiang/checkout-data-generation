from PIL import Image
import os

if __name__ == '__main__':
    path = './data/AIC23_Track4_Automated_Checkout/train_MSRCR'
    save_path = './data/AIC23_Track4_Automated_Checkout/train_RGBA'
    seg_path = './data/AIC23_Track4_Automated_Checkout/segmentation_labels'

    for file in os.listdir(path):
        if file.endswith('.jpg'):
            print(file)
            file = file.strip()
            file_name, _ = file.split(".")
            seg_file_name = file_name + '_seg.jpg'
            #print(seg_file_name)
            im_obj = Image.open(os.path.join(path, file))
            alpha_obj = Image.open(os.path.join(seg_path, seg_file_name))
            im_obj.putalpha(alpha=alpha_obj)
            rgba_file_name = file_name + '.png'
            im_obj.save(os.path.join(save_path, rgba_file_name))
