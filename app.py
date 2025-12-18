import streamlit as st
import pandas as pd

# =================================================
# PAGE CONFIGURATION
# =================================================
st.set_page_config(
    page_title="Niṣedha Explorer – Classical Prohibitions as per Charaka Samhita",
    layout="wide"
)

# =================================================
# TITLE & INTRODUCTION
# =================================================
st.markdown(
    "<h2>Niṣedha Explorer – Classical Prohibitions as per Charaka Samhita</h2>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='font-size:16px;'>Structured exploration of Niṣedha based strictly on Charaka Samhita</p>",
    unsafe_allow_html=True
)

st.divider()

# =================================================
# LOAD EXCEL DATA (DEVANĀGARĪ SAFE)
# =================================================
@st.cache_data
def load_data():
    try:
        df = pd.read_excel(
            "data/Charaka_Nishedas.xlsx",
            engine="openpyxl"
        )

        # Enforce internal canonical column order
        df.columns = [
            "No",
            "Sthana",
            "Chapter",
            "Sloka",
            "Sloka_Text",
            "Meaning",
            "Category",
            "Remarks"
        ]

        return df

    except FileNotFoundError:
        st.error("❌ Excel file not found. Ensure 'Charaka_Nishedas.xlsx' is inside the data folder.")
        st.stop()

    except Exception as e:
        st.error(f"❌ Error reading Excel file: {e}")
        st.stop()

df = load_data()

# =================================================
# FILTER SECTION (BOTH MANDATORY)
# =================================================
st.subheader("Niṣedha Exploration Filters")

# -----------------------------
# Step 1: Sthāna Selection
# -----------------------------
sthana_list = sorted(df["Sthana"].dropna().unique())

selected_sthana = st.multiselect(
    "Step 1: Select one or more **Sthāna** (mandatory)",
    sthana_list
)

# -----------------------------
# Step 2: Domain Selection
# -----------------------------
category_list = sorted(df["Category"].dropna().unique())

selected_category = st.multiselect(
    "Step 2: Select one or more **Niṣedha Domains** (mandatory)",
    category_list
)

st.divider()

# =================================================
# APPLY FILTERS (STRICT LOGIC)
# =================================================
if not selected_sthana or not selected_category:
    st.warning(
        "Please select **at least one Sthāna** AND **at least one Niṣedha domain** "
        "(Āhāra / Vihāra / Ācāra / Vicāra) to view results."
    )
    result_df = pd.DataFrame()  # intentionally empty
else:
    result_df = df[
        (df["Sthana"].isin(selected_sthana)) &
        (df["Category"].isin(selected_category))
    ]

# =================================================
# OUTPUT SECTION
# =================================================
st.subheader("Niṣedha References")

if result_df.empty and selected_sthana and selected_category:
    st.info("No Niṣedha entries found for the selected combination.")
elif not result_df.empty:
    st.markdown(
        f"<p><b>Total Niṣedhas found:</b> {len(result_df)}</p>",
        unsafe_allow_html=True
    )

    for _, row in result_df.iterrows():
        st.markdown(
            f"### 📘 {row['Sthana']} / {row['Chapter']} / {row['Sloka']}"
        )

        st.markdown(
            f"**Śloka (Devanāgarī):**  \n{row['Sloka_Text']}"
        )

        st.markdown(
            f"**Meaning:**  \n{row['Meaning']}"
        )

        st.markdown(
            f"**Niṣedha Domain:**  \n{row['Category']}"
        )

        st.markdown(
            f"**Statement of Prohibition:**  \n{row['Remarks']}"
        )

        st.markdown("---")

# =================================================
# FOOTER
# =================================================
st.markdown(
    """
    <hr>
    <p style="text-align:center; font-size:14px;">
    Data compiled and App developed by <b>Prof.(Dr.) Prasanna Kulkarni</b>
    </p>
    """,
    unsafe_allow_html=True
)
