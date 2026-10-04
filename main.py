import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Constants
GBP_TO_INR = 112
# Using the CLEANED dataset created previously
FILE_PATH = r'D:\Vault\Projects\steam_clean.csv'

# 1. LOAD DATA
df = pd.read_csv(FILE_PATH).head(2000)
df = df.drop_duplicates()

# Process Genre (First value only)
df['genre'] = df['genres'].str.split(';').str[0]

# Compute Rating
total_reviews = df['positive_ratings'] + df['negative_ratings']
df = df[total_reviews > 0].copy() 
df['rating'] = (df['positive_ratings'] / total_reviews) * 100

# Convert Price to INR
df['price_inr'] = df['price'] * GBP_TO_INR

# Final DataFrame
df = df[['name', 'developer', 'genre', 'price_inr', 'rating']]

# NEW ASCII ART STRING
SPLASH_SCREEN = r"""
██████╗  █████╗ ███╗   ███╗███████╗     █████╗ ███╗   ██╗ █████╗ ██╗  ██╗   ██╗███████╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔══██╗████╗  ██║██╔══██╗██║  ╚██╗ ██╔╝╚══███╔╝██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ███████║██╔██╗ ██║███████║██║   ╚████╔╝   ███╔╝ █████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██╔══██║██║╚██╗██║██╔══██║██║    ╚██╔╝   ███╔╝  ██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ██║  ██║██║ ╚████║██║  ██║███████╗██║   ███████╗███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝
"""

# MAIN MENU
while True:
    print(SPLASH_SCREEN)
    print("\n--- STEAM GAME RECOMMENDER & ANALYZER ---")
    print("1. Dataset Overview (Syllabus Check)")
    print("2. Average Price per Genre (Bar Chart)")
    print("3. Free vs Paid Games Share (Pie Chart)")
    print("4. GAME RECOMMENDER (Main Feature)")
    print("5. Exit")
    
    choice = input("\nEnter choice (1-5): ")
    
    if choice == '1':
        print("\n--- Dataset Overview ---")
        print("Shape:", df.shape)
        print("\nColumn Labels:", df.columns)
        print("\nData Types:\n", df.dtypes)
        
        # Syllabus: Series from ndarray
        stats_arr = np.array([df.shape[0], df.shape[1]])
        stats_series = pd.Series(stats_arr, index=["Total Rows", "Total Cols"])
        print("\nMetrics Series:\n", stats_series)

    elif choice == '2':
        # CHART 1: Average Price per Genre
        avg_price = df.groupby('genre')['price_inr'].mean().sort_values(ascending=False)
        print("\nAverage Price per Genre:\n", avg_price)
        
        avg_price.plot(kind='bar', color='skyblue')
        plt.title("Avg Price per Genre")
        plt.xlabel("Genre")
        plt.ylabel("Price (INR)")
        plt.legend(["Avg Price"])
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

    elif choice == '3':
        # CHART 2: Free vs Paid Games Share
        df['Payment_Type'] = df['price_inr'].apply(lambda x: 'Free' if x == 0 else 'Paid')
        payment_counts = df['Payment_Type'].value_counts()
        print("\nGame Distribution:\n", payment_counts)
        
        payment_counts.plot(kind='pie', autopct='%1.1f%%', colors=['gold', 'lightcoral'], startangle=90)
        plt.title("Share of Free vs Paid Games")
        plt.ylabel("") 
        plt.legend(payment_counts.index)
        plt.show()

    elif choice == '4':
        # MAIN FEATURE: RECOMMENDER
        print("\n--- Game Recommender ---")
        
        available_genres = df['genre'].unique()
        min_price = df['price_inr'].min()
        max_price = df['price_inr'].max()
        
        print(f"Available Genres: {', '.join(available_genres)}")
        u_genre = input("Enter Genre: ")
        
        print(f"Price Range: ₹{min_price:.2f} to ₹{max_price:.2f}")
        u_budget = float(input("Enter Max Budget in INR: "))
        
        results = df[(df['genre'] == u_genre) & (df['price_inr'] <= u_budget)]
        results = results.sort_values(by='rating', ascending=False).head(10)
        
        if results.empty:
            print("\nNo games found. Try increasing your budget.")
        else:
            print("\nTop 10 Highest-Rated Games for you:")
            print(results[['name', 'price_inr', 'rating']])
            
            results.plot(kind='bar', x='name', y='rating', color='green')
            plt.title(f"Best {u_genre} Games within Budget")
            plt.ylabel("Rating %")
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()

    elif choice == '5':
        print("Exiting... Thank you!")
        break
    
    else:
        print("Invalid choice! Please try again.")