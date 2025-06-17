import pandas as pd

def condense_spreadsheet(file):
    df = pd.read_excel(file)

    # Standardize column names
    df.columns = df.columns.str.strip().str.upper()

    # Grouping and aggregation logic
    condensed = df.groupby(
        ['ELNOT', 'NOMENCLATURE', 'ALLEGIANCE CODE', 'COUNTRY CODE'],
        as_index=False
    ).agg({
        'QTY ON HAND': 'sum',
        'CONDITION OPERATIONAL STATUS': lambda x: ', '.join(sorted(set(x.dropna().astype(str)))),
        'DATE OF REVIEW': 'max'
    })

    return condensed
