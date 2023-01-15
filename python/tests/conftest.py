from zope import component
from zope import interface

import pytest

from jewellery_storage.interfaces import IJewelleryStorage, ITravelRoll
from jewellery_storage.storage import JewelleryStorage, TravelRoll
from jewellery_storage.packer import bootstrap
from zope.component.hooks import site
from zope.interface.registry import Components


@pytest.fixture(name="bootstrap", scope="session")
def bootstrap_fixture():
    bootstrap()


@pytest.fixture(name="jewellery_storage")
def jewellery_storage_fixture(bootstrap):
    jewellery_storage = component.getUtility(IJewelleryStorage)
    jewellery_storage.__dict__ = JewelleryStorage().__dict__  # A hacky smart hack! I'm too lazy to clear component registry every time.
    return jewellery_storage

@pytest.fixture(name="travel_roll")
def travel_roll_fixture(bootstrap):
    travel_roll = component.getUtility(ITravelRoll)
    travel_roll.__dict__ = TravelRoll().__dict__  # A hacky smart hack! I'm too lazy to clear component registry every time.
    return travel_roll
