# Reddit terminal feed viewer

A command-line tool to view Reddit feeds directly in your terminal, built with Python. This tool uses the Reddit API to fetch posts and displays them in a clean, readable format using the Rich library.

#### Features

- Fetches posts from any public subreddit
- Sorts posts by hot, new, top, or rising
- Customizable limit for the number of posts to display
- Runs in the terminal


## Installation and setup
### Step 1: Clone the repository and navigate to directory

```
git clone https://github.com/alex-infdev/RedditFeedViewer.git
cd RedditFeedVierwer
```

### Step 2: Create a virtual environment

Virtual enviroments are good, mkay?

```python -m venv venv```

#### Activate it

On Windows:
```
venv\Scripts\activate
```
On macOS/Linux:
```
source venv/bin/activate
```
### Step 3: Install dependencies

Install the required Python libraries from the requirements.txt file.

```
pip install -r requirements.txt
```

### Step 4: Configure API credentials

- Get credentials: go to your Reddit app preferences to create a new script app. This will give you a client_id and client_secret.
- Create an .env file
- Add credentials: open your .env file and fill in your Reddit API credentials.
  ```
  REDDIT_CLIENT_ID='YOUR_CLIENT_ID'
  REDDIT_CLIENT_SECRET='YOUR_CLIENT_SECRET'
  ```

### Usage

Run the script from your terminal, specifying a subreddit.

#### Examples

Get the default 15 "hot" posts from r/mildlyinfuriating:

```
python reddit_viewer.py mildlyinfuriating
```
Get the 5 "newest" posts from r/python:

```
python reddit_viewer.py python --sort new --limit 5
```
Get the 20 "top" posts from r/aww:
```
python reddit_viewer.py aww -s top -l 20
```
