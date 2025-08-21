import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =============================
# Profil Singkat
# =============================
st.sidebar.title("Portofolio")
st.sidebar.markdown("""
**Nama:** Sahadewa Hendra Muhammad  
**Bio:** Data Analyst Enthusiast dengan fokus pada EDA, data visualization, dan business insight.  
**Kontak:**  
📧 Email: dewanugelo456@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/dewahendra/) | [GitHub](https://github.com/dewahendra11)
""")

# =============================
# Judul
# =============================
st.title("📊 Data Analyst")
st.subheader("Exploratory Data Analysis pada Data E-Commerce")

st.image("ecomm.jpeg", caption="sumber gambar: midtrans.com/id/blog/e-commerce", use_container_width=True)
st.markdown("""Dataset UCI – Online Retail II merupakan kumpulan data transaksi nyata dari sebuah perusahaan retail online non-store yang berbasis di Inggris, mencatat lebih dari satu juta transaksi yang berlangsung antara Desember 2009 hingga Desember 2011. Setiap baris dalam dataset ini merepresentasikan detail transaksi, mulai dari nomor faktur, kode produk, deskripsi barang, jumlah yang dibeli, harga per unit, hingga identitas pelanggan dan negara asalnya. Data ini penting untuk dianalisis karena menyajikan potret nyata perilaku konsumen dalam e-commerce lintas negara, yang memungkinkan peneliti maupun praktisi bisnis untuk memahami pola pembelian, tren penjualan musiman, hingga hubungan antarproduk yang sering dibeli bersamaan. Selain itu, analisis dataset ini juga dapat membantu perusahaan dalam mengoptimalkan strategi pemasaran, manajemen inventori, hingga pengembangan sistem rekomendasi, menjadikannya sumber yang relevan baik untuk riset akademis maupun pengambilan keputusan bisnis berbasis data.""")

# =============================
# Load Data
# =============================
df = pd.read_csv("ecommerce_cleaned.csv")

# Pastikan kolom waktu bertipe datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Tambahkan kolom waktu
df['Hour'] = df['InvoiceDate'].dt.hour
df['Day'] = df['InvoiceDate'].dt.day
df['Month'] = df['InvoiceDate'].dt.month

# Hitung revenue
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# =============================
# 1. Top 5 Negara Pembelian
# =============================
st.header("1. Top 5 Negara dengan Pembelian Tertinggi")

top_countries = df['Country'].value_counts().head(5)

fig, ax = plt.subplots()
top_countries.plot(kind='bar', ax=ax, color="skyblue")
ax.set_ylabel("Jumlah Pembelian")
st.pyplot(fig)

st.markdown("""
Analisis distribusi pembelian pada dataset e-commerce ini menunjukkan bahwa **United Kingdom** menjadi negara yang paling dominan dalam aktivitas transaksi. Dari total seluruh pembelian yang tercatat, Inggris menyumbang sekitar 90,1% transaksi, sehingga jauh meninggalkan negara lain. Dominasi ini cukup wajar karena basis operasi perusahaan retail yang tercatat dalam dataset memang berada di Inggris, sehingga konsumen domestik otomatis lebih banyak terlibat dalam aktivitas belanja. Sementara itu, negara lain yang masuk ke dalam lima besar, yaitu **Netherlands, Germany, EIRE, dan France**, berkontribusi dalam persentase yang jauh lebih kecil jika dibandingkan dengan Inggris. Fakta ini menggarisbawahi adanya konsentrasi pasar yang sangat tinggi pada satu negara. Dari perspektif bisnis, kondisi ini bisa dianggap sebagai peluang sekaligus tantangan. Di satu sisi, keberhasilan di pasar domestik menjadi bukti kuat bahwa produk memiliki penerimaan yang baik. Namun, di sisi lain, ketergantungan yang terlalu besar terhadap satu pasar menimbulkan risiko apabila terjadi gangguan ekonomi atau perubahan perilaku konsumen di negara tersebut. Oleh karena itu, perlu strategi ekspansi yang lebih seimbang ke pasar internasional agar pertumbuhan bisnis lebih stabil dan berkelanjutan.
""")


# =============================
# 2. Waktu Dominan Pembelian
# =============================
st.header("2. Waktu Paling Dominan dalam Pembelian (Top 5 Negara)")

df_top5 = df[df['Country'].isin(top_countries.index)]
hourly = df_top5.groupby('Hour')['Quantity'].sum()

fig, ax = plt.subplots()
hourly.plot(kind='line', ax=ax, marker='o')
ax.set_xlabel("Jam")
ax.set_ylabel("Total Quantity")
st.pyplot(fig)

