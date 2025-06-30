import random
import string
import streamlit as st

# ---------- 🎨 CSS للتنسيق ----------
st.markdown("""
    <style>
    /* خلفية كاملة */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1604145559206-7a3e34aa2d25?auto=format&fit=crop&w=1950&q=80");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* تظبيط صندوق المحتوى */
    .block-container {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
    }

    /* تعديل شكل الزر */
    .stButton > button {
        background-color: #6C63FF;
        color: white;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 10px;
    }

    /* تكبير العنوان */
    h1 {
        color: #2c3e50;
        text-align: center;
    }

    /* تحسين المخرجات */
    .stSuccess {
        font-size: 20px;
        color: #2c3e50;
    }

    </style>
""", unsafe_allow_html=True)

# ---------- 🧠 عنوان التطبيق ----------
st.title("🔐 Stylish Password Generator")

# ---------- 📝 إدخال البيانات ----------
length_of_word = st.number_input("🔢 Total password length:", min_value=1, step=1)
length_of_litters = st.number_input("🔡 Letters:", min_value=0, step=1)
length_of_numbers = st.number_input("🔢 Numbers:", min_value=0, step=1)
length_of_symbols = st.number_input("❗Symbols:", min_value=0, step=1)

# ---------- زر توليد الباسورد ----------
if st.button("🚀 Generate Password"):
    thetotal = length_of_litters + length_of_numbers + length_of_symbols

    if thetotal != length_of_word:
        st.error("❌ The total doesn't match! Please check your input.")
    else:
        # توليد المكونات
        letters_choiced = random.choices(string.ascii_letters, k=length_of_litters)
        numbers_choiced = random.choices(string.digits, k=length_of_numbers)
        symbols_choiced = random.choices(string.punctuation, k=length_of_symbols)

        # دمج وفردهم
        big_list = [letters_choiced, numbers_choiced, symbols_choiced]
        flat_list = []
        for sublist in big_list:
            for char in sublist:
                flat_list.append(char)

        # Shuffle & Join
        random.shuffle(flat_list)
        password = ''.join(flat_list)

        # ---------- عرض الباسورد ----------
        st.success("🎉 Your generated password is:")
        st.code(password, language='text')
