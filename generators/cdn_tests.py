import logging
import os

from caseconverter import snakecase  # type: ignore

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

for file in files:
    if (
        not os.path.isdir(os.path.join(path, file))
        and not file.startswith("tft")
        and file != ".DS_Store"
    ):
        file = snakecase(file.replace(".json", "").replace("-", ""))  # type: ignore

        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, f"../tests/unit/ddragon/test_{file}.py")

        with open(path, "w") as f:
            content = f"""from pyke import DataDragon

from .base import ddragon


def test_get_all(ddragon: DataDragon):
    get_all = ddragon.{file}.get_all("en_GB")

    assert isinstance(get_all, dict)
"""
            f.write(content)
