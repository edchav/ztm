from pypdf import PdfWriter, PdfReader

watermark = PdfReader('wtr.pdf').pages[0]
writer = PdfWriter("merged.pdf")

for page in writer.pages:
    page.merge_page(watermark, over=False)

writer.write("out_watermark.pdf")