st.markdown("""
Hasil analisis terhadap dimensi waktu pembelian menunjukkan bahwa konsumen dari lima negara dengan jumlah pembelian tertinggi cenderung melakukan transaksi pada siang hari, disusul pagi hari, kemudian sore dan malam hari. Pola ini menggambarkan kecenderungan perilaku konsumen yang berhubungan dengan ritme aktivitas harian. Pada siang hari, khususnya antara pukul 11.00 hingga 14.00, mayoritas konsumen kemungkinan sedang berada dalam jam istirahat atau memiliki waktu senggang sehingga dapat mengakses platform e-commerce dengan lebih leluasa. Sementara itu, aktivitas pembelian pada pagi hari mengindikasikan adanya kelompok konsumen yang terbiasa merencanakan belanja sejak awal hari, baik untuk kebutuhan pribadi maupun keperluan bisnis. Meski volume transaksi pada sore dan malam hari relatif lebih rendah, pola ini tetap konsisten menggambarkan variasi perilaku berdasarkan waktu. Dari sisi bisnis, wawasan ini penting untuk menyusun strategi pemasaran berbasis waktu, misalnya memberikan promosi khusus di jam-jam sibuk untuk meningkatkan konversi atau merancang kampanye di luar jam dominan guna mengoptimalkan penjualan di periode yang biasanya sepi.
""")


# =============================
# 3. Rata-rata Harga per Unit
# =============================
st.header("3. Rata-rata Harga per Unit (Top 5 Negara)")

avg_price = df_top5.groupby('Country')['UnitPrice'].mean().sort_values(ascending=False)

fig, ax = plt.subplots()
avg_price.plot(kind='bar', ax=ax, color="orange")
ax.set_ylabel("Rata-rata Harga per Unit")
st.pyplot(fig)

st.markdown("""
Ketika rata-rata harga per unit produk yang dibeli oleh konsumen dianalisis, terlihat adanya variasi signifikan antarnegara. Negara seperti **Switzerland** tercatat memiliki rata-rata harga per unit yang lebih tinggi, yang dapat diartikan bahwa konsumen di sana cenderung membeli barang-barang yang lebih eksklusif atau berharga mahal, meskipun jumlah unit yang dibeli mungkin tidak terlalu besar. Pola ini dapat mencerminkan daya beli masyarakat yang relatif tinggi serta preferensi terhadap kualitas atau eksklusivitas produk. Sebaliknya, negara seperti **France** memperlihatkan rata-rata harga per unit yang lebih rendah. Hal ini mengindikasikan kecenderungan konsumen untuk membeli produk dalam jumlah besar, tetapi dengan harga yang lebih murah per unitnya. Perbandingan ini memberikan gambaran menarik mengenai perilaku belanja yang berbeda-beda antarnegara. Dari sudut pandang strategi bisnis, informasi ini sangat berharga untuk merancang segmentasi pasar. Produk premium dengan harga lebih tinggi dapat dipasarkan lebih agresif di negara dengan kecenderungan membeli barang eksklusif, sementara produk dengan harga terjangkau dapat lebih ditargetkan ke negara yang lebih responsif terhadap kuantitas dan harga rendah.
""")


# =============================
# 4. Produk Dominan Tiap Negara
# =============================
st.header("4. Produk Dominan pada Top 5 Negara")

top_products = df_top5.groupby(['Country', 'StockCode'])['Quantity'].sum().reset_index()
top_products = top_products.sort_values(['Country', 'Quantity'], ascending=[True, False])

st.write("Top Produk per Negara:")
st.dataframe(top_products.groupby('Country').head(3))

st.markdown("""
Hasil eksplorasi terhadap produk yang paling banyak dibeli oleh lima negara dengan total pembelian tertinggi memperlihatkan bahwa masing-masing negara memiliki produk unggulannya sendiri. Hal ini menunjukkan adanya preferensi lokal yang memengaruhi pola konsumsi. Namun menariknya, ditemukan bahwa terdapat produk dengan **StockCode 22704 (WRAP RED APPLES)** yang muncul sebagai produk dominan di dua negara sekaligus, yakni **Germany** dan **EIRE**. Temuan ini memberikan indikasi bahwa meskipun setiap negara memiliki karakteristik konsumen yang unik, terdapat pula kesamaan selera antarnegara. Kondisi ini bisa menjadi dasar penting untuk strategi pemasaran lintas negara, karena produk yang diterima dengan baik di lebih dari satu pasar berpotensi dikembangkan lebih luas secara global. Pada saat yang sama, perbedaan produk dominan di negara lain tetap perlu diperhatikan, sebab preferensi konsumen sering kali terkait erat dengan budaya, gaya hidup, serta kebutuhan spesifik. Secara keseluruhan, analisis ini menekankan pentingnya memahami perilaku pembelian pada level negara agar strategi distribusi dan promosi dapat lebih terarah dan sesuai dengan kebutuhan pasar lokal maupun regional.
""")


# =============================
# 5. Apakah Penjualan = Revenue?
# =============================
st.header("5. Hubungan Penjualan vs Revenue")

# Pastikan Revenue sudah dihitung
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# Hitung total quantity dan revenue per produk
product_quantity = df.groupby('StockCode')['Quantity'].sum().reset_index()
product_revenue = df.groupby('StockCode')['Revenue'].sum().reset_index()

