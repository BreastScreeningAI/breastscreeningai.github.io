import os
import sys

import pdfplumber


for path in sys.argv[1:]:
    print(f"\n### {path}")
    print(f"exists {os.path.exists(path)}")
    if not os.path.exists(path):
        continue
    try:
        with pdfplumber.open(path) as pdf:
            print(f"pages {len(pdf.pages)}")
            content = "\n".join((page.extract_text() or "") for page in pdf.pages)
            print(content[:12000])
    except Exception as exc:
        print(f"ERROR {exc!r}")
