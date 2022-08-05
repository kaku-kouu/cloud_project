from glob import glob
import os, uuid, sys
from azure.storage.filedatalake import DataLakeServiceClient
from azure.core._match_conditions import MatchConditions
from azure.storage.filedatalake._models import ContentSettings
from azure.core.exceptions import (
    ResourceExistsError,
    ResourceNotFoundError
)
from upload_to_datastore import *
import os
from tqdm import tqdm


storage_account_name = "analysisoutput"
storage_account_key= "TPOuIkXenrHD92AK86HQvj2aRqPbGLARYNySYzWx0539sesObvB1NDyiggRYxPG4jkypeNqt2zFt+AStxINNwA=="
service_client = initialize_storage_account(storage_account_name,storage_account_key)

file_system_client = service_client.get_file_system_client("2022-8-2")

temp = file_system_client.get_file_system_properties()

directory_client = file_system_client.create_directory("higashi_20_29")

# directory_client = file_system_client.get_directory_client("higashi_20_29")
#
# exit()

output_path = "/home/azureuser/cloudfiles/code/Users/kaku.kouu/cloud_project/plane_ws/out"

scale = "020_029"

plys = glob(output_path+"/*.ply")

scale_plys = [a for a in plys if "{}.ply".format(scale) in a]

print(len(scale_plys))

for fname in tqdm(scale_plys):

    basename = os.path.basename(fname)

    file_client = directory_client.create_file(basename)
    local_file = open(fname, 'rb')

    file_contents = local_file.read()

    file_client.append_data(data=file_contents, offset=0, length=len(file_contents))

    file_client.flush_data(len(file_contents))

    












# ws = Workspace.from_config("../config.json")

# print(ws.name, ws.resource_group, ws.location, ws.subscription_id, sep = '\n')

# ds = get_datastore(ws,datastore_name="plane_seg_output") 

# data_paths = [(ds, a) for a in scale_plys]

# file_dataset_4 = Dataset.File.from_files(path=data_paths)

# file_dataset_4.File.upload_directory(src_dir, target, pattern=None, overwrite=True, show_progress=True)



