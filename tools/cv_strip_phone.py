"""Usage: uv run --with pymupdf python tools/cv_strip_phone.py IN.pdf OUT.pdf

Builds the public CV for assets/marc-riera_cv.pdf from the quick-apply CV PDF.
Remove the phone number from the CV header contact line: redact the whole
line (text is deleted, not covered) and re-set it centred without the number."""
import sys, pymupdf
FONT = "/Applications/LibreOffice.app/Contents/Resources/fonts/truetype/LiberationSans-Regular.ttf"
src, dst = sys.argv[1], sys.argv[2]
doc = pymupdf.open(src)
page = doc[0]
hit = None
for b in page.get_text("dict")["blocks"]:
    for l in b.get("lines", []):
        for s in l["spans"]:
            if "+44" in s["text"]:
                hit = s
assert hit, "phone line not found"
new = hit["text"].split(" | +44")[0]
assert new.endswith("marc@riera.co.uk"), new
size, base = hit["size"], hit["origin"][1]
centre = (hit["bbox"][0] + hit["bbox"][2]) / 2
page.add_redact_annot(pymupdf.Rect(hit["bbox"]), fill=False)
page.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE, graphics=pymupdf.PDF_REDACT_LINE_ART_NONE)
font = pymupdf.Font(fontfile=FONT)
w = font.text_length(new, fontsize=size)
page.insert_font(fontname="LibSans", fontfile=FONT)
page.insert_text((centre - w / 2, base), new, fontname="LibSans", fontsize=size, color=(0, 0, 0))
doc.subset_fonts()
doc.save(dst, garbage=4, deflate=True)
