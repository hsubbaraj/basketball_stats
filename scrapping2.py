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

"""
Libraries used:
urllib.request - accessing website data

BeautifulSoup - manipulate the web data

PPrint - Printing dictionaries/lists in a nice format
"""
wiki2 = "http://www.basketball-reference.com/leagues/NBA_2016_leaders.html"  #Accessing web page and converting to BS
page2 = url.urlopen(wiki2)
soup2 = BeautifulSoup(page2, "lxml")
print(type(soup2))								#Check that BS is working (converting to correct object type)
col = soup2.find_all(class_="columns")			#Create list of Stat Columns

each_col = [element for element in col]			#Creating lists for length purposes

leaders = []									#Creating empty list
for j in range(len(each_col)):

	cat_leaders = []							#Resetting each Top 10 list for every new Stat
	rows = col[j].find_all("tr")				#Creating list of each player in the Top 10
	name = col[j].find_all("caption")[0].get_text()	#Finding the name of each stat (KEY OF EACH DICTIONARY)

	minutes = [element for element in rows]
	for i in range(len(minutes)//2):
		cat_leaders.append([rows[i].find_all(class_="who")[0].find_all("a")[0].get_text(), rows[i].find_all(class_="value")[0].get_text()])
		#Append list of (name, value) for each player 
	leaders.append((name, cat_leaders))  				#Create tuple for list entry
pprint.pprint(leaders)							#Print dictionary

appearances = {}
for i in range(len(leaders)):
	lst = leaders[i][1]
	for j in range(len(lst)):
		if(lst[j][0] in appearances):
			appearances[lst[j][0]] += 1
		else:
			appearances[lst[j][0]] = 1
pprint.pprint(appearances)
sorted_x = sorted(appearances.items(), key=operator.itemgetter(1))
pprint.pprint(sorted_x)



