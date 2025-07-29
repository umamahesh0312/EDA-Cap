import pandas as pd

def clean_data(input_file='laptops_raw.csv', output_file='laptops_cleaned.csv'):
    try:
        df = pd.read_csv(input_file)

        # Clean price column
        df['Price'] = df['Price'].replace('[^\d.]', '', regex=True).astype(float)

        # Drop rows with missing values (if any)
        df = df.dropna()

        # Save cleaned data
        df.to_csv(output_file, index=False)
        return df

    except FileNotFoundError:
        return None
