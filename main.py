import PyPDF2

merger = PyPDF2.PdfMerger()
pdfiles = ["1.pdf","2.pdf"]
for i in pdfiles:
    pdffile = open(i,'rb')
    pdfreader=PyPDF2.PdfReader(pdffile)
    merger.append(pdfreader)
pdffile.close()
merger.write("Merged pdf.pdf")
