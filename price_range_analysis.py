
import pandas as pd

import matplotlib.pyplot as plt


# ---------------- LOAD DATASET ---------------- #

data = pd.read_csv(

    "restaurant_data.csv",

    encoding='utf-8-sig'
)

print("\nDATASET PREVIEW:\n")

print(data.head())


# ---------------- HANDLE MISSING VALUES ---------------- #

data = data.dropna()


# ---------------- MOST COMMON PRICE RANGE ---------------- #

price_counts = data['Price range'].value_counts()

most_common_price = price_counts.idxmax()

print("\nMOST COMMON PRICE RANGE:\n")

print(

    f"Price Range {most_common_price}"
)


print("\nPRICE RANGE COUNTS:\n")

print(price_counts)


plt.figure(figsize=(8, 5))

price_counts.plot(

    kind='bar'
)

plt.title(

    "Restaurant Count by Price Range"
)

plt.xlabel(

    "Price Range"
)

plt.ylabel(

    "Number of Restaurants"
)

plt.tight_layout()

plt.show()


# ---------------- AVERAGE RATING BY PRICE RANGE ---------------- #

average_ratings = data.groupby(

    'Price range'

)['Aggregate rating'].mean()

print("\nAVERAGE RATING BY PRICE RANGE:\n")

print(average_ratings)


plt.figure(figsize=(8, 5))

average_ratings.plot(

    kind='bar'
)

plt.title(

    "Average Rating by Price Range"
)

plt.xlabel(

    "Price Range"
)

plt.ylabel(

    "Average Rating"
)

plt.tight_layout()

plt.show()


# ---------------- HIGHEST RATED PRICE RANGE COLOR ---------------- #

rating_by_color = data.groupby(

    'Rating color'

)['Aggregate rating'].mean().sort_values(

    ascending=False
)

highest_color = rating_by_color.idxmax()

highest_rating = rating_by_color.max()

print("\nRATING COLOR ANALYSIS:\n")

print(rating_by_color)


print("\nHIGHEST AVERAGE RATING COLOR:\n")

print(

    f"{highest_color} "

    f"with average rating "

    f"{highest_rating:.2f}"
)


plt.figure(figsize=(8, 5))

rating_by_color.plot(

    kind='bar'
)

plt.title(

    "Average Rating by Rating Color"
)

plt.xlabel(

    "Rating Color"
)

plt.ylabel(

    "Average Rating"
)

plt.tight_layout()

plt.show()


# ---------------- FINAL INSIGHTS ---------------- #

print("\nFINAL INSIGHTS:\n")

print(

    "Some price ranges are more common "
    "than others among restaurants."
)

print(

    "Average ratings vary across "
    "different price categories."
)

print(

    "Certain rating colors represent "
    "higher average restaurant ratings."
)

print(

    "Mid-range restaurants often dominate "
    "the dataset."
)

