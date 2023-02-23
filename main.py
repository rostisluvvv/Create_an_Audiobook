import PyPDF2
import pyttsx3
from pyttsx3 import engine

file_to_read = 'book/lorem_ipsum.pdf'
pdfReader = PyPDF2.PdfFileReader(open(file_to_read, 'rb'))
speaker = pyttsx3.init()

for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()

speaker.stop()

engine.save_to_file(text, f'{file_to_read}.audio')
engine.runAndWait()