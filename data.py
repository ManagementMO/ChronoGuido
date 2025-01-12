import csv
import json

def convert_symptom_csv_to_jsonl(csv_file_path, jsonl_file_path):
    """
    Converts a CSV file with Disease and Symptom columns to a JSONL file.

    Each line in the JSONL will represent a disease and its associated symptoms
    in a format suitable for fine-tuning a generative AI model like Gemini.

    Args:
        csv_file_path: Path to the input CSV file.
        jsonl_file_path: Path to the output JSONL file.
    """
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as csv_file, \
                open(jsonl_file_path, 'w', encoding='utf-8') as jsonl_file:

            reader = csv.DictReader(csv_file)

            for row in reader:
                disease = row['Disease'].strip()
                symptoms = [row[f'Symptom_{i}'].strip() for i in range(1, 18) if row[f'Symptom_{i}'].strip()]

                # Create a prompt and response based on the disease and symptoms
                prompt = f"What are the symptoms of {disease}?"
                response = f"The symptoms of {disease} include: {', '.join(symptoms)}."

                # Create a JSON object for the current row
                json_obj = {
                    "input_text": prompt,
                    "output_text": response
                }

                # Write the JSON object to the JSONL file as a single line
                jsonl_file.write(json.dumps(json_obj) + '\n')

        print(f"Successfully converted '{csv_file_path}' to '{jsonl_file_path}'")

    except FileNotFoundError:
        print(f"Error: CSV file not found at '{csv_file_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example Usage:
csv_file_path = r'C:\Users\zozod\Downloads\DeltaHacks\dataset.csv'  # Your CSV file path
jsonl_file_path = 'training_data.jsonl'  # Path to save the JSONL file

convert_symptom_csv_to_jsonl(csv_file_path, jsonl_file_path)