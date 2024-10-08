import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
day_data = pd.read_csv('./dashboard/day_df.csv')
hour_data = pd.read_csv('./dashboard/hour_df.csv')

# Pemetaan tipe hari menggunakan holiday dan workingday
# Jika 'holiday' = 1 maka hari libur, jika 'workingday' = 0 maka akhir pekan, sisanya hari kerja
hour_data['day_type'] = hour_data.apply(
    lambda row: 'Holiday' if row['holiday'] == 1 else ('Weekend' if row['workingday'] == 0 else 'Working Day'), 
    axis=1
)

# Judul aplikasi dan deskripsi singkat
st.title("Analisis Data Penyewaan Sepeda")

# Sidebar untuk memilih tipe hari
st.sidebar.header("Filter Data")
day_type = st.sidebar.selectbox("Pilih Tipe Hari", options=['Semua Hari'] + list(hour_data['day_type'].unique()))

# 1. Rata-rata penyewaan sepeda berdasarkan tipe hari
st.subheader(f"Rata-rata Penyewaan Sepeda Berdasarkan Tipe Hari")

if day_type == 'Semua Hari':
    avg_rentals_by_day_type = hour_data.groupby('day_type')['cnt'].mean().reset_index()

    fig, ax = plt.subplots()
    sns.barplot(x='day_type', y='cnt', data=avg_rentals_by_day_type, palette='Blues_d', ax=ax)
    ax.set_title('Rata-rata Penyewaan Sepeda untuk Semua Tipe Hari')
    ax.set_xlabel('Tipe Hari')
    ax.set_ylabel('Rata-rata Penyewaan')
    st.pyplot(fig)
else:
    filtered_data_day = hour_data[hour_data['day_type'] == day_type]
    
    avg_rentals_by_day_type = filtered_data_day.groupby('day_type')['cnt'].mean().reset_index()

    fig, ax = plt.subplots()
    sns.barplot(x='day_type', y='cnt', data=avg_rentals_by_day_type, palette='Blues_d', ax=ax)
    ax.set_title(f'Rata-rata Penyewaan Sepeda untuk {day_type}')
    ax.set_xlabel('Tipe Hari')
    ax.set_ylabel('Rata-rata Penyewaan')
    st.pyplot(fig)

# 2. Perbandingan Pengguna Casual dan Registered
st.subheader(f"Perbandingan Pengguna Casual dan Registered Berdasarkan Tipe Hari")

if day_type == 'Semua Hari':
    avg_casual_registered_by_day_type = hour_data.groupby('day_type')[['casual', 'registered']].mean().reset_index()

    fig, ax = plt.subplots()
    avg_casual_registered_by_day_type.set_index('day_type')[['casual', 'registered']].plot(kind='bar', ax=ax, color=['skyblue', 'lightcoral'])
    ax.set_title('Perbandingan Pengguna Casual vs Registered untuk Semua Tipe Hari')
    ax.set_xlabel('Tipe Hari')
    ax.set_ylabel('Rata-rata Pengguna')
    st.pyplot(fig)
else:
    filtered_data_hour = hour_data[hour_data['day_type'] == day_type]
    
    avg_casual_registered_by_day_type = filtered_data_hour.groupby('day_type')[['casual', 'registered']].mean().reset_index()

    fig, ax = plt.subplots()
    avg_casual_registered_by_day_type.set_index('day_type')[['casual', 'registered']].plot(kind='bar', ax=ax, color=['skyblue', 'lightcoral'])
    ax.set_title(f'Perbandingan Pengguna Casual vs Registered untuk {day_type}')
    ax.set_xlabel('Tipe Hari')
    ax.set_ylabel('Rata-rata Pengguna')
    st.pyplot(fig)
