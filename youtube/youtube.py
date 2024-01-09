from googleapiclient.discovery import build

def get_channel_uploads(youtube, channel_id):
# Get channel details
    channel_response = youtube.channels().list(id=channel_id, part='contentDetails').execute()
    uploads_playlist_id = channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    # Get the list of videos
    playlistitems_response = youtube.playlistItems().list(playlistId=uploads_playlist_id, part='snippet', maxResults=10).execute()
    videos = []
    for item in playlistitems_response['items']:
        video_id = item['snippet']['resourceId']['videoId']
        title = item['snippet']['title']
        videos.append({'id': video_id, 'title': title})
    return videos

# Authenticate with the API
youtube = build('youtube', 'v3', developerKey='YOUR_API_KEY')

videos = get_channel_uploads(youtube=youtube, channel_id='CHANNEL_ID')
for video in videos:
    print(f"ID: {video['id']}, Title: {video['title']}")