import json
import re


def convert_to_json(input_file, output_file):
    translations = {}

    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        stripped = line.strip()

        # Skip empty lines and comments
        if not stripped or stripped.startswith("#") or stripped.startswith("//"):
            continue

        # Split key and value by " = "
        if " = " in stripped:
            key, value = stripped.split(" = ", 1)
            key = key.strip()
            value = value.strip()

            # Add to dictionary
            translations[key] = value

    # Create the JSON structure expected by R2API
    json_output = {"strings": translations}

    # Write to JSON file with proper formatting
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(json_output, f, ensure_ascii=False, indent=4)

    print(f"Converted {len(translations)} translations to {output_file}")
    print(f"Output file: {output_file}")


# Usage
if __name__ == "__main__":
    input_file = "fi_converted.language"  # Your current plain text file
    output_file = "fi.json"  # Output JSON file

    convert_to_json(input_file, output_file)