# Gabungkan Quantity dan Revenue
merged_rev = pd.merge(product_quantity, product_revenue, on='StockCode', how='inner')
merged_rev.rename(columns={'Quantity': 'Total_Quantity', 'Revenue': 'Total_Revenue'}, inplace=True)


merged_rev_sorted = merged_rev.sort_values('Total_Revenue', ascending=False).head(5)

# Visualisasi
fig, ax = plt.subplots(figsize=(10,6))
bar_width = 0.4
x = range(len(merged_rev_sorted))

ax.bar(x, merged_rev_sorted['Total_Revenue'], 
       width=bar_width, label='Revenue', color='skyblue')
ax.bar([i + bar_width for i in x], merged_rev_sorted['Total_Quantity'], 
       width=bar_width, label='Quantity', color='orange')

ax.set_xticks([i + bar_width/2 for i in x])
ax.set_xticklabels(merged_rev_sorted['StockCode'])
ax.set_xlabel('Product (StockCode)')
ax.set_ylabel('Total')
ax.set_title('Komparasi Total Revenue dengan Total Quantity Terjual untuk Top 5 Products')
ax.legend()

st.pyplot(fig)




# Heatmap korelasi
st.subheader("Heatmap Korelasi Numerik")

corr = df[['Quantity','UnitPrice','Month','Day','Hour']].corr()

fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

st.markdown("""
Analisis hubungan antara jumlah produk yang terjual dengan total revenue memperlihatkan hasil yang cukup menarik. Tidak semua produk yang memiliki jumlah penjualan tinggi otomatis menghasilkan revenue yang besar. Contoh nyata dapat dilihat pada perbandingan **StockCode 22993** dengan **StockCode 22577**, di mana meskipun salah satu produk terjual dalam jumlah lebih banyak, total revenue yang dihasilkan justru lebih kecil dibanding produk lain dengan volume lebih rendah. Hal ini menunjukkan bahwa faktor harga per unit sangat memengaruhi total pendapatan, sehingga kuantitas penjualan saja tidak bisa dijadikan indikator utama kesuksesan produk. Untuk memperdalam analisis, dilakukan pula visualisasi dalam bentuk heatmap korelasi yang memperlihatkan hubungan antarvariabel numerik seperti UnitPrice, Quantity, Month, Day, dan Hour. Dari hasil tersebut ditemukan bahwa korelasi paling signifikan adalah antara **Quantity dan UnitPrice** dengan nilai -0.34, yang berarti terdapat hubungan negatif. Artinya, semakin tinggi harga per unit, cenderung semakin rendah jumlah unit yang dibeli konsumen. Sementara itu, variabel lain seperti waktu dalam bulan, hari, atau jam tidak menunjukkan korelasi kuat terhadap penjualan. Insight ini sangat penting bagi strategi pricing karena membuktikan bahwa harga memiliki pengaruh langsung terhadap volume pembelian, sementara strategi promosi waktu memerlukan pendekatan berbeda agar lebih efektif.
""")




# =============================
# 4. Insight
# =============================
st.subheader("Kesimpulan dan Insight")

st.markdown(""""Berdasarkan hasil eksplorasi data, terdapat sejumlah wawasan penting yang dapat dijadikan dasar strategi bisnis. Pertama, penjualan masih sangat bergantung pada pasar United Kingdom yang menyumbang lebih dari 90% transaksi, sehingga perusahaan perlu mengantisipasi risiko dengan memperluas penetrasi ke negara lain agar tidak terlalu bergantung pada satu pasar saja. Kedua, perilaku konsumen menunjukkan pola waktu belanja yang dominan pada siang hari sekitar pukul 12.00, sehingga waktu ini dapat dimanfaatkan sebagai momen strategis untuk meluncurkan promosi atau kampanye pemasaran. Ketiga, analisis rata-rata harga per unit mengungkap adanya segmentasi daya beli antarnegara; beberapa negara cenderung membeli produk eksklusif dengan harga tinggi dalam jumlah kecil, sementara negara lain lebih banyak membeli produk dengan harga murah. Hal ini mengisyaratkan pentingnya diferensiasi strategi pemasaran berdasarkan daya beli konsumen. Keempat, meskipun ada kesamaan dalam beberapa produk populer, tiap negara tetap memiliki produk favorit yang berbeda, sehingga pendekatan pemasaran lokal tetap diperlukan agar lebih relevan dengan kebutuhan konsumen. Terakhir, ditemukan bahwa jumlah penjualan tidak selalu sejalan dengan revenue tinggi, karena harga per unit memiliki pengaruh yang signifikan terhadap total pendapatan. Oleh sebab itu, strategi bisnis tidak hanya perlu mengejar kuantitas penjualan, tetapi juga memperhatikan positioning harga produk agar dapat mengoptimalkan revenue. """)