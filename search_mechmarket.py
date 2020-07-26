import praw
import datetime
from models import SubRedditModel
from db import Sesson

reddit = praw.Reddit(
    client_id="1EkdAIYXKO82XQ",
    client_secret="Po0hAGpUutXIxOCNhHhiYu8__1g",
    user_agent="script",
)

search_for = ("dox", "planck", "kyria", "corne", "minidox")
search_no = 1000
report = {}
for s in search_for:
    report[s] = []


def pAttrs(obj):
    attrs = sorted(obj.__dir__())
    print([attr for attr in attrs if attr[:1] != "_"])


def db_add(found):
    message = found.selftext
    title = found.title
    created = datetime.datetime.fromtimestamp(found.created)
    flair = found.link_flair_text
    subreddit: SubRedditModel = SubRedditModel(
        title=title, date_created=created, description=message, flair=flair
    )

    # print(f"X{created}X")
    existing_sr = (
        sesson.query(SubRedditModel)
        .filter(SubRedditModel.date_created == f"{created}")
        .first()
    )
    # print(existing_sr)
    if not existing_sr:
        sesson.add(subreddit)


def search():
    subreddit = reddit.subreddit("mechmarket")
    attrs = sorted(subreddit.__dir__())
    # print(subreddit.title)
    all_found = []
    for submission in subreddit.stream.submissions():
        flair: SubmissionFlair = submission.flair
        print(datetime.datetime.now(), submission.link_flair_text)
        all_found.append(submission)
        # print([attr for attr in attrs if attr[:1] != '_'])
        all_found = sorted(all_found, key=lambda x: x.created)
        for found in all_found:
            message = found.selftext
            title = found.title
            flair = found.link_flair_text
            created = datetime.datetime.fromtimestamp(found.created)
            # pAttrs(found)
            for s in search_for:
                if s in title.lower():
                    report[s].append([title, created, flair])
                    db_add(found)
            sesson.commit()
        all_found = []
        for s, v in report.items():
            if v:
                print(s)
                for t, time, flair in v:
                    print(time, t, flair)
                report[s] = []


def search_by_num():
    subreddit = reddit.subreddit("mechmarket")
    attrs = sorted(subreddit.__dir__())
    # print(subreddit.title)
    all_found = []
    # for submission in subreddit.stream.submissions():
    for submission in subreddit.new(limit=search_no):
        print(datetime.datetime.now(), submission.title, submission.link_flair_text)
        all_found.append(submission)
        # print([attr for attr in attrs if attr[:1] != '_'])
    all_found = sorted(all_found, key=lambda x: x.created)
    for found in all_found:
        message = found.selftext
        title = found.title
        flair = found.link_flair_text
        created = datetime.datetime.fromtimestamp(found.created)
        # pAttrs(found)
        for s in search_for:
            if s in title.lower():
                report[s].append([title, created, flair])
                db_add(found)
            sesson.commit()
    all_found = []
    for s, v in report.items():
        if v:
            print(s)
            for t, time, flair in v:
                print(time, t, flair)
            report[s] = []


sesson = Sesson()
search_by_num()
search()
