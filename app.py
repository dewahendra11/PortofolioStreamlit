import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# =========================
# SIDEBAR PROFIL
# =========================
st.sidebar.title("Profil Singkat")
st.sidebar.image("https://via.placeholder.com/150", caption="Foto Profil")  # Bisa diganti dengan foto kamu
st.sidebar.markdown("""
**Nama:** Sahadewa Hendra Muhammad  
**Bio:** Lorem ipsum dolor sit amet, consectetur adipiscing elit.  
**Kontak:** email@example.com | LinkedIn | GitHub
""")

# =========================
# HALAMAN UTAMA
# =========================
st.title("📊 Portofolio Data Analyst")
st.markdown("Selamat datang di dashboard portofolio saya. Berikut adalah beberapa proyek analisis data yang pernah saya kerjakan.")

# Tabs untuk memisahkan proyek
tab1, tab2, tab3 = st.tabs(["📈 Proyek 1", "📉 Proyek 2", "🌍 Proyek 3"])

# =========================
# TAB 1
# =========================
with tab1:
    st.header("Judul Proyek 1: Lorem Ipsum")
    st.markdown("""
    **Tujuan:** Lorem ipsum dolor sit amet, consectetur adipiscing elit.  
    **Hasil Analisis:** Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.  
    **Insight:** Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.
    """)
    
    # Contoh data random
    df = pd.DataFrame({
        "Bulan": pd.date_range("2023-01-01", periods=12, freq="M"),
        "Penjualan": np.random.randint(100, 500, size=12)
    })
    
    # Visualisasi interaktif
    fig = px.line(df, x="Bulan", y="Penjualan", title="Tren Penjualan Bulanan")
    st.plotly_chart(fig, use_container_width=True)

# =========================
# TAB 2
# =========================
with tab2:
    st.header("Judul Proyek 2: Lorem Ipsum Dolor")
    st.markdown("""
    **Tujuan:** Lorem ipsum dolor sit amet, consectetur adipiscing elit.  
    **Hasil Analisis:** Vivamus suscipit tortor eget felis porttitor volutpat.  
    **Insight:** Curabitur non nulla sit amet nisl tempus convallis quis ac lectus.
    """)
    
    # Data random
    df2 = pd.DataFrame({
        "Kategori": ["A", "B", "C", "D"],
        "Jumlah": np.random.randint(50, 200, size=4)
    })
    
    # Visualisasi interaktif
    fig2 = px.bar(df2, x="Kategori", y="Jumlah", title="Perbandingan Kategori Produk", text="Jumlah")
    st.plotly_chart(fig2, use_container_width=True)

# =========================
# TAB 3
# =========================
with tab3:
    st.header("Judul Proyek 3: Lorem Ipsum World Data")
    st.markdown("""
    **Tujuan:** Lorem ipsum dolor sit amet, consectetur adipiscing elit.  
    **Hasil Analisis:** Proin eget tortor risus. Nulla quis lorem ut libero malesuada feugiat.  
    **Insight:** Donec sollicitudin molestie malesuada.
    """)
    
    # Data random untuk scatter plot
    df3 = pd.DataFrame({
        "x": np.random.randn(100),
        "y": np.random.randn(100),
        "size": np.random.randint(10, 50, size=100),
        "color": np.random.choice(["Group A", "Group B", "Group C"], size=100)
    })
    
    fig3 = px.scatter(df3, x="x", y="y", size="size", color="color",
                      title="Distribusi Data Acak (Scatter Plot)", opacity=0.7)
    st.plotly_chart(fig3, use_container_width=True)
