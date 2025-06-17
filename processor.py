import pandas as pd

def condense_spreadsheet(file):
    df = pd.read_excel(file)

    # Standardize column names
    df.columns = df.columns.str.strip().str.upper()

    # Identify grouping columns: all except 'QTY ON HAND'
    group_cols = [col for col in df.columns if col != 'QTY ON HAND']

    # Group only exact duplicates (all columns except quantity), and sum QTY ON HAND
    condensed = df.groupby(group_cols, as_index=False)['QTY ON HAND'].sum()

    return condensed
