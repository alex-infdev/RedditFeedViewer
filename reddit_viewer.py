import os
import argparse
import praw
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.markup import escape

load_dotenv()

def get_reddit_instance():
    try:
        reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent=os.getenv("REDDIT_USER_AGENT"),
        )
        reddit.read_only
        return reddit
    except Exception as e:
        console.print(f"[bold red]Error authing with Reddit API: {e}[/bold red]")
        exit()

def fetch_posts(reddit, subreddit_name, sort_order, limit):
    try:
        subreddit = reddit.subreddit(subreddit_name)
        fetch_method = getattr(subreddit, sort_order)
        return fetch_method(limit=limit)
    except Exception as e:
        console.print(f"[bold red]Could not fetch posts for 'r/{subreddit_name}': {e}[/bold red]")
        exit()

def display_posts(posts):
    table = Table(
        title=f"Reddit Feed",
        header_style="bold cyan",
        box=None,
        padding=(0, 1)
    )

    table.add_column("Score", style="magenta", width=6, justify="right")
    table.add_column("Title & Author", style="bright_white", no_wrap=False)
    table.add_column("Comments", style="yellow", justify="right", width=8)

    for post in posts:
        score_text = Text(str(post.score))
        if post.score > 5000:
            score_text.stylize("bold green")
        elif post.score > 1000:
            score_text.stylize("bold yellow")

        author_name = post.author.name if post.author else "[deleted]"
        
        escaped_title = escape(post.title)
        escaped_author = escape(author_name)
        escaped_subreddit = escape(post.subreddit.display_name)

        post_details = Text.from_markup(
            f"{escaped_title}\n[dim itallic]by u/{escaped_author} on r/{escaped_subreddit}[/dim itallic]"
        )
        
        post_panel = Panel(
            post_details,
            border_style="dim",
            expand=False
        )

        table.add_row(
            score_text,
            post_panel,
            str(post.num_comments)
        )
    
    console.print(table)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="View Reddit feeds right in your terminal.")
    parser.add_argument(
        "subreddit",
        help="The subreddit you want to view (e.g., 'aww)"
    )
    parser.add_argument(
        "-s", "--sort",
        choices=["hot", "new", "top", "rising"],
        default="hot",
        help="Sort order for posts"
    )
    parser.add_argument(
        "-l", "--limit",
        type=int,
        default=10,
        help="Number of posts to display (10 by default)"
    )    
    args = parser.parse_args()

    console = Console()
    reddit = get_reddit_instance()
    posts = fetch_posts(reddit, args.subreddit, args.sort, args.limit)
    display_posts(posts)
