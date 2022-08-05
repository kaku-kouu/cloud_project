from calculate import plane_one_file
from utils import ply_from_bin_file,pcd_from_csv_file
import open3d as o3d
from pathlib import Path
import os
import time

start = time.time()
ROOT = Path(__file__).parent.parent

plane_ws = "plane_ws"

for d in ["normal_ply","out"]:
    os.makedirs(ROOT/plane_ws/d,exist_ok=True)

ply_root = ROOT / "temp"

os.makedirs(ply_root,exist_ok=True)

fname = './original_files/higashiku/jetson_04/pc_2022-02-15_16-00-04_652507.bin.csv'

pcd = pcd_from_csv_file(fname)


bname = os.path.basename(fname).replace(".csv",".ply")

ply_path = str(ply_root/bname)

o3d.io.write_point_cloud(ply_path,pcd)

print("processing csv ",fname,"\n","saved ply path ",ply_path)

plane_one_file(ply_path)

end = time.time()

print(end - start)