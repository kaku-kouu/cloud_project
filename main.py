import os, uuid, sys
from azure.storage.filedatalake import DataLakeServiceClient
from azure.core._match_conditions import MatchConditions
from azure.storage.filedatalake._models import ContentSettings
from azure.core.exceptions import (
    ResourceExistsError,
    ResourceNotFoundError
)

from azure_utils import *
import pathlib
from argparse import ArgumentParser

try:
    from configparser import ConfigParser
    parser = ConfigParser()
    pwd = pathlib.Path(__file__).parent
    par = pathlib.Path(pwd).parent
    parser.read(pwd / "config" / 'env.conf')
    input_storage_account_name= parser.get("xxxx","input_storage_account_name")
    input_storage_account_key= parser.get("xxxx","input_storage_account_key")
    out_storage_account_name = parser.get("xxxx","out_storage_account_name")
    out_storage_account_key = parser.get("xxxx","out_storage_account_key")

except:
    print("env.conf error mlib")
    sys.exit(1)


from azureml.core import Workspace

# ws = Workspace.create(name='myworkspace',
#                subscription_id='<azure-subscription-id>',
#                resource_group='myresourcegroup',
#                create_resource_group=True,
#                location='eastus2'
#                )




# Press the green button in the gutter to run the script.

if __name__ == '__main__':

    parser = ArgumentParser(description="multiscale plane detection")
    # parser.add_argument("input_")
    source_client =initialize_storage_account(input_storage_account_name, input_storage_account_key)
    out_client = initialize_storage_account(out_storage_account_name, out_storage_account_key)

    root1=source_client.get_file_system_client("pointclouds")

    dirs1 = list(root1.get_paths())

    fsystems = source_client.list_file_systems()
    # for fs in fsystems:
    #     print(fsystems.name)

    # list1  = [a.name for a in source_client.list_file_systems()]
    # d=12


    # initialize_storage_account(input_storage_account_name, input_storage_account_key)






    # create_file_system("my-file-system")
    # create_directory("my-directory")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
