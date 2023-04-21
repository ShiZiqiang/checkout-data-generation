from PIL import Image
import os

if __name__ == '__main__':
    path1 = './generate_backgrounds/temp/LSUN_256x256_N2M2S128/'
    path2 = './generate_backgrounds/temp/CelebA_128x128_N2M2S64/'
    path3 = './generate_backgrounds/temp/biggan_imagenet/'
    path4 = './generate_backgrounds/temp/random_bg/'
    save_path1 = './data/backgrounds/LSUN_256x256_N2M2S128/'
    save_path2 = './data/backgrounds/CelebA_128x128_N2M2S64/'
    save_path3 = './data/backgrounds/biggan_imagenet/'
    save_path4 = './data/backgrounds/random_bg/'

    for file in os.listdir(path1):
        if file.endswith('.png'):
            #print(file)
            file = file.strip()
            file_name, _ = file.split(".")
            save_file_name = file_name + '.jpg'
            #print(save_file_name)
            im_obj = Image.open(os.path.join(path1, file))

            out = im_obj.resize((491, 381))
            out.save(save_path1 + save_file_name)

    for file in os.listdir(path2):
        if file.endswith('.png'):
            #print(file)
            file = file.strip()
            file_name, _ = file.split(".")
            save_file_name = file_name + '.jpg'
            #print(save_file_name)
            im_obj = Image.open(os.path.join(path2, file))

            out = im_obj.resize((491, 381))
            out.save(save_path2 + save_file_name)

    for file in os.listdir(path3):
        if file.endswith('.png'):
            #print(file)
            file = file.strip()
            file_name, _ = file.split(".")
            save_file_name = file_name + '.jpg'
            #print(save_file_name)
            im_obj = Image.open(os.path.join(path3, file))

            out = im_obj.resize((491, 381))
            out.save(save_path3 + save_file_name)

    for file in os.listdir(path4):
        if file.endswith('.png'):
            #print(file)
            file = file.strip()
            file_name, _ = file.split(".")
            save_file_name = file_name + '.jpg'
            #print(save_file_name)
            im_obj = Image.open(os.path.join(path4, file))

            out = im_obj.resize((491, 381))
            out.save(save_path4 + save_file_name)


