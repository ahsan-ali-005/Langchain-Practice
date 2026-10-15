from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import json

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

st.header("AI Blog Generator")

with open("Prompts/prompt_template.json", "r", encoding="utf-8") as f:
    template_data = json.load(f)

raw_template = template_data.get("template", template_data) if isinstance(template_data, dict) else template_data

niche = st.selectbox("Your Blog niche", ('Tech', 'Finance', 'Medical'))
blog_topic = st.text_input("Topic")
primary_keyword = st.text_input("Primary Keyword")
target_audience = st.text_input("Target Audience")
length = st.selectbox("Words of Blog", ('300', '500', '600'))
tone = st.selectbox("Tone", ('Formal', 'Friendly', 'Professional'))
writing_style = st.selectbox("Writing Style", ('Beginner Friendly', 'High Level', 'Article type'))


if st.button("Generate Blog"):
    if not blog_topic or not primary_keyword or not target_audience:
        st.warning("Please fill in all required text fields before generating.")
    else:
        with st.spinner("Generating blog post..."):
            prompt = raw_template.format(
                niche=niche,
                blog_topic=blog_topic,
                primary_keyword=primary_keyword,
                target_audience=target_audience,
                length=length,
                tone=tone,
                writing_style=writing_style
            )
            
            response = model.invoke(prompt)
            st.markdown("### Output")
            st.write(response.content[0]["text"].strip())