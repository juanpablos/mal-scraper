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


# write an username's MAL list to a file.
def scrape_mal_list(username, outfile="mal_scrape.csv"):

    try:
        with open(outfile, 'w', newline="\n", encoding='utf-8') as f:
            writer = csv.writer(f)

            keys = ['name', 'ani_id', 'ani_status', 'is_rewatch', 'score', 'progress', 'url']
            writer.writerow(keys)

            # type list - dict
            data = get_user_anime_list(username)  # possibly make more than 10 requests
            for anime in data:
                writer.writerow(get_values(anime, keys).insert(0, username))
    except AssertionError:
        pass
    except:
        time.sleep(20)
        scrape_mal_list(username, outfile)


# run this to generate a file with recently active MAL users.
# set times to a big value (ex: 100-1000) to save more users.
def scrape_users(outfile="users.txt", times=10):
    with open(outfile, 'w', newline="\n", encoding='utf-8') as uu:
        us = csv.writer(uu)
        for _ in range(times):
            print("iter {}".format(_))
            time.sleep(3)
            _users = list(discover_users())
            for u in _users:
                if not file_utilities.is_in_file(outfile, u):
                    us.writerow([u])
            uu.flush()


def run_list_scraper(username_file, outfile="mal_scrape.csv"):
    with open(username_file, 'r', newline="\n", encoding='utf-8') as f:
        for line in f:
            try:
                time.sleep(5)
                scrape_mal_list(line.strip(), outfile)

                print("{} done".format(line))
            except:
                time.sleep(20)
                pass


user_out = "users.txt"
mal_out = "mal_scrape.csv"
#scrape_users(user_out, 500)  # 3 seconds waiting per iteration

# run this after the users finish
run_list_scraper(user_out, mal_out)  # 5+ seconds per user average + 5 seconds waiting between users to not get 429'd
