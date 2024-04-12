"""import praw
import pandas as pd

reddit = praw.Reddit(client_id='Th7P7pEu76iII0P4BNDpwQ', client_secret='jb2FHNH7YBuLNK6lVGPqNvDuCEoEdQ', user_agent='Social app')
posts = []
ml_subreddit = reddit.subreddit('anime')
for post in ml_subreddit.hot(limit=20):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
    

posts_df = pd.DataFrame(posts, columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
print(posts_df)
posts_df.to_csv('reddit_posts.csv', index=False)
"""
"""
import praw
import pandas as pd

reddit_client_id = 'Th7P7pEu76iII0P4BNDpwQ'
reddit_client_secret = 'jb2FHNH7YBuLNK6lVGPqNvDuCEoEdQ'
reddit_user_agent = 'Social app'

reddit = praw.Reddit(client_id=reddit_client_id, client_secret=reddit_client_secret, user_agent=reddit_user_agent)

def reddit_crawler(keyword):
    posts = []
    ml_subreddit = reddit.subreddit(keyword)
    for post in ml_subreddit.hot(limit=20):
        posts.append({
            'title': post.title,
            'score': post.score,
            'id': post.id,
            'subreddit': post.subreddit.display_name,
            'url': post.url,
            'num_comments': post.num_comments,
            'body': post.selftext,
            'created': post.created
        })
    posts_df = pd.DataFrame(posts)
    return posts_df
"""
"""
import praw
import pandas as pd


def reddit_crawler(keyword):
    posts = []
    ml_subreddit = reddit.subreddit(keyword)
    for post in ml_subreddit.hot(limit=20):
        posts.append({
            'title': post.title,
            'score': post.score,
            'id': post.id,
            'subreddit': post.subreddit.display_name,
            'url': post.url,
            'num_comments': post.num_comments,
            'body': post.selftext,
            'created': post.created
        })
    posts_df = pd.DataFrame(posts)

    return posts_df"""

"""
import praw
import pandas as pd
import datetime

def reddit_crawler(keyword):
    posts = []
    for post in reddit.subreddit("all").search(keyword, limit=20):  # Search for posts containing the keyword
        post.comments.replace_more(limit=None)  # Retrieve all comments
        for comment in post.comments.list():
            created_utc = datetime.datetime.fromtimestamp(comment.created_utc).strftime('%Y/%m/%d %H:%M:%S')
            if keyword in post.title or keyword in comment.body:  # Check if keyword is present in post title or comment
                posts.append({
                    'title': post.title,
                    'score': post.score,
                    'id': post.id,
                    'subreddit': post.subreddit.display_name,
                    'url': post.url,
                    'num_comments': post.num_comments,
                    'body': comment.body,
                    'created': created_utc
                })
    posts_df = pd.DataFrame(posts)
    return posts_df"""
