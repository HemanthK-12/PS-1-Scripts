import pandas as pd
df = pd.read_csv('paste this file in the same folder as the list of stations file,right click and select copy relative path and paste it here')
mask1 = df['Discipline'].apply(lambda x: ('A7' in str(x))or('Any' in str(x)))#this will check all the blocks in the Discipline column and return True if it contains A7 or Any
df = df[mask1]#this will delete all the remaining rows that are False
df.to_csv('A7_Onsite_AND_Online.csv', index=False)
mask2 = df['Mode of PS'].apply(lambda x:('Online' in str(x)))#now this will check online ps stations
df = df[mask2]
df.to_csv('A7_Only_Online.csv', index=False)