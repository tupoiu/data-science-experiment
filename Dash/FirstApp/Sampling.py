import pandas as pd


def create_sample_to_array(method, args, trials=10):
    data = []
    for i in range(trials):
        data.append(method(*args))
    return data


def create_sample_to_dataframe(method, args, trials=10) -> pd.DataFrame:
    data = create_sample_to_array(method, args, trials)
    df = pd.DataFrame(columns=["Result"], data=data)
    return df