"""
import praw
import pandas as pd
import pytz
from datetime import datetime

def reddit_crawler(keyword):
    posts = []
    ml_subreddit = reddit.subreddit("all")  # Search in all subreddits
    keyword = keyword.lower()  # Convert keyword to lowercase for case-insensitive matching

    for post in ml_subreddit.hot(limit=20):  # Search for hot posts
        post.comments.replace_more(limit=None)  # Retrieve all comments
        created_utc = datetime.fromtimestamp(post.created_utc, pytz.utc).astimezone(pytz.timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')  # Convert to IST

        # Check if keyword is present in the post title or any comment
        if keyword in post.title.lower():
            posts.append({
                'title': post.title,
                'score': post.score,
                'id': post.id,
                'subreddit': post.subreddit.display_name,
                'url': post.url,
                'num_comments': post.num_comments,
                'body': post.selftext,
                'created': created_utc
            })

        for comment in post.comments.list():
            if keyword in comment.body.lower():
                created_utc = datetime.fromtimestamp(comment.created_utc, pytz.utc).astimezone(pytz.timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')  # Convert to IST
                posts.append({
                    'title': post.title,
                    'score': post.score,
                    'id': post.id,
                    'subreddit': post.subreddit.display_name,
                    'url': post.url,
                    'num_comments': post.num_comments,
                    'body': comment.body,
                    'created': created_utc
                })

    posts_df = pd.DataFrame(posts)
    return posts_df
"""
"""
import praw
import pandas as pd
import pytz
from datetime import datetime

def reddit_crawler(keyword, language='english'):
    posts = []
    ml_subreddit = reddit.subreddit("all")  # Search in all subreddits
    keyword = keyword.lower()  # Convert keyword to lowercase for case-insensitive matching

    for post in ml_subreddit.hot(limit=20):  # Search for hot posts
        post.comments.replace_more(limit=None)  # Retrieve all comments
        created_utc = datetime.fromtimestamp(post.created_utc, pytz.utc).astimezone(pytz.timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')  # Convert to IST

        # Check if keyword is present in any comment
        for comment in post.comments.list():
            if keyword in comment.body.lower() and (language == 'english' or comment.body.isascii()):
                created_utc = datetime.fromtimestamp(comment.created_utc, pytz.utc).astimezone(pytz.timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')  # Convert to IST
                posts.append({
                    'title': post.title,
                    'score': post.score,
                    'id': post.id,
                    'subreddit': post.subreddit.display_name,
                    'url': post.url,
                    'num_comments': post.num_comments,
                    'body': comment.body,
                    'created': created_utc
                })
                break  # Break the loop if a match is found in comments

        # Check if keyword is present in the post title
        if keyword in post.title.lower() and (language == 'english' or post.title.isascii()):
            posts.append({
                'title': post.title,
                'score': post.score,
                'id': post.id,
                'subreddit': post.subreddit.display_name,
                'url': post.url,
                'num_comments': post.num_comments,
                'body': post.selftext,
                'created': created_utc
            })

    posts_df = pd.DataFrame(posts)
    return posts_df"""
"""
import praw
import pandas as pd
import pytz
from datetime import datetime

def reddit_crawler(keyword, language='english', format='csv'):
    posts = []
    ml_subreddit = reddit.subreddit("all")  # Search in all subreddits
    keyword = keyword.lower()  # Convert keyword to lowercase for case-insensitive matching

    for post in ml_subreddit.hot(limit=20):  # Search for hot posts
        post.comments.replace_more(limit=None)  # Retrieve all comments
        created_utc = datetime.fromtimestamp(post.created_utc, pytz.utc).astimezone(pytz.timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')  # Convert to IST

        # Check if keyword is present in any comment
        for comment in post.comments.list():
            if keyword in comment.body.lower() and (language == 'english' or comment.body.isascii()):
                created_utc = datetime.fromtimestamp(comment.created_utc, pytz.utc).astimezone(pytz.timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')  # Convert to IST
                posts.append({
                    'title': post.title,
                    'score': post.score,
                    'id': post.id,
                    'subreddit': post.subreddit.display_name,
                    'url': post.url,
                    'num_comments': post.num_comments,
                    'body': comment.body,
                    'created': created_utc
                })
                break  # Break the loop if a match is found in comments

        # Check if keyword is present in the post title
        if keyword in post.title.lower() and (language == 'english' or post.title.isascii()):
            posts.append({
                'title': post.title,
                'score': post.score,
                'id': post.id,
                'subreddit': post.subreddit.display_name,
                'url': post.url,
                'num_comments': post.num_comments,
                'body': post.selftext,
                'created': created_utc
            })

    posts_df = pd.DataFrame(posts)

    # Export the data in the specified format
    if format == 'csv':
        posts_df.to_csv('reddit_data.csv', index=False)
    elif format == 'json':
        posts_df.to_json('reddit_data.json', orient='records')
    elif format == 'excel':
        posts_df.to_excel('reddit_data.xlsx', index=False)
    else:
        print(f"Invalid format: {format}. Data export not supported for this format.")

    return posts_df
    if format == 'csv':
        file_path = 'reddit_data.csv'
        posts_df.to_csv(file_path, index=False)
    elif format == 'json':
        file_path = 'reddit_data.json'
        posts_df.to_json(file_path, orient='records')
    elif format == 'excel':
        file_path = 'reddit_data.xlsx'
        posts_df.to_excel(file_path, index=False)
    else:
        return f"Invalid format: {format}. Data export not supported for this format."

    return send_file(file_path, as_attachment=True)"""

