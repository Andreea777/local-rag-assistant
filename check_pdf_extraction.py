from pypdf import PdfReader

reader = PdfReader("data/docs/France.pdf")
for i, page in enumerate (reader.pages[:3]):  # just first 3 pages
    text = page.extract_text() or ""
    print(f"--- Page {i+1} ({len(text)} characters) ---")
    print(text[:300])  # print first 300 characters of the page
    print()
