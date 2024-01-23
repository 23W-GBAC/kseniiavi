import re


def extract_headlines(file_path):
    headlines = []
    try:
        with open(file_path, 'r', encoding='utf-8') as readme_file:
            for line in readme_file:
                # Use a regular expression to match Markdown-style headlines (lines starting with #)
                match = re.match(r'^#\s+(.+)', line)
                if match:
                    headline = match.group(1)
                    headlines.append(headline)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return headlines


if __name__ == "__main__":
    # Replace 'path/to/your/README.md' with the actual path to your README file
    readme_path = input("Enter the path to your README file: ")

    headlines = extract_headlines(readme_path)

    if headlines:
        print("Extracted Headlines:")
        for headline in headlines:
            print(f"- {headline}")
    else:
        print("No headlines found.")
