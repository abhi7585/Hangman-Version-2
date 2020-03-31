import pandas as pd
import numpy as np
import random

# Reading data set
df1 = pd.read_csv('./data/wordsDataSet.csv')
# Removed Count coloumn as it was not required
df1 = df1.drop('count', 1)
# Added length column to remove words with small length
df1['length'] = df1.word.str.len()
df1 = df1[df1.length > 6.0]

df2 = pd.read_csv('./data/CountriesName.csv')
# Removing irrelevant columns
df2.drop(['Region', 'Population', 'Area (sq. mi.)', 'Pop. Density (per sq. mi.)', 'Coastline (coast/area ratio)', 'Net migration', 'Infant mortality (per 1000 births)', 'GDP ($ per capita)',
          'Literacy (%)', 'Phones (per 1000)', 'Arable (%)', 'Crops (%)', 'Other (%)', 'Climate', 'Birthrate', 'Deathrate', 'Agriculture', 'Industry', 'Service'], axis=1, inplace=True)

# Removing irrelevant columns
df3 = pd.read_csv('./data/ColorNames.csv')
df3.drop(['hex_24_bit', 'red_8_bit', 'green_8_bit', 'blue_8_bit',
          'hue_degrees', 'hsl_s', 'hsl_l'], axis=1, inplace=True)

# To keep track of used words
usedWord = np.empty(1, str)

# Converting the DataFrame to numpy
wordArray = df1[['word']].to_numpy()
countriesArray = df2[['Country']].to_numpy()
colorArray = df3[['name']].to_numpy()


def get_word(category):
    if category == 1:
        getWord = ''.join(random.choice(wordArray))
        while (getWord in usedWord):
            # Generating another word as the fetched word has been used before
            getWord = ''.join(random.choice(wordArray))
        return getWord.lower()
    elif category == 2:
        getWord = ''.join(random.choice(countriesArray))
        while (getWord in usedWord):
            # Generating another word as the fetched word has been used before
            getWord = ''.join(random.choice(countriesArray))
        return getWord.lower()
    elif category == 3:
        getWord = ''.join(random.choice(colorArray))
        while (getWord in usedWord):
            # Generating another word as the fetched word has been used before
            getWord = ''.join(random.choice(colorArray))
        return getWord.lower()
