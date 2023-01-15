import pathlib
from dataclasses import asdict
import pytest
import yaml
from testfixtures import compare
from jewellery_storage.packer import pack
from jewellery_storage import storage

_HERE = pathlib.Path(__file__).parent


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



def get_annotations(cls: type):
    all_ann = [c.__annotations__ for c in cls.mro()[:-1]]
    all_ann_dict = dict()
    for aa in all_ann[::-1]:
        all_ann_dict.update(**aa)
    return all_ann_dict


def deserialize(value, jewellery_storage, travel_roll):

    factory_class = getattr(storage, value["jewellery_type"])
    kwargs = {
        k: getattr(get_annotations(factory_class)[k], v.title()) if isinstance(v, str) else deserialize(v, jewellery_storage, travel_roll)
        for k,v in value["jewellery_params"].items()
    }
    item = factory_class(**kwargs)
    if value.get("in_travel_roll"):
        travel_roll.items.append(item)
    return item


@pytest.mark.ddt(_HERE.glob("data/*.yaml"))
def test_pack(jewellery_storage, travel_roll, condition, expectation):
    item = deserialize(condition, jewellery_storage, travel_roll)
    pack(item)
    compare(expectation, asdict(jewellery_storage))
