import pandas as pd

def condense_spreadsheet(file):
    df = pd.read_excel(file)

    # Clean column names
    df.columns = df.columns.str.strip().str.upper()

    # Define group columns (exclude QTY ON HAND and DATE OF REVIEW)
    group_cols = [col for col in df.columns if col not in ['QTY ON HAND']

    # Aggregate QTY ON HAND and DATE OF REVIEW
    condensed = df.groupby(group_cols, as_index=False).agg({
        'QTY ON HAND': 'sum',
        
    })

    return condensed
