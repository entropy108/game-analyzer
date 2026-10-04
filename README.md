# game-analyzer

+# 🎮 Steam Games Market Analyzer & Recommender
+
+This is a Python-based project created for my **Class 12 Informatics Practices (IP)** board project. The goal was to build a tool that analyzes a Steam games dataset and helps users find the best games based on their budget and preferred genre.
+
+## 📌 What this project does
+The program is a menu-driven application that uses a Kaggle dataset of Steam games. It provides a few different ways to look at the data and a recommendation system to find high-rated games.
+
+### Main Features:
+- **Dataset Overview:** Shows the basic structure of the data (shape, dtypes, and column labels).
+- **Price Analysis:** A bar chart showing the average price of games across different genres.
+- **Market Share:** A pie chart showing the ratio of Free vs. Paid games on the platform.
+- **Smart Recommender:** The user enters a genre and a budget (in INR), and the program suggests the top 10 highest-rated games that fit those criteria.
+
+## 🛠️ Tech Stack
+- **Language:** Python
+- **Libraries:** 
+  - `pandas`: For data cleaning and manipulation.
+  - `matplotlib`: For creating the analysis charts.
+  - `numpy`: For numerical operations and series creation.
+
+## 📚 CBSE Syllabus Coverage
+This project demonstrates the following concepts from the IP syllabus:
+- Creating pandas Series from dictionaries and ndarrays.
+- DataFrame manipulation (filtering, sorting, and cleaning).
+- Using `groupby` for data aggregation.
+- Data visualization using `matplotlib` (Bar and Pie charts).
+- Handling CSV files (importing and exporting data).
+
+## 🚀 How to run it
+1. Make sure you have the `steam_clean.csv` file in the project folder.
+2. Install the required libraries:
+   ```bash
+   pip install pandas matplotlib numpy
+   ```
+3. Run the script:
+   ```bash
+   python main.py
+   ```
+
+## 📝 Credits
+- **Dataset:** Sourced from Kaggle (Steam Store Games Dataset).
+- **Development:** Built as a team project for the Class 12 IP practicals.
