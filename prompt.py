def get_prompt(file_path):
    return f"""The following text is from the file: {file_path}
This file may contain code or text content we need to extract. Our goal is to extract the user-facing content to an MD file. Just output the MD content.

On top of the output, add the path to the file containing the content, like this:
# Page: {file_path}

Here's an example:
# Page: ../pages/api-pricing.tsx

##  Meeting Baas 🐟 | Pricing

Run your own meeting bots with AI in 2 minutes

Sign up, get 4 hours free then pay $0.69 / hour. Pay less as you scale.

DO NOT ADD YOUR OWN TITLE AT THE BEGINNING, THE FILE PATH AS PROVIDED IS THE TITLE. AS YOU CAN SEE IT'S THE MD TITLE WITH a #
DO NOT MODIFY OR INVENT A FILE PATH, USE THE ONE PROVIDED EXACTLY AS IS
"""

def prompt_to_check_if_user_facing(file_path, content):
    return f"""Based on the following file content, determine if this file is user-facing (i.e., contains content that would be directly visible or relevant to end-users of a website or application).
    
    File path: {file_path}
    
    File content:
    {content}
    
    Answer with ONLY 'YES' if the file is user-facing, or 'NO' if it is not. Do not provide any explanation, just the single word answer."""

