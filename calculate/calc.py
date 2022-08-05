import subprocess
from glob import glob
import os
import open3d as o3d
from utils import *
from pathlib import Path
from multiprocessing import Pool

ROOT = Path(__file__).parent.parent

plane_ws = "plane_ws"

for d in ["normal_ply","out"]:
    os.makedirs(ROOT/plane_ws/d,exist_ok=True)



ply_root = ROOT / "temp"
pcds = glob(os.path.join(ply_root, "*.ply"))
pcds.sort()

exe_dir="executable2"

def plane_one_file(file):
    
    # ROOT = Path("/home/azureuser/cloudfiles/code/Users/kaku.kouu/cloud_project")
    # file = str(ROOT/file)

    monitoring = False
    if monitoring:
        print("start monitor")
        print(file)
    fname = os.path.basename(file)
    base_name = os.path.splitext(fname)[0]
    pcd = o3d.io.read_point_cloud(file)
    file_normal = ROOT / plane_ws / "normal_ply/{}".format(fname)
    out_dir = str(ROOT / plane_ws / "out" ) + "/"
    # print(out_dir)
    out_file = ROOT / plane_ws / "out" / "{}".format(fname)
    out_without_file = ROOT / plane_ws / "out" / "{}".format(base_name)
    # temp=out_file+"_result"
    out_result = ROOT / plane_ws / "out" / (base_name + "_result1")
    print(file_normal)
    if len(pcd.normals) == 0:
        try:
            a = save_ply_with_normal(file, file_normal)
        except : print("error")

    if monitoring:
        print("\n passed norm\n ")
    # for ply in pcds:
    cmd1 = "{}/pdpcComputeMultiScaleFeatures -v -i {} -o {}".format(ROOT / exe_dir, file_normal, out_without_file)
    subprocess.run(cmd1, shell=True)

    if monitoring:
        print("\n passed cmd1\n")
    cmd2 = "{}/pdpcSegmentation -v -i {} -s {}_scales.txt -f {}_features.txt -o {}".format(ROOT / exe_dir,
                                                                                                   file_normal,
                                                                                                   out_dir+ base_name, out_dir+base_name,
                                                                                                   out_without_file)
    subprocess.run(cmd2,shell=True)
    
    if monitoring:
        print("\n passed cmd2\n")
    cmd3 = "{}/pdpcPostProcess -v -i {} -s {}_seg.txt -c {}_comp.txt -o {} -range 0 9 10 19 20 29 30 39 40 49 -col".format(ROOT / exe_dir, str(file_normal), out_dir+base_name, out_dir+base_name, str(out_result))
    subprocess.run(cmd3, shell=True)
    print("done ",base_name)

if __name__ == "__main__":



    # plane_one_file(pcds[3])

    with Pool() as p:
        p.map(plane_one_file,pcds)



    # for file in pcds:
