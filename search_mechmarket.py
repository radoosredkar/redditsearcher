import praw
import datetime

reddit = praw.Reddit(
    client_id="1EkdAIYXKO82XQ",
    client_secret="Po0hAGpUutXIxOCNhHhiYu8__1g",
    user_agent="script",
)

search_for = ("dox", "planck", "kyria", "corne", "minidox")
search_no = 500
report = {}
for s in search_for:
    report[s] = []

subreddit = reddit.subreddit("mechmarket")
attrs = sorted(subreddit.__dir__())
# print([attr for attr in attrs if attr[:1] != '_'])
print(subreddit.title)
all_found = []
for submission in subreddit.hot(limit=search_no):
    all_found.append(submission)
# print([attr for attr in attrs if attr[:1] != '_'])
all_found = sorted(all_found, key=lambda x: x.created)
print("DB BUILD")
for found in all_found:
    title = found.title
    created = datetime.datetime.fromtimestamp(found.created)
    for s in search_for:
        if s in title.lower():
            report[s].append([title, created])

for s, v in report.items():
    print(s)
    for t, time in v:
        print(time, t)
