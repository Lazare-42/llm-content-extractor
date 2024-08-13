import os
import sys
import anthropic

# Set up the Anthropic client
client = anthropic.Anthropic()

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Call the Anthropic API
        message = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1000,
            temperature=0,
            system="The following text is a code file, or of similar type. We need to extract the user facing content to an MD file. Just output the MD content.",
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
        
        return f"# Summary of {os.path.basename(file_path)}\n\n{message.content[0].text}\n\n"
    except Exception as e:
        return f"Error processing {file_path}: {str(e)}\n\n"

def main():
    if len(sys.argv) < 2:
        print("Usage: python claude_api_call.py <file1> <file2> ...")
        sys.exit(1)

    output = ""
    for file_path in sys.argv[1:]:
        output += process_file(file_path)

    # Write the output to output.md
    with open("output.md", "w") as output_file:
        output_file.write(output)

    print("Processing complete. Results written to output.md")

if __name__ == "__main__":
    main()
