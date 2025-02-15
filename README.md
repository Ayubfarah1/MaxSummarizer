# **YouTube Transcript Summarizer**
A **Chrome extension** that extracts and summarizes YouTube video transcripts using **Flask, Hugging Face NLP models, and youtube-transcript-api**. This tool helps users quickly understand YouTube videos without watching the entire content.

---

## **🚀 Features**
✔ Extracts **YouTube transcripts** automatically.  
✔ Summarizes long transcripts into **concise, easy-to-read summaries**.  
✔ **Displays the summary inside the Chrome extension popup** for convenience.  
✔ Uses **Flask API + Hugging Face Transformers** for **NLP-based text summarization**.  
✔ Handles **character tokenization limits** and optimizes text processing.  

---

## **🛠 Prerequisites (Before Running the Application)**
Make sure you have the following installed on your system:

### **1️⃣ Install Python (if not already installed)**
Download and install Python (3.8+ recommended) from:  
🔗 [Python Download](https://www.python.org/downloads/)

### **2️⃣ Install Required Dependencies**  
Run the following command in your terminal:
```bash
pip install flask flask-cors 

pip install youtube-transcript-api transformers 

pip install torch torchvision torchaudio

pip install tf-keras

pip install transformers
```
### 3️⃣ Install Google Chrome (for Extension)
Download and install Google Chrome (if not already installed)



## 🔧 How to Set Up & Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Youtube-Transcript-Summarizer.git

cd Youtube-Transcript-Summarizer
```

### 2️⃣ Start the Flask Backend
Run the following command to start the Flask API:
```bash
python app.py
```

The API will start on: http://127.0.0.1:5000/

### 3️⃣ Load the Chrome Extension

- Open Google Chrome.
- Go to chrome://extensions/.
- Enable Developer Mode (toggle in the top-right).
- Click Load Unpacked and select the /extension folder from this project.
- The YouTube Transcript Summarizer extension will now be installed.


### 4️⃣ Using the Extension

- Open YouTube and play any video.

- Click on the YouTube Transcript Summarizer extension icon.

- Click "Summarize" → It will fetch the transcript and generate a summary.

- The summary will be displayed inside the extension popup.


## 🐞 Troubleshooting

### Error: API not responding

- Ensure that Flask is running (python app.py).

- Check that the API is available at http://127.0.0.1:5000/.

- Restart the Flask server and try again.

### Error: CORS issue (Chrome extension not connecting to API)

- Install Flask-CORS:
 ```bash
 pip install flask-cors
```

### Error: Summarization is too slow

- Try a smaller NLP model like sshleifer/distilbart-cnn-6-6 instead of facebook/bart-large-cnn.

- Reduce the text chunk size before sending it to the summarization model.



## 📌 Future Improvements

✅ Improve summary readability with bullet points & formatting.

✅ Optimize speed by using smaller NLP models.

✅ Deploy API to cloud services for remote access.

✅ Enhance UI/UX in the Chrome extension.

✅ Implement copy-to-clipboard functionality for easy summary sharing.

✅ Add a retry button in case of failed  summarization attempts.

✅ Introduce a toggle for summary length (short, medium, detailed).


## 🤝 Contributing

- Fork the repo

- Create a new branch (git checkout -b feature-name)

- Commit changes (git commit -m "Add new feature")

- Push to your branch (git push origin feature-name)

- Open a Pull Request


