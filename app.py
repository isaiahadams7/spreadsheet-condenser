import streamlit as st
import pandas as pd
from io import BytesIO
from processor import condense_spreadsheet

st.set_page_config(page_title="Spreadsheet Condenser", layout="centered")
st.title("📊 Spreadsheet Condenser Tool")

uploaded_file = st.file_uploader("Upload a spreadsheet (.xlsx)", type=["xlsx"])

if uploaded_file:
    st.success("✅ File uploaded successfully!")

    st.markdown("⏳ Condensing entries... Please wait a moment.")
    condensed_df = condense_spreadsheet(uploaded_file)

    st.success("🎉 Done! Your spreadsheet has been condensed successfully.")
    st.markdown(
        "**What's been done:** Rows with identical data (except for Quantity and Review Date) were combined. "
        "Quantities were summed, and the most recent review date kept."
    )

    st.dataframe(condensed_df)

    # Create downloadable Excel file
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        condensed_df.to_excel(writer, index=False, sheet_name='Condensed')
    output.seek(0)

    st.download_button(
        label="📥 Download Condensed Spreadsheet",
        data=output,
        file_name="condensed_output.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
