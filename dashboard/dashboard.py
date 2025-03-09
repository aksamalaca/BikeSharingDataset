import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
day_df = pd.read_csv("data/day.csv")

# Konversi tanggal ke datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Sidebar Dropdown
st.sidebar.title("Analisis Data Bike Sharing")
option = st.sidebar.selectbox(
    "Pilih Tampilkan Visualisasi Data",
    [
        "Bulan Tertinggi Penyewaan Sepeda",
        "Pengaruh Cuaca Terhadap Penyewaan Sepeda",
        "Hari Kerja vs Hari Libur"
    ]
)

if option == "Bulan Tertinggi Penyewaan Sepeda":
    st.title("Bulan Tertinggi Penyewaan Sepeda")
    
    monthly_rentals = day_df.groupby('mnth')['cnt'].sum()
    
    plt.figure(figsize=(10,5))
    plt.plot(monthly_rentals.index, monthly_rentals.values, marker='o', linestyle='-', color='b')
    plt.xlabel("Bulan")
    plt.ylabel("Jumlah Penyewaan")
    plt.title("Jumlah Penyewaan Sepeda per Bulan")
    plt.xticks(rotation=45)
    plt.grid()
    st.pyplot(plt)

    #Penjelasan Kode
    st.write("Kode yang digunakan untuk **memvisualisasikan jumlah penyewaan sepeda per bulan dalam satu tahun** menggunakan **diagram garis (line chart)**.")
    st.write("1. Kolom **dteday**, yang berisi data tanggal, dikonversi menjadi bulan dengan dt.month dan disimpan dalam kolom **month**.")
    st.write("2. Data dikelompokkan berdasarkan bulan **(groupby('month'))**, lalu dihitung total penyewaan sepeda **(cnt)** untuk setiap bulan.")
    st.write("3. Diagram garis dibuat dengan plt.plot(), di mana:")
    st.write("- Sumbu-X mewakili bulan, ditampilkan dalam angka 1 hingga 12 (Januari hingga Desember).")
    st.write("- Sumbu y menunjukkan jumlah total penyewaan sepeda untuk setiap bulan.")
    st.write("3. Garis biru dengan marker lingkaran (marker='o', color='b') digunakan untuk menampilkan tren secara lebih jelas.")
    st.write("4. **plt.grid()** ditambahkan untuk membantu pembacaan nilai pada grafik.")

    st.title("Mengapa menggunakan diagram garis (line chart)?")
    st.write("Diagram garis cocok untuk menunjukkan tren atau pola perubahan data dari waktu ke waktu. Dalam hal ini, kita bisa melihat bagaimana jumlah penyewaan sepeda naik dan turun sepanjang tahun, sehingga memudahkan dalam mengidentifikasi pola musiman atau tren penggunaan sepeda."
             )
    #Conclusion
    st.title("Conclusion:")
    st.write("1. Bulan dengan jumlah penyewaan tertinggi adalah bulan Agustus.")
    st.write("2. Cuaca hangat dan musim liburan dapat meningkatkan penyewaan, sedangkan cuaca dingin di akhir tahun cenderung menurunkannya.")
    st.write("3. Line chart membantu memahami pola perubahan penyewaan sepeda sepanjang tahun, memudahkan analisis dan pengambilan keputusan strategis.")


