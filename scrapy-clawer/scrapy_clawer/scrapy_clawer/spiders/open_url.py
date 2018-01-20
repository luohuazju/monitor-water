from selenium import webdriver

path2phantom = '/opt/phantomjs/bin/phantomjs'
browser = webdriver.PhantomJS(path2phantom)
browser.get('https://hydromet.lcra.org/riverreport')

tables = browser.find_elements_by_css_selector('table.table-condensed')

tbody = tables[5].find_element_by_tag_name("tbody")
for row in tbody.find_elements_by_tag_name("tr"):
    cells = row.find_elements_by_tag_name("td")
    if(cells[0].text == 'Marble Falls (Starcke)'):
        print cells[1].text

browser.quit()