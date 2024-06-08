import datetime
import pandas as pd

url = "https://drive.google.com/uc?export=download&id="

years = {
    2014: "12syQsRH2QnKrQZTQQ6G5zyVeTG2pAYvu",
    2015: "1qyckLuw0-hJM8XqFhlV9l1xAbr3H78T_",
    2016: "1muyfpaIqk8_0BFkgLCWXDGNgWSXoPBwG",
    2017: "11fx3nNjSYB0X8vKxLAbYOrS2Bu6avm9A",
    2018: "1GsNetJQOMx0QJ6_FN8M1kwGvU_GPPcPZ",
    2019: "11eKtScnZcpfZcD3w3UrD7nnpfLHvj9_t",
    2020: "1dlSIczXShnv1vIfGNvBjgk-thMKA5j7d",
    2021: "1fzwTTz77hcnYjOnO9ONeoPrkWCoOSecA",
    2022: "1EHmptHyzY8owv0BAcNKtkQpMwfkURwRy",
    2023: "1XXk2LO0CsNADBB1LRGOV5rUpyZdEZ8s2",
    2024: "1IjIEhLc9n8eLKeY-yh_YigKVWbhgGBsN"
}
def year_to_url(year: int):
    return url + years.get(year)
def csv_extractor(years: list):
    df = pd.DataFrame()
    for year in years:
        current_year = pd.read_csv(year_to_url(year), dtype={"url": str})
        df = pd.concat([df, current_year], ignore_index=True)
    return df
    
class DataExtractor:
    def __init__(self, years: list):
        self.main_df = csv_extractor(years)
        self.players_names = self.get_players_names()
        self.teams_names = self.get_teams_names()

    def get_players_names(self):
        return list(self.main_df["playername"].dropna().unique())
    
    def get_teams_names(self):
        return list(self.main_df["teamname"].dropna().unique())