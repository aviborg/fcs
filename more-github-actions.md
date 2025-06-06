## ✅ Recommended GitHub Actions for DO-178C MBD Projects

### 1. ✅ **Run Simulink Compliance Checks**

Use MATLAB Actions to run **Model Advisor** checks or custom rule sets (e.g., MAAB).

```yaml
- name: Run MAAB Compliance Check
  run: |
    matlab -batch "checkModelCompliance('models/FCS_main.slx')"
```

Add a function `checkModelCompliance.m`:

```matlab
function checkModelCompliance(model)
  load_system(model);
  advisor = Simulink.ModelAdvisor.getModelAdvisor(model);
  advisor.setCheck('maab');
  advisor.run;
  advisor.saveReport('exports/model_advisor_report.html','html');
end
```

---

### 2. ✅ **Auto-generate Requirements Traceability Matrix**

Use exported requirements and model structure from `generate_exports.m` and process with Python.

```yaml
- name: Generate Requirements Traceability Matrix
  run: python3 scripts/generate_rtm.py
```

This script reads `exports/req_trace.csv` and `exports/model_structure.txt` and outputs `exports/RTM.xlsx`.

---

### 3. ✅ **Verify Coverage Thresholds (MC/DC)**

After running Simulink coverage:

```yaml
- name: Check MC/DC Coverage Threshold
  run: python3 scripts/check_coverage.py
```

Example `check_coverage.py`:

```python
from bs4 import BeautifulSoup

with open("exports/coverage_report/index.html", "r") as f:
    soup = BeautifulSoup(f, "html.parser")

coverage = float(soup.find("td", text="MC/DC").find_next("td").text.strip('%'))
assert coverage >= 95.0, f"MC/DC coverage {coverage}% below threshold"
```

---

### 4. ✅ **Upload Artifacts to GitHub Release**

Automatically attach generated reports to your tagged release.

```yaml
- name: Upload Documents to GitHub Release
  uses: softprops/action-gh-release@v1
  with:
    files: |
      exports/*.html
      exports/*.pdf
      exports/*.zip
```

> Requires this to run on `on: push: tags:` so it triggers only for release tags.

---

### 5. ✅ **Generate PDF Reports (Using LaTeX or Pandoc)**

If you generate Markdown outputs (e.g., SAS.md, SVP.md), convert them to PDF.

```yaml
- name: Convert Markdown to PDF
  run: |
    sudo apt install pandoc texlive-xetex -y
    pandoc documents/SAS.md -o exports/SAS.pdf
```

---

### 6. ✅ **Lint or Validate Requirements Format**

Basic consistency check for requirement IDs or YAML/CSV structure.

```yaml
- name: Validate Requirements Format
  run: python3 scripts/validate_requirements.py
```

Example: check for missing REQ-IDs, duplicates, empty fields.

---

### 7. ✅ **Run Model-Based Testing in CI**

If your tests are automated using Simulink Test Manager:

```yaml
- name: Run Simulink Test Suite
  run: matlab -batch "runTestSuite('tests/FCS_TestSuite.mldatx')"
```

With helper `runTestSuite.m`:

```matlab
function runTestSuite(testFile)
  sltest.testmanager.load(testFile);
  results = sltest.testmanager.run;
  sltest.testmanager.report(results, ...
    'FilePath', 'exports/test_results_ci.html', ...
    'IncludeTestResults', true);
end
```

---

### 8. ✅ **Trigger Tool Qualification Check**

Verify that qualified tools haven’t changed or require requalification.

```yaml
- name: Verify Tool Integrity
  run: sha256sum tools/tool_versions.json > exports/tool_hashes.txt
```

Then compare it with stored baseline to detect drift.

