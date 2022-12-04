import pathlib
from dataclasses import asdict

import pytest
import yaml
from testfixtures import compare

from jewellery_storage.packer import pack
from jewellery_storage.storage import *

from jewellery_storage import storage

_HERE = pathlib.Path(__file__).parent

# def test_pack_earring_stud(jewellery_storage):
#     item = Earring(type=EarringType.Stud, stone=Jewel.Amber)
#     pack(item, jewellery_storage)
#     print(asdict(jewellery_storage))
#     # TODO: check it packed it correctly


# def test_pack_diamond_pendant_necklace(jewellery_storage):
#     item = PendantNecklace(
#         chain=Necklace(Jewel.Plain, NecklaceType.Chain), pendant=Pendant(Jewel.Diamond)
#     )
#     pack(item, jewellery_storage)
#     # TODO: new feature - only the pendant should be in the safe, not the chain


def make_params(files):
    params = []
    for file in files:
        data = yaml.safe_load(file.read_text())
        param = pytest.param(
            data["condition"], data["expectation"],
            id=file.name.split(".", 1)[0],
        )
        params.append(param)
    return params


def pytest_generate_tests(metafunc):
    # called once per each test function
    ddt = [i for i in metafunc.function.pytestmark if i.name == "ddt"]
    if not ddt:
        return
    metafunc.parametrize(
        "condition,expectation",
        make_params(ddt[0].args[0]),
    )


@pytest.mark.ddt(_HERE.glob("data/*.yaml"))
def test_jewellery(jewellery_storage, condition, expectation):
    factory_class = getattr(storage, condition["jewellery_type"])
    item = factory_class(**condition["jewellery_params"])
    pack(item, jewellery_storage)
    compare(expectation, asdict(jewellery_storage))
