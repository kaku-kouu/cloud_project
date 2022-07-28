import os, uuid, sys
from azure.storage.filedatalake import DataLakeServiceClient
from azure.core._match_conditions import MatchConditions
from azure.storage.filedatalake._models import ContentSettings
from azure.core.exceptions import (
    ResourceExistsError,
    ResourceNotFoundError
)

from azureml.core import Workspace

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
    storage_account_name="main-test-mine.py"
    storage_account_key ="fSKV+Dk0n4wxNa/CaJhuA9VVe1ip7C68FscYWZtpjtLoYUJrk8ymf/mE0Sjz1ID1dnUnYJfdej68JorqMSLt+w=="
    service_client = initialize_storage_account(storage_account_name,storage_account_key)

    file_system_client = service_client.get_file_system_client("pointclouds")
    paths = file_system_client.get_paths(path="senbahiroba")
    for path in paths:
        print(path.name + '\n')
    # dir_client = file_system_client.get_directory_client("senbahiroba")
    # temp1 = dir_client.get_directory_properties()

    d=1
    # for i in range(3):
    #     service_client.create_file_system("aaaaaa{}".format(str(i)))



    # create_directory("my-directory")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
