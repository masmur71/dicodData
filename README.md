# Dashboard Analisis Penyewaan Sepeda

## Pertanyaan
- Apakah ada perubahan pola penyewaan sepeda antara hari kerja, akhir pekan, dan hari libur?
- Apakah terdapat perbedaan jumlah penyewaan sepeda antara pengguna casual (tidak terdaftar) dan pengguna registered (terdaftar) pada hari libur, akhir pekan dan hari kerja?

## Deskripsi

Dashboard ini menampilkan analisis data penyewaan sepeda berdasarkan pembagian hari menjadi **Hari Libur**, **Akhir Pekan**, dan **Hari Kerja**. Data ini mencakup perbandingan antara penyewaan sepeda oleh pengguna **casual (tidak terdaftar)** dan **registered (terdaftar)**. 
Dashboard ini dibangun menggunakan **Streamlit**, sebuah framework Python yang memudahkan pembuatan aplikasi web interaktif.

## Fitur Utama

1. **Rata-rata Penyewaan Sepeda Berdasarkan Tipe Hari**:
   - Visualisasi ini menunjukkan rata-rata jumlah penyewaan sepeda untuk **Hari Libur**, **Akhir Pekan**, **Hari Kerja**, atau keseluruhan data pada **Semua Hari**.
   
2. **Perbandingan Pengguna Casual dan Registered**:
   - Grafik ini memperlihatkan perbandingan jumlah penyewaan antara pengguna **casual** dan **registered** berdasarkan tipe hari yang dipilih dari filter.



## Cara Menjalankan Dashboard

### 1. Instalasi Dependencies


```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pip install streamlit matplotlib seaborn pandas

```
### Run steamlit app


streamlit run dashboard/dashboard.py


### URL

https://masmurdata.streamlit.app/

