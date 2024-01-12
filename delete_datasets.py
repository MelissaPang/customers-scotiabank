import tamr_toolbox as tbox
from tamr_unify_client import Client
import json
import time


def truncate_a_dataset_by_name(*, client: Client, dataset_name: str):
    if tbox.dataset.manage.exists(client=client, dataset_name=dataset_name):
        api_path = "/api/dataset/datasets/" + dataset_name + "/truncate"
        response = client.post(api_path)
        response_dict = json.loads(response.content)
        if not response.ok:
            error_message = f'Truncate failed: {response_dict["message"]}'
            raise Exception(error_message)
        else:
            message = f"{dataset_name} is successfully truncated."
    else:
        message = f"{dataset_name} doesn't exist."
    return print(message)


if '__main__':
    config_address = "/Users/melissapanggwugmail.com/Desktop/bigquery/config_delete_dataset"  # Please change the location of the config file here
    CONFIG = tbox.utils.config.from_yaml(config_address)
    tamr = tbox.utils.client.create(**CONFIG["tamr_instance"])
    for dataset_name in CONFIG["truncate_datasets_names"]:
        truncate_a_dataset_by_name(client=tamr, dataset_name=dataset_name)
        time.sleep(5)
