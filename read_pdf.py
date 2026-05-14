import sys

try:
    import pypdf
    reader = pypdf.PdfReader(sys.argv[1])
    for i, page in enumerate(reader.pages):
        print(f"--- Page {i+1} ---")
        print(page.extract_text())
except ImportError:
    print("pypdf not installed. Trying PyMuPDF (fitz)...")
    try:
        import fitz
        doc = fitz.open(sys.argv[1])
        for i, page in enumerate(doc):
            print(f"--- Page {i+1} ---")
            print(page.get_text())
    except ImportError:
        print("PyMuPDF not installed either. Let's try PyPDF2...")
        try:
            import PyPDF2
            reader = PyPDF2.PdfReader(sys.argv[1])
            for i, page in enumerate(reader.pages):
                print(f"--- Page {i+1} ---")
                print(page.extract_text())
        except ImportError:
            print("No PDF reading libraries found. Please install pypdf: pip install pypdf")
