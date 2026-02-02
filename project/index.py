# importing necessary libraries
import pandas as pd
import numpy as np

data = pd.read_csv("employee_dirty_data.csv")
# print(data)

# checking missing values
print("Missing values")
print(data.head(10))

print(data.isnull().sum())

# for replacing missing value of age
# data["age"].fillna(data["age"].mean(), inplace= True) -> this method won't work in future so,
# alternative
# data["age"] = data["age"].fillna(data["age"].mean())
data.fillna({"age": data["age"].mean()}, inplace=True) # try using this one is more effetive and readable

# for replacing missing value of salary
# From the dirty CSV we’re using, salary contains:
# NaN
# inf
# -inf
# negative salaries
# possibly strings (depending on parsing)
# Pandas does NOT ignore inf when calculating the mean.

# lets convery string  into a number
data["salary"] = pd.to_numeric(data["salary"], errors="coerce")
# lets convert infinite positive and negative infinite to nan
data.replace([np.inf, -np.inf], np.nan, inplace=True)

# Now fill out the missing data by mean
data.fillna({"salary": data["salary"].mean()}, inplace=True)


# Lets try before filling out the missing value of city: clear the text
data["city"] = data["city"].str.strip().str.title() # this give you text into title form

# now lets fill out the missing names
name = data["city"].mode()[0]
data.fillna({"city": name}, inplace= True)



# for performance_rating we use differe nt approact
# lets assume
ratings = {
    'Excellent' : 5,
    'good': 4,
}
data["performance_rating"] = data["performance_rating"].replace(ratings)
data["performance_rating"] = pd.to_numeric(data["performance_rating"], errors="coerce")
data.fillna({"performance_rating": data["performance_rating"].median()}, inplace= True)

print(data["performance_rating"])

# Now lets delete the duplicate datas
data.drop_duplicates(inplace=True)


# Now deleting/managing the negataive value
data["age"] = np.where(data["age"] < 0, data["age"].mean(), data["age"])
data["salary"] = np.where(data["salary"] < 0, data["salary"].mean(), data["salary"],)

data.to_csv('cleaned_employee_data.csv', index=False)
print("data Cleaning completed")