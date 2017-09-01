

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



class BasketballPlayer:

	#instance variables
	stats = []

	def __init__(self, title, statistics):
		self.name = title
		self.stats = statistics

	def player_print(self):
		print(self.name)
		pprint.pprint(self.stats)

def find_closest(location, centroids):
    """Return the centroid in centroids that is closest to location.
    If multiple centroids are equally close, return the first one.

    >>> find_closest([3.0, 4.0], [[0.0, 0.0], [2.0, 3.0], [4.0, 3.0], [5.0, 5.0]])
    [2.0, 3.0]
    """
    # BEGIN Question 3
    return min([x for x in centroids], key = lambda x:distance(location, x))
    # END Question 3


def group_by_first(pairs):
    """Return a list of pairs that relates each unique key in the [key, value]
    pairs to a list of all values that appear paired with that key.

    Arguments:
    pairs -- a sequence of pairs

    >>> example = [ [1, 2], [3, 2], [2, 4], [1, 3], [3, 1], [1, 2] ]
    >>> group_by_first(example)
    [[2, 3, 2], [2, 1], [4]]
    """
    keys = []
    for key, _ in pairs:
        if key not in keys:
            keys.append(key)
    return [[y for x, y in pairs if x == key] for key in keys]


def group_by_centroid(restaurants, centroids):
    """Return a list of clusters, where each cluster contains all restaurants
    nearest to a corresponding centroid in centroids. Each item in
    restaurants should appear once in the result, along with the other
    restaurants closest to the same centroid.
    """
    # BEGIN Question 4
    closest_list = [[find_closest(restaurant_location(restaurant), centroids), restaurant] for restaurant in restaurants]
    return group_by_first(closest_list)
    # END Question 4


def find_centroid(cluster):
    """Return the centroid of the locations of the restaurants in cluster."""
    # BEGIN Question 5
    lat = mean([restaurant_location(restaurant)[0] for restaurant in cluster])
    lon = mean([restaurant_location(restaurant)[1] for restaurant in cluster])
    return [lat, lon]
    # END Question 5

def distance(pos1, pos2):
	return sum([abs(po)])
def k_means(restaurants, k, max_updates=100):
    """Use k-means to group restaurants by location into k clusters."""
    assert len(restaurants) >= k, 'Not enough restaurants to cluster'
    old_centroids, n = [], 0
    # Select initial centroids randomly by choosing k different restaurants
    centroids = [restaurant_location(r) for r in sample(restaurants, k)]

    while old_centroids != centroids and n < max_updates:
        old_centroids = centroids
        # BEGIN Question 6
        clusters = group_by_centroid(restaurants, centroids)
        centroids = [find_centroid(cluster) for cluster in clusters]
        # END Question 6
        n += 1
    return centroids


def run(*args):
	wiki2 = "http://insider.espn.com/nba/hollinger/statistics/_/position/pg/year/2016"  #Accessing web page and converting to BS
	page2 = url.urlopen(wiki2)
	soup2 = BeautifulSoup(page2, "lxml")
	print(type(soup2))								#Check that BS is working (converting to correct object type)
	col = soup2.find_all(class_="tablehead")[0].find_all("tr")			#Create list of Stat Columns
	print(len(col))

	total_rankings = []
	for i in range(2,len(col)):
		row = col[i].find_all("td")
		stats = []
		for j in range(1, len(row)):
			stats.append(row[j].get_text())
		total_rankings.append(stats)
	#pprint.pprint(total_rankings)

	players = []
	for i in range(len(total_rankings)):
		players.append(BasketballPlayer(total_rankings[i][0],total_rankings[i][1::]))

	print(len(players))	
	for i in range(len(players)):
		players[i].player_print()

if  (__name__ =='__main__'):
	run()

