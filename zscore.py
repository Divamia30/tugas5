import streamlit as st
import math
import pandas as pd
import numpy as np

def main():
    st.title("Mencari Apa Yang Mau Kamu Cari")
    
  
    st.sidebar.title("Aku Bisa Membantumu")
    menu = st.sidebar.radio("Go to", ["Menghitung Uji Statustik Prporsi satu populasi"])

    
    if menu == "Nilai Z-Score":
        st.write("Menghitung Nilai Proporsi Z-Score")
    if menu == "Nilai T-Score":
        st.write("Menghitung Nilai T-Score")


if __name__ == "__main__":
    main()


def Nilai_Z_Score(sampel_proporsi, populasi_proporsi, banyak_sampel):
    p_hat = sampel_proporsi
    p = populasi_proporsi
    n = banyak_sampel
    q = 1-p

    z = (p_hat - p)/ math.sqrt((p *q)/n)
    return z


def main():
    st.title("Menghitung Z-Score Proporsi")

    sampel_proporsi = st.number_input("Proporsi Sampel", min_value=0.0, max_value=1.0, step=0.01)
    populasi_proporsi = st.number_input("Proporsi Populasi", min_value=0.0, max_value=1.0, step=0.01)
    banyak_sampel = st.number_input("Banyak Sampel", min_value=0, max_value=30, step=0)

    if st.button("Hitung"):
        z_score = Nilai_Z_Score(sampel_proporsi, populasi_proporsi, banyak_sampel)
        st.success(f"Nilai Z-Score adalah {z_score:.4f}")
        st.balloons()

if __name__ == '__main__':
    main()