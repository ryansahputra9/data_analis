import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Visualisasi Data Peminjaman Sepeda :bike:")

# Load data
day_df = pd.read_csv("day.csv")

# ----------------------------------STATSITIK DESKRIPTIF-----------------------#

# STATISTIK DESKRIPTIF
cnt_mean = day_df["cnt"].mean()
cnt_total = day_df["cnt"].sum()
cnt_max = day_df["cnt"].max()
cnt_min = day_df["cnt"].min()


def format_number(number):
    if number < 1000:
        return str(number)
    elif number < 1000000:
        return f"{number/1000:.1f}K"
    else:
        return f"{number/1000000:.1f}M"


# Display the metrics for 'cnt'
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Mean CNT", value=format_number(cnt_mean))
with col2:
    st.metric(label="Total CNT", value=format_number(cnt_total))
with col3:
    st.metric(label="Max CNT", value=cnt_max)
with col4:
    st.metric(label="Min CNT", value=cnt_min)
st.text("CNT merupakan jumlah dari total rental sepeda Casual dan Register ")

##-----------------------BAR CHART PER BULAN---------------------------##

# JUDUL
st.subheader("Distribusi Total Pinjaman Sepeda per Bulan :calendar:")

# Aggregating monthly data
monthly_data = day_df.groupby("mnth")["cnt"].sum().reset_index()
st.markdown("<br>", unsafe_allow_html=True)

bulan_labels = [
    "JANUARI",
    "FEBRUARI",
    "MARET",
    "APRIL",
    "MEI",
    "JUNI",
    "JULI",
    "AGUSTUS",
    "SEPTEMBER",
    "OKTOBER",
    "NOVEMBER",
    "DESEMBER",
]

# Plot distribusi total pinjaman sepeda per bulan menggunakan Matplotlib dan Streamlit
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(monthly_data["mnth"], monthly_data["cnt"])
ax.set_title(
    "Bar Chart Distribusi Total Pinjaman Sepeda per Bulan", fontsize=18
)  # Perbaikan tulisan
ax.set_xlabel("Bulan")
ax.set_ylabel("Total Pinjaman Sepeda (cnt)")
ax.set_xticks(range(1, 13))
ax.set_xticklabels(bulan_labels, rotation=60)

for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        yval,
        round(yval, 2),
        ha="center",
        va="bottom",
    )
st.pyplot(fig)

##----------------LINE CHART----------------------------##
st.subheader("Distribusi Total Pinjaman Sepeda per Bulan :calendar:")

# Line chart dengan markers
fig, ax = plt.subplots(figsize=(10, 6))
line = ax.plot(monthly_data["mnth"], monthly_data["cnt"], marker="o")
ax.set_title("Line Chart Distribusi Total Pinjaman Sepeda per Bulan", fontsize=18)
ax.set_xlabel("Bulan")
ax.set_ylabel("Total Pinjaman Sepeda (cnt)")
ax.set_xticks(range(1, 13))
ax.set_xticklabels(bulan_labels, rotation=60)

# Membuat notasi
for i, txt in enumerate(monthly_data["cnt"]):
    ax.annotate(
        txt,
        (monthly_data["mnth"][i], monthly_data["cnt"][i]),
        textcoords="offset points",
        xytext=(0, 5),
        ha="center",
    )
# menampilkan visualisasi
st.pyplot(fig)

st.info(
    "INSIGHT \n - Puncak Peminjaman pada Bulan Juni dan Agustus: \n Jumlah peminjaman sepeda mencapai puncak tertinggi pada bulan Juni dan Agustus, masing-masing dengan 346,342 dan 351,194. Ini menunjukkan tren peningkatan peminjaman selama musim panas, di mana cuaca cenderung lebih baik dan lebih banyak orang terlibat dalam aktivitas outdoor. \n - Penurunan Peminjaman pada Bulan Januari: Bulan Januari menunjukkan jumlah peminjaman yang relatif rendah, sebanyak 134,933. Hal ini dapat dipahami sebagai dampak dari cuaca dingin dan kurangnya kegiatan outdoor selama bulan-bulan musim dingin. \n - Pertumbuhan Stabil hingga Oktober: Peminjaman sepeda mengalami pertumbuhan yang stabil hingga bulan Oktober, di mana mencapai 322,352. Bulan-bulan ini mungkin masih memberikan cuaca yang relatif baik, memungkinkan orang untuk terus bersepeda."
)
st.info(
    "IMPLIKASI DAN STRATEGI BISNIS \n - Persiapan Ekstra pada Musim Panas: \n Mengingat puncak peminjaman terjadi selama musim panas, perusahaan dapat mempersiapkan stok sepeda ekstra dan meningkatkan kapasitas layanan pelanggan selama periode ini. \n - Promosi dan Diskon pada Bulan-Bulan Berkurang Aktif:\n Pada bulan-bulan dengan peminjaman rendah, perusahaan dapat merancang promosi atau diskon khusus untuk meningkatkan minat pengguna dan mempertahankan keterlibatan pelanggan. \n - Pengembangan Acara Khusus pada Bulan-Bulan Tertentu: \n Menganalisis tren bulanan dapat membantu perusahaan dalam merencanakan acara khusus atau kampanye pemasaran untuk meningkatkan kesadaran dan partisipasi pengguna selama bulan-bulan tertentu."
)
##--------------pie chart-------------------------##

