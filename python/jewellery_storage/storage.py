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

    # @property
    # def jewellery(self):
    #     return field(init=False, default_factory=lambda: self.__class__.__name__)

    def is_ring(self):
        return False

    def is_small(self):
        return False

    def is_earring(self):
        return False

    def is_necklace(self):
        return False

    def is_heavy(self):
        return False


@dataclass
class Ring(Jewellery):
    def is_ring(self):
        return True


@dataclass
class Earring(Jewellery):
    type: EarringType

    def is_small(self):
        return self.type is EarringType.Stud

    def is_earring(self):
        return True


@dataclass
class Necklace(Jewellery):
    type: NecklaceType

    def is_necklace(self):
        return True

    def is_heavy(self):
        return self.type is NecklaceType.Beads or self.type is NecklaceType.LongChain


@dataclass
class PendantNecklace(Jewellery):
    chain: Necklace
    pendant: Jewellery

    def __init__(self, chain: Necklace, pendant: Jewellery):
        Jewellery.__init__(self, pendant.stone)
        self.chain = chain
        self.pendant = pendant
        self.type = NecklaceType.Pendant

    def is_heavy(self):
        return self.chain.is_heavy() or self.pendant.is_heavy()

    def is_necklace(self):
        return True


@dataclass
class Pendant(Jewellery):
    def is_small(self):
        return True


@dataclass
class JewelleryBox:
    ring_compartment: list = field(default_factory=list)
    top_shelf: list = field(default_factory=list)
    main_section: list = field(default_factory=list)


@dataclass
class JewelleryStorage:
    tree: list = field(default_factory=list)
    travel_roll: list = field(default_factory=list)
    safe: list = field(default_factory=list)
    dresser_top: list = field(default_factory=list)
    box: JewelleryBox = field(default_factory=JewelleryBox)

    def is_in_travel_roll(self, item):
        return item in self.travel_roll
