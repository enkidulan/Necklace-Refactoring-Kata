import pytest

from jewellery_storage.storage import *
from jewellery_storage.packer import pack
from dataclasses import asdict



def test_pack_earring_stud(jewellery_storage):
    item = Earring(type=EarringType.Stud, stone=Jewel.Amber)
    pack(item, jewellery_storage)
    print(asdict(jewellery_storage))
    import pdb; pdb.set_trace()
    # TODO: check it packed it correctly


def test_pack_diamond_pendant_necklace(jewellery_storage):
    item = PendantNecklace(chain=Necklace(Jewel.Plain, NecklaceType.Chain), pendant=Pendant(Jewel.Diamond))
    pack(item, jewellery_storage)
    # TODO: new feature - only the pendant should be in the safe, not the chain
