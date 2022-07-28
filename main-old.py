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
        global service_client

        service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
            "https", storage_account_name), credential=storage_account_key)

    except Exception as e:
        print(e)


def create_file_system(fname):
    try:
        global file_system_client

        file_system_client = service_client.create_file_system(file_system=fname)

    except ResourceExistsError:
        file_system_client = service_client.get_file_client(file_system=fname)

    except Exception as e:

        print(e)


def create_directory(dirname):
    try:
        file_system_client.create_directory(dirname)

    except Exception as e:
        print(e)

# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    storage_account_name="myacc001"
    storage_account_key ="Pmx6Ii7ZdpanSBHoi2nrePGSlZ+smBUBrq6mwaKShGa24uwIrYTuoJVwyDNCGrccgVzBX2A+H4dD+AStxE8Dcg=="
    initialize_storage_account(storage_account_name,storage_account_key)

    create_file_system("my-file-system")
    create_directory("my-directory")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
