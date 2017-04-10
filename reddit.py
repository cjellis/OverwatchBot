import praw
import decision_module

reddit = praw.Reddit(
    client_id='',
    client_secret='',
    user_agent='python:chatbot:owchatbot1.0.0 (by /u/OverwatchChatBot)',
    username='OverwatchChatBot',
    password='OWChatBot1'
)

already_commented = set()


def check(comment):
    text = comment.body
    if "/u/overwatchchatbot" in text.lower():
        return True


def action(comment):
    text = comment.body
    response = decision_module.generate_response("", ["hanzo","bad","switch"])
    comment.reply(response)
    print response


ow = reddit.subreddit('testingground4bots')
file = open('')
for comment in ow.stream.comments():
    if check(comment) and comment.id not in already_commented:
        already_commented.add(comment.id)
        action(comment)
