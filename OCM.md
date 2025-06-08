# DO-178C Objective Compliance Matrix (Level B)

This matrix provides a summary of compliance with DO-178C objectives for software level B using model-based development with Simulink, Git version control, CI/CD, and AI-assisted documentation.

| Objective ID | Description                                        | Level B Req | Method of Compliance                             | Reference Artifact(s)                  | Status |
| ------------ | -------------------------------------------------- | ----------- | ------------------------------------------------ | -------------------------------------- | ------ |
| A-3 #1       | Plan for Software Aspects of Certification         | Yes         | Documented PSAC                                  | `planning/PSAC.md`                     | ✔️     |
| A-3 #2       | Software Development Plan                          | Yes         | Documented SDP                                   | `planning/SDP.md`                      | ✔️     |
| A-3 #3       | Software Verification Plan                         | Yes         | Documented SVP                                   | `planning/SVP.md`                      | ✔️     |
| A-3 #4       | Software Configuration Management Plan             | Yes         | Documented SCMP                                  | `planning/SCMP.md`                     | ✔️     |
| A-3 #5       | Software Quality Assurance Plan                    | Yes         | Documented SQAP                                  | `planning/SQAP.md`                     | ✔️     |
| A-3 #6       | Tool Qualification Plan                            | If needed   | GCC Tool Qualification Plan and Report           | `tool_qualification/TQP.md`, `TVR.md`  | ✔️     |
| A-4 #1       | High-level software requirements defined           | Yes         | Requirements in Markdown                         | `requirements/software.md`             | ✔️     |
| A-4 #2       | Software architecture described                    | Yes         | SAD and ICD created                              | `architecture/SAD.md`, `ICD.md`        | ✔️     |
| A-4 #3       | Low-level requirements described                   | Yes         | Reflected in model-level and Simulink components | `requirements/software.md`             | ✔️     |
| A-4 #4       | Source code consistent with low-level requirements | Yes         | Simulink-to-code trace, verified via AI          | `traceability/trace.yaml`              | ✔️     |
| A-4 #5       | Software design is consistent with architecture    | Yes         | Verified via Functional Decomposition Diagram    | `architecture/FDD.png`                 | ✔️     |
| A-4 #6       | Source code traceable to low-level requirements    | Yes         | RTM and Simulink block annotations               | `exports/RTM.md`                       | ✔️     |
| A-5 #1       | Reviews performed                                  | Yes         | GitHub PR reviews + markdown comments            | `reviews/*.md`                         | ✔️     |
| A-5 #2       | Test results reviewed                              | Yes         | Markdown test reviews in verification folder     | `verification/Verification_Report.md`  | ✔️     |
| A-5 #3       | Software quality assurance activities performed    | Yes         | Documented QA procedures and evidence            | `quality/SQA_Record.md`                | ✔️     |
| A-5 #4       | Configuration management activities performed      | Yes         | Git logs and SECI                                | `configuration/SECI.md`                | ✔️     |
| A-6 #1       | Software requirements coverage via tests           | Yes         | Requirements mapped to test cases                | `traceability/trace.yaml`              | ✔️     |
| A-6 #2       | Structural coverage (statement, decision, MC/DC)   | Yes         | Simulink Coverage reports + CI-based metrics     | `coverage/SimulinkCoverage.html`       | ✔️     |
| A-6 #3       | Robustness and boundary testing performed          | Yes         | Explicit test cases for edge inputs              | `testcases/TC_robust.md`               | ✔️     |
| A-6 #4       | Data and control coupling verified                 | Yes         | MBD test harness coverage                        | `verification/Verification_Report.md`  | ✔️     |
| A-7 #1       | Test results demonstrate requirements met          | Yes         | Results documented and passed in CI/CD           | `exports/Verification_Report.md`       | ✔️     |
| A-7 #2       | Tests verify correct code implementation           | Yes         | MBD test + object code analysis                  | `exports/fcs_disassembly.txt`          | ✔️     |
| A-7 #3       | Structural coverage met                            | Yes         | MC/DC coverage report generated                  | `coverage/SimulinkCoverage.html`       | ✔️     |
| A-7 #4       | No unintended functions                            | Yes         | Object code disassembly reviewed by AI           | `reports/disassembly_analysis.md`      | ✔️     |
| A-7 #5       | Tests performed on final object code               | Yes         | HIL or target testing via CI/CD pipeline         | `testlogs/target_output.log`           | ✔️     |
| A-8 #1       | Configuration identification                       | Yes         | All artifacts versioned in Git                   | `configuration/SECI.md`, `SCI.md`      | ✔️     |
| A-9 #1       | Software quality assurance activities documented   | Yes         | QA reviews, checklists, audit records            | `quality/SQA_Record.md`                | ✔️     |
| A-10 #1      | Tool qualification documented (if required)        | Optional    | TQP and tool verification results                | `tool_qualification/TVCP.md`, `TVR.md` | ✔️     |

---

**Legend:** ✔️ = Completed and compliant; 🚧 = In progress or requires review.

**Note:** All artifacts are version-controlled and reproducible using Git + CI/CD pipelines, and supported by AI-generated summaries, coverage validation, and traceability matrices.
