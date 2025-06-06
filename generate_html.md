## ✅ 1. Source Format: Use Markdown or YAML

You're already using:

* `requirements/*.md`
* `traceability/trace.yaml`
* `traceability/results.yaml`

These are excellent inputs because they’re:

* Structured
* Easy to convert
* Version-controllable in Git

---

## ✅ 2. Convert to HTML Using a Generator

Here are **3 good options** to create HTML reports in GitHub Actions:

---

### ⚙️ Option A: Use `Pandoc` (easy)

```bash
pandoc exports/RTM.md -o exports/RTM.html
pandoc exports/Verification_Report.md -o exports/Verification_Report.html
```

> ✔ Great for converting Markdown to HTML or PDF
> ✖ Doesn't support custom styling without tweaking

#### Add to GitHub Actions:

```yaml
- name: Install Pandoc
  run: sudo apt-get update && sudo apt-get install -y pandoc

- name: Convert Reports to HTML
  run: |
    pandoc exports/RTM.md -o exports/RTM.html
    pandoc exports/Verification_Report.md -o exports/Verification_Report.html
```

---

### ⚙️ Option B: Use a Python HTML Generator (customizable)

You can extend your `gen_rtm.py` to generate HTML instead of Markdown:

```python
with open('exports/RTM.html', 'w') as out:
    out.write('<html><head><title>RTM</title></head><body><h1>Requirements Trace Matrix</h1><table border="1">')
    out.write('<tr><th>Requirement ID</th><th>Model Block</th><th>Test Case</th><th>Parent</th></tr>')
    for req_id, trace in trace_data.items():
        out.write(f"<tr><td>{req_id}</td><td>{trace['model_block']}</td><td>{trace['test_case']}</td><td>{trace['parent']}</td></tr>")
    out.write('</table></body></html>')
```

> ✔ Full control over formatting and CSS
> ✔ Can embed charts, links, tooltips
> ✖ More scripting effort

---

### ⚙️ Option C: Use a Static Site Generator (e.g., MkDocs)

If you want a **navigable documentation website**, use:

```bash
pip install mkdocs
```

Structure your project like:

```
docs/
  index.md
  requirements.md
  rtm.md
  verification.md
mkdocs.yml
```

Then run:

```bash
mkdocs build
```

GitHub Action:

```yaml
- name: Build Docs with MkDocs
  run: |
    pip install mkdocs
    mkdocs build
```

> ✔️ Fully styled, searchable HTML documentation
> ✔️ Easily hosted with GitHub Pages
> ✖️ More setup, suited for ongoing web access

---

## ✅ 3. Optional Enhancements

| Feature              | Tool                  |
| -------------------- | --------------------- |
| Export to PDF too    | Pandoc / WeasyPrint   |
| Embed coverage plots | Python + Matplotlib   |
| Create dashboard     | GitHub Pages + HTML   |
| Package as ZIP       | GitHub Release Assets |

---

## 🔚 Summary

| Method     | Best For                     | Tools          |
| ---------- | ---------------------------- | -------------- |
| **Pandoc** | Simple Markdown → HTML       | `pandoc`       |
| **Python** | Custom tables, inline logic  | `open()`, HTML |
| **MkDocs** | Website-like structured docs | `mkdocs`       |

