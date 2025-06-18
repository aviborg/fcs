# **Software Modeling Methodology using Simulink**

## 1. Purpose

This document defines the methodology for software modeling using **Simulink** to ensure consistency, quality, traceability, and compliance with applicable standards such as **DO-178C** and **DO-331**.

---

## 2. Scope

This methodology applies to all software components modeled in **MathWorks Simulink** and **Stateflow** as part of the Model-Based Development (MBD) process.

---

## 3. References

* RTCA DO-178C – Software Considerations in Airborne Systems
* RTCA DO-331 – Model-Based Development and Verification Supplement
* MathWorks Simulink User Guide
* Company-Specific Modeling Standards

---

## 4. Tools and Environment

| Tool                  | Purpose                       |
| --------------------- | ----------------------------- |
| MATLAB/Simulink       | Modeling and simulation       |
| Simulink Coder        | Code generation (C/C++)       |
| Simulink Test         | Test harness and verification |
| Simulink Coverage     | Structural coverage analysis  |
| Polyspace Code Prover | Static code analysis          |
| Git/GitHub            | Version control               |
| Github                | Automation pipeline           |

---

## 5. Modeling Methodology

### 5.1 Development Workflow

1. **Requirement Import and Linking**

   * Import requirements using `Requirements Toolbox`
   * Link Simulink elements to high-level and low-level requirements

2. **Model Design**

   * Create top-down hierarchical models
   * Use atomic subsystems for modularity
   * Apply control/data flow separation

3. **Simulation and Behavioral Verification**

   * Simulate models using test inputs
   * Use `Simulink Test` for test scenarios
   * Document expected vs. actual outputs

4. **Model Review**

   * Peer review against modeling guidelines
   * Verify completeness, correctness, and style

5. **Code Generation**

   * Use `Simulink Coder` with verified settings
   * Ensure MISRA C compliance if required

6. **Software-in-the-Loop (SIL) Testing**

   * Execute generated code in MATLAB/Simulink to verify functional equivalence

7. **Hardware-in-the-Loop (HIL) Testing**

   * Optional: deploy on target platform for integration testing

---

### 5.2 Modeling Rules and Best Practices

| Rule ID | Description                                                            |
| ------- | ---------------------------------------------------------------------- |
| MR-001  | Use **atomic subsystems** for code generation boundaries               |
| MR-002  | Avoid **algebraic loops** unless mathematically justified              |
| MR-003  | Use **typed buses** for interface definition                           |
| MR-004  | Annotate each block with **rationale or requirement reference**        |
| MR-005  | Maintain **one output per block** when possible                        |
| MR-006  | Do not use **Goto/From** blocks in safety-critical logic               |
| MR-007  | Use **Model Advisor** with a custom checklist                          |
| MR-008  | Keep signal names consistent with requirements                         |
| MR-009  | Limit **Stateflow complexity** (e.g., no more than 2 hierarchy levels) |
| MR-010  | Time-based logic must use **discrete-time blocks** only                |

---

### 5.3 Model Verification Activities

| Activity                  | Tool                 | Output              |
| ------------------------- | -------------------- | ------------------- |
| Requirements Traceability | Requirements Toolbox | Traceability Matrix |
| Structural Coverage       | Simulink Coverage    | Coverage Report     |
| Model Testing             | Simulink Test        | Test Results        |
| Static Analysis           | Polyspace            | Code Quality Report |
| Model Check               | Model Advisor        | Pass/Fail Checklist |

---

## 6. Code Generation

### 6.1 Configuration

Use the following code generation settings:

* **System Target File**: `ert.tlc`
* **Language**: C (or C++ as required)
* **Generate Code Only**: Enabled for review before build
* **Include Comments**: Enabled with trace to model
* **Optimization**: Level 2 (with care to preserve traceability)
* **File Packaging**: Create separate `.c` and `.h` per subsystem

### 6.2 Naming Conventions

* Models: `SWC_<ComponentName>`
* Subsystems: `SS_<Function>`
* Signals: `sig_<Name>_<Unit>`
* Parameters: `param_<Name>_<Unit>`
* States: `st_<Name>`

---

## 7. Instructions

### 7.1 Creating a New Model

```matlab
new_system('SWC_Controller');
open_system('SWC_Controller');

add_block('built-in/Inport','SWC_Controller/In1');
add_block('built-in/Outport','SWC_Controller/Out1');
add_block('simulink/Commonly Used Blocks/Gain','SWC_Controller/Gain');
```

### 7.2 Simulating the Model

```matlab
set_param('SWC_Controller', 'SimulationCommand', 'start');
```

### 7.3 Generating Code

```matlab
rtwbuild('SWC_Controller');
```

### 7.4 Verifying Code Equivalence (SIL)

```matlab
sltest.testmanager.run;
results = sltest.testmanager.getResults;
disp(results.Status);
```

---

## 8. Configuration Management

* All models are version-controlled using Git
* Branching strategy: `main`, `dev`, `feature/*`, `release/*`
* CI Pipeline:

  * Run `Model Advisor` on commit
  * Execute test cases
  * Generate artifacts (code, reports, traceability)

---

## 9. Deliverables

| Deliverable         | Format           | Location             |
| ------------------- | ---------------- | -------------------- |
| Simulink Model      | `.slx`           | `models/`            |
| Test Harness        | `.slx`           | `test/`              |
| Code                | `.c`, `.h`       | `codegen/`           |
| Traceability Matrix | `.xlsx`, `.html` | `docs/traceability/` |
| Coverage Report     | `.html`          | `docs/coverage/`     |
| Verification Report | `.pdf`           | `docs/verification/` |

---

## 10. Review and Auditing

* All modeling activities undergo **peer review**
* Review checklist includes:

  * Compliance with modeling rules
  * Test completeness
  * Code traceability
* Model snapshots are archived for audits

---

## 11. Appendix

### A. Model Advisor Custom Configuration

Use the following checks:

* Simulink Check > Modeling Standards
* Stateflow Check > Design Issues
