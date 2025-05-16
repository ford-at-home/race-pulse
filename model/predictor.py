from model.features import extract_features

def predict_winner(df):
    features = extract_features(df)
    predictions = []
    for t in range(len(features)):
        # Simplified: horse in lead at time t
        current = features.iloc[t]
        lead_horse = current.idxmin()
        lead_confidence = 0.6  # Placeholder confidence
        predictions.append((t, lead_confidence))
    return predictions
