import requests

from pydantic.fields import Field
from pydantic import BaseModel

from aoe2_api import Regions, MatchTypes

API_URL = "https://api.ageofempires.com/api/v2/Ageii/Leaderboard"

class LeaderboardRecord(BaseModel):
    game_id: str = Field(alias='gameId')
    user_id: str = Field(alias='userId', default=None)
    rl_user_id: int = Field(alias='rlUserId', default=None)
    username: str = Field(alias='userName')
    avatar_url: str = Field(alias='avatarUrl', default=None)
    player_number: int = Field(alias='playerNumber', default=None)
    elo: int = Field(alias='elo')
    elo_rating: int = Field(alias='eloRating')
    elo_highest: int = Field(alias='eloHighest')
    rank: int = Field(alias='rank')
    region: Regions = Field(alias='region')
    wins: int = Field(alias='wins')
    win_percent: float = Field(alias='winPercent')
    losses: int = Field(alias='losses')
    win_streak: int = Field(alias='winStreak')
    rank_level: int = Field(alias='rankLevel', default=None)
    rank_icon: str = Field(alias='rankIcon', default=None)
    leaderboard_key: str = Field(alias='leaderboardKey', default=None)

    def __str__(self):
        return f'LeaderboardRecord - Username: {self.username}, Rank: {self.rank}, ELO: {self.elo}'

    def __repr__(self):
        return str(self)

class LeaderboardStats():
    @staticmethod
    def search_leaderboard(region: Regions = Regions.GLOBAL, match_type: MatchTypes = MatchTypes.RM, player_name: str = "", page: int = 1) -> list[LeaderboardRecord]:
        """Searches the AoE2: DE leaderboards, returning a list of user data

        :param region: Region to search over, defaults to Regions.GLOBAL
        :type region: Regions, optional
        :param match_type: Type of match to search over, defaults to MatchTypes.RM
        :type match_type: MatchTypes, optional
        :param player_name: Player name to search for, defaults to ""
        :type player_name: str, optional
        :param page: Page of the leadboards to check - 100 entries per page, defaults to 1
        :type page: int, optional
        :return: List of LeaderboardRecords containing all relevant information
        :rtype: list[LeaderboardRecord]
        """
        json_data = {
            'region': region.value,
            'matchType': match_type.value,
            'searchPlayer': player_name,
            'page': page,
        }

        print(json_data)

        req = requests.post(API_URL, json = json_data)
        print(req.content)

        try:
            return [LeaderboardRecord(**data) for data in req.json()['items']]
        except requests.exceptions.JSONDecodeError:
            return list()