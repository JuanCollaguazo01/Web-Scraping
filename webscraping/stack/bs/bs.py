import requests
from bs4 import BeautifulSoup
# Import MongoClient from pymongo so we can connect to the database
from pymongo import MongoClient


if __name__ == '__main__':
    # Instantiate a client to our MongoDB instance
    db_client = MongoClient()
    my_db = db_client.my_db
    my_posts = my_db.posts


    response = requests.get("http://andythemoron.com")
    soup = BeautifulSoup(response.content, "lxml")

    post_titles = soup.find_all("a", class_="post-title")

    extracted = []
    for post_title in post_titles:
        extracted.append({
            'title' : post_title['title'],
            'link'  : "andythemoron.com" + post_title['href']
        })

    # Iterate over each post. If the link does not exist in the database, it's new! Add it.
    for post in extracted:
        if db_client.my_db.my_posts.find_one({'link': post['link']}) is None:
            # Let's print it out to verify that we added the new post
            print("Found a new listing at the following url: ", post['link'])
            db_client.my_db.my_posts.insert(post)