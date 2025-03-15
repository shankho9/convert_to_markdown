import os
import pypandoc

def convert_docx_to_md(input_path, output_path=None):
    if not output_path:
        output_path = os.path.splitext(input_path)[0] + ".md"
    
    try:
        pypandoc.convert_file(input_path, 'gfm', outputfile=output_path)
        print(f"✅ Conversion complete! Markdown file saved at: {output_path}")
    except Exception as e:
        print(f"❌ Error during conversion: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python markdownconvertor.py <path_to_docx_file>")
    else:
        convert_docx_to_md(sys.argv[1])
