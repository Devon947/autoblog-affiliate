import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_blog_post(keyword):
    prompt = (
        f"Write a full-length SEO-optimized blog post about '{keyword}'. "
        "Include a catchy title, introduction, subheadings, and conclusion. Format in HTML."
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    content = response.choices[0].message["content"]
    title_start = content.find("<h1>") + 4
    title_end = content.find("</h1>")
    title = content[title_start:title_end] if title_start > 3 and title_end > title_start else keyword.title()
    return title, content
