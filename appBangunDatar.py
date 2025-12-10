import streamlit as st

#halaman utama
st.title('aplikasi perhitungan luas bangun datar')
st.header('ini buatan anak SI')

menu = st.sidebar.selectbox('pilih aplikasi',['luas persegi, 'luas segitiga', 'luas lingkaran'])

if menu == 'luas persegi':
    st.write(':blue[ini halaman untuk menghitung luas persegi]:balloon::balloon:')
st.image('https://www.doyanblog.com/wp-content/uploads/2023/05/rumus-luas-persegi.jpg')
sisi = st.number_input('silahkan masukkan sisi', min_value=0,)
if st.button('hitung'):
    luas = sisi * sisi
st.write(f'luas perseegi adalah {luas}')

    elif menu == 'luas segitiga':
        st.write('ini halaman untuk menghitung luas segitiga')