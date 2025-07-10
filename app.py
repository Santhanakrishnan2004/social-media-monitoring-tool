

from flask import Flask, render_template, request, send_file, redirect, url_for
import csv
import praw
import pandas as pd
from linkedin import scrape_linkedin
from twitter_keyword import tweet_extraction
import hashlib
import subprocess
import tweepy

app = Flask(__name__, static_folder='static')


reddit_client_id = ''
reddit_client_secret = ''
reddit_user_agent = ''

reddit = praw.Reddit(client_id=reddit_client_id, client_secret=reddit_client_secret, user_agent=reddit_user_agent)
# create a dictionary of users with hashed passwords
users = {
    'user1': '5f4dcc3b5aa765d61d8327deb882cf99',  # password: password
    'user2': '202cb962ac59075b964b07152d234b70',  # password: 123
}

# create a set of allowed users
allowed_users = set(users.keys())
@app.route('/', methods=['GET', 'POST'])
def login():
    # Handle form submission
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username is allowed
        if username not in users:
            error = 'Invalid username'
        else:
            # Hash the password and compare it to the stored hash
            hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
            if hashed_password != users[username]:
                error = 'Invalid password'
            else:
                return redirect(url_for('home'))

        return render_template('login.html', error=error)

    return render_template('login.html')

# Create account route
@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']

    # Hash the password and add the user to the users dictionary
    hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
    users[email] = hashed_password

    return redirect(url_for('register_confirmation'))

# Register confirmation route
@app.route('/register-confirmation')
def register_confirmation():
    return render_template('register.html')




@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/createaccount')
def createaccount():
    return render_template('createaccount.html')


consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)



from flask import redirect, url_for


def reddit_crawler(keyword):
    reddit = praw.Reddit(client_id=reddit_client_id, client_secret=reddit_client_secret, user_agent=reddit_user_agent)
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

# Update the home route
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'card1' in request.form:
            # Handle Twitter keyword
            keyword_twi = request.form['card1']
            print("Keyword (Twitter):", keyword_twi)
            # Call the tweet_extraction function and pass the keyword and api object
            tweet_data = tweet_extraction(api, keyword_twi)
            print(tweet_data)
            return render_template('twitter.html', tweets=tweet_data)
        elif 'card2' in request.form:
            # Handle Reddit keyword
            keyword = request.form['card2']
            print("Keyword (Reddit):", keyword)
            # Call the reddit_crawler function and pass the keyword
            posts_data = reddit_crawler(keyword)
            print(posts_data)
            return render_template('reddit.html', posts=posts_data.values.tolist())
        elif 'card3' in request.form:
            # Handle LinkedIn keyword
            keyword = request.form['card3']
            print("Keyword (LinkedIn):", keyword)
            # Call the scrape_linkedin function and pass the keyword
            data = scrape_linkedin(keyword)
            print(data)
            return render_template('linkedin.html', data=data)
        else:
            error = 'Invalid form input'
            return render_template('home.html', error=error)
    else:
        return render_template('home.html')
# ...
from linkedin import scrape_linkedin

@app.route('/linkedin', methods=['POST'])
def linkedin():
    if 'card3' in request.form:
        keyword = request.form['card3']
        print("Keyword (LinkedIn):", keyword)
        # Call the scrape_linkedin function and pass the keyword as an argument
        data = scrape_linkedin(keyword)
        print(data)

        return render_template('linkedin.html', data=data)

    else:
        print("Error")
        error = 'Invalid form input'
        return render_template('home.html', error=error)





@app.route('/twitter', methods=['POST'])
def twitter():
    if 'card1' in request.form:
        keyword = request.form['card1']
        print("Keyword (Twitter):", keyword)
        # Call the tweet_extraction function and pass the keyword and api object
        tweet_data = tweet_extraction(api, keyword)
        print(tweet_data)
        return render_template('twitter.html', tweets=tweet_data)
    else:
        print("Error")
        error = 'Invalid form input'
        return render_template('home.html', error=error)




@app.route('/reddit', methods=['GET', 'POST'])
def reddit():
    if request.method == 'POST':
        keyword = request.form['card2']
        print("Keyword (Reddit):", keyword)
        # Call the reddit_crawler function and pass the keyword
        posts_data = reddit_crawler(keyword)
        print(posts_data)  
        
        # Verify that data is fetched correctly

        # Render the template and pass the DataFrame to it
        return render_template('reddit.html', posts=posts_data.values.tolist())
    else:
        print("Error")
        error = 'Invalid form input'
        return render_template('home.html', error=error)

@app.route('/download_csv')
def download_csv():
    keyword = request.args.get('keyword')
    filename = f'scraped_tweets_{keyword}.csv'

    return send_file(filename, as_attachment=True)


@app.route('/download')
def download():
    keyword = 'your_keyword'
    language = 'english'
    format = 'csv'
    return reddit_crawler(keyword, language, format)


if __name__ == '__main__':
    app.run(port=8000)

