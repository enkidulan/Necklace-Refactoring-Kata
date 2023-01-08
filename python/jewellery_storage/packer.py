from jewellery_storage.storage import Jewellery, JewelleryStorage, Jewel, EarringType, NecklaceType


def pack(item: Jewellery, storage: JewelleryStorage):

    if storage.is_in_travel_roll(item) and not item.is_heavy():  # what does that mean?
        storage.box.top_shelf.append(item)
    elif item.stone == Jewel.Diamond:
        storage.safe.append(item)
    elif item.is_necklace() and item.type == NecklaceType.Pendant:
        storage.tree.append(item.chain)
        storage.box.top_shelf.append(item.pendant)
    elif item.is_small():
        storage.box.top_shelf.append(item)
    elif not item.is_heavy() and item.is_necklace():
        storage.box.top_shelf.append(item)
    elif item.is_earring() and item.type == EarringType.Hoop:
        storage.tree.append(item)
    elif item.is_earring() and item.type == EarringType.Drop and item.stone is not Jewel.Plain:
        storage.box.top_shelf.append(item)
    elif item.is_earring() and item.type == EarringType.Drop:
        storage.box.main_section.append(item)
    elif item.is_necklace():
        storage.tree.append(item)
    else:
        storage.dresser_top.append(item)

    if storage.is_in_travel_roll(item):    # what does that mean? looks like a hack
        storage.travel_roll.remove(item)
