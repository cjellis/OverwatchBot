import praw
import input_module
#################################################
already_commented = set()
#################################################


def check(comment):
    """
    Determines if comment should be made
    :param comment: the comment from reddit
    :return: Boolean
    """
    if comment.id not in already_commented:
        text = comment.body
        if "/u/overwatchchatbot" in text.lower():
            return True
    return False


def action(comment):
    """
    The action the bot will take
    :param comment: 
    :return: 
    """
    text = comment.body
    response = input_module.parse(text)
    comment.reply(response)
    print(response)


def main():
    """
    Runs the Reddit Bot
    :return: 
    """
    # Connect to Reddit
    reddit = praw.Reddit(
        client_id='',
        client_secret='',
        user_agent='python:chatbot:owchatbot1.0.0 (by /u/OverwatchChatBot)',
        username='',
        password=''
    )
    ow = reddit.subreddit('testingground4bots')
    print("Connected to Reddit and Subreddit...")

    # Load in previously commented items
    # Can probably be removed once the bot has more use and regular uptime
    id_file = open('already_commented.txt', 'r+')
    for line in id_file:
        already_commented.add(line.rstrip())
    print("Previous posts populated...")

    # Stream new comments
    for comment in ow.stream.comments():
        if check(comment):
            already_commented.add(comment.id)
            id_file.write(comment.id+"\n")

            action(comment)
