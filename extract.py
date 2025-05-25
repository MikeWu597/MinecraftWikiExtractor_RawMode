# extract.py

import os
import json

def extract_content_from_jsonl(jsonl_file, output_dir="result_extracted"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(jsonl_file, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data = json.loads(line.strip())
                content = data['response']['body']['choices'][0]['message']['content']
                custom_id = data['custom_id']

                output_path = os.path.join(output_dir, f"{custom_id}.md")
                with open(output_path, 'w', encoding='utf-8') as out_f:
                    out_f.write(content)
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error processing line: {e}")
                continue

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python extract.py <input_jsonl_file>")
        sys.exit(1)

    jsonl_file = sys.argv[1]
    extract_content_from_jsonl(jsonl_file)