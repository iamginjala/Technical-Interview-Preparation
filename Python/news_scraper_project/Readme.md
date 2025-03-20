# 📰 News Headline Scraper

A simple Python script that scrapes the latest news headlines from **BBC News** and saves them to a CSV file with their corresponding URLs.

---

## 🚀 Features
✅ Scrapes top news headlines from BBC News  
✅ Saves the headlines along with URLs to a CSV file  
✅ Displays the results in the terminal  
✅ Uses dynamic HTML parsing for reliability  
✅ Simple and easy to use  

---

## 📦 Requirements
Make sure you have **Python 3+** installed. Then, install the required libraries using:

```sh
pip install beautifulsoup4 requests
```

---

## 🔧 How to Use
1️⃣ Clone this repository:
```sh
git clone https://github.com/iamginjala/news-headline-scraper.git
```

2️⃣ Navigate to the project folder:
```sh
cd news-headline-scraper
```

3️⃣ Run the script:
```sh
python news_scraper.py
```

4️⃣ The script will:
   - Fetch the latest headlines and their URLs from BBC News
   - Display them in the terminal
   - Save them to `news_headlines.csv`

---

## 📂 Output Example
```
Latest News Headlines:
1. UK economy rebounds stronger than expected - https://www.bbc.com/news/example1
2. Scientists discover new exoplanet with potential life - https://www.bbc.com/news/example2
3. AI advancements reshape medical research - https://www.bbc.com/news/example3
...

✅ Headlines saved to 'news_headlines.csv'!
```

---

## 📜 File Structure
```
📂 news-headline-scraper
 ├── news_scraper.py   # Main Python script
 ├── news_headlines.csv # Output file (auto-generated)
 ├── README.md         # Project documentation
```

---

## 🛠️ Future Enhancements
🔹 Allow scraping from multiple news sources  
🔹 Add a GUI interface  
🔹 Store results in a database  

---

## 📜 License
Feel free to use and modify it. 😊