elif option == "Pengaruh Cuaca Terhadap Penyewaan Sepeda":
    st.title("Pengaruh Cuaca Terhadap Penyewaan Sepeda")
    
    weather_rentals = day_df.groupby('weathersit')['cnt'].mean()
    
    plt.figure(figsize=(10,5))
    sns.barplot(x=weather_rentals.index.astype(str), y=weather_rentals.values, palette='viridis', dodge=False)
    plt.xlabel("Kondisi Cuaca")
    plt.ylabel("Rata-rata Jumlah Penyewaan")
    plt.title("Pengaruh Cuaca terhadap Peminjaman Sepeda")
    plt.xticks(ticks=[0, 1, 2, 3], labels=['Cerah', 'Mendung', 'Hujan Ringan', 'Hujan Lebat'])
    st.pyplot(plt)

    #Penjelasan Kode
    st.write("Kode yang digunakan untuk memvisualisasikan **pengaruh kondisi cuaca terhadap rata-rata jumlah penyewaan sepeda** menggunakan **diagram batang (bar chart)**.")
    st.write("1. Data dikelompokkan berdasarkan kondisi cuaca (weathersit), lalu dihitung rata-rata jumlah penyewaan sepeda (cnt) untuk setiap kategori cuaca.")
    st.write("2. Menggunakan Seaborn (sns.barplot), diagram batang dibuat dengan kondisi cuaca sebagai sumbu-x dan rata-rata penyewaan sebagai sumbu-y.")
    st.write("3. palette='viridis' memberikan warna yang lebih bervariasi, sedangkan dodge=False memastikan setiap kategori cuaca memiliki satu batang.")
    st.write("4. Label sumbu-x diubah menjadi **Cerah**, **Mendun**, **Hujan Ringan**, dan **Hujan Lebat** agar lebih mudah dipahami.")

    st.title("Mengapa menggunakan diagram batang (bar chart)?")
    st.write("Diagram batang dipilih karena **cocok untuk membandingkan nilai rata-rata antar kategori yang berbeda**. Dalam hal ini, kita ingin membandingkan bagaimana jumlah rata-rata penyewaan sepeda berubah berdasarkan kondisi cuaca. Diagram batang mempermudah analisis perbandingan antar kategori dengan tampilan yang jelas dan mudah dibaca.")

    #Conclusion
    st.title("Conclusion:")
    st.write("1. Cuaca sangat mempengaruhi jumlah penyewaan, di mana saat hujan jumlah peminjaman menurun drastis dan cuaca cerah berkontriusi pada jumlah penyewaan tertinggi.")
    st.write("2. Diagram batang memudahkan perbandingan rata-rata penyewaan antar kategori cuaca, menunjukkan pola yang dapat dianalisis lebih lanjut.")
    st.write("3. Informasi ini berguna bagi penyedia layanan penyewaan sepeda untuk menyesuaikan strategi operasional, seperti promosi pada hari cerah atau penyediaan perlengkapan hujan di musim basah.")

elif option == "Hari Kerja vs Hari Libur":
    st.title("Hari Kerja vs Hari Libur")
    
    workingday_counts = day_df['workingday'].value_counts()
    labels = ['Hari Kerja', 'Hari Libur']
    colors = ['#ff9999','#66b3ff']
    
    plt.figure(figsize=(7,7))
    plt.pie(workingday_counts, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90, shadow=True)
    plt.title("Proporsi Penyewaan Sepeda pada Hari Kerja vs Hari Libur")
    st.pyplot(plt)

    #Penjelasan Kode
    st.write("Kode yang digunakan untuk **memvisualisasikan proporsi penyewaan sepeda pada hari kerja dan hari libur** menggunakan **diagram lingkaran (pie chart)**.")
    st.write("1. Data dihitung berdasarkan jumlah kemunculan masing-masing kategori di kolom 'workingday', yaitu **hari kerja (1)** dan **hari libur (0)**.")
    st.write("2. Label pada diagram ditentukan sebagai **Hari Kerja** dan **Hari Libur**, dengan warna **merah muda (#ff9999)** untuk hari kerja dan **biru (#66b3ff)** untuk hari libur.")
    st.write("3. **plt.pie()** digunakan untuk membuat pie chart, dengan")
    st.write("- autopct='%1.1f%%' menampilkan persentase pada setiap bagian,")
    st.write("- startangle=90 memutar diagram agar lebih mudah dibaca,")
    st.write("- shadow=True menambahkan efek bayangan untuk tampilan lebih menarik.")
    
    st.title("Mengapa menggunakan diagram lingkaran (pie chart?)")
    st.write("**Pie chart dipilih karena cocok untuk menunjukkan perbandingan proporsi dalam satu kategori data**. Dalam kasus ini, kita ingin melihat seberapa besar persentase penyewaan sepeda terjadi pada hari kerja dibandingkan hari libur secara visual. Dengan pie chart, kita bisa **dengan cepat memahami distribusi dan proporsi antara dua kategori tersebut**.")

    #Conclusion
    st.title("Conclusion:")
    st.write("1. Hari kerja memiliki jumlah peminjaman lebih tinggi yaitu sebesar 68,4% dibandingkan hari libur yang sebesar 31,6%, menunjukkan bahwa banyak pengguna sepeda menggunakan layanan ini untuk keperluan transportasi sehari-hari.")
    st.write("2. Pie chart membantu dengan jelas menunjukkan perbandingan antara penyewaan di hari kerja dan hari libur, memudahkan analisis pola penggunaan sepeda.")

st.write("\nSumber data: [Bike Sharing Dataset](https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ/view)")