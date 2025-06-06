
import yaml

# Load the traceability YAML
with open('traceability/trace.yaml', 'r') as file:
    trace_data = yaml.safe_load(file)

# Generate RTM as Markdown
with open('exports/RTM.md', 'w') as out:
    out.write('| Requirement ID | Model Block | Test Case | Parent Requirement |\n')
    out.write('|----------------|-------------|-----------|--------------------|\n')
    for req_id, trace in trace_data.items():
        out.write(f"| {req_id} | {trace['model_block']} | {trace['test_case']} | {trace['parent']} |\n")

print("RTM generated at exports/RTM.md")
