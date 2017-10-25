import requests
import csv

URL = 'http://stats.nba.com/stats/teamdashboardbyshootingsplits?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlusMinus=N&Rank=N&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&TeamID=1610612744&VsConference=&VsDivision='
REQUEST_HEADERS = {
	'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
	'From': 'rodellrodriguez53@gmail.com'
}
response = requests.get(URL, headers=REQUEST_HEADERS)
response.raise_for_status()

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