import streamlit as st
from mongodb import fetch_data
from data_processing import clean_data
from visualizations import create_heatmap, create_map

def main():
    st.title('Crime Data Visualization Dashboard')

    # Fetch and clean data
    df = fetch_data()
    df = clean_data(df)

    # Create visualizations
    heatmap_fig = create_heatmap(df)
    map_fig = create_map(df)

    # Display visualizations
    st.plotly_chart(heatmap_fig)
    st.plotly_chart(map_fig)

if __name__ == "__main__":
    main()
