import os, uuid, sys
from azure.storage.filedatalake import DataLakeServiceClient
from azure.core._match_conditions import MatchConditions
from azure.storage.filedatalake._models import ContentSettings
from azure.core.exceptions import (
    ResourceExistsError,
    ResourceNotFoundError
)

def initialize_storage_account(storage_account_name, storage_account_key):    #storage account
    try:
        # global input_service_client

        service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
            "https", storage_account_name), credential=storage_account_key)

    except Exception as e:
        print(e)

    return service_client

# def initialize_output_storage_account(storage_account_name, storage_account_key):
#     try:
#         global output_service_client
#
#         output_service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
#             "https", storage_account_name), credential=storage_account_key)
#
#     except Exception as e:
#         print(e)

def create_file_system(fname,service_client):                   #container
    try:
    #     global file_system_client
        file_system_list = service_client.list_file_systems()

        file_system_client = service_client.create_file_system(file_system=fname)

    except ResourceExistsError:
        file_system_client = service_client.get_file_client(file_system=fname)

    except Exception as e:

        print(e)
    return file_system_client


def create_directory(dirname,file_system_client):
    try:
        file_system_client.create_directory(dirname)

    except Exception as e:
        print(e)


def upload_file_to_directory(service_client,):
    try:

        file_system_client = input_service_client.get_file_system_client(file_system="my-file-system")

        directory_client = file_system_client.get_directory_client("my-directory")

        file_client = directory_client.create_file("uploaded-file.txt")
        local_file = open("C:\\file-to-upload.txt", 'r')

        file_contents = local_file.read()

        file_client.append_data(data=file_contents, offset=0, length=len(file_contents))

        file_client.flush_data(len(file_contents))

    except Exception as e:
        print(e)
