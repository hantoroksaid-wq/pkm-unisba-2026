import streamlit as st

# Konfigurasi Halaman
st.set_page_config(
    page_title="Laporan PkM Tim Hantoro",
    page_icon="🎓",
    layout="centered"
)

# --- HEADER & JUDUL ---
st.title("Laporan Kegiatan Pengabdian kepada Masyarakat (PkM)")
st.subheader("Universitas Islam Bandung")
st.write("---")

# --- INFORMASI UMUM ---
st.header("📌 Detail Kegiatan")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Judul PkM:**")
    st.write("Pelatihan Peningkatan Ekonomi Kreatif Berbasis Digital") # Ubah sesuai judul Anda
    
    st.markdown("**Mitra PkM:**")
    st.write("UMKM Kecamatan X, Bandung") # Ubah sesuai mitra

with col2:
    st.markdown("**Waktu Pelaksanaan:**")
    st.write("Juli 2026")
    
    st.markdown("**Lokasi:**")
    st.write("Bandung, Jawa Barat")

st.write("---")

# --- TIM PELAKSANA ---
st.header("👥 Tim Pelaksana")
# Anda bisa menuliskan nama tim Anda di sini
st.markdown("""
*   **Ketua:** Hantoro Ksaid Notolegowo, S.E., M.Si.
*   **Anggota 1:** [Nama Anggota 1]
*   **Anggota 2:** [Nama Anggota 2]
*   **Mahasiswa:** [Nama Mahasiswa]
""")

st.write("---")

# --- RINGKASAN KEGIATAN & HASIL ---
st.header("📝 Ringkasan & Hasil Kegiatan")
st.write("""
Tuliskan ringkasan kegiatan PkM Anda di sini. Apa latar belakang masalah yang dihadapi mitra, 
solusi apa yang tim Anda tawarkan, dan bagaimana jalannya kegiatan tersebut.
""")

# Menampilkan metrik pencapaian (opsional)
st.subheader("📊 Indikator Capaian")
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric(label="Jumlah Peserta", value="40 Orang")
kpi2.metric(label="Tingkat Kepuasan", value="92%")
kpi3.metric(label="Produk Dihasilkan", value="5 Rintisan")

st.write("---")

# --- DOKUMENTASI ---
st.header("📷 Dokumentasi Kegiatan")
st.info("Tips: Anda bisa memasukkan foto kegiatan dengan meletakkan file foto di folder yang sama.")
# Jika ada foto bernama 'foto1.jpg', hapus tanda pagar (#) di bawah ini untuk menampilkannya:
# st.image("foto1.jpg", caption="Foto Bersama Peserta PkM")

st.write("---")
st.caption("© 2026 Tim PkM Hantoro Ksaid Notolegowo - Universitas Islam Bandung")
