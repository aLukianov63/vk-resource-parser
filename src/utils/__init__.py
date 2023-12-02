import uuid

import requests
from rich.progress import track

from src.utils.resource_type import ResourceType


def resource_download(resources: list[str], path: str, r_type: ResourceType) -> None:
    for resource in track(resources, "[red]Download resources..."):
        data = requests.get(resource)
        with open(f"{path}/{uuid.uuid4()}{r_type.value}", 'wb') as file:
            file.write(data.content)
