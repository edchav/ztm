from pypdf import PdfReader, PdfWriter

# rb stands for read binary, needed to read pdf or else its a bunch of values
# some IDE or code editors won't be able to read the pdf unles rb is specified.
with open('dummy.pdf', 'rb') as file:
    # print(file) prints out an object called TextIOWrapper
    reader = PdfReader(file)
    page = reader.get_page(0)
    print(page.rotate(180)) # prints the obj in memory does not actually modify the file
    writer = PdfWriter()
    writer.add_page(page)
    with open('tilt.pdf', 'wb') as newFile:
        writer.write(newFile)