import streamlit as st
import joblib
import numpy as np
import json

# Load model
model = joblib.load('gbr_model.joblib')

# Judul aplikasi
st.title("📊 Prediksi Harga Rumah")
st.markdown("Upload file `.json` yang berisi data input untuk model regresi harga rumah.")

# Upload file JSON
uploaded_file = st.file_uploader("Upload file JSON", type="json")

if uploaded_file is not None:
    try:
        # Parse JSON
        input_json = json.load(uploaded_file)

        # Ambil input dari key "data"
        input_array = np.array(input_json["data"])

        st.subheader("📥 Input Data dari JSON:")
        st.write(input_array)

        # Tombol prediksi
        if st.button("🔮 Prediksi"):
            prediction = model.predict(input_array)[0]
            st.success(f"💰 Perkiraan harga rumah: **${prediction:,.2f}**")
    except Exception as e:
        st.error(f"❌ Terjadi kesalahan saat memproses file: {e}")
