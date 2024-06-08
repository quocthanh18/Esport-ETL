from mwrogue.esports_client import EsportsClient
from mwrogue.wiki_client import WikiClient
from src.data_extractor import DataExtractor
import pandas as pd

class DataEnricher:
    def __init__(self, data: DataExtractor):
        lol = EsportsClient("lol")
        self.leaguepedia_players = self.leaguepedia_players_extractor()
        self.enrich_player = self.enrich_player_transformer(data, self.leaguepedia_players)

    def leaguepedia_player(self):
        players_field = "ID, OverviewPage, Player, Image, Name, NativeName, NameAlphabet, NameFull, Country, Nationality, NationalityPrimary, Age, Birthdate, ResidencyFormer, Team, Team2, CurrentTeams, TeamSystem, Team2System, Residency, Role, FavChamps, SoloqueueIds, Askfm, Discord, Facebook, Instagram, Lolpros, Reddit, Snapchat, Stream, Twitter, Vk, Website, Weibo, Youtube, TeamLast, RoleLast, IsRetired, ToWildrift, IsPersonality, IsSubstitute, IsTrainee, IsLowercase, IsAutoTeam, IsLowContent"
        player = self.lol.cargo_client.query(tables="Players",
                                            fields = players_field,
                                            limit="max"
                                            )
        return player
    
    def enrich_player_transformer(self, data: DataExtractor, leaguepedia_players: pd.DataFrame):
        players_info = {}
        for player in leaguepedia_players:
            if player.get("ID") in data.players_names:
                players_info[player["ID"]] = player
        return players_info

    

