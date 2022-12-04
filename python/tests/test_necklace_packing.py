from jewellery_storage.storage import *
from jewellery_storage.packer import pack_necklace

def test_pack_pearl_necklace(jewellery_storage):
    item = Necklace(stone=Jewel.Pearl, type=NecklaceType.Beads)
    pack_necklace(item, jewellery_storage)

    # TODO: check it packed it correctly


def test_pack_diamond_pendant_necklace(jewellery_storage):
    item = PendantNecklace(chain=Necklace(Jewel.Plain, NecklaceType.Chain), pendant=Pendant(Jewel.Diamond))
    pack_necklace(item, jewellery_storage)
    # TODO: new feature - only the pendant should be in the safe, not the chain
