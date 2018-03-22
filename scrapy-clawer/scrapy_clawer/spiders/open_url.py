from selenium import webdriver

options = webdriver.ChromeOptions()
#options.binary_location = '/usr/bin/google-chrome-unstable'
options.add_argument('headless')
options.add_argument('window-size=1200x600')
browser = webdriver.Chrome(chrome_options=options)

browser.get('https://hydromet.lcra.org/riverreport')

tables = browser.find_elements_by_css_selector('table.table-condensed')

tbody = tables[5].find_element_by_tag_name("tbody")
for row in tbody.find_elements_by_tag_name("tr"):
    cells = row.find_elements_by_tag_name("td")
    if(cells[0].text == 'Marble Falls (Starcke)'):
        print(cells[1].text)

browser.quit()