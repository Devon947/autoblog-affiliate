import os
import requests

def post_to_blogger(title, content):
    api_key = os.getenv("BLOGGER_API_KEY")
    blog_id = os.getenv("BLOG_ID")

    url = f"https://www.googleapis.com/blogger/v3/blogs/{blog_id}/posts/"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "kind": "blogger#post",
        "title": title,
        "content": content
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200 or response.status_code == 201:
        print(f"✅ Posted: {title}")
    else:
        print(f"❌ Failed to post: {response.status_code}, {response.text}")