# JUDUL
st.subheader("Distribusi Pengaruh Cuaca Pada Peminjaman Sepeda 	:mostly_sunny:")
weather_data = day_df.groupby("weathersit")["cnt"].sum()

# Definisi label cuaca
weather_labels = [
    "Clear",
    "Mist",
    "Light Snow",
]

# Plot distribusi total pinjaman sepeda berdasarkan cuaca (menggunakan pie chart)
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    weather_data, labels=weather_data.index, autopct="%1.1f%%", startangle=140
)

# Menambahkan legenda
ax.legend(
    wedges,
    weather_labels,
    title="Cuaca",
    loc="center",
    bbox_to_anchor=(0.5, 0),
    ncol=len(weather_labels),
)

# Menambahkan judul
ax.set_title("Pengaruh Cuaca terhadap Total Pinjaman Sepeda")

# Tampilkan diagram pie chart
st.pyplot(fig)

##----------BAR CHART----------------##

weather_labels = ["Clear", "Mist", "Light Snow"]

# Plot distribusi total pinjaman sepeda berdasarkan cuaca
fig, ax = plt.subplots(figsize=(8, 6))
weather_data.plot(kind="bar", ax=ax)
ax.set_title("Pengaruh Cuaca terhadap Total Pinjaman Sepeda")
ax.set_xlabel("Cuaca")
ax.set_ylabel("Total Pinjaman Sepeda (cnt)")
ax.set_xticks(range(len(weather_labels)))
ax.set_xticklabels(weather_labels, rotation=0)

# Tampilkan diagram bar chart
st.pyplot(fig)
st.info(
    "INSIGHT \n - Dominasi Peminjaman pada Cuaca Cerah: \n Dari diagram pie, dapat dilihat bahwa cuaca cerah mendominasi peminjaman sepeda dengan porsi sebesar 68,6%. Hal ini menunjukkan bahwa individu cenderung lebih aktif meminjam sepeda saat cuaca sedang cerah. \n - Peminjaman Berkabut Mencapai 30,3%: Meskipun cuaca cerah mendominasi, kondisi berkabut juga memiliki andil yang signifikan sebesar 30,3%. Ini menunjukkan bahwa sebagian pengguna tetap tertarik untuk meminjam sepeda meskipun cuaca kurang cerah dan mungkin memiliki visibilitas yang lebih rendah. \n - Pengaruh Salju Ringan yang Minim: Kondisi salju ringan memiliki kontribusi yang sangat kecil, hanya 1,2% dari total peminjaman sepeda. Ini dapat diartikan bahwa kondisi salju ringan kurang mendukung aktivitas peminjaman sepeda, mungkin karena faktor cuaca yang kurang nyaman dan lebih sulit untuk bersepeda."
)
st.info(
    " IMPLIKASI DAN STRATEGI BISNIS \n - Optimalkan Promosi pada Cuaca Cerah: \n Fokuskan kampanye pemasaran dan penawaran khusus selama periode cuaca cerah, Kembangkan program loyalitas atau diskon untuk mendorong peminjaman sepeda lebih lanjut saat cuaca sedang cerah, Gunakan media sosial dan saluran pemasaran online untuk meningkatkan kesadaran tentang keuntungan bersepeda saat cuaca cerah. \n - Perluas Layanan Saat Berkabut: Evaluasi dan perluas layanan pada hari-hari berkabut dengan menawarkan solusi khusus, Kembangkan opsi penyewaan sepeda dengan aksesori tambahan seperti lampu dan reflektor untuk meningkatkan visibilitas, Tawarkan diskon khusus atau paket berkabut untuk menarik lebih banyak pelanggan selama kondisi ini \n - Kesadaran Terhadap Cuaca Ekstrem: Meskipun peminjaman pada kondisi salju ringan rendah, perusahaan perlu meningkatkan kesadaran terhadap kondisi cuaca ekstrem. Ini dapat mencakup strategi pemasaran yang berfokus pada kenyamanan dan keamanan pengguna selama kondisi cuaca yang lebih ekstrem."
)

# Watermark
watermark_text = "Dibuat dengan cinta dan sakit kepala oleh Ryan Sahputra, demi memenuhi tugas dan kewajiban dari dicoding, salam santun, kecup hangat di keningmu :)"
st.markdown(
    f'<div style="position: fixed; bottom: 0; left: 50%; transform: translateX(-50%); text-align: center; width: 100%; background-color: #f0f0f0; padding: 5px; font-size: 15px; color: #888;">{watermark_text}</div>',
    unsafe_allow_html=True,
)
