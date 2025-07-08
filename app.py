import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Cek Jadwal Jagamu?", page_icon="📅")

st.title("📅 Cek Jadwal Jagamu?")
st.write("Mau ada acara yaaa...? Ayo cek dulu jadwal jagamu!")

with st.form("shift_checker"):
    tanggal_pagi1 = st.date_input("Masukkan tanggal Jaga Pagi ke-1", format="DD-MM-YYYY")
    tanggal_dicek = st.date_input("Masukkan tanggal yang ingin dicek", format="DD-MM-YYYY")
    submitted = st.form_submit_button("Cek")

if submitted:
    shift_pattern = [
        "Pagi ke-1", "Pagi ke-2",
        "Sore ke-1", "Sore ke-2",
        "Malam ke-1", "Malam ke-2",
        "Libur ke-1", "Libur ke-2"
    ]

    delta_hari = (tanggal_dicek - tanggal_pagi1).days
    if delta_hari < 0:
        st.error("Tanggal yang dicek tidak boleh sebelum tanggal awal jaga.")
    else:
        index_shift = delta_hari % len(shift_pattern)
        shift_hari_ini = shift_pattern[index_shift]
        st.success(f"Pada tanggal {tanggal_dicek.strftime('%d-%m-%y')}, kamu masuk: **{shift_hari_ini}**")
