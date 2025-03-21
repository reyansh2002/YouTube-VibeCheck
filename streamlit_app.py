import streamlit as st
import youtube_sentiment
import re
import pandas as pd
import time

# Custom CSS for a Modern, Professional UI
st.markdown("""
    <style>
    /* Full Page Background */
    body {
        background: linear-gradient(to right, #000428, #004e92);
        color: white;
    }

    /* Centered Container */
    .main-container {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 30px;
        box-shadow: 0px 4px 20px rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
    }

    /* Title Styling */
    .title {
        text-align: center;
        font-size: 38px;
        font-weight: bold;
        color: #00eaff;
        margin-bottom: 5px;
    }

    /* Subtitle */
    .sub-title {
        text-align: center;
        font-size: 18px;
        color: #d1e8ff;
        margin-bottom: 20px;
    }

    /* Styled Buttons */
    .stButton>button {
        background-color: #00eaff;
        color: black;
        font-size: 16px;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px;
        width: 100%;
        transition: 0.3s;
        border: none;
    }
    .stButton>button:hover {
        background-color: #00c7d6;
        transform: scale(1.05);
    }

    /* Metrics Styling */
    .stMetric {
        text-align: center;
        font-weight: bold;
        font-size: 18px;
        color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

def extract_video_id(url):
    """Extracts video ID from YouTube links (normal & Shorts)."""
    match = re.search(r"(?:v=|/shorts/|youtu\.be/|v=)([a-zA-Z0-9_-]+)", url)
    return match.group(1) if match else None

def main():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    # Title and Subtitle
    st.markdown('<p class="title">📊 YouTube Sentiment Analysis</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Analyze video comments and understand audience sentiment.</p>', unsafe_allow_html=True)

    st.divider()

    # Input field for YouTube URL
    video_url = st.text_input("🔗 Enter YouTube Video URL:")

    # Buttons in a row
    col1, col2 = st.columns([1, 1])
    with col1:
        preview_clicked = st.button("🎥 Preview Video")
    with col2:
        analyze_clicked = st.button("📊 Analyze Sentiment")

    # Video Preview Section
    if preview_clicked:
        video_id = extract_video_id(video_url)
        if video_id:
            st.write("### 🎬 Video Preview:")
            st.video(f"https://www.youtube.com/embed/{video_id}")
        else:
            st.error("❌ Invalid YouTube URL. Please enter a valid video link.")

    # Sentiment Analysis Section
    if analyze_clicked:
        video_id = extract_video_id(video_url)
        if video_id:
            st.info("⏳ Fetching comments... Please wait.")

            start_time = time.time()  # Start timer

            # Progress Bar Animation
            progress_bar = st.progress(0)
            for percent in range(100):
                time.sleep(0.02)
                progress_bar.progress(percent + 1)

            comments_data = youtube_sentiment.get_youtube_comments(video_id)

            if comments_data:
                st.success(f"✅ Analysis Complete! {len(comments_data)} comments retrieved.")

                sentiment_results = youtube_sentiment.analyze_sentiment(comments_data)

                st.write("### 📊 Sentiment Analysis Results")
                df = pd.DataFrame(sentiment_results)

                # Display structured data
                st.dataframe(df.style.set_table_styles([
                    {'selector': 'th', 'props': [('background-color', '#00eaff'), ('color', 'black'), ('font-weight', 'bold')]}
                ]))

                # Sentiment Summary
                st.write("### 📈 Sentiment Overview")
                col1, col2 = st.columns(2)
                col1.metric("😊 Positive", f"{(df['sentiment_score'] > 0).sum()} comments")
                col2.metric("😡 Negative", f"{(df['sentiment_score'] < 0).sum()} comments")

                st.line_chart(df["sentiment_score"])

                # Calculate total time taken
                total_time = round(time.time() - start_time, 2)
                st.metric("⏳ Time Taken", f"{total_time} seconds")

                # Format CSV output
                csv_file = "youtube_comments.csv"
                df.to_csv(csv_file, index=False)
                with open(csv_file, "rb") as f:
                    st.download_button("📥 Download CSV Report", f, file_name="youtube_comments.csv", mime="text/csv")

            else:
                st.warning("⚠ No comments found.")
        else:
            st.error("❌ Invalid YouTube URL. Please enter a valid link.")

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
