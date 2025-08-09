import streamlit as st

st.title("サンプル Streamlit ページ")
st.write("これは Streamlit で作成したシンプルなページです。")

name = st.text_input("お名前を入力してください")
if name:
    st.write(f"こんにちは、{name}さん！")
