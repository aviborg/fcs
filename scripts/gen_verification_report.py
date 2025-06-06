
import yaml
from datetime import datetime

# Load verification results
with open('traceability/results.yaml', 'r') as file:
    results = yaml.safe_load(file)

# Generate Markdown report
with open('exports/Verification_Report.md', 'w') as out:
    out.write(f"# Software Verification Report\n")
    out.write(f"**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    out.write("| Test Case | Requirement | Result | Tested On | Coverage | Notes |\n")
    out.write("|-----------|-------------|--------|-----------|----------|-------|\n")

    for tc_id, data in results.items():
        req = data.get("requirement", "N/A")
        result = data.get("result", "N/A")
        date = data.get("tested_on", "N/A")
        notes = data.get("notes", "")
        coverage = data.get("coverage", "N/A")
        out.write(f"| {tc_id} | {req} | {result} | {date} | {coverage} | {notes} |\n")

print("Verification Report generated at exports/Verification_Report.md")
