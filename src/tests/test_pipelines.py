from bs4 import BeautifulSoup

from scraper.items import DhOMessage
from scraper.pipelines import RemoveDhOBlockquotesPipeline, HtmlToTextPipeline


def test_dho_blockquotes_are_removed():

    # GIVEN some HTML with DhO-style block quote tag
    html = '<div class="quote other">A QUOTE</div>OTHER TEXT'

    # WHEN the HTML is filtered
    filtered = RemoveDhOBlockquotesPipeline._remove_blockquotes(html)

    # THEN the result does not contain quotes anymore (but other text)
    assert 'OTHER TEXT' in filtered
    assert 'A QUOTE' not in filtered


def test_html_is_removed_from_message(msg_with_blockquote):

    # GIVEN a DhO message with HTML tags
    html = msg_with_blockquote.msg
    assert '<' in html

    # WHEN the HTML is turned into text
    text = HtmlToTextPipeline._html_to_text(html)

    # THEN tags are removed and regular text preserved
    assert 'Buddha inflation' in text
    assert '<' not in text
