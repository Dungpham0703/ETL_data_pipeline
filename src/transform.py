def transform_data(df):

    df.rename(columns={
        "userId": "user_id",
        "movieId": "movie_id"
    }, inplace=True)

    df = df.dropna()
    
    df["rating"] = df["rating"].astype(float)

    df["liked"] = df["rating"].apply(lambda x: 1 if x >= 4 else 0)
    
    print('Transform data successfully')
    return df
