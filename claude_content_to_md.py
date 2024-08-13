import os
import sys
import anthropic
import csv
from prompt import get_prompt, prompt_to_check_if_user_facing


# Set up the Anthropic client
client = anthropic.Anthropic()

CSV_FILE = 'extracted.csv'

def file_already_extracted(file_path):
    if not os.path.exists(CSV_FILE):
        return False
    with open(CSV_FILE, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        return any(row[0] == file_path for row in reader)

def add_to_csv(file_path):
    with open(CSV_FILE, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([file_path])

def is_user_facing(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        message = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1,
            temperature=0,
            messages=[
                {
                    "role": "user",
                    "content": prompt_to_check_if_user_facing(file_path, content)
                }
            ]
        )
        
        answer = message.content[0].text.strip().upper()
        return answer == 'YES'
    except Exception as e:
        print(f"Error checking if {file_path} is user-facing: {str(e)}")
        return False

def process_file(file_path):
    if file_already_extracted(file_path):
        print(f"Skipping {file_path} as it has already been extracted.")
        return ""
    if not is_user_facing(file_path):
        print(f"Skipping {file_path} as it is not user-facing.")
        return ""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Call the Anthropic API
        message = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1000,
            temperature=0,
            system=get_prompt(file_path),
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": content
                        }
                    ]
                }
            ]
        )
        
        return f"\n\n{message.content[0].text}\n\n"
    except Exception as e:
        return f"Error processing {file_path}: {str(e)}\n\n"

def main():
    if len(sys.argv) < 2:
        print("Usage: python claude_api_call.py <file1> <file2> ...")
        sys.exit(1)

    # print("prompt is", get_prompt())
    # output = ""
    # for file_path in sys.argv[1:]:
    #     output += process_file(file_path)

    # Write the output to output.md
    with open("output.md", "a") as output_file:
        for file_path in sys.argv[1:]:
            result = process_file(file_path)
            output_file.write(result)
            if "Error processing" not in result:
                add_to_csv(file_path) 

    print("Processing complete. Results written to output.md")

if __name__ == "__main__":
    main()
