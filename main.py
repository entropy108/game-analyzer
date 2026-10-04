import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Constants
GBP_TO_INR = 112
# CSV Directory
FILE_PATH = r'D:\Vault\Projects\steam_clean.csv'

# 1. LOAD DATA (Limit to 2000 rows from the clean pool)
df = pd.read_csv(FILE_PATH).head(2000)
df = df.drop_duplicates()

# Process Genre (First value only)
df['genre'] = df['genres'].str.split(';').str[0]

# Compute Rating: (pos / (pos + neg)) * 100
total_reviews = df['positive_ratings'] + df['negative_ratings']
df = df[total_reviews > 0].copy() 
df['rating'] = (df['positive_ratings'] / total_reviews) * 100

# Convert Price to INR
df['price_inr'] = df['price'] * GBP_TO_INR

# Final DataFrame for the project
df = df[['name', 'developer', 'genre', 'price_inr', 'rating']]

# MAIN MENU
while True:
    print("\n--- STEAM GAME RECOMMENDER & ANALYZER ---")
    print("1. Dataset Overview (Syllabus Check)")
    print("2. Average Price per Genre (Analysis)")
    print("3. GAME RECOMMENDER (Main Feature)")
    print("4. Exit")
    
    choice = input("Enter choice (1-4): ")
    
    if choice == '1':
        # Syllabus: Row/Col labels, dtypes, shape, and Series from ndarray
        print("\n--- Dataset Overview ---")
        print("Shape:", df.shape)
        print("\nColumn Labels:", df.columns)
        print("\nData Types:\n", df.dtypes)
        
        # Series from ndarray example for syllabus
        stats_arr = np.array([df.shape[0], df.shape[1]])
        stats_series = pd.Series(stats_arr, index=["Total Rows", "Total Cols"])
        print("\nMetrics Series:\n", stats_series)

    elif choice == '2':
        # Syllabus: Groupby and Bar Plot
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
        # MAIN FEATURE: RECOMMENDER
        print("\n--- Game Recommender ---")
        
        # Dynamic Guidance
        available_genres = df['genre'].unique()
        min_price = df['price_inr'].min()
        max_price = df['price_inr'].max()
        min_rat = df['rating'].min()
        max_rat = df['rating'].max()
        
        print(f"Available Genres: {', '.join(available_genres)}")
        u_genre = input("Enter Genre: ")
        
        print(f"Price Range: ₹{min_price:.2f} to ₹{max_price:.2f}")
        u_budget = float(input("Enter Max Budget in INR: "))
        
        print(f"Rating Range: {min_rat:.2f}% to {max_rat:.2f}%")
        u_rating = float(input("Enter Minimum Rating %: "))
        
        # Filtering
        results = df[(df['genre'] == u_genre) & 
                    (df['price_inr'] <= u_budget) & 
                    (df['rating'] >= u_rating)]
        
        # Ranking
        results = results.sort_values(by='rating', ascending=False).head(10)
        
        if results.empty:
            print("\nNo games found matching your criteria. Try increasing budget or lowering rating.")
        else:
            print("\nTop 10 Recommended Games:")
            print(results[['name', 'price_inr', 'rating']])
            
            # Result plot
            results.plot(kind='bar', x='name', y='rating', color='green')
            plt.title(f"Top {u_genre} Games within Budget")
            plt.ylabel("Rating %")
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()

    elif choice == '4':
        print("Exiting... Thank you!")
        break
    
    else:
        print("Invalid choice! Please try again.")