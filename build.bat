pyinstaller.exe .\main.py .\parse.py .\pdfCreator.py .\App.py --name fermage.exe -F
xcopy  .\dist\fermage.exe .\fermage.exe* /y
