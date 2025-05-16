def extract_features(df):
    # Example: calculate position changes, velocity, acceleration
    df['pos_change'] = df.diff()
    return df.fillna(0)
