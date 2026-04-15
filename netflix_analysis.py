#   NETFLIX DATA ANALYSIS

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r'C:\Users\Jhanvi Sharma\Downloads\archive.zip')
print(df.head())

#CHECKING FOR MISSING VALUES
print(df.isnull().sum())

#FILLING MISSING VALUES
df["director"].fillna("Unknown",inplace=True)
df["cast"].fillna("Unknown",inplace=True)
df["country"].fillna("Unknown",inplace=True)
df.dropna(subset=["rating"],inplace=True)
print(df.isnull().sum())

#DISTRIBUTION OF MOVIES AND TV SHOWS
sns.countplot(x="type",data=df)
plt.title("Distribution of Movies and TV Shows")
plt.savefig("content_distribution.png")
plt.show()

#WHICH COUNTRIES HAVE THE MOST CONTENT
top_countries=df["country"].value_counts().head(10)
sns.barplot(x=top_countries.index,y=top_countries.values)
plt.title("Top 10 Countries with Most Content")
plt.xlabel("Country")
plt.ylabel("Number of Content Items")
plt.xticks(rotation=45)
plt.savefig("top_countries.png")
plt.show()

#DISTRIBUTION OF CONTENT BY YEAR ADDED
df["year"]=df["date_added"].str.extract(r'(\d{4})').astype(float)
sns.countplot(x="year",data=df)
plt.title("Distribution of Content by Year Added")
plt.xlabel("Year")
plt.ylabel("Number of Content Items")
plt.xticks(rotation=45)
plt.savefig("content_by_year.png")
plt.show()

#Rating distribution
sns.countplot(x="rating",data=df)
plt.title("Distribution of Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Content Items")
plt.xticks(rotation=45)
plt.savefig("rating_distribution.png")
plt.show()
