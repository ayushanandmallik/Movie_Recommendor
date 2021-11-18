#!/usr/bin/env python
# coding: utf-8

# In[84]:


import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import seaborn as sns


# In[85]:


movies= pd.read_csv(r"D:\AyushAnand\Personal_project\Movierecommendordjango\movie_recommendor\archive\movies.csv")


# In[86]:


ratings= pd.read_csv(r"D:\AyushAnand\Personal_project\Movierecommendordjango\movie_recommendor\archive\ratings.csv")


# In[87]:


movies.head()


# In[88]:


ratings.head()


# In[89]:


final_dataset= ratings.pivot(index='movieId',columns='userId',values='rating')


# In[90]:


final_dataset.head()


# In[91]:


final_dataset.fillna(0,inplace=True)


# In[92]:


final_dataset.head()


# In[93]:


no_user_voted= ratings.groupby('movieId')['rating'].agg('count')
no_movies_voted= ratings.groupby('userId')['rating'].agg('count')


# In[94]:

'''
f,ax= plt.subplots(1,1,figsize=(16,4))
#ratings['rating'].plot(kind='hist')
plt.scatter(no_user_voted.index,no_user_voted,color='mediumseagreen')
plt.axhline(y=10,color='r')
plt.xlabel('MovieId')
plt.ylabel('No. of users voted')
plt.show()'''


# In[95]:


final_dataset= final_dataset.loc[no_user_voted[no_user_voted>10].index,:]


# In[96]:

'''
f,ax= plt.subplots(1,1,figsize=(16,4))
plt.scatter(no_movies_voted.index,no_movies_voted,color='mediumseagreen')
plt.axhline(y=50,color='r')
plt.xlabel('UserId')
plt.ylabel('No. of votes by uesr')
plt.show()
'''

# In[97]:


final_dataset= final_dataset.loc[:,no_movies_voted[no_movies_voted>50].index]


# In[98]:


csr_data= csr_matrix(final_dataset.values)


# In[100]:


final_dataset.reset_index(inplace=True)
knn= NearestNeighbors(metric='cosine',algorithm='brute',n_neighbors=20,n_jobs=-1)


# In[102]:


knn= NearestNeighbors(metric='cosine',algorithm='brute',n_neighbors=20,n_jobs=-1)
knn.fit(csr_data)


# In[112]:


def get_movie_recommendation(movie_name):
    n=10
    movie_list= movies[movies['title'].str.contains(movie_name.title())]
    try:
        if len(movie_list):
            movie_idx= movie_list.iloc[0]['movieId']
            movie_idx= final_dataset[final_dataset['movieId']==movie_idx].index[0]

            distances,indices= knn.kneighbors(csr_data[movie_idx],n_neighbors=n+1)
            rec_idx= sorted(list(zip(indices.squeeze().tolist(),distances.squeeze().tolist())),key=lambda x: x[1])[:0:-1]
            recommend_frame=[]
            for val in rec_idx:
                movie_idx= final_dataset.iloc[val[0]]['movieId']
                idx= movies[movies['movieId']==movie_idx].index
                recommend_frame.append({'Title':movies.iloc[idx]['title'].values[0],'Distance':val[1],'Genre':movies.iloc[idx]['genres'].values[0]})
            df= pd.DataFrame(recommend_frame,index= range(1,n+1))
            return df
        else:
            return 'No movies found!!'
    except:
        return 'movie not in dataset...try another movie or correct movie name'

#print(get_movie_recommendation('Iron Man'))




