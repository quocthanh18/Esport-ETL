from mwrogue.esports_client import EsportsClient

from src.data_extractor import DataExtractor
import pandas as pd
import requests

def 
class DataEnricher:
    def __init__(self, data: DataExtractor):
        lol = EsportsClient("lol")
        
        #Players
        self.leaguepedia_players = self.leaguepedia_players_extractor()
        self.additional_player_info = self.enrich_player_transformer(data, self.leaguepedia_players)

        #Teams
        self.leaguepedia_teams = self.leaguepedia_teams_extractor()
        self.additonal_team_info = self.enrich_team_transformer(data, self.leaguepedia_teams)

        #Geology
        self.countries = self.get_player_countries(self.additional_player_info)
        self.coords = self.get_country_coordinates(self.countries)
    def leaguepedia_players_extractor(self):
        players_field = "ID, OverviewPage, Player, Image, Name, NativeName, NameAlphabet, NameFull, Country, Nationality, NationalityPrimary, Age, Birthdate, ResidencyFormer, Team, Team2, CurrentTeams, TeamSystem, Team2System, Residency, Role, FavChamps, SoloqueueIds, Askfm, Discord, Facebook, Instagram, Lolpros, Reddit, Snapchat, Stream, Twitter, Vk, Website, Weibo, Youtube, TeamLast, RoleLast, IsRetired, ToWildrift, IsPersonality, IsSubstitute, IsTrainee, IsLowercase, IsAutoTeam, IsLowContent"
        player = self.lol.cargo_client.query(tables="Players",
                                            fields = players_field,
                                            limit="max"
                                            )
        return player
    
    def enrich_player_transformer(self, data: DataExtractor, leaguepedia_players: list):
        players_info = {}
        for player in leaguepedia_players:
            if player.get("ID") in data.players_names:
                players_info[player["ID"]] = player
        return players_info
    
    def leaguepedia_teams_extractor(self):
        teams_field =  "Name, OverviewPage, Short, Location, TeamLocation, Region, OrganizationPage, Image, Twitter, Youtube, Facebook, Instagram, Discord, Snapchat, Vk, Subreddit, Website, RosterPhoto, IsDisbanded, RenamedTo, IsLowercase"
        teams = self.lol.cargo_client.query(tables="Teams",
                                            fields = teams_field,
                                            limit="max"
                                            )
        return teams
    
    def enrich_team_transformer(self, data: DataExtractor, leaguepedia_teams: list):
        teams_info = {}
        for team in leaguepedia_teams:
            if team.get("OverviewPage ") in data.teams_names:
                teams_info[team["OverviewPage"]] = team
        return teams_info
    
    def get_player_countries(self, players_info: dict):
        countries = {"United States": "USA", "China": "CN"}
        return list(set([ countries.get(info.get("Country"), info.get("Country")) for info in players_info.values()]))
    
    def get_country_coordinates(self, countries: list):
        coords = {}
        for country in countries:
            url = "https://restcountries.com/v3.1/name/"
            request = url + country
            response = requests.get(request)
            response = response.json()
            coords[country] = response[0]["latlng"]
        return coords
    
    def append_players_info(self, data: DataExtractor, addtional_players_info: dict):
        data["Player_info"] = data["playername"].map(addtional_players_info)

    def append_team_info(self, data: DataExtractor, additonal_teams_info: dict):
        data["Team_info"] = data["teamname"].map(additonal_teams_info)

    



    

