from dataclasses import dataclass
from enum import Enum


class UserPresenceStatus(Enum):
    OFFLINE = 0
    ONLINE = 1
    IN_GAME = 2
    IN_STUDIO = 3
    INVISIBLE = 4


@dataclass
class UserPresenceGame:
    id: str
    place_id: int
    root_place_id: int


@dataclass
class UserPresence:
    status: UserPresenceStatus
    name: str  # lastLocation
    game: UserPresenceGame | None


@dataclass
class FriendUser:
    """
    Represents a friend user in Roblox.
    """

    id: int
    name: str
    display_name: str
    presence: UserPresence | None
