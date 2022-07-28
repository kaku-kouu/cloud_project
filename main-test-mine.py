import os, uuid, sys
from azure.storage.filedatalake import DataLakeServiceClient
from azure.core._match_conditions import MatchConditions
from azure.storage.filedatalake._models import ContentSettings
from azure.core.exceptions import (
    ResourceExistsError,
    ResourceNotFoundError
)
from time import sleep
from tqdm import tqdm
from azureml.core import Workspace
from glob import glob
import os
# ws = Workspace.create(name='myworkspace',
#                subscription_id='<azure-subscription-id>',
#                resource_group='myresourcegroup',
#                create_resource_group=True,
#                location='eastus2'
#                )


def initialize_storage_account(storage_account_name, storage_account_key):
    try:
        # global service_client

        service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
            "https", storage_account_name), credential=storage_account_key)

    except Exception as e:
        print(e)
    return service_client


def create_file_system(fname,service_client):
    try:
        # global file_system_client

        file_system_client = service_client.create_file_system(file_system=fname)

    except ResourceExistsError:
        file_system_client = service_client.get_file_client(file_system=fname)

    except Exception as e:

        print(e)


def create_directory(dirname,file_system_client):
    try:
        file_system_client.create_directory(dirname)

    except Exception as e:
        print(e)

# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    storage_account_name="myacc001"
    storage_account_key ="Pmx6Ii7ZdpanSBHoi2nrePGSlZ+smBUBrq6mwaKShGa24uwIrYTuoJVwyDNCGrccgVzBX2A+H4dD+AStxE8Dcg=="
    service_client = initialize_storage_account(storage_account_name,storage_account_key)



    # for i in range(3):
    #     service_client.create_file_system("aaaaaa{}".format(str(i)))

    service1=service_client.get_file_system_client("aaaaaa0")

    directory_client = service1.get_directory_client("bbbbb0")

    temp =[os.path.basename(f.name) for f in list(service1.get_paths()) if len(f.name.split("/"))>1]

    temp2 =[os.path.basename(f.name) for f in list(service1.get_paths()) if f.name.endswith(".ply")]

    for fname in tqdm(temp):
        file_client = directory_client.get_file_client(fname)
        download = file_client.download_file()
        download_bytes = download.readall()

        local_file = open(os.path.join("temp",fname),"wb")
        local_file.write(download_bytes)
        local_file.close()

    exit()

    # directory_client.create_directory("ccccccc1")
    # exit()
    all = glob("/mnt/ssd2/pcd_project/temp/*")
    files = [a for a in all if a.endswith(".ply")]

    directory_client.get_file_client()

    # for f in tqdm(files):
    #     name = os.path.basename(f)
    #
    #     file_client = directory_client.create_file(name)
    #     local_file = open(f, 'rb')
    #
    #     file_contents = local_file.read()
    #
    #     file_client.append_data(data=file_contents, offset=0, length=len(file_contents))
    #
    #     file_client.flush_data(len(file_contents))


    # file1 =

    # file1.create_directory("bbbbbc2")

    # for k in range(10):
    #
    #     file1.create_directory("bbbbb{}".format(str(k)))
        # sleep(2)

    # create_directory("my-directory")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
