import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ======================
# 1. Load Dataset
# ======================
@st.cache_data
def load_data():
    df = pd.read_csv("ecommerce.csv", encoding="latin1")
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Revenue'] = df['Quantity'] * df['UnitPrice']
    return df

df = load_data()

# ======================
# Sidebar Navigation
# ======================
st.sidebar.title("📊 E-Commerce Dashboard")
page = st.sidebar.radio("Navigasi", [
    "Profil Proyek",
    "Overview",
    "Analisis Produk",
    "Analisis Pelanggan",
    "Segmentasi RFM",
    "Deteksi Anomali",
    "Kesimpulan & Rekomendasi"
])

# ======================
# 2. Profil Proyek
# ======================
if page == "Portofolio":
    st.title("📌 Portofolio")
    st.subheader("Nama: Sahadewa Hendra Muhammad")
    st.write("Bio: Data Analyst Enthusiast dengan fokus pada analisis E-Commerce.")
    st.write("Kontak: dewanugelo456@gmail.com | [LinkedIn](https://www.linkedin.com/in/dewahendra/)")
    st.markdown("---")
    st.write("**Judul Proyek:** E-Commerce Customer & Product Analysis")
    st.write("**Deskripsi:** Analisis ini bertujuan mengeksplorasi perilaku pelanggan, kinerja produk, dan mendeteksi anomali transaksi untuk mendukung pengambilan keputusan bisnis.")

# ======================
# 3. Overview
# ======================
elif page == "Overview":
    st.title("📊 Overview Bisnis")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Revenue", f"${df['Revenue'].sum():,.0f}")
    col2.metric("Total Transaksi", f"{df['InvoiceNo'].nunique():,}")
    col3.metric("Total Customer", f"{df['CustomerID'].nunique():,}")

    st.subheader("Tren Penjualan Bulanan")
    monthly = df.groupby(df['InvoiceDate'].dt.to_period("M"))['Revenue'].sum().reset_index()
    monthly['InvoiceDate'] = monthly['InvoiceDate'].astype(str)
    fig, ax = plt.subplots(figsize=(10,4))
    sns.lineplot(data=monthly, x="InvoiceDate", y="Revenue", marker="o", ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# ======================
# 4. Analisis Produk
# ======================
elif page == "Analisis Produk":
    st.title("📦 Analisis Produk")

    st.subheader("Top 10 Produk Berdasarkan Revenue")
    top_products = df.groupby("Description")['Revenue'].sum().nlargest(10).reset_index()
    fig, ax = plt.subplots(figsize=(8,4))
    sns.barplot(data=top_products, x="Revenue", y="Description", ax=ax)
    st.pyplot(fig)

    st.subheader("Produk dengan Retur Tertinggi")
    retur = df[df['Quantity'] < 0].groupby("Description")['Quantity'].sum().nsmallest(10).reset_index()
    st.dataframe(retur)

# ======================
# 5. Analisis Pelanggan
# ======================
elif page == "Analisis Pelanggan":
    st.title("👥 Analisis Pelanggan")

    st.subheader("Distribusi Total Belanja per Customer")
    customer_revenue = df.groupby("CustomerID")['Revenue'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(8,4))
    sns.histplot(customer_revenue['Revenue'], bins=50, ax=ax)
    st.pyplot(fig)

    st.subheader("Top 10 Customer")
    top_customers = customer_revenue.nlargest(10, "Revenue")
    st.dataframe(top_customers)

# ======================
# 6. Segmentasi RFM
# ======================
elif page == "Segmentasi RFM":
    st.title("📈 Segmentasi Pelanggan (RFM)")

    ref_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)
    rfm = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (ref_date - x.max()).days,
        'InvoiceNo': 'count',
        'Revenue': 'sum'
    }).reset_index()
    rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']

    st.dataframe(rfm.head())

    st.subheader("Scatter Plot: Frequency vs Monetary")
    fig, ax = plt.subplots(figsize=(6,4))
    sns.scatterplot(data=rfm, x="Frequency", y="Monetary", ax=ax)
    st.pyplot(fig)

# ======================
# 7. Deteksi Anomali
# ======================
elif page == "Deteksi Anomali":
    st.title("🚨 Deteksi Anomali")

    st.subheader("Boxplot Quantity")
    fig, ax = plt.subplots(figsize=(6,4))
    sns.boxplot(x=df['Quantity'], ax=ax)
    st.pyplot(fig)

    st.subheader("Boxplot UnitPrice")
    fig, ax = plt.subplots(figsize=(6,4))
    sns.boxplot(x=df['UnitPrice'], ax=ax)
    st.pyplot(fig)

    st.subheader("Contoh Transaksi Anomali (Quantity > 1000)")
    st.dataframe(df[df['Quantity'] > 1000].head())

# ======================
# 8. Kesimpulan
# ======================
elif page == "Kesimpulan & Rekomendasi":
    st.title("📝 Kesimpulan & Rekomendasi")
    st.write("""
    - Produk tertentu berkontribusi besar terhadap revenue.
    - Pelanggan VIP memberikan sebagian besar pendapatan.
    - Ada indikasi anomali pada transaksi dengan jumlah produk sangat besar atau harga abnormal.
    
    **Rekomendasi:**
    1. Fokuskan promosi pada produk best seller.
    2. Buat program loyalitas untuk pelanggan top spender.
    3. Lakukan kontrol kualitas pada produk dengan retur tinggi.
    4. Investigasi transaksi anomali untuk fraud detection.
    """)
