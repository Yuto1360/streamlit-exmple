import streamlit as st
import requests

st.title("📚 BooKS API - 書籍検索アプリ")

# 検索キーワード入力
query = st.text_input("検索キーワードを入力してください", "Python")

if st.button("検索"):
    url = "http://openlibrary.org/search.json"
    params = {"q": query, "limit": 10}

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        docs = data.get("docs", [])

        if docs:
            for doc in docs:
                title = doc.get("title", "No Title")
                author = ", ".join(doc.get("author_name", ["Unknown"]))
                year = doc.get("first_publish_year", "Unknown")
                st.subheader(title)
                st.write(f"👤 著者: {author} | 📅 初版: {year}")
                # Open Library のページリンク
                if "key" in doc:
                    st.markdown(f"[📖 Open Libraryで見る](https://openlibrary.org{doc['key']})")
                st.markdown("---")
        else:
            st.warning("該当する書籍が見つかりませんでした。")
    except Exception as e:
        st.error(f"取得エラー: {e}")