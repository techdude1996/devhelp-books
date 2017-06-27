#!/usr/bin/python
# Blender API Scraper

from bs4 import BeautifulSoup
import sys, getopt
from lxml import etree

def main(argv):
    url = ''
    try:
        opts, args = getopt.getopt(argv, "hu:f:")
    except getopt.GetoptError:
        print 'blender_api.py [-h] [-u <url>] [-f <context.html path>]'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'Blender API Scraper Usage:'
            print 'To Scrape a web url:       blender_api.py -u <content.html url>'
            print 'To Scrape a local file:    blender_api.py -f <content.html path>'
            print 'To view this help message: blender_api.py -h'
            sys.exit(0)
        elif opt == '-u':
            scrape_url(arg)
            sys.exit(0)
        elif opt == '-f':
            scrape_file(arg)
            sys.exit(0)
    print 'Blender API url is: ' + url


def scrape_url(url):
def scrape_file(path):
    processing = True
    folder_path = os.path.dirname(os.abspath(path))
    # Set the home page flag for unique processing
    home_page = True
    # Get the current page:
    current_page = 'content.html'
    # Create the xml document:
    book_node = etree.Element('book')
    book = etree.ElementTree(book_node)
    book_node.attrib['xmlns'] = 'http://www.devhelp.net/book'
    book_node.attrib['title'] = 'Blender 2.78c API Documentation'
    book_node.attrib['link'] = 'content.html'
    book_node.attrib['author'] = 'Blender Foundation'
    book_node.attrib['name'] = 'blender-api-doc'
    book_node.attrib['version'] = '2.78c'
    book_node.attrib['language'] = 'Python'
    book_node.attrib['online'] = 'https://docs.blender.org/api/blender_python_api_2_78c_release/'

    chapters = etree.SubElement(book_node, 'chapters')
    functions = etree.SubElement(book_node, 'functions')
    while processing:
        # Open the HTML file to process:
        file html_doc = open(path, 'r+')
        # Read the HTML file into a string:
        html_raw = html_doc.read()
        # Create a structure (soup) for the html string:
        html_soup = BeautifulSoup(html_raw)
        # Find and get the current page name:
        current_page_title = html_soup.find_all("h1").text
        # Find and get the next chapter:
        next_page = html_soup.find("a", title="next chapter").a['href']
        # Scrape the current page:
        scrape_html()

# Funciton to recursively scrape all of the html pages, one at a time:
def scrape_html(top_node, functions_node, html_page, current_page):
    html_soup = BeautifulSoup(html_page)
    # Process categories first
    html_entries = html_soup.find_all("div", class="section")
    # xml_header = etree.SubElement(parent_node, html_entries[0].parent.text)
    del html_sections[0]
    previous_level = 1
    for html_headers in html_entries:
        current_header = html_headers.find("h" + str(current_level))


if __name__ == '__main__':
    main(sys.argv[1:])