"""
import requests
from bs4 import BeautifulSoup
import math
import pandas as pd

def scrape_linkedin(keyword, location="India"):
    l = []
    o = {}
    k = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }

    # Update the target URL with the desired keyword and location
    target_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={}&location={}&geoId=100293800&currentJobId=3415227738&start={}'

    for i in range(0, math.ceil(117/25)):
        res = requests.get(target_url.format(keyword, location, i))
        soup = BeautifulSoup(res.text, 'html.parser')
        alljobs_on_this_page = soup.find_all("li")
        print(len(alljobs_on_this_page))
        for x in range(0, len(alljobs_on_this_page)):
            jobid = alljobs_on_this_page[x].find("div", {"class": "base-card"}).get('data-entity-urn').split(":")[3]
            l.append(jobid)

    target_url = 'https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{}'

    for j in range(0, len(l)):
        resp = requests.get(target_url.format(l[j]))
        soup = BeautifulSoup(resp.text, 'html.parser')

        try:
            o["company"] = soup.find("div", {"class": "top-card-layout__card"}).find("a").find("img").get('alt')
        except:
            o["company"] = None

        try:
            o["job-title"] = soup.find("div", {"class": "top-card-layout__entity-info"}).find("a").text.strip()
        except:
            o["job-title"] = None

        try:
            o["level"] = soup.find("ul", {"class": "description__job-criteria-list"}).find("li").text.replace(
                "Seniority level", "").strip()
        except:
            o["level"] = None

        hashtags = soup.find_all("a", {"class": "hashtag-link"})
        o["hashtags"] = [tag.text.strip() for tag in hashtags]

        k.append(o)
        o = {}
    
    df = pd.DataFrame(k)
    return df.to_dict('records')
"""
import requests
from bs4 import BeautifulSoup
import math
import pandas as pd
import firebase_admin


def scrape_linkedin(keyword, location="India"):
    l = []
    o = {}
    k = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }

    # Update the target URL with the desired keyword and location
    target_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={}&location={}&geoId=100293800&currentJobId=3415227738&start={}'

    for i in range(0, math.ceil(117/25)):
        res = requests.get(target_url.format(keyword, location, i))
        soup = BeautifulSoup(res.text, 'html.parser')
        alljobs_on_this_page = soup.find_all("li")
        print(len(alljobs_on_this_page))
        for x in range(0, len(alljobs_on_this_page)):
            jobid = alljobs_on_this_page[x].find("div", {"class": "base-card"}).get('data-entity-urn').split(":")[3]
            l.append(jobid)

    target_url = 'https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{}'

    for j in range(0, len(l)):
        resp = requests.get(target_url.format(l[j]))
        soup = BeautifulSoup(resp.text, 'html.parser')

        try:
            o["company"] = soup.find("div", {"class": "top-card-layout__card"}).find("a").find("img").get('alt')
        except:
            o["company"] = None

        try:
            o["job-title"] = soup.find("div", {"class": "top-card-layout__entity-info"}).find("a").text.strip()
        except:
            o["job-title"] = None

        try:
            o["level"] = soup.find("ul", {"class": "description__job-criteria-list"}).find("li").text.replace(
                "Seniority level", "").strip()
        except:
            o["level"] = None

        hashtags = soup.find_all("a", {"class": "hashtag-link"})
        o["hashtags"] = [tag.text.strip() for tag in hashtags]

        k.append(o)
        o = {}

    # Store data in Firebase
    for job in k:
        doc_ref = db.collection('jobs').document()
        doc_ref.set(job)

    df = pd.DataFrame(k)
    return df.to_dict('records')
