from dataclasses import dataclass as base_dataclass, field
from enum import StrEnum, auto

def dataclass(cls):
    new_cls = base_dataclass(cls)
    new_cls.name = cls.__name__.lower()
    return new_cls

class Jewel(StrEnum):
    Plain = auto()
    Diamond = auto()
    Pearl = auto()
    Amber = auto()


class EarringType(StrEnum):
    Stud = auto()
    Hoop = auto()
    Drop = auto()


class NecklaceType(StrEnum):
    Beads = auto()
    Chain = auto()
    Pendant = auto()
    LongChain = auto()


@dataclass
class Jewellery:
    stone: Jewel
    name: str = field(init=False, default=None)


@dataclass
class Ring(Jewellery):
    pass


@dataclass
class Earring(Jewellery):
    type: EarringType

@dataclass
class Necklace(Jewellery):
    type: NecklaceType


@dataclass
class PendantNecklace(Jewellery):
    chain: Necklace
    pendant: Jewellery
    type = NecklaceType.Pendant

    def __init__(self, chain: Necklace, pendant: Jewellery):
        Jewellery.__init__(self, pendant.stone) # XXX
        self.chain = chain
        self.pendant = pendant

@dataclass
class Pendant(Jewellery):
    pass


@dataclass
class JewelleryBox:
    ring_compartment: list = field(default_factory=list)
    top_shelf: list = field(default_factory=list)
    main_section: list = field(default_factory=list)


@dataclass
class JewelleryStorage:
    tree: list = field(default_factory=list)
    safe: list = field(default_factory=list)
    dresser_top: list = field(default_factory=list)
    box: JewelleryBox = field(default_factory=JewelleryBox)


@dataclass
class TravelRoll:
    items: list = field(default_factory=list)
