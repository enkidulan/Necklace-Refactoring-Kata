import pytest
from jewellery_storage.storage import JewelleryStorage

@pytest.fixture
def jewellery_storage():
    return JewelleryStorage()
