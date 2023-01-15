from zope import component, interface

from jewellery_storage.storage import (
    Earring,
    EarringType,
    Jewel,
    Jewellery,
    JewelleryStorage,
    TravelRoll,
    Necklace,
    NecklaceType,
    Ring,
    PendantNecklace,
)

from .interfaces import IJewelleryStorage, ITravelRoll


def travel_roll_handler(item):
    storage = component.getUtility(IJewelleryStorage)
    if not item.is_heavy():
        storage.box.top_shelf.append(item)
    else:
        storage.dresser_top.append(item)


def diamond_handler(item):
    pass


@component.adapter(PendantNecklace)
def pendant_necklace_handler(item):
    component.handle(item.chain)
    component.handle(item.pendant)


@component.adapter(Necklace)
def necklace_handler(item):
    storage = component.getUtility(IJewelleryStorage)
    if item.stone == Jewel.Diamond:
        storage.safe.append(item)
    elif not(item.type is NecklaceType.Beads or item.type is NecklaceType.LongChain):
        storage.box.top_shelf.append(item)
    else:
        storage.tree.append(item)


@component.adapter(Earring)
def earring_handler(item):
    storage = component.getUtility(IJewelleryStorage)
    if item.stone == Jewel.Diamond:
        storage.safe.append(item)
    elif item.type == EarringType.Hoop:
        storage.tree.append(item)
    elif item.type == EarringType.Drop and item.stone is not Jewel.Plain:
        storage.box.top_shelf.append(item)
    elif item.type == EarringType.Drop:
        storage.box.main_section.append(item)
    else:
        storage.box.top_shelf.append(item)


@component.adapter(Ring)
def ring_handler(item):
    storage = component.getUtility(IJewelleryStorage)
    if item.stone == Jewel.Diamond:
        storage.safe.append(item)
    else:
        storage.dresser_top.append(item)


def pack(item: Jewellery):
    # storage = component.getUtility(ITravelRoll)
    # if storage.is_in_travel_roll(item):  # XXX:
    #     travel_roll_handler(item)
    # else:
    component.handle(item)


def bootstrap():
    component.provideUtility(JewelleryStorage(), IJewelleryStorage)
    component.provideUtility(TravelRoll(), ITravelRoll)
    component.provideHandler(ring_handler)
    component.provideHandler(earring_handler)
    component.provideHandler(necklace_handler)
    component.provideHandler(pendant_necklace_handler)
