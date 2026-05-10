import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi

st.set_page_config(page_title="مستخرج نصوص يوتيوب", layout="wide")

st.title("📺 مستخرج السبتيتل الذكي")
st.caption("انسخ النص من أي فيديو يوتيوب بسهولة")

url = st.text_input("ضع رابط الفيديو هنا:", placeholder="https://www.youtube.com/watch?v...")

if url:
    try:
        video_id = url.split("v=")[1].split("&")[0]
        st.video(url)
        st.subheader("📝 النص المستخرج:")
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['ar', 'en'])
        
        full_text = ""
        for entry in transcript:
            time = int(entry['start'])
            minutes = time // 60
            seconds = time % 60
            text = entry['text']
            st.markdown(f"**[{minutes:02d}:{seconds:02d}]** {text}")
            full_text += f"{text} "

        st.divider()
        st.download_button("تحميل النص كاملاً كملف", full_text)
        
    except Exception as e:
        st.error("عذراً، هذا الفيديو لا يحتوي على ترجمة مفعلة أو الرابط غير صحيح.")
