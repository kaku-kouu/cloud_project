import cv2
import numpy as np
from glob import glob
import os
from tqdm import tqdm
from pathlib import Path


def plys_to_video(plys):

    ROOT = Path(__file__).parent.parent

    img_array = []

    video_root = ROOT/"plane_ws"/"videos"
    imgs_root = ROOT/"plane_ws"/"imgs"
    os.makedirs(video_root,exist_ok=True)
    os.makedirs(imgs_root,exist_ok=True)


    # 
    imgs_fname = [a for a in glob("../caps/*") if a.endswith(".jpg")]
    imgs_fname.sort()
    # img = cv2.imread(imgs_fname[0])
    # h,w,c = img.shape
    # size=(w,h)

    for file in tqdm(imgs_fname):
        img = cv2.imread(file)
        h,w,c = img.shape
        size=(w,h)
        img_array.append(img)


    out = cv2.VideoWriter(os.path.join(video_root,"nuscenes.mp4"),cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),10,size)

    for i in tqdm(range(len(img_array))):
        out.write(img_array[i])

    out.release()

