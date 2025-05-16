import argparse
import pandas as pd
from model.predictor import predict_winner
from utils.preprocess import preprocess_data

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    processed = preprocess_data(df)
    predictions = predict_winner(processed)

    for timestamp, prob in predictions:
        print(f"At t={timestamp}s, top horse win probability: {prob:.2%}")
