import os

import httpx
from caseconverter import snakecase, titlecase  # type: ignore

dirname = os.path.dirname(__file__)

dragontail_dirs = sorted(d for d in os.listdir(dirname) if d.startswith("dragontail-"))
if not dragontail_dirs:
    raise FileNotFoundError("No dragontail-* directory found in generators/")

version = dragontail_dirs[-1].replace("dragontail-", "")

latest_version = httpx.get(
    "https://ddragon.leagueoflegends.com/api/versions.json"
).json()[0]
if version != latest_version:
    raise RuntimeError(
        f"Local dragontail ({version}) is out of date. Latest is {latest_version}. "
        f"Download it from https://ddragon.leagueoflegends.com/cdn/dragontail-{latest_version}.tgz"
    )
path = os.path.join(dirname, f"./dragontail-{version}/{version}/data/en_GB/")

files = os.listdir(path)

imports: list[str] = []
objects: list[str] = []

for file in files:
    if (
        not os.path.isdir(os.path.join(path, file))
        and not file.startswith("tft")
        and file != ".DS_Store"
    ):
        cdn_key = file.replace(".json", "")
        file = snakecase(cdn_key.replace("-", "_"))

        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, f"../src/pyke/ddragon/{file}.py")

        with open(path, "w") as f:
            class_name = f"{titlecase(file).replace(' ', '')}Data"
            content = f'''from typing import Any

from .._base_data_dragon_client import _BaseDataDragonClient


class {class_name}:
    def __init__(self, client: _BaseDataDragonClient):
        self._client = client

    async def get_all(self, locale: str) -> dict[str, Any]:
        """# Get all {file} by locale

        **Example:**
            `{file} = await ddragon.{file}.get_all("en_GB")`

        **Args:**
            `locale (str)` Locale to use.

        **Returns:**
            `dict[str, Any]`
        """  # fmt: skip

        return await self._client._data_dragon_cdn_request(locale, "{cdn_key}")
'''
            f.write(content)

        objects.append(f"self.{file} = {class_name}(self._client)")
        imports.append(f"from .ddragon.{file} import {class_name}")

for object_str in objects:
    print(object_str)

print("-" * 20)

for import_str in imports:
    print(import_str)
