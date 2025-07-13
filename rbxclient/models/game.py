from dataclasses import dataclass


@dataclass
class Game:
    universe_id: int
    place_id: int
    name: str
    player_count: int
    total_up_votes: int
    total_down_votes: int
    is_sponsored: bool


@dataclass
class GameDiscoverTopic:
    sort_id: str
    sort_display_name: str
    applied_filter_detail: str
    games: list[Game]
