# Compiler Confidence Report

## 1. Introduction

This document provides compiler confidence evidence for the use of GCC in the development of safety-critical airborne software under RTCA DO-178C, Level B. The compiler is treated as a non-qualified tool, with confidence derived through controlled configuration, validation testing, and AI-assisted analysis of generated object code.

## 2. Compiler Identification

* **Compiler Name:** GCC (GNU Compiler Collection)
* **Target Architecture:** ARM Cortex-M4
* **Version:** `arm-none-eabi-gcc (GNU Arm Embedded Toolchain) 10.3-2021.10`
* **Executable Path:** `/usr/bin/arm-none-eabi-gcc`
* **SHA256 Hash:** `e9b5c7279c2a71e16745313cf845c2b09d38ae74e3127c53b52b4e30c6a7e531`
* **Build Flags:** `-O2 -Wall -fshort-enums -std=c99 -mfloat-abi=hard`

## 3. Configuration Control

The compiler binary and flags are locked through the CI/CD configuration and tracked via hash digest. The configuration is documented in:

* `exports/compiler_version.txt`
* `exports/compiler_hash.txt`
* `exports/compiler_flags.txt`
  These files are committed in the source repository and referenced in the Software Environment Configuration Index (SECI).

## 4. Behavior Verification via Test Cases

A suite of known-output test cases was compiled and executed to validate correct code generation and execution behavior.

### 4.1 Test Categories

* Integer and floating-point arithmetic
* Bitwise logic and masking
* Structure packing and alignment
* Pointer arithmetic
* Volatile and atomic access
* Loop unrolling and branching

### 4.2 Results

All test cases passed successfully. Output logs are stored in `exports/compiler_selftest.log` and verified by CI jobs and reviewed by AI assistant.

## 5. Object Code Analysis

### 5.1 Disassembly Review

The executable (`bin/fcs.elf`) was disassembled using `objdump`. Key points validated:

* Each function in the source is traceable in the object code
* No evidence of injected or compiler-generated functions outside expected set
* Function inlining matches optimization expectations

Report reviewed by AI for anomalies: see `exports/fcs_disassembly.txt` and AI summary in `reports/disassembly_analysis.md`.

### 5.2 Unused Code Analysis

Static and dynamic code coverage results confirm no unintended code is present in final build. Analysis tools include:

* `gcov`
* Simulink Coverage

## 6. Optimization Safety Checks

Object code was built under both `-O0` and `-O2`. The resulting binaries:

* Passed identical test suites
* Matched structural coverage within 99.8%

AI-reviewed results confirm functional and structural equivalence.

## 7. Flag Configuration Audit

Compiler flags were reviewed for:

* Determinism
* Safety impact
* Optimization risks

AI-assisted review concluded that current flags are acceptable under DO-178C Level B assumptions. See `reports/compiler_flag_review.md`.

## 8. Conclusion

Based on version control, known-behavior tests, disassembly reviews, and AI validation, the compiler is shown to produce predictable and verifiable object code within the scope of its use.

**Qualification Level:** Not formally qualified (TQL-5 not invoked)
**Verification Method:** Confidence built through structural testing and independent validation.

The compiler is acceptable for use in this DO-178C Level B project.

---

**Prepared By:** Software Assurance Engineer
**Date:** 2025-06-06

---

**Attachments:**

* `exports/compiler_selftest.log`
* `exports/compiler_flags.txt`
* `exports/fcs_disassembly.txt`
* `reports/compiler_flag_review.md`
* `reports/disassembly_analysis.md`
