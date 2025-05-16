import pandas as pd
from model.predictor import predict_winner

def test_predict_output():
    df = pd.DataFrame({
        'timestamp': [0, 1, 2],
        'horse_1': [3, 2, 1],
        'horse_2': [1, 1, 2],
        'horse_3': [2, 3, 3]
    })
    predictions = predict_winner(df.drop(columns='timestamp'))
    assert len(predictions) == 3
