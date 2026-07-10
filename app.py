import streamlit as st

# Konfigurasi Halaman (Nama Tab di Browser)
st.set_page_config(
    page_title="Unisba Perkuat Daya Saing UMKM Desa Mekarmanik",
    page_icon="📰",
    layout="centered"
)

# --- JUDUL BERITA (HEADLINE) ---
st.title("Unisba Perkuat Daya Saing UMKM Desa Mekarmanik melalui Pelatihan Business Model Canvas dan Sertifikasi Halal")

# --- DATELINE & INFO PENULIS ---
st.caption("📍 **Bandung** | 📅 *Juni 2026* | 👤 *Tim PkM Prodi Ekonomi Pembangunan Unisba*")
st.write("---")

# --- HIGHLIGHT / INTRO ---
st.markdown("""
**BANDUNG** — Tim Pengabdian kepada Masyarakat (PkM) Program Studi Ekonomi Pembangunan, 
Fakultas Ekonomi dan Bisnis Universitas Islam Bandung (Unisba) menyelenggarakan pelatihan 
bertema *"Penguatan Produk Unggulan Mitra Berbasis Nilai-Nilai Islam dan Ekosistem 
Halal untuk Mendorong Ekonomi Berkelanjutan di Desa Mekarmanik Kecamatan Cimenyan"* 
pada 13 Juni 2026 di GOR Desa Mekarmanik, Kecamatan Cimenyan, Kabupaten Bandung.
""")

# --- DOKUMENTASI (TEMPAT FOTO) ---
# Jika nanti ada foto, Anda bisa mengaktifkan baris di bawah ini:
# st.image("foto_kegiatan.jpg", caption="Pelaksanaan PkM Tim Unisba di GOR Desa Mekarmanik")

# --- ISI BERITA PARAGRAF 2-3 ---
st.write("""
Kegiatan ini merupakan bagian dari Program Pengembangan Produk Unggulan Mitra (P3UM) 
yang bertujuan meningkatkan kapasitas pelaku usaha mikro, kecil, dan menengah (UMKM) agar 
mampu menghasilkan produk yang lebih berkualitas, memiliki daya saing, serta memenuhi aspek 
legalitas dan kebutuhan pasar melalui penerapan ekosistem halal dan penguatan manajemen usaha.
""")

st.write("""
Pelatihan diikuti oleh 14 peserta, terdiri atas 11 pelaku UMKM, 1 perwakilan Pemerintah 
Desa Mekarmanik, 1 perwakilan BUMDes, dan 1 perwakilan Koperasi Rasagalor. 
Kehadiran berbagai unsur tersebut menunjukkan komitmen bersama dalam mendorong 
pengembangan ekonomi desa yang lebih inklusif dan berkelanjutan.
""")

# --- STATISTIK PESERTA (VISUALISASI DATA) ---
st.write(" ")
st.subheader("📊 Statistik Kehadiran Peserta PkM")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Peserta", "14")
col2.metric("Pelaku UMKM", "11")
col3.metric("Pemdes/BUMDes", "2")
col4.metric("Koperasi", "1")
st.write(" ")

# --- EMPAT MATERI UTAMA ---
st.subheader("📌 Empat Pilar Materi Utama Pelatihan")
st.write("""
Dalam kegiatan tersebut, tim PkM Unisba memberikan empat materi utama yang saling terintegrasi:
""")

# Menggunakan expander agar pembaca bisa mengklik materi yang ingin dibaca detail
with st.expander("1. Sertifikasi Halal"):
    st.write("Meliputi pentingnya jaminan produk halal, prosedur sertifikasi, serta manfaatnya dalam meningkatkan kepercayaan konsumen dan daya saing produk UMKM.")

with st.expander("2. Business Model Canvas (BMC)"):
    st.write("Membantu peserta memahami cara menyusun model bisnis secara sistematis, mulai dari identifikasi segmen pelanggan, proposisi nilai, saluran distribusi, hingga struktur biaya dan sumber pendapatan.")

with st.expander("3. Pencatatan Keuangan Sederhana"):
    st.write("Agar pelaku UMKM mampu mengelola arus kas, memisahkan keuangan usaha dengan keuangan pribadi, serta memiliki dasar yang lebih baik dalam mengambil keputusan bisnis.")

with st.expander("4. Digitalisasi Usaha (TikTok Shop & Google Business)"):
    st.write("Peserta memperoleh pelatihan pembuatan akun TikTok Shop dan Google Business sehingga produk yang dihasilkan memiliki peluang lebih besar untuk dikenal masyarakat melalui platform digital.")

# --- KELANJUTAN BERITA ---
st.write("""
Kegiatan ini tidak hanya berorientasi pada penyampaian materi, tetapi juga memberikan 
pendampingan praktis kepada peserta agar mampu mengimplementasikan pengetahuan yang diperoleh 
dalam pengelolaan usahanya. Melalui diskusi interaktif, peserta menyampaikan berbagai tantangan 
yang dihadapi, mulai dari pengembangan produk, pemasaran, hingga proses memperoleh sertifikasi halal.
""")

st.info("""
💡 **Hasil Evaluasi Kegiatan:**
Menunjukkan adanya peningkatan pemahaman peserta terhadap penerapan Business Model Canvas, 
pentingnya sertifikasi halal, pengelolaan keuangan usaha, serta pemanfaatan teknologi digital 
dalam pemasaran produk. Peningkatan tersebut diperoleh berdasarkan hasil evaluasi menggunakan 
kuesioner yang menunjukkan meningkatnya pemahaman mitra dalam mengadopsi teknologi dan inovasi.
""")

st.write("""
Selain meningkatkan kompetensi pelaku UMKM, kegiatan ini juga memperkuat sinergi antara 
perguruan tinggi, government desa, BUMDes, koperasi, dan masyarakat dalam membangun ekosistem 
usaha berbasis nilai-nilai Islam yang berkelanjutan. Kolaborasi tersebut diharapkan mampu mendorong 
lahirnya produk unggulan Desa Mekarmanik yang memiliki kualitas lebih baik, memenuhi standar halal, 
serta mampu bersaing di pasar yang semakin kompetitif.
""")

st.write("""
Melalui kegiatan pengabdian ini, Unisba menegaskan komitmennya dalam menjalankan tridarma 
perguruan tinggi, khususnya pengabdian kepada masyarakat, dengan menghadirkan solusi yang aplikatif 
bagi pengembangan ekonomi lokal. Pendampingan akan terus dilanjutkan melalui proses implementasi 
hasil pelatihan, penguatan kelembagaan usaha, serta fasilitasi sertifikasi halal sehingga manfaat 
program dapat dirasakan secara berkelanjutan oleh masyarakat Desa Mekarmanik.
""")

# --- FOOTER ---
st.write("---")
st.caption("© 2026 Program Studi Ekonomi Pembangunan - Universitas Islam Bandung (Unisba)")
