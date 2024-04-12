"""from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# List of valid users
valid_users = {'user1': 'password1', 'user2': 'password2', 'user3': 'password3'}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password are valid
        if username in valid_users and valid_users[username] == password:
            # If the user is valid, redirect to the home page
            return redirect('/home')
        else:
            # If the user is not valid, show an error message
            return render_template('login.html', error='Invalid username or password')

    # If the request method is GET, show the login page
    return render_template('login.html')


@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
"""
"""
from flask import Flask, render_template, request, redirect, url_for
import hashlib

app = Flask(__name__, static_folder='static')

# create a dictionary of users with hashed passwords
users = {
    'user1': '5f4dcc3b5aa765d61d8327deb882cf99',  # password: password
    'user2': '202cb962ac59075b964b07152d234b70',  # password: 123
}

# create a set of allowed users
allowed_users = set(users.keys())

# define a route for the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # check if the username is allowed
        if username not in allowed_users:
            error = 'Invalid username'
        else:
            # hash the password and compare it to the stored hash
            hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
            if hashed_password != users[username]:
                error = 'Invalid password'
            else:
                return redirect(url_for('home'))

    return render_template('login.html', error=error)


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        keyword = request.form['Keyword']
        print(keyword)
        # do something with the keyword here
        return redirect(url_for('home'))

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)


"""
"""
from flask import Flask, render_template, request, redirect, url_for, Response
import csv
import hashlib

app = Flask(__name__, static_folder='static')

# create a dictionary of users with hashed passwords
users = {
    'user1': '5f4dcc3b5aa765d61d8327deb882cf99',  # password: password
    'user2': '202cb962ac59075b964b07152d234b70',  # password: 123
}

# create a set of allowed users
allowed_users = set(users.keys())

# define a route for the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # check if the username is allowed
        if username not in allowed_users:
            error = 'Invalid username'
        else:
            # hash the password and compare it to the stored hash
            hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
            if hashed_password != users[username]:
                error = 'Invalid password'
            else:
                return redirect(url_for('home'))

    return render_template('login.html', error=error)


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        keyword = request.form['Keyword']
        # do something with the keyword here and save results to a CSV file
        with open('results.csv', mode='w', newline='') as results_file:
            results_writer = csv.writer(results_file)
            results_writer.writerow(['Column 1', 'Column 2', 'Column 3'])  # example headers
            results_writer.writerow(['Data 1', 'Data 2', 'Data 3'])  # example data
        # send the CSV file to the user for download
        with open('results.csv', mode='r') as results_file:
            contents = results_file.read()
        return Response(
            contents,
            mimetype='text/csv',
            headers={
                'Content-Disposition': 'attachment; filename="results.csv"'
            }
        )

    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
"""
"""
from flask import Flask, render_template, request, redirect, url_for, Response
import hashlib

app = Flask(__name__, static_folder='static')

# create a dictionary of users with hashed passwords
users = {
    'user1': '5f4dcc3b5aa765d61d8327deb882cf99',  # password: password
    'user2': '202cb962ac59075b964b07152d234b70',  # password: 123
}

# create a set of allowed users
allowed_users = set(users.keys())

# define a route for the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # check if the username is allowed
        if username not in allowed_users:
            error = 'Invalid username'
        else:
            # hash the password and compare it to the stored hash
            hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
            if hashed_password != users[username]:
                error = 'Invalid password'
            else:
                return redirect(url_for('home'))

    return render_template('login.html', error=error)


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        insta_word = request.form['insta-word']
        print(insta_word)
        twitter_word = request.form['twitter-word']
        print(twitter_word)
        fb_word = request.form['fb-word']
        print(fb_word)
        # do something with the keywords here and return the results to the user
        results = f"Results for Instagram word: {insta_word}, Twitter word: {twitter_word}, Facebook word: {fb_word}"
        return Response(
            results,
            mimetype='text/plain',
            headers={
                'Content-Disposition': 'attachment; filename="results.txt"'
            }
        )

    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)

"""
"""
from flask import Flask, render_template, request, redirect, url_for, Response
import csv
import tweet_scrape
import hashlib
import subprocess

app = Flask(__name__, static_folder='static')

# create a dictionary of users with hashed passwords
users = {
    'user1': '5f4dcc3b5aa765d61d8327deb882cf99',  # password: password
    'user2': '202cb962ac59075b964b07152d234b70',  # password: 123
}

# create a set of allowed users
allowed_users = set(users.keys())

# define a route for the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # check if the username is allowed
        if username not in allowed_users:
            error = 'Invalid username'
        else:
            # hash the password and compare it to the stored hash
            hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
            if hashed_password != users[username]:
                error = 'Invalid password'
            else:
                return redirect(url_for('home'))

    return render_template('login.html', error=error)


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')



@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form.get('card1'):
            # Call the insta_scrape function
            keyword = request.form['card1']
            insta_scrape()
            message = "Instagram scraping complete"
        elif request.form.get('card2'):
            # Call the twi.py script and pass the keyword as an argument
            keyword = request.form['card2']
            subprocess.run(['python', 'twi.py', keyword], capture_output=True)
            with open(f"{keyword}.csv", 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                data = next(reader)
            message = f"Twitter scraping complete for keyword '{keyword}'"
            return render_template('result.html', name=data['name'], description=data['description'],
                                   followers_count=data['followers_count'], friends_count=data['friends_count'],
                                   created_at=data['created_at'], active=data['active'], message=message)
        elif request.form.get('card3'):
            # Get the keyword from the form input
            keyword = request.form['card3']
            # Call the fb_scrape function with the keyword argument
            fb_scrape()
            message = f"Facebook scraping complete for keyword '{keyword}'"
        else:
            error = 'Invalid form input'
            return render_template('home.html', error=error)

        return redirect(url_for('home', _anchor='result', message=message))

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

"""
"""
from flask import Flask, render_template, request, redirect, url_for, Response
import csv
import tweet_scrape
import hashlib
import subprocess

app = Flask(__name__, static_folder='static')

# create a dictionary of users with hashed passwords
users = {
    'user1': '5f4dcc3b5aa765d61d8327deb882cf99',  # password: password
    'user2': '202cb962ac59075b964b07152d234b70',  # password: 123
}

# create a set of allowed users
allowed_users = set(users.keys())

# define a route for the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # check if the username is allowed
        if username not in allowed_users:
            error = 'Invalid username'
        else:
            # hash the password and compare it to the stored hash
            hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
            if hashed_password != users[username]:
                error = 'Invalid password'
            else:
                return redirect(url_for('home'))

    return render_template('login.html', error=error)


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

"""
"""
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form.get('card1'):
            # Call the insta_scrape function
            keyword = request.form['card1']
            insta_scrape()
            message = "Instagram scraping complete"
        elif request.form.get('card2'):
            # Call the twi.py script and pass the keyword as an argument
            keyword = request.form['card2']
            subprocess.run(['python', 'twi.py', keyword], capture_output=True)
            with open(f"{keyword}.csv", 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                data = next(reader)
            message = f"Twitter scraping complete for keyword '{keyword}'"
            return render_template('result.html', name=data['name'], description=data['description'],
                                   followers_count=data['followers_count'], friends_count=data['friends_count'],
                                   created_at=data['created_at'], active=data['active'], message=message)
        elif request.form.get('card3'):
            # Get the keyword from the form input
            keyword = request.form['card3']
            # Call the fb_scrape function with the keyword argument
            fb_scrape()
            message = f"Facebook scraping complete for keyword '{keyword}'"
        else:
            error = 'Invalid form input'
            return render_template('home.html', error=error)

        return redirect(url_for('home', _anchor='result', message=message))

    return render_template('home.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form.get('card2'):
            # Get the username from the form input
            username = request.form['card2']
            
            # Call the `Twitter.scrap` method to retrieve Twitter data
            data = Twitter.scrap(username)
            
            if data:
                # Create CSV file
                filename = f"{username}.csv"
                with open(filename, mode='w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(['Name', 'Followers Count', 'Friends Count', 'Created At', 'Description', 'Active'])
                    writer.writerow([data['name'], data['followers_count'], data['friends_count'], data['created_at'], data['description'], data['active']])
                
                # Prepare the data to be displayed
                message = f"Twitter scraping complete for username '{username}'"
                name = data['name']
                followers_count = data['followers_count']
                friends_count = data['friends_count']
                created_at = data['created_at']
                description = data['description']
                active = data['active']

                return render_template('result.html', name=name, description=description,
                                       followers_count=followers_count, friends_count=friends_count,
                                       created_at=created_at, active=active, message=message)
            else:
                return render_template('result.html', message="Failed to get data.")
        
        # Handle other form inputs or errors here
        
    return render_template('home.html')


def insta_scrape():
    print("Instagram scraper")


def fb_scrape():
    print("Facebook scraper")


if __name__ == '__main__':
    app.run(debug=True)
"""


