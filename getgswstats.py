import requests
import csv

gswshootingurl = 'http://stats.nba.com/stats/teamdashboardbyshootingsplits?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlusMinus=N&Rank=N&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&TeamID=1610612744&VsConference=&VsDivision='
requestheaders = {
	
	'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
	'From': 'rodellrodriguez53@gmail.com'
}
response = requests.get(gswshootingurl, headers=requestheaders)
response.raise_for_status()

gsw_overall_stats_headers =  response.json()['resultSets'][0]['headers']
gsw_5ft_stats_headers = response.json()['resultSets'][1]['headers']
gsw_8ft_stats_headers = response.json()['resultSets'][2]['headers']
gsw_shot_area_stats_headers = response.json()['resultSets'][3]['headers']
gsw_assisted_shot_stats_headers = response.json()['resultSets'][4]['headers']
gsw_shot_type_stats_headers = response.json()['resultSets'][5]['headers']
gsw_assisted_by_stats_headers = response.json()['resultSets'][6]['headers']

gsw_overall_stats =  response.json()['resultSets'][0]['rowSet']
gsw_5ft_stats = response.json()['resultSets'][1]['rowSet']
gsw_8ft_stats = response.json()['resultSets'][2]['rowSet']
gsw_shot_area_stats = response.json()['resultSets'][3]['rowSet']
gsw_assisted_shot_stats = response.json()['resultSets'][4]['rowSet']
gsw_shot_type_stats = response.json()['resultSets'][5]['rowSet']
gsw_assisted_by_stats = response.json()['resultSets'][6]['rowSet']

directory = 'Stats/'
with open(directory+ 'gsw_overall_stats.csv', 'w',newline='') as csv_out:
    writer = csv.writer(csv_out)
    writer.writerow(gsw_overall_stats_headers)
    writer.writerows(gsw_overall_stats)

with open(directory+ 'gsw_5ft_stats.csv', 'w',newline='') as csv_out:
    writer = csv.writer(csv_out)
    writer.writerow(gsw_5ft_stats_headers)
    writer.writerows(gsw_5ft_stats)

with open(directory+ 'gsw_8ft_stats.csv', 'w',newline='') as csv_out:
    writer = csv.writer(csv_out)
    writer.writerow(gsw_8ft_stats_headers)
    writer.writerows(gsw_8ft_stats)

with open(directory+ 'gsw_shot_area_stats.csv', 'w',newline='') as csv_out:
    writer = csv.writer(csv_out)
    writer.writerow(gsw_shot_area_stats_headers)
    writer.writerows(gsw_shot_area_stats)

with open(directory+ 'gsw_assisted_shot_stats.csv', 'w',newline='') as csv_out:
    writer = csv.writer(csv_out)
    writer.writerow(gsw_assisted_shot_stats_headers)
    writer.writerows(gsw_assisted_shot_stats)

with open(directory+ 'gsw_shot_type_stats.csv', 'w',newline='') as csv_out:
    writer = csv.writer(csv_out)
    writer.writerow(gsw_shot_type_stats_headers)
    writer.writerows(gsw_shot_type_stats)

with open(directory+ 'gsw_assisted_by_stats.csv', 'w',newline='') as csv_out:
    writer = csv.writer(csv_out)
    writer.writerow(gsw_assisted_by_stats_headers)
    writer.writerows(gsw_assisted_by_stats)
