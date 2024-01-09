import praw

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    password="",
    user_agent="testscript by u/someuser",
    username="someuser",
)

# To verify that you are authenticated as the correct user run:

print(reddit.user.me())

subreddit = reddit.subreddit('test')

# get 10 most hot posts
for submission in subreddit.hot(limit=10):
    print(submission.title)



image_url = 'https://fastly.picsum.photos/id/237/536/354.jpg?hmac=i0yVXW1ORpyCZpQ-CknuyV-jbtU7_x9EBQVhvT5aRr0'
title = 'Check out this image!'
submission = subreddit.submit(title, url=image_url)

# text only post
title = 'Your post title'
selftext = 'Your post content'
subreddit.submit(title, selftext=selftext)

# text linked in post
image_urls = ['https://fastly.picsum.photos/id/866/536/354.jpg?hmac=tGofDTV7tl2rprappPzKFiZ9vDh5MKj39oa2D--gqhA', 
              'https://fastly.picsum.photos/id/1084/536/354.jpg?grayscale&hmac=Ux7nzg19e1q35mlUVZjhCLxqkR30cC-CarVg-nlIf60', 
              'https://fastly.picsum.photos/id/1060/536/354.jpg?blur=2&hmac=0zJLs1ar00sBbW5Ahd_4zA6pgZqCVavwuHToO6VtcYY']  # Add as many as you have

post_text = '\n'.join(f'![Image]({url})' for url in image_urls)
title = 'Check out these images!'
submission = subreddit.submit(title, selftext=post_text)
print("Post URL:", submission.url)


# gallery post
title = "My favorite pictures"
image = "C:/Pictures/1.jpg"
image2 = "C:/Pictures/2.jpg"
image3 = "C:/Pictures/3.jpg"
images = [
    {"image_path": image},
    {
        "image_path": image2,
        "caption": "Image caption 2",
    },
    {
        "image_path": image3,
        "caption": "Image caption 3",
        "outbound_url": "https://example.com/link3",
    },
]
subreddit.submit_gallery(title, images)


# single image post
title = "My favorite picture"
image = "C:/Pictures/one.jpg"
subreddit.submit_image(title, image)