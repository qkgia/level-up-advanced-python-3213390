import re


def convert_italics(html):
    html = re.sub(r'<\/?em>', "*", html)
    
    return html


def convert_spaces(html):
    html = re.sub(r'\s{1,}', " ", html)

    return html


def convert_paragraphs(html):
    html = re.sub(r'^<p>', "", html)
    html = re.sub(r'</p>$', "", html)
    html = re.sub(r'</p><p>', "\n\n", html)
    
    return html


def convert_urls(html):
    matches_urls = re.findall(r'href="(.*?)"', html)
    matches_name = re.findall(r'<a .*?>(.*?)</a>', html)
    matches = re.findall(r'(<a .*?>.*?</a>)', html)

    for match, match_name, match_url in zip(matches, matches_name, matches_urls):
        html = html.replace(match, '[{}]({})'.format(match_name, match_url))
    return html


def html2markdown(html):
    '''Take in html text as input and return markdown'''

    html = convert_italics(html)

    html = convert_spaces(html)

    html = convert_paragraphs(html)

    html = convert_urls(html)

    return html
