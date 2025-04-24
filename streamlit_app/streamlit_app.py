
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
st.title("🔍 Intelligent Material Discovery Dashboard")
st.markdown("Filter and visualize materials based on multi-criteria scoring and physical properties.")

@st.cache_data
def load_data():
    return pd.read_csv("data/materials_combined_dataset.csv")

df = load_data()

# Sidebar filter options
st.sidebar.header("🔧 Filters")
target_property = st.sidebar.selectbox("Select property to sort by", df.columns[df.dtypes != 'object'])

min_val = float(df[target_property].min())
max_val = float(df[target_property].max())
val_range = st.sidebar.slider(f"Filter range for {target_property}", min_val, max_val, (min_val, max_val))
filtered_df = df[(df[target_property] >= val_range[0]) & (df[target_property] <= val_range[1])]

# Show filtered table
st.subheader("📊 Filtered Material Table")
st.dataframe(filtered_df.sort_values(by=target_property, ascending=False).reset_index(drop=True))

# Plot top materials
st.subheader("📈 Top Materials by Selected Property")
top_n = st.slider("Number of top materials to show", 5, 30, 10)
top_df = filtered_df.sort_values(by=target_property, ascending=False).head(top_n)

fig, ax = plt.subplots()
ax.barh(top_df["Material"], top_df[target_property], color='skyblue')
ax.set_xlabel(target_property)
ax.set_ylabel("Material")
ax.invert_yaxis()
ax.set_title(f"Top {top_n} Materials by {target_property}")
st.pyplot(fig)

# Export option
st.download_button("📥 Download Filtered Data", filtered_df.to_csv(index=False), file_name="filtered_materials.csv")
