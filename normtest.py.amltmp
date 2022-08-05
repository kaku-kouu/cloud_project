import open3d as o3d

pcd = o3d.io.read_point_cloud ("/home/azureuser/cloudfiles/code/Users/kaku.kouu/cloud_project/temp/pc_2022-02-15_08-00-48_529780.bin.ply")

print(pcd)

pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))


print("done")