import random
import string
import streamlit as st

st.title("🔐 Password Generator")

# المستخدم يدخل البيانات من خلال Streamlit
length_of_word = st.number_input("Enter total number of characters in the password:", min_value=1, step=1)
length_of_litters = st.number_input("Enter number of letters:", min_value=0, step=1)
length_of_numbers = st.number_input("Enter number of numbers:", min_value=0, step=1)
length_of_symbols = st.number_input("Enter number of symbols:", min_value=0, step=1)

# لما المستخدم يضغط على الزر
if st.button("Generate Password"):
    thetotal = length_of_litters + length_of_numbers + length_of_symbols

    if thetotal != length_of_word:
        st.error("❌ Invalid input! The sum of letters, numbers, and symbols doesn't match the total length.")
    else:
        # توليد مكونات الباسورد
        letters_choiced = random.choices(string.ascii_letters, k=length_of_litters)
        numbers_choiced = random.choices(string.digits, k=length_of_numbers)
        symbols_choiced = random.choices(string.punctuation, k=length_of_symbols)

        # دمجهم في قائمة وحدة
        big_list = [letters_choiced, numbers_choiced, symbols_choiced]
        flat_list = []
        for sublist in big_list:
            for char in sublist:
                flat_list.append(char)

        # Shuffle + Join
        random.shuffle(flat_list)
        password = "".join(flat_list)

        # عرض النتيجة
        st.success(f"🔐 Your Generated Password: {password}")
        st.code(password, language="text")
