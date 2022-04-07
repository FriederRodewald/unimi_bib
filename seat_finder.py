from tkinter import *
from functools import partial
from splinter import Browser
import time


def lookup(floor):

    #executes chromedriver for selenium-automation
    executable_path = {'executable_path':r'C:\Users\Gangolf\.wdm\drivers\chromedriver\win32\chromedriver.exe'}
    browser = Browser('chrome', **executable_path, error = True, headless = False)

    #numbers found by inspecting (<select id="area" ...>)
    bib_selected = "44" #Science Politiche
    
    if floor == '-2':
        bib_spec_selected = "37" #Piano Meno Due
    if floor == '-1':
        bib_spec_selected = "44" #Piano Meno Uno
    if floor == '1':
        bib_spec_selected = "36" #Primo Piano
    if floor == '2':
        bib_spec_selected = "35" #Secondo Piano
    if floor == '3':
        bib_spec_selected = "34" #Terzo Piano

    if floor == 'S':
        bib_selected = "2" #Sala Crociera
        bib_spec_selected = "6" #Sala

    try:
        #open browser and insert information
        url = "https://orari-be.divsi.unimi.it/PortaleEasyPlanning/biblio/index.php?include=form"
        browser.visit(url)

        bib = browser.find_by_name('area').first
        bib.select(bib_selected)

        bib_spec = browser.find_by_name("servizio")
        bib_spec.select(bib_spec_selected)

        date = browser.find_by_name("data_inizio")
        date.click()
        time.sleep(0.1)
        date_active = browser.find_by_css('td[class="active day"]')
        time.sleep(0.1)
        date_active.click()

        #insert your correct information here!
        browser.fill('codice_fiscale', 'FSDISN...')
        browser.fill('cognome_nome', 'Ringar, Fox')
        browser.fill('email', 'fox.ringar@gmail.com')

        browser.find_by_id("verify").click()

        #browser.find_by_css('span[class="custom-icon custom-plus custom-default"]').click()

        lbl=Label(window, text="Hey, it worked. \nNow just pick your desired slot! \n\nIf you need another slot, just click on the buttons.", fg='black', justify= 'left', font=("Helvetica", 10))
        lbl.place(x = 15, y = 120)

        

    except:
        #error message (mostly if no date available)
        lbl=Label(window, text="Oops; something went wrong. \nProbabaly there are no dates available for this floor. \n\nJust try another floor!", fg='black', justify= 'left', font=("Helvetica", 10))
        lbl.place(x = 15, y = 120)

        browser.quit()


#code for the GUI
window = Tk()
window.title('Pick your LibSlot')
window.geometry('400x200+1200+300')

lbl=Label(window, text="Welcome. You've chosen some library. \nOn which floor do you want to study?", fg='black', justify= 'left', font=("Helvetica", 10))
lbl.place(x = 20, y = 15)


floors = ['-2', '-1', '1', '2', '3', 'S']

for i, floor in enumerate(floors):
    btn = Button(window, text=floor, fg='black', width = 3, command = partial(lookup, floor))
    btn.place(x = 30 + 50*i, y = 80)

#txtfld = Entry(window, text="This", bd = 2)
#txtfld.place(x = 10, y = 100)

window.mainloop()



