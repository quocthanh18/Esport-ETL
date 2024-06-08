from mwrogue.esports_client import EsportsClient
import pandas as pd
site = EsportsClient("lol")
TEAM_FIELDS = "Name, OverviewPage, Short, Location, TeamLocation, Region, OrganizationPage, Image, Twitter, Youtube, Facebook, Instagram, Discord, Snapchat, Vk, Subreddit, Website, RosterPhoto, IsDisbanded, RenamedTo, IsLowercase"
teams = site.cargo_client.query(tables="Teams",
                                 fields = TEAM_FIELDS,
                                 limit=20
                                 )
print(teams[0])