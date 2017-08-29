import csv

import time

import file_utilities
from mal_scraper.users import get_user_anime_list
from mal_scraper.user_discovery import discover_users


def get_values(dictionary, key_arr):
    w = []
    for key in key_arr:
        w.append(dictionary[key])
    return w


def temp():

    an = open("Testing3.txt", 'w', newline="\n", encoding='utf-8')
    r = csv.writer(an)

    keys = ['name', 'ani_id', 'ani_status', 'is_rewatch', 'score', 'progress', 'url']
    r.writerow(keys)

    # type list - dict
    data=get_user_anime_list("HeavensC")
    for i in data:
        print(i)
        r.writerow(get_values(i, keys))


def scrape_users(outfile="users.txt", times=10):
    uu = open(outfile, 'w', newline="\n", encoding='utf-8')
    us = csv.writer(uu)
    for _ in range(times):
        print("iter {}".format(_))
        time.sleep(3)
        _users = list(discover_users())
        for u in _users:
            if not file_utilities.is_in_file(outfile, u):
                us.writerow([u])
        uu.flush()
    uu.close()



