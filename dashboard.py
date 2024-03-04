# Import Packages/Library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Gathering Data
hour = pd.read_csv('hour.csv')
hour.describe(include="all")

# Membuat Dashboard
st.header('✨Bike Sharing Dataset Dashboard by Amira Salma✨')
from PIL import Image
gambar = Image.open('/Users/LENOVO/Downloads/dashboard/bike.png')
st.image(gambar, use_column_width=True)

# Pertanyaan 1
st.subheader('Rata-rata Jumlah Sepeda Disewakan Berdasarkan Kecepatan Angin')
# Menghitung rata-rata jumlah sepeda yang disewakan untuk setiap kecepatan angin
def calculate_avgwindspeed_df(hour):
    # Menghitung rata-rata jumlah sepeda yang disewakan untuk setiap kecepatan angin
    avgwindspeed = hour.groupby('windspeed')['cnt'].mean()
    # Membuat Data Frame
    avgwindspeed_df = pd.DataFrame({
        'Kecepatan Angin': avgwindspeed.index,
        'Rata-rata Jumlah Sepeda Disewakan': avgwindspeed.values
    })
    return avgwindspeed_df

if __name__ == '__main__':
    # Memanggil fungsi untuk menghitung rata-rata dan membuat data frame
    avgwindspeed_df = calculate_avgwindspeed_df(hour)
    # Menampilkan data frame
    st.dataframe(avgwindspeed_df)
    # Menampilkan grafik
    st.line_chart(avgwindspeed_df.set_index('Kecepatan Angin'))

# Pertanyaan 2
st.subheader('Tren Jumlah Penyewaan Sepeda di Tahun 2011')
# Membuat kolom "Bulan" dan "Tahun" dari kolom "Tanggal"
def create_month_year_columns(hour):
    hour['Tanggal'] = pd.to_datetime(hour['dteday'])
    hour['Bulan'] = hour['Tanggal'].dt.month
    hour['Tahun'] = hour['Tanggal'].dt.year
    return hour

def calculate_monthly_bike_rentals(hour, target_year):
    # Memfilter data hanya untuk tahun tertentu
    data2011 = hour[hour['Tahun'] == 2011]
    # Menghitung jumlah sepeda yang disewakan setiap bulan pada tahun tertentu
    trend_penyewaan_bulanan_2011 = data2011.groupby('Bulan')['cnt'].sum()
    # Membuat Data Frame
    trend_df = pd.DataFrame({
        'Bulan': trend_penyewaan_bulanan_2011.index,
        'Jumlah Sepeda Disewakan': trend_penyewaan_bulanan_2011.values
    })
    return trend_df

if __name__ == '__main__':
    # Memanggil fungsi untuk membuat kolom "Bulan" dan "Tahun"
    hour_data_with_date_columns = create_month_year_columns(hour)
    # Memanggil fungsi untuk menghitung tren penyewaan bulanan untuk tahun tertentu
    trend_df_2011 = calculate_monthly_bike_rentals(hour_data_with_date_columns, target_year=2011)
    # Menampilkan data frame
    st.dataframe(trend_df_2011)
    # Menampilkan
    st.line_chart(trend_df_2011.set_index('Bulan'))

# Pertanyaan 3
st.subheader('Perbandingan Jumlah Sepeda Disewakan Berdasarkan Jenis Pengguna')
# Menghitung jumlah sepeda yang disewakan setiap jenis pengguna
def calculate_bike_rentals_by_user_type(hour):
    TotalTerdaftar = hour['registered'].sum()
    TotalBiasa = hour['casual'].sum()
    # Membuat Data Frame
    Perbandingan_df = pd.DataFrame({
        'Jenis Pengguna': ['Terdaftar', 'Biasa'],
        'Jumlah Sepeda Disewakan': [TotalTerdaftar, TotalBiasa]
    })
    return Perbandingan_df

if __name__ == '__main__':
    # Memanggil fungsi untuk menghitung jumlah sepeda disewakan per jenis pengguna
    Perbandingan_df = calculate_bike_rentals_by_user_type(hour)
    # Menampilkan data frame dalam aplikasi Streamlit
    st.dataframe(Perbandingan_df)
    # Menampilkan grafik bar chart dengan nama sumbu
    st.bar_chart(Perbandingan_df.set_index('Jenis Pengguna'))