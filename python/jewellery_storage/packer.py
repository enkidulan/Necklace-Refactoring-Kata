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


def inject(service, by_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            provider = component.getUtility(service)
            kwargs[by_name] = provider
            return func(*args, **kwargs)
        return wrapper
    return decorator

# def travel_roll_handler(item):
#     storage = component.getUtility(IJewelleryStorage)
#     if not item.is_heavy():
#         storage.box.top_shelf.append(item)
#     else:
#         storage.dresser_top.append(item)


@inject(IJewelleryStorage, by_name="storage")
def diamond_handler(item, storage):
    storage.safe.append(item)


@component.adapter(PendantNecklace)
def pendant_necklace_handler(item):
    component.handle(item.chain)
    component.handle(item.pendant)


@component.adapter(Necklace)
@inject(IJewelleryStorage, by_name="storage")
def necklace_handler(item, storage):
    if item.type is NecklaceType.Beads or item.type is NecklaceType.LongChain:
        storage.tree.append(item)
    else:
        storage.box.top_shelf.append(item)


@component.adapter(Earring)
@inject(IJewelleryStorage, by_name="storage")
def earring_handler(item, storage):
    if item.type == EarringType.Hoop:
        storage.tree.append(item)
    elif item.type == EarringType.Drop:
        if item.stone is not Jewel.Plain:
            storage.box.top_shelf.append(item)
        else:
            storage.box.main_section.append(item)
    else:
        storage.box.top_shelf.append(item)


@component.adapter(Ring)
@inject(IJewelleryStorage, by_name="storage")
def ring_handler(item, storage):
    storage.dresser_top.append(item)


def pack(item: Jewellery):
    # if storage.is_in_travel_roll(item):  # XXX:
    #     travel_roll_handler(item)
    # else:
    if item.stone == Jewel.Diamond:
        diamond_handler(item)
    else:
        component.handle(item)


def bootstrap():
    component.provideUtility(JewelleryStorage(), IJewelleryStorage)
    component.provideUtility(TravelRoll(), ITravelRoll)
    component.provideHandler(ring_handler)
    component.provideHandler(earring_handler)
    component.provideHandler(necklace_handler)
    component.provideHandler(pendant_necklace_handler)
