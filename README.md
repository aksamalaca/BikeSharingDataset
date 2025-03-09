Dashboard Analisis Data Bike Sharing
Cara Menjalankan Dashboard
1. Pastikan Anda memiliki Python terinstal di komputer.
2. Instal dependensi yang diperlukan dengan menjalankan perintah berikut:
pip install -r requirements.txt
3. Jalankan aplikasi Streamlit dengan menjalankan perintah berikut:
streamlit run dashboard/dashboard.py

Deskripsi Dashboard
Dashboard ini menampilkan analisis data dari Bike Sharing Dataset. Pengguna dapat memilih salah satu dari tiga pertanyaan yang telah dianalisis:
1. Pada bulan apa jumlah penyewaan sepeda tertinggi terjadi?
2. Bagaimana pengaruh cuaca terhadap jumlah peminjaman sepeda?
3. Apakah jumlah peminjaman sepeda lebih tinggi pada hari kerja dibandingkan dengan hari libur?
Visualisasi akan diperbarui berdasarkan pilihan yang dipilih di sidebar.

Struktur Direktori
submission
├───dashboard
|   └───dashboard.py
├───data
|   ├───day.csv
|   └───hour.csv
├───notebook.ipynb
├───README.md
└───requirements.txt
└───url.txt

Sumber Data
Dataset diperoleh dari Bike Sharing Dataset yang berisi informasi mengenai penyewaan sepeda berdasarkan waktu, cuaca, dan faktor lainnya.