"""
from flask import Flask, render_template, request, redirect, url_for, make_response, session
import csv
from flask import send_file
import hashlib
import subprocess
import json

app = Flask(__name__, static_folder='static')
app.secret_key = 'your-secret-key'  # Add a secret key for session


# create a dictionary of users with hashed passwords
users = {
    'user1': '5f4dcc3b5aa765d61d8327deb882cf99',  # password: password
    'user2': '202cb962ac59075b964b07152d234b70',  # password: 123
}

# create a set of allowed users
allowed_users = set(users.keys())


# define a route for the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # check if the username is allowed
        if username not in allowed_users:
            error = 'Invalid username'
        else:
            # hash the password and compare it to the stored hash
            hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
            if hashed_password != users[username]:
                error = 'Invalid password'
            else:
                return redirect(url_for('home'))

    return render_template('login.html', error=error)


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form.get('card2'):
            keyword = request.form['card2']
            # Call the twi.py script and pass the keyword as an argument
            process = subprocess.run(['python', 'twi.py', keyword], capture_output=True, text=True)
            print(process.stdout)
            print(process.stderr)
            data = {
                'name': '',
                'description': '',
                'followers_count': '',
                'friends_count': '',
                'created_at': '',
                'active': '',
                'filename': f'{keyword}.csv',
            }
            with open(f'{keyword}.csv', 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                data = next(reader)
            return render_template('result.html', name=data['name'], description=data['description'],
                                   followers_count=data['followers_count'], friends_count=data['friends_count'],
                                   created_at=data['created_at'], active=data['active'], filename=data['filename'])
        else:
            error = 'Invalid form input'
            return render_template('home.html', error=error)

    return render_template('home.html')

# Result route to display the scraped data
@app.route('/result')
def result():
    keyword = request.args.get('keyword')
    data = {
        'name': '',
        'description': '',
        'followers_count': '',
        'friends_count': '',
        'created_at': '',
        'active': '',
        'filename': f'{keyword}.csv',
    }

    with open(f'{keyword}.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = next(reader)

    return render_template('result.html', name=data['name'], description=data['description'],
                           followers_count=data['followers_count'], friends_count=data['friends_count'],
                           created_at=data['created_at'], active=data['active'], filename=data['filename'])

# Route for downloading the CSV file
@app.route('/download_csv', methods=['GET'])
def download_csv():
    filename = request.args.get('filename')
    try:
        return send_file(filename, attachment_filename=filename, as_attachment=True)
    except Exception as ex:
        print(f"Error downloading CSV file: {ex}")



def insta_scrape():
    print("Instagram scraper")


def twi_scrape(keyword):
    result = subprocess.run(['python', 'twi.py', keyword], capture_output=True, text=True)
    output = result.stdout.strip()
    data = json.loads(output)
    return data
if __name__ == '__main__':
    app.run(debug=True)"""

