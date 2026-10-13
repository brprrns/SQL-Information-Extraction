import json
import re
import sys
from pathlib import Path


def extract_procedures(sql_text):
    procedures = []

    procedure_pattern = re.compile(
        r"CREATE\s+PROCEDURE\s+(\w+)\s*\((.*?)\)\s*BEGIN",
        re.IGNORECASE | re.DOTALL
    )

    parameter_pattern = re.compile(
        r"\b(IN|OUT|INOUT)\s+(\w+)\s+"
        r"([A-Z]+(?:\s*\([^)]*\))?)",
        re.IGNORECASE
    )

    matches = procedure_pattern.findall(sql_text)

    for procedure_name, parameters_text in matches:
        parameters = []

        for direction, name, data_type in parameter_pattern.findall(
            parameters_text
        ):
            parameters.append(
                {
                    "direction": direction.upper(),
                    "name": name,
                    "type": data_type.upper()
                }
            )

        procedures.append(
            {
                "name": procedure_name,
                "parameters": parameters
            }
        )

    return {"procedures": procedures}


def main():
    if len(sys.argv) != 2:
        print("Usage: python extraction.py <sql_file>")
        sys.exit(1)

    sql_file = Path(sys.argv[1])

    if not sql_file.exists():
        print(f"File not found: {sql_file}")
        sys.exit(1)

    sql_text = sql_file.read_text(encoding="utf-8")

    result = extract_procedures(sql_text)

    output_file = sql_file.with_suffix(".json")

    with output_file.open("w", encoding="utf-8") as file:
        json.dump(result, file, indent=2)

    print(f"Output created: {output_file}")


if __name__ == "__main__":
    main()