import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
day_data = pd.read_csv('./dashboard/day_df.csv')
hour_data = pd.read_csv('./dashboard/hour_df.csv')

# Streamlit title and description
st.title("Bike Sharing Data Analysis")


# Sidebar for data filtering
st.sidebar.header("Filter Data")
day_type = st.sidebar.selectbox("Pilih Tipe Hari", options=day_data['day_type'].unique())

# 1. Average rentals by day type - Filter based on user selection
st.subheader(f"Rata-rata Penyewaan Sepeda untuk '{day_type}'")
filtered_data_day = day_data[day_data['day_type'] == day_type]
avg_rentals_by_day_type = filtered_data_day.groupby('day_type')['cnt'].mean().reset_index()

fig, ax = plt.subplots()
sns.barplot(x='day_type', y='cnt', data=avg_rentals_by_day_type, palette='Blues_d', ax=ax)
ax.set_title(f'Average Bike Rentals for {day_type}')
ax.set_xlabel('Day Type')
ax.set_ylabel('Average Rentals')
st.pyplot(fig)

# 2. Casual vs Registered Users - Filter based on user selection
st.subheader(f"Perbandingan Pengguna Casual dan Registered pada '{day_type}'")
hour_data['day_type'] = hour_data.apply(lambda row: 'Holiday' if row['holiday'] == 1 else ('Weekend' if row['workingday'] == 0 else 'Working Day'), axis=1)
filtered_data_hour = hour_data[hour_data['day_type'] == day_type]
avg_casual_registered_by_day_type = filtered_data_hour.groupby('day_type')[['casual', 'registered']].mean().reset_index()

fig, ax = plt.subplots()
avg_casual_registered_by_day_type.set_index('day_type')[['casual', 'registered']].plot(kind='bar', ax=ax, color=['skyblue', 'lightcoral'])
ax.set_title(f'Average Bike Rentals for {day_type}')
ax.set_xlabel('Day Type')
ax.set_ylabel('Average Rentals')
st.pyplot(fig)