"""from flask import Flask, render_template, request, send_file,redirect,url_for
import csv
import hashlib
import subprocess
from twi import Twitter
app = Flask(__name__)

# create a dictionary of users with hashed passwords
users = {
    'user1': '5f4dcc3b5aa765d61d8327deb882cf99',  # password: password
    'user2': '202cb962ac59075b964b07152d234b70',  # password: 123
}

# create a set of allowed users
allowed_users = set(users.keys())


# define a route for the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # check if the username is allowed
        if username not in allowed_users:
            error = 'Invalid username'
        else:
            # hash the password and compare it to the stored hash
            hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
            if hashed_password != users[username]:
                error = 'Invalid password'
            else:
                return redirect(url_for('home'))

    return render_template('login.html', error=error)


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'card1' in request.form:
            keyword_twi = request.form['card1']
            print("Keyword (Twitter):", keyword_twi)
            # Call the twi.py script and pass the keyword as an argument
            process = subprocess.run(['python', 'twi.py', keyword_twi], capture_output=True, text=True)
            print(process.stdout)
            print(process.stderr)
            return redirect(url_for('result', keyword=keyword_twi.strip(), platform='Twitter'))
        elif 'card2' in request.form:
            keyword_inst = request.form['card2']
            print("Keyword (Instagram):", keyword_inst)
            # Call the inst.py script and pass the keyword as an argument
            process = subprocess.run(['python', 'inst.py', keyword_inst], capture_output=True, text=True)
            print(process.stdout)
            print(process.stderr)
            return redirect(url_for('result', keyword=keyword_inst.strip(), platform='Instagram'))
        else:
            print("error")
            error = 'Invalid form input'
            return render_template('home.html', error=error)
    else:
        print("Error")        
    return render_template('home.html')
@app.route('/result')
def result():
    keyword = request.args.get('keyword')
    platform = request.args.get('platform')

    data = {
        'name': '',
        'description': '',
        'followers_count': '',
        'friends_count': '',
        'created_at': '',
        'active': '',
        'filename': f'{keyword}.csv',
    }

    try:
        with open(f'{keyword}.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = next(reader)
    except FileNotFoundError:
        error = f"No CSV file found for keyword '{keyword}'"
        return render_template('result.html', error=error)

    if platform == 'Twitter':
        return render_template('result.html', twitter_data=data)
    elif platform == 'Instagram':
        return render_template('result.html', instagram_data=data)
    else:
        error = f"Invalid platform: {platform}"
        return render_template('result.html', error=error)


@app.route('/download_csv', methods=['GET'])
def download_csv():
    filename = request.args.get('filename')
    try:
        return send_file(filename, attachment_filename=filename, as_attachment=True, mimetype='text/csv')
    except Exception as ex:
        print(f"Error downloading CSV file: {ex}")
    return "Error downloading CSV file"




if __name__ == '__main__':
    app.run(debug=True)
"""
#main

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


reddit_client_id = 'Th7P7pEu76iII0P4BNDpwQ'
reddit_client_secret = 'jb2FHNH7YBuLNK6lVGPqNvDuCEoEdQ'
reddit_user_agent = 'Social app'

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


consumer_key = "QwIUrhUcRJXQfXzBcxZbdAFjn"
consumer_secret = "bkjd0Wm3bGUaxZeW1T4Z8teFPeclKquMmO51O19UbNaREH6jFK"
access_key = "1590364288673538050-UtvTI0R7o4acaVS0ZSYPz3VV9yGLT4"
access_secret = "EnvzvkBpTBfCMpSGq1CjvQsTpw4Lnm0XKI6d90HH3Y5wx"

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

