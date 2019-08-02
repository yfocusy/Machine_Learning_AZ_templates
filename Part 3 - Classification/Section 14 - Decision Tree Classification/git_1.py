import numpy as np
import pandas as pd


moviesPath = './data/ml-latest-small/movies.csv'
names = ['user_id', 'item_id', 'rating', 'timestamp']
#df_movie =pd.read_csv(moviesPath, sep='\t', names=names)
#df_movie.head()


moviesDF = pd.read_csv(moviesPath,index_col=None)
df_movie.head(5)