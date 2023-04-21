
import os

if __name__ == '__main__':
    for i in range(117):
        prd_cnt = i+1
        train_path = "./alladd2/train/class" + str(prd_cnt)  
        val_path = "./alladd2/val/class" + str(prd_cnt)  
        
        if not os.path.exists(train_path):
            os.makedirs(train_path)
        
        if not os.path.exists(val_path):
            os.makedirs(val_path)

