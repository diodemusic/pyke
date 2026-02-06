import logging
import os

from caseconverter import camelcase, snakecase, titlecase  # type: ignore

from pyke import DataDragon

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)

ddragon = DataDragon()
version = ddragon._client.version
dirname = os.path.dirname(__file__)
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
        file = snakecase(file.replace(".json", "").replace("-", ""))  # type: ignore

        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, f"../src/pyke/ddragon/{file}.py")

        with open(path, "w") as f:
            class_name = f"{titlecase(file).replace(' ', '')}Data"
            content = f'''from typing import Any

from .._base_data_dragon_client import _BaseDataDragonClient


class {class_name}:
    def __init__(self, client: _BaseDataDragonClient):
        self._client = client

    def get_all(self, locale: str) -> dict[str, Any]:
        """# Get all {file} by locale

        **Example:**
            `{file} = ddragon.{file}.get_all("en_GB")`

        **Args:**
            `locale (str)` Locale to use.

        **Returns:**
            `dict[str, any]`
        """  # fmt: skip

        return self._client._data_dragon_cdn_request(locale, "{camelcase(file)}")
'''
            f.write(content)

        objects.append(f"self.{file} = {class_name}(self._client)")
        imports.append(f"from .ddragon.{file} import {class_name}")

for object_str in objects:
    print(object_str)

print("-" * 20)

for import_str in imports:
    print(import_str)
