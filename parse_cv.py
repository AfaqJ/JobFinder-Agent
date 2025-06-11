
import os
from PyPDF2 import PdfReader   
from docx import Document        

def extract_text_from_pdf(path):
    """
    Extract all text from a PDF file.
    Args:
        path (str): Path to the PDF file.
    Returns:
        str: The concatenated text of all pages.
    """
    # 1. Initialize the PDF reader for the given file path
    reader = PdfReader(path)
    # 2. Prepare a list to hold text from each page
    all_text = []
    # 3. Loop over every page in the PDF
    for page in reader.pages:
        #   a) Attempt to extract text; if None, use empty string
        text = page.extract_text() or ""
        #   b) Append this page’s text to our list
        all_text.append(text)
    # 4. Join all page texts with newline separators into one big string
    return "\n".join(all_text)

def extract_text_from_docx(path):
    """
    Extract all text from a .docx file.
    Args:
        path (str): Path to the DOCX file.
    Returns:
        str: The concatenated text of all paragraphs.
    """
    # 1. Load the DOCX document
    doc = Document(path)
    # 2. Extract each paragraph’s text into a list
    paragraphs = [para.text for para in doc.paragraphs]
    # 3. Join paragraphs with newline separators into one big string
    return "\n".join(paragraphs)

def main():
    """
    Main entry point:
      1) Detect CV file in input/
      2) Extract its text via PDF or DOCX extractor
      3) Write the result to data/cv.txt
    """
    input_dir = "input"
    output_file = os.path.join("data", "cv.txt")

    # 1. Scan input/ for a PDF or DOCX file
    for fname in os.listdir(input_dir):
        if fname.lower().endswith(".pdf"):
            # 1a. If it’s a PDF, extract using our PDF function
            text = extract_text_from_pdf(os.path.join(input_dir, fname))
            break
        if fname.lower().endswith(".docx"):
            # 1b. If it’s a DOCX, extract using our DOCX function
            text = extract_text_from_docx(os.path.join(input_dir, fname))
            break
    else:
        # 1c. If neither found, inform the user and exit
        print("No cv.pdf or cv.docx found in input/. Please add your CV there.")
        return

    # 2. Ensure the data/ directory exists
    os.makedirs("data", exist_ok=True)
    # 3. Write the extracted text to data/cv.txt using UTF-8 encoding
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)
    # 4. Inform the user of success
    print(f"✅ CV text extracted to {output_file}")

# Only run main() when this script is executed directly:
if __name__ == "__main__":
    main()
