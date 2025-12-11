import streamlit as st

# halaman utama
st.title('aplikasi perhitungan luas bangun datar')
st.header('ini buatan anak SI')

menu = st.sidebar.selectbox('menu',['luas persegi','luas segitiga','luas lingkaran'])

if menu == 'luas persegi':
    st.write('ini halaman untuk menghitung luas persegi')
    st.image('https://www.doyanblog.com/wp-content/uploads/2023/05/rumus-luas-persegi-200x135.jpg', caption='gambar persegi')
    def luaspersegi(a):
        return a*a
    sisi = st.number_input('silahkan masukan sisi', min_value=0, )
    
    if st.button('hitung'):
        luas = luaspersegi(sisi)
        st.write(f'luas persegi adalah {luas} ')

elif menu == 'luas segitiga':
    st.write('ini halaman untuk menghitung luas segitiga')
    st.image('https://media.suara.com/pictures/970x544/2021/11/11/76640-rumus-luas-segitiga-jadijuaracom.jpg', caption='gambar segitiga')
    alas = st.number_input('masukan alas segitiga',min_value=0)
    tinggi = st.number_input('masukan tinggi segitiga', min_value=0, )
    
    if st.button('hitung'):
        luas = 0,5 * alas * tinggi
        st.success (f'luas segitiga adalah {luas}')

else :
    st.write('ini halaman untuk menghitung luas lingkaran')
    st.image('https://i.pinimg.com/736x/e3/ec/fc/e3ecfc747bbfe1186aa4992e19ea8596.jpg', caption='gambar lingkaran')
    def math_pi(r):
        return 3.14 * r * r
    jarijari = st.number_input('masukkan jari-jari lingkaran',min_value=0)
    
    if st.button('hitung_lingkaran') :
        luas_lingkaran = math_pi(jarijari)
        st.success (f'luas lingkaran adalah {luas_lingkaran}')