#question 5 - create a dataframe from this link https://jsonplaceholder.typicode.com/albums
import pandas as pd
albums = requests.get("https://jsonplaceholder.typicode.com/albums").json()

df = pd.DataFrame(albums)

print(df.head())
