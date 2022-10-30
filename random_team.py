import sys
import random
from team_map import TEAM_MAP


def _get_random_team(num_teams):
    random_league_index = random.randrange(1, len(TEAM_MAP))
    league_name = list(TEAM_MAP)[random_league_index]
    league = list(TEAM_MAP.values())[random_league_index]
    print(f"League: {league_name}")
    for num in range(1, num_teams + 1):
        team = league[random.randrange(1, len(league))]
        print(f"Team {num}: {team}")


def get_randoms(same_league):
    if same_league:
        _get_random_team(2)
        sys.exit()
    for x in range(2):
        _get_random_team(1)


user_input = None
while user_input not in ["1", "0"]:
    user_input = (
        input("Do you want to use the same league? [Yes or No] ")
        .lower()
        .replace("yes", "1")
        .replace("no", "0")
    )

get_randoms(int(user_input))
