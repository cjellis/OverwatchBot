import praw
import input_module

reddit = praw.Reddit(
    client_id='',
    client_secret='',
    user_agent='python:chatbot:owchatbot1.0.0 (by /u/OverwatchChatBot)',
    username='',
    password=''
)

already_commented = set()


def check(comment):
    text = comment.body
    if "/u/overwatchchatbot" in text.lower():
        return True


def action(comment):
    text = comment.body
    response = input_module.parse(text)
    comment.reply(response)
    print response

print "Starting..."
ow = reddit.subreddit('testingground4bots')
print "Connected to Reddit..."
id_file = open('already_commented.txt', 'r+b')
for line in id_file:
    already_commented.add(line.rstrip())
print "Previous posts populated..."
for comment in ow.stream.comments():
    if check(comment) and comment.id not in already_commented:
        already_commented.add(comment.id)
        id_file.write(comment.id+"\n")
        action(comment)
