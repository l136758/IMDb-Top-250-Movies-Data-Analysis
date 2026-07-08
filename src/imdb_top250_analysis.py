import pandas as pd
import matplotlib.pyplot as plt


# Task 1: Reading the csv file that contains the dataset
data = pd.read_csv("IMDB Top 250 Movies.csv",
                   na_values=["Not Available", 
                              "Unrated", "Not Rated"],
                   thousands=',')

print("**** file is loaded!!****")

# Task 2: Displaying basic statistics using the following functions
print("\nThe First 5 Rows of the Data:: \n")   
print(data.head())

print("\nData Info: ")   
print(data.info())  
 
print("\nData Description: \n")   
print(data.describe())

# Task 3: Checking and Handling missing data
print("Counting all the missing values :\n\n",data.isna().sum())

data['box_office'] = pd.to_numeric(data['box_office'],errors = 'coerce')
data['box_office']= data['box_office'].fillna(data['box_office'].mean())

data['budget']= data['budget'].str.replace('$','')
data['budget'] = pd.to_numeric(data['budget'],errors = 'coerce')
data['budget']= data['budget'].fillna(data['budget'].mean())

data["run_time"] = data["run_time"].fillna("Unknown")

data["certificate"] = data["certificate"].fillna("Unknown")

print("Counting all the missing values after handling them :\n\n"
      ,data.isna().sum())

# Task 5: Creative Implementation
# Number.1
data['movie_age'] = data['year'].apply(lambda x: 'New' if x >= 2010 else 'Old')
print("Determining whether a movie is considered old or new: \n",data["movie_age"])

# Number.2
data["main_genre"] = data["genre"].apply(lambda x: x.split(",")[0] if pd.notna(x)
                                         else "Unknown")
grouped_data = data.groupby('main_genre')  
genre_rating = grouped_data["rating"].mean().sort_values(ascending=False)

print("\n",genre_rating)

# Task 4: Bar - Visualization
genre_boxOffice = grouped_data['box_office'].mean()
genre_boxOffice = genre_boxOffice.sort_values(ascending=False)
genre_boxOffice.plot.bar()
plt.title('Average Box Office per Genre')
plt.xlabel('Genre')
plt.ylabel('Average Box Office')
plt.savefig('BoxOfficeGenre.png', dpi=400)
plt.show()

# Task 4: Histogram - Visualization
data["rating"].plot.hist(bins=10, edgecolor='black', figsize=(8,5), 
                         title="Distribution of Movie Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Movies")
plt.savefig('MovieRatings.png', dpi=400)
plt.show()

# Task 4: Line Plot - Visualization
avg_rating = data.groupby('year')['rating'].mean()

plt.figure(figsize=(15, 7))
plt.plot(avg_rating, color='steelblue')  
plt.title('Average Movie Ratings Over the Years', fontname='Times New Roman'
          , fontsize=16)
plt.xlabel('Year', fontname='Times New Roman', fontsize=15)
plt.ylabel('Average IMDB Rating', fontname='Times New Roman', fontsize=15)
plt.savefig('AvgRatingOverYears.png', dpi=400)
plt.show()

 
# Saving a clean CSV with all the changes
data.to_csv('CleanedResult.csv', index=False)
print("The final result has been saved!")

