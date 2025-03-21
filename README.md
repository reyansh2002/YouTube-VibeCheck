# 📊 YouTube Sentiment Analysis

Analyze YouTube video comments, generate sentiment insights, and visualize data in real-time using **Streamlit, Google YouTube API, and TextBlob**.

![YouTube Sentiment Analysis](https://img.shields.io/badge/YouTube-Sentiment%20Analysis-blue?style=for-the-badge&logo=youtube)
![Streamlit](https://img.shields.io/badge/Streamlit-Powered-red?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-brightgreen?style=for-the-badge)

---

## 🚀 Features
✅ **Fetch Comments** – Retrieves all comments from any YouTube video.  
✅ **Sentiment Analysis** – Classifies comments as **Positive 😊, Negative 😡, or Neutral 😐**.  
✅ **Real-time Visualizations** – View sentiment trends with a **line chart**.  
✅ **CSV Export** – Download analyzed results for offline use.  
✅ **Modern UI** – Built with **Streamlit** for a sleek and user-friendly experience.  
✅ **Supports YouTube Shorts & Regular Videos**.  

---

## 📷 Screenshots
### **Home Screen**
![Home Screen](screenshots/home_screen.png)

### **Sentiment Analysis Results**
![Sentiment Analysis](screenshots/sentiment_results.png)

### **Graphical Representation**
![Graph Output](https://github.com/reyansh2002/YouTube-VibeCheck/blob/main/Graph%20Output.png)

(Ensure you upload these screenshots to your GitHub repository.)

---

## 📦 Installation
### 🔧 Prerequisites
Ensure you have **Python 3.8+** installed. Then, install the required libraries:

```bash
pip install -r requirements.txt
```

### 🔑 Set Up Your YouTube API Key
1. Create a `.env` file in the root directory.  
2. Add your **YouTube API Key** inside:  

```plaintext
YOUTUBE_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application
Launch the **Streamlit** app by running:

```bash
streamlit run streamlit_app.py
```

This will start a local server, and you can access the app in your browser.

---

## 📁 Project Structure
```
📂 YouTube-Sentiment-Analysis
│── .env                      # Stores API Key
│── streamlit_app.py           # Main Streamlit app
│── youtube_sentiment.py       # Functions for fetching & analyzing comments
│── youtube_comments.csv       # Example CSV output
│── requirements.txt           # Python dependencies
│── README.md                  # Documentation
│── screenshots/               # Screenshots for README
```

---

## 🔍 How It Works
### 1️⃣ Fetching Comments  
- Uses the **YouTube API** to fetch all comments.  
- Extracts **author name, comment text, and timestamp**.  

### 2️⃣ Sentiment Analysis  
- Uses **TextBlob** to analyze sentiment.  
- Assigns a **sentiment score** between **-1 (Negative) and +1 (Positive)**.  
- Labels comments as **Positive 😊, Neutral 😐, or Negative 😡**.  

### 3️⃣ Visualization & Export  
- Displays results in a **Streamlit DataFrame**.  
- Generates a **line chart** of sentiment scores.  
- Allows **CSV export** for further analysis.  

---

## 🛠️ Technologies Used
- **Python 3.8+**
- **Streamlit** – Frontend UI  
- **Google YouTube API v3** – Fetching video comments  
- **TextBlob** – Sentiment analysis  
- **Pandas** – Data processing  
- **dotenv** – Secure API key handling  

---

