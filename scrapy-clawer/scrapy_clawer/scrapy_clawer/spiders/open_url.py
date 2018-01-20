from selenium import webdriver
import os

path2phantom = '/opt/phantomjs/bin/phantomjs'
browser = webdriver.PhantomJS(path2phantom)
browser.get('https://hydromet.lcra.org/riverreport')

tables = browser.find_elements_by_css_selector('table.table-condensed')

#print tables[5].text
tbody = tables[5].find_element_by_tag_name("tbody")
#print tbody.text
for row in tbody.find_elements_by_tag_name("tr"):
    #print row.text
    cells = row.find_elements_by_tag_name("td")
    if(cells[0].text == 'Marble Falls (Starcke)'):
        print cells[1].text

browser.quit()