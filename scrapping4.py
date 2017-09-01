"""
------------------------------------------------FIRST PYTHON WEB SCRAPER------------------------------------------------
I am taking data from the statistical leaders of the 2015-2016 NBA season from basketball-reference and inputting them 
into a Python dictionary. The structure of the data is as follows:

LIST 
	TUPLE[0]: Name of Statistic 
	TUPLE[1]: LIST
			   0. LIST ([0]- Name of Player, [1]- Value) #1 Player
			   |
			   |
			   9. LIST ([0]- Name of Player, [1]- Value) #10 Player
"""
import urllib.request as url
import pprint
import operator
from bs4 import BeautifulSoup
import numpy as np

"""
Libraries used:
urllib.request - accessing website data

BeautifulSoup - manipulate the web data

PPrint - Printing dictionaries/lists in a nice format
"""
"""
wiki2 = "http://bkref.com/pi/shareit/CVdvk"  #Accessing web page and converting to BS
page2 = url.urlopen(wiki2)
soup2 = BeautifulSoup(page2, "lxml")
# print(type(soup2))								#Check that BS is working (converting to correct object type)
col = soup2.find("table").find("tbody").find_all('tr')


each_row = [element for element in col]

teams = []
for i in range(len(each_row)-1):
	links = col[i].find_all("a")
	teams.append([links[0]['href'], links[1]['href']])
	# print(type(links[1]['href']))
	# print(teams)
	# print(links[0]['href'])
	# print(links[1]['href'])


# teams is now the 2d array of all the links of each series, winner is item 0, loser is item 1
stats = []
for i in range(len(teams)-1):
	win = BeautifulSoup(url.urlopen(teams[i][0]), "lxml")
	lose = BeautifulSoup(url.urlopen(teams[i][1]), "lxml")
	win_pts = float(win.find_all("p")[5].get_text()[15:20])
	win_opp_pts = float(win.find_all("p")[5].get_text()[57:62])
	win_offrtg = float(win.find_all("p")[7].get_text()[10:15])
	win_defrtg = float(win.find_all("p")[7].get_text()[43:48])
	
	lose_pts = float(lose.find_all("p")[5].get_text()[15:20])
	lose_opp_pts = float(lose.find_all("p")[5].get_text()[57:62])
	lose_offrtg = float(lose.find_all("p")[7].get_text()[10:15])
	lose_defrtg = float(lose.find_all("p")[7].get_text()[43:48])

	series_stats = [win_pts, win_opp_pts, win_offrtg, win_defrtg, lose_pts, lose_opp_pts, lose_offrtg, lose_defrtg]
	stats.append(series_stats)

print(stats[0][0])
"""
wiki1 = "http://bkref.com/pi/shareit/klTxd"
page1 = url.urlopen(wiki1)
soup1 = BeautifulSoup(page1, "lxml")

col1 = soup1.find("table").find("tbody").find_all('td')
each_row1 = [element for element in col1]
print(len(each_row1))

teams = []
i = 0
while i<len(each_row1):
	links = col1[i].find("a")
	teams.append([col1[i].find("a")['href'], col1[i+1].find("a")['href']])
	# print(teams)
	i+=2

# win = BeautifulSoup(url.urlopen(teams[0][0]), "lxml")
# lose = BeautifulSoup(url.urlopen(teams[0][1]), "lxml")
# win_pts = float(win.find_all("p")[4].get_text()[15:20])
# win_opp_pts = float(win.find_all("p")[4].get_text()[57:62])
# win_offrtg = float(win.find_all("p")[6].get_text()[10:15])
# win_defrtg = float(win.find_all("p")[6].get_text()[43:48]) 

# lose_pts = float(lose.find_all("p")[4].get_text()[15:20])
# lose_opp_pts = float(lose.find_all("p")[4].get_text()[57:62])
# lose_offrtg = float(lose.find_all("p")[6].get_text()[10:15])
# lose_defrtg = float(lose.find_all("p")[6].get_text()[43:48])

# series_stats = [win_pts, win_opp_pts, win_offrtg, win_defrtg, lose_pts, lose_opp_pts, lose_offrtg, lose_defrtg]
# print(series_stats)
print(len(teams))
stats = []
for i in range(len(teams)-1):
	win = BeautifulSoup(url.urlopen(teams[i][0]), "lxml")
	lose = BeautifulSoup(url.urlopen(teams[i][1]), "lxml")
	win_pts = float(win.find_all("p")[4].get_text()[15:20])
	win_opp_pts = float(win.find_all("p")[4].get_text()[57:62])
	win_offrtg = float(win.find_all("p")[6].get_text()[10:15])
	win_defrtg = float(win.find_all("p")[6].get_text()[43:48])
	
	lose_pts = float(lose.find_all("p")[4].get_text()[15:20])
	lose_opp_pts = float(lose.find_all("p")[4].get_text()[57:62])
	lose_offrtg = float(lose.find_all("p")[6].get_text()[10:15])
	lose_defrtg = float(lose.find_all("p")[6].get_text()[43:48])

	series_stats = [win_pts, win_opp_pts, win_offrtg, win_defrtg, lose_pts, lose_opp_pts, lose_offrtg, lose_defrtg]
	stats.append(series_stats)
	print(series_stats)
print("Number of series", len(stats))
print("Should be 8: ", len(stats[0]))
print("First one", stats[0][0])



# print(type(col))			#Create list of Stat Columns

# each_col = [element for element in col]			#Creating lists for length purposes

# leaders = []									#Creating empty list
# for j in range(len(each_col)):

# 	cat_leaders = []							#Resetting each Top 10 list for every new Stat
# 	rows = col[j].find_all("tr")				#Creating list of each player in the Top 10
# 	name = col[j].find_all("caption")[0].get_text()	#Finding the name of each stat (KEY OF EACH DICTIONARY)

# 	minutes = [element for element in rows]
# 	for i in range(len(minutes)//2):
# 		cat_leaders.append([rows[i].find_all(class_="who")[0].find_all("a")[0].get_text(), rows[i].find_all(class_="value")[0].get_text()])
# 		#Append list of (name, value) for each player 
# 	leaders.append((name, cat_leaders))  				#Create tuple for list entry
# pprint.pprint(leaders)							#Print dictionary

# appearances = {}
# for i in range(len(leaders)):
# 	lst = leaders[i][1]
# 	for j in range(len(lst)):
# 		if(lst[j][0] in appearances):
# 			appearances[lst[j][0]] += 1
# 		else:
# 			appearances[lst[j][0]] = 1
# pprint.pprint(appearances)
# sorted_x = sorted(appearances.items(), key=operator.itemgetter(1))
# pprint.pprint(sorted_x)



