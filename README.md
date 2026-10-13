# SQL Information Extraction

This project extracts stored procedure information from a SQL file and saves it as a JSON file.

## What it does

The Python script uses regular expressions to extract:

- Stored procedure name
- Parameter direction (`IN`, `OUT`, `INOUT`)
- Parameter name
- Parameter data type

## Files

- `extraction.py` - Python script
- `sample_stored_procedure.sql` - Input SQL file
- `sample_stored_procedure.json` - Extracted output

## How to Run

Run the following command:

```bash
python extraction.py sample_stored_procedure.sql