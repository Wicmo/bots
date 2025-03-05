import praw
import os 
import requests

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    password="",
    user_agent="<platform>:<app ID>:<version string> (by /u/<reddit username>)",
    username="",
)
print(reddit.read_only)


subreddit = reddit.subreddit("test")


def create_folder(save_dir):
    CHECK_FOLDER = os.path.isdir(save_dir)
    if not CHECK_FOLDER:
        os.makedirs(save_dir, exist_ok=True)

save_dir = "reddit/downloaded_images"
create_folder(save_dir)

name = ''






def main():
    value = 0
    url_best = ''
    for submission in subreddit.hot(limit=100):
        url = submission.url

        if value < submission.score and submission.url.endswith((".jpg", ".jpeg", ".png")):
            value = submission.score
            url_best = submission.url
            image_name = os.path.join(save_dir, f"{submission.id}.jpg")
            name = submission.title

    print(url_best)

    response = requests.get(url_best)
    print(response)
    if response.status_code == 200:
        with open(image_name, 'wb') as f:
            f.write(response.content)
        print('image downloaded')

    else:
        print('download failed')



main()