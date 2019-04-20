from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'C:\\Py\\geckodriver.exe')


# path = 'file:///' + 'C:\\Path\\To\\Local\\file\\index.html'

path = "https://ortegajohn.github.io/Pokemon_fix/"

driver.get (path)

PageSource = driver.page_source

PageSplit = PageSource.splitlines()

pokemon_list = []

for line in PageSplit:
    if 'pokelist.push' in line:
        start = 0
        end = 0
        for j in range(len(line)):
            if line[j:j+2] == '( ':
                start = j+3
            if line[j:j+2] == ' )':
                end = j-1
        pokemon_list.append(line[start:end])


print(pokemon_list)

click_go = driver.find_element_by_id('begin-button')
click_go.click()

for i in pokemon_list:

    input_name = driver.find_element_by_id('form-name-input')
    input_name.send_keys(i)

    click_submit = driver.find_element_by_xpath(".//*[@id='submit-form']/input[2]")
    click_submit.click()
