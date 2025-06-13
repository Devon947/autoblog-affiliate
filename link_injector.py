import os

def inject_affiliate_links(keyword, html_content):
    amazon_tag = os.getenv("AMAZON_TAG")
    clickbank_id = os.getenv("CLICKBANK_ID")

    amazon_link = f"https://www.amazon.com/s?k={keyword.replace(' ', '+')}&tag={amazon_tag}"
    clickbank_link = f"https://{clickbank_id}.hop.clickbank.net/?cbitems={keyword.replace(' ', '_')}"

    affiliate_html = (
        f'<p>Check it out on Amazon: <a href="{amazon_link}" target="_blank">{keyword}</a></p>'
        f'<p>Or find similar offers on ClickBank: <a href="{clickbank_link}" target="_blank">{keyword}</a></p>'
    )

    call_to_action = (
        f'<p><strong>Ready to take action?</strong> <a href="{clickbank_link}" target="_blank">'
        f'Click here to learn more</a>.</p>'
    )

    # Insert after first paragraph and before end
    html_parts = html_content.split("</p>", 1)
    if len(html_parts) == 2:
        html_content = html_parts[0] + "</p>" + affiliate_html + html_parts[1] + call_to_action
    else:
        html_content += affiliate_html + call_to_action

    return html_content
