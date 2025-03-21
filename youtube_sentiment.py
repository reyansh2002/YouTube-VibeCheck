import os
import csv
import googleapiclient.discovery
from textblob import TextBlob
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")

def get_youtube_comments(video_id):
    """Fetches ALL comments from a YouTube video using pagination."""
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)

    comments_data = []
    next_page_token = None  # Used for pagination

    while True:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,  # Max comments per request
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response.get("items", []):
            comment = item["snippet"]["topLevelComment"]["snippet"]
            author = comment.get("authorDisplayName", "Unknown")
            text = comment.get("textDisplay", "")
            published_at = comment.get("publishedAt", "N/A")

            comments_data.append({"author": author, "comment": text, "date_time": published_at})

        # Get next page token (if available)
        next_page_token = response.get("nextPageToken")

        # If no more pages, break loop
        if not next_page_token:
            break

    return comments_data

def analyze_sentiment(comments_data):
    """Analyzes sentiment and adds sentiment scores."""
    results = []
    for data in comments_data:
        analysis = TextBlob(data["comment"])
        polarity = round(analysis.sentiment.polarity, 3)  # Sentiment score

        if polarity > 0:
            sentiment = "Positive 😊"
        elif polarity < 0:
            sentiment = "Negative 😡"
        else:
            sentiment = "Neutral 😐"

        data["sentiment"] = sentiment
        data["sentiment_score"] = polarity
        results.append(data)

    # Save to CSV
    save_to_csv(results)
    return results

def save_to_csv(results, filename="youtube_comments.csv"):
    """Saves analyzed comments to a CSV file."""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["author", "comment", "date_time", "sentiment", "sentiment_score"])
        writer.writeheader()
        writer.writerows(results)

    print(f"✅ Saved results to {filename}")
