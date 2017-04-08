import json
import praw
from praw.models import MoreComments

characters = [
    'GENJI',
    'MCCREE',
    'PHARAH',
    'REAPER',
    'SOLDIER',
    '76',
    'SOMBRA',
    'TRACER',
    'BASTION',
    'HANZO',
    'JUNKRAT',
    'MEI',
    'TORBJORN',
    'WIDOWMAKER',
    'DVA',
    'D.VA',
    'ORISA',
    'REIN',
    'REINHARDT',
    'ROADHOG',
    'WINSTON',
    'ZARYA',
    'ANA',
    'LUCIO',
    'MERCY',
    'SYMMETRA',
    'ZENYATTA'
]

char_obj = {
    'genji': [],
    'mccree': [],
    'pharah': [],
    'reaper': [],
    'soldier: 76': [],
    'sombra': [],
    'tracer': [],
    'bastion': [],
    'hanzo': [],
    'junkrat': [],
    'mei': [],
    'torbjorn': [],
    'widowmaker': [],
    'd.va': [],
    'orisa': [],
    'reinhardt': [],
    'roadhog': [],
    'winston': [],
    'zarya': [],
    'ana': [],
    'lucio': [],
    'mercy': [],
    'symmetra': [],
    'zenyatta': []
}

reddit = praw.Reddit(client_id='',
    client_secret='',
    user_agent='python:chatbot:0.0.1 (by /u/golf1052)')

overwatch = reddit.subreddit('overwatch')

for submission in overwatch.hot(limit=100):
    all_comments = submission.comments.list()
    for comment in all_comments:
        if isinstance(comment, MoreComments):
            continue
        split = comment.body.splitlines()
        for line in split:
            for character in characters:
                if character in line.upper():
                    try:
                        if character in ['SOLDIER', '76']:
                            char_obj['soldier: 76'].append(line.strip())
                        elif character in ['DVA', 'D.VA']:
                            char_obj['d.va'].append(line.strip())
                        elif character in ['REIN', 'REINHARDT']:
                            char_obj['reinhardt'].append(line.strip())
                        else:
                            char_obj[character.lower()].append(line.strip())
                    except:
                        pass

print json.dumps(char_obj, indent=4, separators=(',', ': '))
