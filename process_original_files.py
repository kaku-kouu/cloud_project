import os
import glob
from multiprocessing import Pool,set_start_method
from calculate import plane_one_file
from utils import ply_from_bin_file,pcd_from_csv_file
import open3d as o3d
from pathlib import Path
import os
import time

download_dir = "original_files"
ROOT = Path(__file__).parent

blob_download_dir = ROOT/ download_dir

ply_root = ROOT / "temp"

os.makedirs(ply_root,exist_ok=True)

def process_one_file(fname):

    # fname = './original_files/higashiku/jetson_04/pc_2022-02-15_16-00-04_652507.bin.csv'

    # ROOT = Path(__file__).parent
    # ROOT = Path("/home/azureuser/cloudfiles/code/Users/kaku.kouu/cloud_project")

    pcd = pcd_from_csv_file(fname)



    bname = os.path.basename(fname).replace(".csv",".ply")

    ply_path = str(ply_root/bname)

    o3d.io.write_point_cloud(ply_path,pcd)

    # print("processing csv ",fname,"\n","saved ply path ",ply_path)



    print("prossed fname",str(ROOT/ply_path))
    plane_one_file(str(ROOT/ply_path))

    return 0 


if __name__ =="__main__":

    set_start_method('spawn')

    import os

    # Get the current working directory
    cwd = os.getcwd()

    # Print the current working directory
    print("Current working directory: {0}".format(cwd))

    csv_files = result = [y for x in os.walk(
        blob_download_dir) for y in glob.glob(os.path.join(x[0], '*.bin.csv'))]

    

    # print("prefix:", prefix)

    # csv_files = [x for x in csv_files if (prefix in x)]
    csv_files.sort()

    # print(len(csv_files))

    # for item in csv_files[::100]:
        # process_one_file(item)

    p = Pool()
    p.map(process_one_file,csv_files[::10])