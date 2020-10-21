import pyttsx3
import PyPDF2
book = open('python sci.pdf', 'rb')
pdReader = PyPDF2.PdfFileReader(book)
pages = pdReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdReader.getPage(7)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
