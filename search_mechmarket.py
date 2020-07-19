import praw
import datetime
from models import SubReddit
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:////home/rado/software/python3/reddit/migrations/app.db", echo=False
)


Sesson = sessionmaker(bind=engine)


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
    subreddit: SubReddit = SubReddit(
        title=title, date_created=created, description=message
    )

    # print(f"X{created}X")
    existing_sr = sesson.query(SubReddit).filter(SubReddit.date_created
                                                 ==f"{created}").first()
    # print(existing_sr)
    if not existing_sr:
        sesson.add(subreddit)

def search():
    subreddit = reddit.subreddit("mechmarket")
    attrs = sorted(subreddit.__dir__())
    # print(subreddit.title)
    all_found = []
    for submission in subreddit.hot(limit=search_no):
        all_found.append(submission)
    # print([attr for attr in attrs if attr[:1] != '_'])
    all_found = sorted(all_found, key=lambda x: x.created)
    print("DB BUILD")
    for found in all_found:
        message = found.selftext
        title = found.title
        created = datetime.datetime.fromtimestamp(found.created)
        # pAttrs(found)
        for s in search_for:
            if s in title.lower():
                report[s].append([title, created])
                db_add(found)


    sesson.commit()
    for s, v in report.items():
        print(s)
        for t, time in v:
            print(time, t)


sesson = Sesson()
search()
