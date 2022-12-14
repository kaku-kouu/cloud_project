# forked from pointcloud_clipping_utils/examples/example6_xxx.py

import numpy as np
import pointcloud_clipping_utils as pcu
import cv2
import os
import glob
import open3d as o3d
import sys
import argparse
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from calculate import plane_one_file
import logging
from sympy import im
from tqdm import tqdm
import random
# NOTE: 220408 既にあるデータを確認して、元のファイルを消しつつ、新しいファイルを作成するようにした
# NOTE: 220408 seg_planeについては、数が0のときはフォイルを出力しないので、毎時点で存在確認して消している。

if __name__ == '__main__':

    import functools
    print = functools.partial(print, flush=True)

    pcu.set_silent()

    # get date and time from arguments
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--date', type=str,
                        default="2022-02-15",  help="(default: %(default)s)")
    parser.add_argument('--time', type=str, default="16",
                        help="(default: %(default)s)")
    parser.add_argument('--min', type=int, default=None,
                        help="specity minute (default: %(default)s)")
    parser.add_argument('--obj_path', type=str, default="./objs/higashiku_jetson04_pc.obj",
                        help="(default: %(default)s)")
    parser.add_argument('--datastore_in', type=str, default="pointclouds_adls",
                        help="(default: %(default)s)")
    parser.add_argument('--datastore_out', type=str, default="plane_seg_output",
                        help="(default: %(default)s)")
    parser.add_argument('--dir', type=str, default="higashiku/jetson_04",
                        help="(default: %(default)s)")
    parser.add_argument('--blob_download_dir', type=str, default="./original_files",
                        help="(default: %(default)s)")


    parser.add_argument('--save_graph_results_only', action='store_true', default=False,
                        help="save graph and exit without upload (default: %(default)s)")

    args = parser.parse_args()

    print("args:", args, file=sys.stderr)

    save_graph_results_only = args.save_graph_results_only

    datastore_in = args.datastore_in
    datastore_out = args.datastore_out

    ws = pcu.get_workspace()
    client = pcu.get_adls_service_client_from_workspace(ws)

    all=[]

    dirs=[]
    places = ["higashiku","senbahiroba"]
    # places = ["senbahiroba"]

    for i in range(4,6):
        jetsons = "jetson_0{}".format(str(i))
        # dirs.append(places[0]+"/"+jetsons)

    for k in range(4,5):
        subfold = "j{}_lidar{}".format(str(k),str(k))
        dirs.append(places[1]+"/"+subfold)

    for dir_names in dirs:

        for mon in random.sample(range(2,13),4):

            for hi in tqdm(random.sample(range(1,32),3)):
                _date = str(hi).zfill(2)
                for t in random.sample(range(8,19),2):
                    # _time = args.time
                    _time = str(t).zfill(2)
                    _min = args.min
                    _range = range(60)

                    if save_graph_results_only:
                        _range = range(1)

                    if _min is not None:
                        _range = [_min]

                    for min in _range:

                        prefix = f"{dir_names}/pc_2022-{mon:02d}-{_date}_{_time}-{min:02d}"  #original
                        # prefix = f"{dir_names}/pc_"

                        # prefix = f"{dir_names}/pc_2022-02-15_16"

                        # ws = pcu.get_workspace()
                        ds = pcu.get_datastore(ws, datastore_in) #ds.get_paths(),  list_blobs() doesn't work
                        containers = list(ds.blob_service.list_containers())
                        
                        # files = ds.blob_service.list_blobs("higashiku")

                        temp = ds.path
                        # client = pcu.get_adls_container_client(ds)
                        # file_clients = client.list_file_systems()
                        # files=[a.name for a in list(file_clients)]
                        # all.append(files)
                        # # csv_file_path = blob_list_names[0]

                        # continue


                        ds_env = pcu.get_datastore(ws, datastore_out)
                        client_env = pcu.get_adls_container_client(ds_env)

                        # csv_file_path = "senbahiroba/j4_lidar4/pc_2022-02-15_16-30-01_373198.bin.csv"
                        # print("csv_file_path:", csv_file_path)

                        blob_download_dir = args.blob_download_dir
                        os.makedirs(blob_download_dir, exist_ok=True)
                        # print("downoading prefix:", prefix)

                        pcu.download_blob(ds, blob_download_dir, prefix)

                        # list csv_files from ./pointclouds_adls
                        csv_files = result = [y for x in os.walk(
                            blob_download_dir) for y in glob.glob(os.path.join(x[0], '*.bin.csv'))]

                    print("prefix:", prefix)

                    csv_files = [x for x in csv_files if (prefix in x)]
                    csv_files.sort()
                    print("downloaded x files",len(csv_files))
                    print(csv_files[:2])
                # print("csv_files:", csv_files)
    print(len(all))
    exit()
            
            # for file_path in csv_files:

            #     # print("file_path:", file_path)


            #     plane_one_file(file_path)

            #     continue


            # load pointcloud

            # points = pcu.load_points_from_bin_csv(
            #     file_path, voxel_size=0.1)
            # print("points.shape:", points.shape)

            # # get outside points of cubes

            # points_outside = pcu.get_outside_cubes(points, cubes)
            # print("points_outside.shape: ", points_outside.shape)

            # base_cube = pcu.get_base_cube()
            # # print("base_cube.shape: ", base_cube.shape)

            # ret, M, mask = cv2.estimateAffine3D(guide, base_cube)
            # # print("ret: ", ret)
            # # print("M: \n", M)

            # points_target = pcu.get_inside(points_outside, guide)
            # if points_target.shape[0] == 0:
            #     points_converted = np.array([])
            # else:
            #     points_converted = pcu.apply_affine_mat_to_points(
            #         points_target, M)

            #     if save_graph_results_only:
            #         fig = plt.figure()
            #         ax = fig.add_subplot(projection='3d')
            #         ax.set_xlim(0, 1)
            #         ax.set_ylim(0, 1)
            #         ax.set_zlim(0, 5)
            #         ax.scatter(
            #             points_converted[:, 0], points_converted[:, 1], points_converted[:, 2], s=2, c='gray')
            #         fig.savefig(
            #             f"{save_graph_dir}/{graph_base_name}_3d_view.png")

            #         fig = plt.figure()
            #         ax = fig.add_subplot()
            #         ax.set_title("Bird's eye view")
            #         ax.set_aspect('equal')
            #         ax.scatter(
            #             points_converted[:, 0] * bins[0], points_converted[:, 1] * bins[1], s=2, c='gray')
            #         fig.savefig(
            #             f"{save_graph_dir}/{graph_base_name}_bird_eye_view.png")

            #         fig = plt.figure()
            #         ax = fig.add_subplot()
            #         ax.set_title("Front view")
            #         ax.set_aspect('equal')
            #         ax.scatter(
            #             points_converted[:, 0], points_converted[:, 2], s=2, c='gray')
            #         fig.savefig(
            #             f"{save_graph_dir}/{graph_base_name}_front_view.png")

            #         fig = plt.figure()
            #         ax = fig.add_subplot()
            #         ax.set_title("Left view")
            #         ax.set_aspect('equal')
            #         ax.scatter(
            #             points_converted[:, 1], points_converted[:, 2], s=2, c='gray')
            #         fig.savefig(
            #             f"{save_graph_dir}/{graph_base_name}_left_view.png")

            # # print("points_target.shape: ", points_target.shape)
            # print("points_converted.shape: ", points_converted.shape)

            # if points_converted.shape[0] == 0:
            #     X = np.array([])
            #     Y = np.array([])

            #     persons_count = 0
            #     pos_str = ""

            # else:
            #     X = points_converted[:, 0]
            #     Y = points_converted[:, 1]

            #     bins_range = [np.arange(0.0, 1.0, 1/bins[0]), np.arange(0.0, 1.0, 1/bins[1])]
            #     H = np.histogram2d(X, Y, bins=bins_range)
            #     H = H[0].T
            #     # print("H.shape = ", H.shape)
            #     thresh_near = histogram_threshold_near
            #     thresh_far = histogram_threshold_far
            #     sep_meter = histogram_near_far_sep_meter
            #     # print("H: \n", H)
            #     H_near = H[0:sep_meter, :]
            #     H_far = H[sep_meter:, :]
            #     H_filtered_near = np.where(H_near > thresh_near, H_near, 0)
            #     H_filtered_far = np.where(H_far > thresh_far, H_far, 0)
            #     H_filtered = np.concatenate([H_filtered_near, H_filtered_far])
            #     persons_count = len(H_filtered[H_filtered > 0])

            #     if save_graph_results_only:
            #         fig = plt.figure()
            #         ax = fig.add_subplot()

            #         im = ax.imshow(H, interpolation='nearest', origin='lower', extent=[
            #                        0, H.shape[1], 0, H.shape[0]], cmap=cm.jet)
            #         ax.set_title('histogram')
            #         ax.set_xlabel('x')
            #         ax.set_ylabel('y')
            #         fig.colorbar(im, ax=ax)
            #         fig.savefig(
            #             f"{save_graph_dir}/{graph_base_name}_histogram.png")

            #         fig = plt.figure()
            #         ax = fig.add_subplot()

            #         im = ax.imshow(H_filtered, interpolation='nearest', origin='lower', extent=[
            #                        0, H.shape[1], 0, H.shape[0]], cmap=cm.jet)
            #         ax.set_title(f'histogram (filtered, thresh near={thresh_near} far={thresh_far} sep={sep_meter}m)')
            #         ax.set_xlabel('x')
            #         ax.set_ylabel('y')
            #         fig.colorbar(im, ax=ax)
            #         fig.savefig(
            #             f"{save_graph_dir}/{graph_base_name}_histogram_filtered.png")

            #     # get indices of values in H_filtered
            #     H_indices = np.where(H_filtered > 0)
            #     xs = H_indices[1] / bins_x
            #     ys = H_indices[0] / bins_y

            #     # xs_raw = H_indices[1]
            #     # ys_raw = H_indices[0]
            #     # poss_raw = [f"{xs_raw[i]},{ys_raw[i]}" for i in range(len(xs_raw))]
            #     # pos_raw_str = "\n".join(poss_raw)
            #     # print(pos_raw_str)
            #     # print("bins_x: ", bins_x)
            #     # print("bins_y: ", bins_y)

            #     poss = [f"{xs[i]:.3f},{ys[i]:.3f}" for i in range(len(xs))]
            #     pos_str = "\n".join(poss)
            #     # print(pos_str)

            # print("Persons:", persons_count)

            # # sys.exit(0)

            # persons_count_file_path = file_path.replace(
            #     ".bin.csv", "_person_count.csv")

            # # write persons count to file
            # with open(persons_count_file_path, "w") as f:
            #     f.write(pos_str)

            # o3d.utility.set_verbosity_level(o3d.utility.VerbosityLevel.Error)

            # if points_converted.shape[0] == 0:
            #     seg_plane_count = 0
            # else:
            #     pcd_outside = pcu.points_to_pointcloud(points_outside)

            #     try:
            #         seg_plane_count = pcu.segments_and_planes_count(
            #             pcd_outside,
            #             guide,
            #             eps=eps,
            #             size_max1_thresh=size_max1_thresh,
            #             size_max2_thresh=size_max2_thresh,
            #             size_min_thresh=size_min_thresh,
            #             seg_min_points=seg_min_points
            #         )
            #     except:
            #         import traceback
            #         traceback.print_exc()
            #         seg_plane_count = -1

            # print("SegPlaneCount:", seg_plane_count, flush=True)

            # seg_plane_count_file_path = file_path.replace(
            #     ".bin.csv", "_seg_plane_count.csv")

            # # write persons count to file
            # with open(seg_plane_count_file_path, "w") as f:
            #     f.write(str(seg_plane_count))

            # # print()
            # # client = pcu.get_adls_container_client(ds)
            # # blob_list_names = pcu.get_adls_blob_list_names(client, prefix)
            # # csv_file_path = blob_list_names[0]

            # # print(ds)

            # # pcu.upload_file_to_directory(
            # #     client,
            # #     persons_count_file_path,
            # #     os.path.basename(persons_count_file_path),
            # #     dir_names + "/person_count",
            # #     'pointclouds-env-removed'
            # # )

            # persons_count_meta_file_path = persons_count_file_path.replace(
            #     ".csv", "_") + f"{persons_count}.csv"

            # if not save_graph_results_only:
            #     # if already exists, delete it first

            #     check_file_prefix = os.path.basename(file_path.replace(".bin.csv", ""))
            #     existing_file_list = pcu.get_adls_blob_list_names(client_env, dir_names + "/person_count_meta/" + check_file_prefix)

            #     if len(existing_file_list) > 0:
            #         pcu.delete_file(
            #             client,
            #             os.path.basename(existing_file_list[0]),
            #             dir_names + "/person_count_meta/",
            #             'pointclouds-env-removed'
            #         )

            #     # then upload new one

            #     pcu.upload_file_to_directory(
            #         client,
            #         persons_count_file_path,
            #         os.path.basename(persons_count_meta_file_path),
            #         dir_names + "/person_count_meta",
            #         'pointclouds-env-removed'
            #     )

            #     # next seg_plane

            #     # if already exists, delete it first
                
            #     check_file_prefix = os.path.basename(file_path.replace(".bin.csv", ""))
            #     existing_file_list = pcu.get_adls_blob_list_names(client_env, dir_names + "/seg_plane_count_meta/" + check_file_prefix)

            #     if len(existing_file_list) > 0:
            #         pcu.delete_file(
            #             client,
            #             os.path.basename(existing_file_list[0]),
            #             dir_names + "/seg_plane_count_meta/",
            #             'pointclouds-env-removed'
            #         )

            #     # pcu.upload_file_to_directory(
            #     #     client,
            #     #     seg_plane_count_file_path,
            #     #     os.path.basename(seg_plane_count_file_path),
            #     #     dir_names + "/seg_plane_count",
            #     #     'pointclouds-env-removed'
            #     # )

            # if seg_plane_count > 0:
            #     seg_plane_count_meta_file_path = seg_plane_count_file_path.replace(
            #         ".csv", "_") + f"{seg_plane_count}.csv"

            #     if not save_graph_results_only:
            #         pcu.upload_file_to_directory(
            #             client,
            #             seg_plane_count_file_path,
            #             os.path.basename(seg_plane_count_meta_file_path),
            #             dir_names + "/seg_plane_count_meta",
            #             'pointclouds-env-removed'
            #         )

            # # delete original csv and uploaded files
            # if os.path.exists(file_path):
            #     os.remove(file_path)
            # if os.path.exists(persons_count_file_path):
            #     os.remove(persons_count_file_path)
            # if os.path.exists(seg_plane_count_file_path):
            #     os.remove(seg_plane_count_file_path)

            # print("", flush=True)

            # if save_graph_results_only:
            #     sys.exit(0)
