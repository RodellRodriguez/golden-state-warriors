import requests
import csv
import json
import random
import time
import pandas as pd

#Practicing web scraping etiquette by injecting delays in my requests to not stress NBA's production server
DOWNLOAD_DELAY = 5

years_list = [x for x in range(1996,2018)]
for index,year in enumerate(years_list[:-1]):
    years_list[index] = str(year)+'-'+ str(years_list[index+1])[-2:]
years_list.pop()

years_dict = {}
dataframe_keys = ['overall_df', 'shot_5_ft_df', 'shot_8_ft_df', 'shot_area_df', 'assisted_shot_df', 'shot_type_df', 'assisted_by_df']

for year in years_list:
    time.sleep(random.uniform(0,DOWNLOAD_DELAY))

    URL = 'http://stats.nba.com/stats/teamdashboardbyshootingsplits?' + \
    'DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&' + \
    'Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&' + \
    'PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlusMinus=N&Rank=N&' + \
    'Season=' + year + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&' + \
    'TeamID=1610612744&VsConference=&VsDivision='
    
    REQUEST_HEADERS = {
        'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0',
        'From': 'rodellrodriguez53@gmail.com'
    }
    response = requests.get(URL, headers=REQUEST_HEADERS)
    response.raise_for_status()

    years_dict[year] = {}
    for index,(resultSets_dict,dataframe_name) in enumerate(zip(response.json()['resultSets'], dataframe_keys)):
        if dataframe_name not in years_dict[year]:
            years_dict[year][dataframe_name] =  pd.DataFrame(data=response.json()['resultSets'][index]['rowSet'], 
            columns=response.json()['resultSets'][index]['headers'])    


overall_df, shot_5_ft_df, shot_8_ft_df, shot_area_df, assisted_shot_df, shot_type_df, assisted_by_df = (None,)*7
teams['Golden State Warriors'] = [overall_df, shot_5_ft_df, shot_8_ft_df, shot_area_df, assisted_shot_df, shot_type_df, assisted_by_df]
for index,stat_type in enumerate(teams['Golden State Warriors']):
    teams['Golden State Warriors'][index] = pd.DataFrame(data=response.json()['resultSets'][index]['rowSet'], 
        columns=response.json()['resultSets'][index]['headers'])


"""

stat_headers = ['gsw_overall', 'gsw_5ft','gsw_8ft','gsw_shot_area','gsw_assisted_shot','gsw_shot_type','gsw_assisted_by']
stats = list(stat_headers)
stat_file_names = list(stat_headers)

for index,header_type in enumerate(stat_headers):
	stat_headers[index] = response.json()['resultSets'][index]['headers']

for index,stat_type in enumerate(stats):
	stats[index] = response.json()['resultSets'][index]['rowSet']

for index,file_name in enumerate(stat_file_names):
	stat_file_names[index] = file_name + '_stats.csv'

directory = 'Stats/'
for header,stat,file_name in zip(stat_headers,stats, stat_file_names):
	with open(directory + file_name, 'w', newline = '') as csv_out:
		writer = csv.writer(csv_out)
		writer.writerow(header)
		writer.writerows(stat)        

"""
def main():
    pass


if __name__ = '__main__':
	main()     """