# Issuu-Profile-Parser
Parses all the document links from an issuu.com profile

It requires the use of Selenium, Geckodriver, Firefox and Python3.

To install Selenium run the following command on Powershell/Terminal

`pip install selenium`

You can download the Geckodriver [here](https://github.com/mozilla/geckodriver/releases). Once you download it, open the zip and put
the file in the same file with the script. You will need to change the path of the drive in the file in the line that contains: 
`driver = webdriver.Firefox(options=options,executable_path=r'C:\Users\%%USER%%\Desktop\linkconverter\geckodriver.exe')`

To run the program you just type `python ./issuulinkscraper.py`
