import PyPDF2

filename = input("Eneter PDF filename: ")
ip = open(filename, 'rb')

pdfReader = PyPDF2.PdfFileReader(ip)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())
ip.close()