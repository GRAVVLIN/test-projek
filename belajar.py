import streamlit as st
import pandas as pd

def main():
    st.title('INAUGURAKOM 2023')

    # Sidebar untuk navigasi
    menu = st.sidebar.radio("INAUGURAKOM 2023", ["BAHTERA NAWASENA", "ADD YOUR PRESENCE HERE"])

    if menu == "BAHTERA NAWASENA":
        st.write("LOGO BAHTERA BAWASENA")
        st.image('INAU_PICS.png', caption='BAHTERA NAWASENA', use_column_width=True)

    elif menu == "ADD YOUR PRESENCE HERE":
        st.subheader("WRITE HERE 💜")

        # Membuat input field untuk nama dan angkatan
        nama = st.text_input('Masukkan Nama')
        angkatan = st.selectbox('Pilih Angkatan', list(range(1996, 2023)))

        # Mengecek apakah kedua input sudah diisi
        if st.button('Submit'):
            if nama and angkatan:
                # Membuat DataFrame untuk menyimpan data
                df = pd.DataFrame({'Nama': [nama], 'Angkatan': [angkatan]})

                # Menyimpan data ke dalam file Excel
                try:
                    existing_data = pd.read_excel('absensi.xlsx')
                    updated_data = pd.concat([existing_data, df], ignore_index=True)
                    updated_data.to_excel('absensi.xlsx', index=False)
                except FileNotFoundError:
                    df.to_excel('absensi.xlsx', index=False)

                st.success(f"Data berhasil disimpan!\nNama: {nama}\nAngkatan: {angkatan}")
            else:
                st.warning("Mohon isi kedua field dengan benar.")
        # Menampilkan daftar nama dan angkatan yang sudah diinput dari file Excel
        try:
            absensi_data = pd.read_excel('absensi.xlsx')
            st.subheader("Daftar Nama dan Angkatan yang Sudah Diinput:")
            st.write(absensi_data)
        except FileNotFoundError:
            st.warning("Belum ada data absensi yang tersimpan.")

if __name__ == '__main__':
    main()
