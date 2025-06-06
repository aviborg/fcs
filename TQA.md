# Tool Qualification Artifacts

---

## 1. Tool Operational Requirements (TOR)

### 1.1 Tool Identification

* **Tool Name:** GCC (GNU Compiler Collection)
* **Version:** 10.3-2021.10
* **Vendor:** GNU Project / ARM Embedded Toolchain
* **Host Environment:** Ubuntu 22.04 LTS
* **Target Architecture:** ARM Cortex-M4

### 1.2 Intended Use

* To compile C source code into executable object code (.elf, .bin) for embedded software deployed on airborne systems.

### 1.3 Tool Category

* **Category:** Development Tool
* **Function:** Code Translator (Compiler)
* **Classification:** Tool whose output is not verified by independent means → **Qualification required** under TQL-5 (if relied upon for verification output)

### 1.4 Operational Requirements

| Req ID  | Requirement Description                                                                   |
| ------- | ----------------------------------------------------------------------------------------- |
| TOR-001 | The tool shall compile C99-compliant source code into object code for ARM Cortex-M4.      |
| TOR-002 | The compiled code shall preserve logical behavior as defined by the source code.          |
| TOR-003 | The tool shall support deterministic optimizations suitable for safety-critical software. |
| TOR-004 | The tool shall provide debug symbols for traceability.                                    |
| TOR-005 | The tool shall be configurable with fixed flags and version-locked installation.          |
| TOR-006 | The tool shall not introduce unintended executable functions.                             |

---

## 2. Tool Qualification Plan (TQP)

### 2.1 Purpose

This document defines the plan for qualifying GCC for use in the airborne software development per DO-178C and DO-330.

### 2.2 Tool Classification and TQL

* **Tool Category:** Development tool
* **Tool Qualification Level:** TQL-5 (based on DO-330 Table B-1)

### 2.3 Qualification Approach

* Establish fixed configuration and version
* Perform requirement-based tool verification tests (TVCP)
* Analyze object code for fidelity, determinism, and absence of unintended code
* Document results and deviations

### 2.4 Tool Configuration Control

All compiler binaries, flags, and supporting files are tracked in Git. SHA256 hashes are logged in the Software Environment Configuration Index (SECI).

### 2.5 Tool Verification Plan Summary

* Unit tests to verify code translation behavior
* Object code disassembly analysis
* Optimization-level comparison tests

---

## 3. Tool Configuration Index (TCI)

### 3.1 Tool Configuration Summary

| Item               | Description                                                      |
| ------------------ | ---------------------------------------------------------------- |
| Tool Name          | GCC (arm-none-eabi-gcc)                                          |
| Version            | 10.3-2021.10                                                     |
| Executable Hash    | e9b5c7279c2a71e16745313cf845c2b09d38ae74e3127c53b52b4e30c6a7e531 |
| Build Flags        | -O2 -Wall -std=c99 -fshort-enums -mfloat-abi=hard                |
| Platform           | Ubuntu 22.04 LTS                                                 |
| Source Control Ref | tools/gcc-setup.sh @ commit 75ea6c1                              |

### 3.2 Supporting Scripts and Environment

* `tools/gcc-setup.sh`: Installation script
* `exports/compiler_flags.txt`: Compiler configuration snapshot
* `exports/compiler_hash.txt`: Binary hash log

---

## 4. Tool Verification Cases & Procedures (TVCP)

| TVC ID  | Related TOR | Description                                                                    |
| ------- | ----------- | ------------------------------------------------------------------------------ |
| TVC-001 | TOR-001     | Compile and execute basic C99 source file; verify correct output.              |
| TVC-002 | TOR-002     | Compare execution results of compiled object code at `-O0` vs. `-O2`.          |
| TVC-003 | TOR-003     | Execute loop unrolling and inlining edge cases; verify behavioral equivalence. |
| TVC-004 | TOR-004     | Generate symbol table; verify traceability from function names to source.      |
| TVC-005 | TOR-005     | Log build flags and verify hash matches approved config.                       |
| TVC-006 | TOR-006     | Disassemble ELF output; verify no unintended functions or padding code.        |

---

## 5. Tool Verification Results (TVR)

| TVC ID  | Result | Notes                                                                           |
| ------- | ------ | ------------------------------------------------------------------------------- |
| TVC-001 | PASS   | Output from basic arithmetic and logic tests matched expectations.              |
| TVC-002 | PASS   | `-O2` optimization preserved logic and test results; coverage matched baseline. |
| TVC-003 | PASS   | Inlining and unrolling had no observable impact on behavior.                    |
| TVC-004 | PASS   | Symbol table confirmed source-to-binary traceability.                           |
| TVC-005 | PASS   | Compiler hash and flags matched SECI record.                                    |
| TVC-006 | PASS   | Disassembly reviewed by AI and engineer; no anomalies found.                    |

All tool verification cases passed successfully. Compiler is cleared for use in the scope defined in the TQP.

---

**Prepared By:** Software Assurance Engineer
**Date:** 2025-06-06

**Attachments:**

* `exports/compiler_selftest.log`
* `exports/fcs_disassembly.txt`
* `exports/compiler_flags.txt`
* `reports/disassembly_analysis.md`
