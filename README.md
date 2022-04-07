# unimi_bib
Library seat reservation automation for UNIMI with Python.

This program is aimed to automate the cumbersome reservations process for seats in UNIMI libraries. It opens a tkinter-GUI which lets you select floors in the Political Science library and the Sala Crociera. It then opens the reservation-URL and uses splinter to select/insert the correct information. Nothing fancy, just faster and less tedious that way.

To customize it to your own library you have to find your "number" by inspecting the webpage (you will need the library AND the floor number). Don't forget to put in your personal information in your script.
