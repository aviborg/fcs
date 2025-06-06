## ✅ Automation Pipeline Overview

### **Step 1: Export Simulink Metadata**

Create scripts to extract:

* Model hierarchy
* Subsystems and functions
* Requirement links

### **Step 2: Export Requirements Traceability**

* Export Simulink Requirements (`.slreqx`) to XML/CSV

### **Step 3: Export Test and Coverage Reports**

* Simulink Test results
* Coverage metrics (decision, condition, MC/DC)

### **Step 4: Export Git Metadata**

* Commit messages, tags, file change history

---

## 🧩 Step-by-Step Script Examples

### 📘 1. Export Model Structure

```matlab
model = 'YourModelName';
load_system(model);

blocks = find_system(model, 'Type', 'Block');
fid = fopen('exports/model_structure.txt', 'w');

for i = 1:length(blocks)
    fprintf(fid, '%s\n', blocks{i});
end

fclose(fid);
```

### 📘 2. Export Requirements Links

```matlab
reqSet = slreq.find('Type','ReqSet');
slreq.export(reqSet, 'exports/req_trace.xml');
```

Or convert to CSV:

```matlab
links = slreq.find('Type','Link');
fid = fopen('exports/req_trace.csv', 'w');
fprintf(fid, 'ID,Source,Destination\n');
for i = 1:length(links)
    src = links(i).Source;
    dest = links(i).Destination;
    fprintf(fid, '%s,%s,%s\n', links(i).ID, src.Artifact, dest.Artifact);
end
fclose(fid);
```

### 📘 3. Export Test Results

```matlab
resultFile = 'exports/test_results.html';
sltest.testmanager.report(resultFile, ...
    'IncludeTestResults', true, ...
    'IncludeTestRequirements', true, ...
    'IncludeCoverage', true);
```

### 📘 4. Export Coverage Results

```matlab
cvdo = cvsim(model); % run coverage
cvhtml('exports/coverage_report', cvdo);
cvsave('exports/coverage_data', cvdo);
```

### 📘 5. Extract Git Metadata

From terminal (run in root of repo):

```bash
git log --pretty=format:"%h,%an,%ad,%s" > exports/git_log.csv
git diff HEAD^ HEAD --name-status > exports/git_diff.txt
```

---

## 🧠 Step 5: Feed to ChatGPT

Once the `exports/` folder contains:

* `model_structure.txt`
* `req_trace.csv`
* `test_results.html`
* `coverage_report/index.html`
* `git_log.csv`

You can zip and upload them here. I’ll generate:

* Requirements Traceability Matrix (RTM)
* Software Verification Report (SVR)
* Test Plan (SVP)
* Accomplishment Summary (SAS)
* Software Configuration Index (SCI)
* Tool Qualification evidence (if needed)

