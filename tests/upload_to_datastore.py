import azureml.core
from azureml.core import Workspace, Datastore, Dataset
from azure.storage.blob import ContainerClient
from azure.storage.filedatalake import DataLakeServiceClient

def get_datastore(ws: Workspace, datastore_name='pointclouds_adls') -> Datastore:
    datastore = Datastore.get(ws, datastore_name)
    return datastore

def upload_blob(ds: Datastore, src: str, target_path: str, overwrite: bool = False, show_progress: bool = True):
    ds.upload(src_dir=src, target_path=target_path, overwrite=overwrite,
              show_progress=show_progress)

# print(ws.get_details())

def initialize_storage_account(storage_account_name, storage_account_key):
    try:
        # global service_client

        service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
            "https", storage_account_name), credential=storage_account_key)

    except Exception as e:
        print(e)
    return service_client


