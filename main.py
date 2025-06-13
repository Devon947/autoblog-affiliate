from modules.keyword_finder import get_keyword
from modules.content_generator import generate_blog_post
from modules.link_injector import inject_affiliate_links
from modules.autoposter_blogger import post_to_blogger
import os

def main():
    posts_per_run = int(os.getenv("POSTS_PER_RUN", 1))
    for _ in range(posts_per_run):
        keyword = get_keyword()
        title, html_content = generate_blog_post(keyword)
        html_with_links = inject_affiliate_links(keyword, html_content)
        post_to_blogger(title, html_with_links)

if __name__ == "__main__":
    main()
