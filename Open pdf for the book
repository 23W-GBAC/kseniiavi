import webbrowser, re
from googlesearch import search


def get_first_google_link(query_to_search):
    try:
        # Perform a Google search and get the first result
        search_results = search(query_to_search, num_results=1)
        first_result = next(search_results, None)

        if first_result:
            print(f"Opening the first result: {first_result}")
            # Open the first result in the default web browser
            webbrowser.open(first_result)
        else:
            print("No search results found.")
    except Exception as e:
        print(f"An error occurred: {e}")



def extract_headlines(file_path):
    headlines = []

    try:
        with open(file_path, 'r', encoding='utf-8') as readme_file:
            for line in readme_file:
                # Use a regular expression to match Markdown-style headlines (lines starting with #)
                match = re.match(r'^##\s+(.+)', line)
                if match:
                    headline = match.group(1)
                    headlines.append(headline)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return headlines



if __name__ == "__main__":
    # Replace 'path/to/your/README.md' with the actual path to your README file
    readme_path = input("Enter the path to your README file: ")
    # C:\Users\79163\Desktop\Универ\дз\kseniiavi-main\README.md
    headlines = extract_headlines(readme_path)

    if headlines:
#        print("Extracted link:")
#        for headline in headlines:
        Number = int(input("Type the number of the book: ")) - 1

        query_to_search = str(headlines[Number]) + " " + "read"
        pdf_url = get_first_google_link(query_to_search)
#        print(pdf_url)
    else:
        print("No headlines found.")





