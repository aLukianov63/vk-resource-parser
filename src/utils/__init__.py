import uuid
from datetime import datetime

import requests
from rich.progress import track

from src.utils.resource_type import ResourceType


def resource_download(resources: list[str], path: str, r_type: ResourceType) -> None:
    for resource in track(resources, "[red]Download resources..."):
        data = requests.get(resource)
        with open(f"{path}/{uuid.uuid4()}{r_type.value}", 'wb') as file:
            file.write(data.content)


def save_messages_to_file(resources: list[dict], path: str) -> None:
    with open(f"{path}/{uuid.uuid4()}.txt", 'w') as file:
        for resource in track(resources, "[red]Write to file..."):
            file.write(f"{datetime.utcfromtimestamp(resource['date']).strftime('%Y-%m-%d %H:%M:%S')}"
                       f" {resource['from']}"
                       f" {resource['text']}\n")
