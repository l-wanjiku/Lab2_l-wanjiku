# Lab 2: ALU Transcript Generator & Workspace Organizer

## Overview
This repository contains the complete solution for **Lab 2** at the African Leadership University (ALU). The project features a robust Python academic transcript evaluator (`grade-evaluator.py`) that enforces ALU grading policies, calculates weighted GPAs, determines category-specific pass/fail statuses, and identifies target assignments for resubmission. It also includes an automated Bash utility (`organizer.sh`) to manage workspace archiving and logging.

---

## Repository Structure

* **`grade-evaluator.py`**: Python script that processes student grades from CSV data, performs score and weight validations, computes category percentages and final GPAs on a 5.0 scale, and checks resubmission criteria.
* **`grades.csv`**: The primary input data source containing assignment names, category groups, scores, and weights.
* **`organizer.sh`**: Bash shell script that automates backing up current grade files into a timestamped `archive/` folder, resets the workspace with a fresh template, and updates `organizer.log`.
* **`README.md`**: Project documentation and execution guide.

---

## ALU Grading Rules Enforced
1. **Category Weighting**: Formative assessments carry a total weight of 60%, and Summative assessments carry 40% (Total = 100%).
2. **Independent Pass Thresholds**: Students must independently pass both categories (Formative $\ge 30/60$ or $50\%$; Summative $\ge 20/40$ or $50\%$). Failing either category results in an overall failure.
3. **GPA Scale**: Final GPAs are calculated on ALU's standard **5.0 scale**.
4. **Resubmission Logic**: If a student fails overall, the script identifies the eligible failed Formative assignment(s) with the highest weight to target for resubmission.

---

## Execution Instructions

### 1. Run the Grade Evaluator (Python)
Execute the Python script in your terminal and enter your CSV filename (e.g., `grades.csv`) when prompted:
```bash
python grade-evaluator.py
2. Run the Workspace Organizer (Bash)
To archive your current grades with a timestamp, clean your workspace, and log the activity, run:

Bash
bash organizer.sh
(Note: Ensure the shell script has execution permissions by running chmod +x organizer.sh first).
