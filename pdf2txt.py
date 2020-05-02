import PyPDF2
import sys
from PyPDF2 import utils
try:
        for pdf in sys.argv[1:]:
                
                pdfobj = open(pdf, 'rb')
                txtnme = pdf[:-4]       #cuts out ".pdf" extension

                pdfreader = PyPDF2.PdfFileReader(pdfobj)

                print(f"Total Pages::\t{pdfreader.numPages}\nPlease wait while your pdf is converting to txt file.")
                mlt = open(f"{txtnme}.txt", "a")
                for num in range(pdfreader.numPages):
                        
                        page_obj = pdfreader.getPage(num)

                        st = page_obj.extractText()
                        mlt.write(st)

                mlt.close()
                input(f"\aYour text file is saved {txtnme}.txt.")
                pdfobj.close()

except IndexError:
        input("""\aNote: Drag and Drop your pdf file over the
python icon. It ain't execut-able, man\a""")

except utils.PdfReadError:       #handles the error when file format other than .pdf is dragged and dropped over
        input("""\aPlease choose a ".pdf" file format.
Press Enter to close the window""")
