# LLM Content Extractor

## Purpose

This project is designed to automatically extract user-facing content from various file types and convert it into Markdown format. It's particularly useful  to quickly generate documentation or content summaries from codebases, where user facing content is disseminated.
You can then easily input that content to another LLM for ghost-writing, finding answers, irrelancies, ...

## How It Works

1. The script scans through specified files in your project.
2. It uses the Anthropic API (Claude AI) to determine if a file contains user-facing content.
3. If the file is deemed user-facing, the script extracts the relevant content and converts it to Markdown format.
4. The extracted content is appended to an `output.md` file.
5. The script keeps track of processed files to avoid duplicate extractions in a `extracted.csv`. file.

## Key Features

- Automatic detection of user-facing content
- Conversion of various file types to Markdown
- Avoidance of duplicate processing
- Utilization of advanced AI (Claude) for content extraction and summarization

## Prerequisites

- Python 3.x
- Anthropic API key

## Setup

1. Clone the repository:
   ```
   git clone [repository-url]
   cd llm_content_extractor
   ```

2. Set up your Anthropic API key:
   ```
   export ANTHROPIC_API_KEY='your-api-key-here'
   ```

3. Run the setup script to create a virtual environment and install dependencies:
   ```
   chmod +x set_up_and_run.sh
   ./set_up_and_run.sh
   ```

## Usage

To extract content from files, run:

```
./set_up_and_run.sh file1.py file2.js file3.html
```

Replace `file1.py`, `file2.js`, `file3.html` with the paths to the files you want to process.

The script will:
- Create and activate a virtual environment
- Install necessary dependencies
- Run the content extraction process
- Deactivate the virtual environment when done

## Output

- Extracted content is appended to `output.md` in the project root.
- A list of processed files is maintained in `extracted.csv` to avoid reprocessing.

## Notes

- The script uses the Anthropic API, which may incur costs. Please check your usage and pricing.
- Ensure your API key is kept secure and not shared publicly.

## Contributing

Contributions to improve the script or extend its functionality are welcome. Please submit pull requests or open issues for any bugs or feature requests.

## License

MIT
