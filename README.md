# Health Study Data Analysis - Individuell Uppgift

This repository contains Del 1 of the Health Study individual assignment.

## Overview

This project analyzes a health study dataset containing information about 800 participants, including:
- Age, sex, height, weight
- Systolic blood pressure (systolic_bp)
- Cholesterol levels
- Smoking status (smoker)
- Disease presence (disease)

## Project Structure

```
health_study_project/
├── .gitignore              # Git ignore file
├── README.md               # This file
├── RUN_ANALYSIS.md         # Instructions for running the analysis
├── requirements.txt        # Python dependencies
├── data/
│   └── health_study_dataset.csv  # Dataset (800 participants)
├── del1/                   # Del 1 files
│   └── health_analysis_del1.py   # Basic analysis script
└── output/                 # Generated visualizations (ignored)
```

## Del 1 Requirements

**Del 1 Requirements (G):**
- ✅ Descriptive analysis (mean, median, min, max)
- ✅ 3 different graphs (histogram, boxplot, bar chart)
- ✅ Simulation with numpy.random
- ✅ Confidence interval for systolic_bp
- ✅ Hypothesis testing (smokers vs non-smokers)

**Del 1 Requirements (VG):**
- ✅ Confidence interval with 2 methods (normal approximation + bootstrap)
- ✅ Power analysis simulation
- ✅ Method motivation and documentation

## Requirements

- **Python version:** 3.11 or higher (recommended: 3.14.3)
- **Dependencies:** See `requirements.txt`

### Required Libraries
```
numpy==1.26.4
pandas==2.2.2
matplotlib==3.9.2
scipy==1.14.1
scikit-learn==1.5.2
jupyter==1.0.0
ipykernel==6.29.5
seaborn==0.13.2
```

## Quick Start

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd health_study_project
   ```

2. **Create virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Del 1:**
   ```bash
   python del1/health_analysis_del1.py
   ```

## Del 1 Analysis Summary

The Del 1 script (`health_analysis_del1.py`) performs:

1. **Descriptive Statistics**
   - Calculates mean, median, min, max for: age, weight, height, systolic_bp, cholesterol
   
2. **Visualizations**
   - Histogram of systolic blood pressure
   - Boxplot of weight by gender
   - Bar chart of smoking prevalence

3. **Simulation**
   - Simulates 1000 individuals with same disease probability
   - Compares simulated vs actual disease prevalence

4. **Confidence Intervals**
   - Normal approximation for systolic_bp mean
   - Bootstrap method for systolic_bp mean (VG)
   - Comparison of both methods (VG)

5. **Hypothesis Testing**
   - Tests: "Smokers have higher mean blood pressure than non-smokers"
   - Uses t-test
   - Uses permutation test (VG)
   - Power analysis (VG)

6. **Documentation**
   - Method motivation (VG)
   - References to statistical theory

## Key Features

### Reproducibility
- Fixed random seed: `np.random.seed(42)`
- Relative file paths: `../data/health_study_dataset.csv`
- All graphs saved to `output/` directory

### Data Integrity
- Original dataset preserved in `data/` directory
- No modifications to source data
- All calculations performed on raw data

### Quality Assurance
- All code tested and verified

## Grading Criteria

### Godkänt (G)
- ✅ All Del 1 requirements met
- ✅ Code runs without errors
- ✅ Proper use of Python libraries

### Väl Godkänt (VG)
- ✅ All G requirements
- ✅ Additional methods (bootstrap, permutation test)
- ✅ Power analysis
- ✅ Method motivation and documentation

## Submission

To submit your work:

1. Make sure your GitHub repository is **public**
2. Test that the script runs successfully
3. Submit the GitHub repository URL

## Notes

- The `.venv` directory is excluded via `.gitignore`
- The `output/` directory is excluded via `.gitignore`
- All Python scripts use UTF-8 encoding
- All visualizations are saved as PNG files

## Contact

For questions or issues, please refer to the assignment instructions or contact your instructor.

---

**Project created:** November 2024  
**Python version:** 3.14.3  
**Author:** [Your Name]
