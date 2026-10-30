# Real-World Student Performance Analysis

A Python exploratory data analysis project using the UCI Student Performance Mathematics dataset.

## Dataset
- Source: UCI Machine Learning Repository — Student Performance
- File used: `student-mat.csv` (Mathematics subject)
- Records: 395
- Attributes: 33
- The source CSV is semicolon-separated, so the project reads it with `sep=";"`.

## Project objectives
1. Inspect dataset structure and data quality.
2. Check missing values and duplicate records.
3. Explore final grades, study time, absences and grade progression.
4. Create visualizations and interpret the results.
5. Export a validated analysis copy.

## Run locally
```bash
python -m pip install -r requirements.txt
python main.py
```

## Key findings
- Average final grade (G3): 10.42
- Students with G3 >= 10: 265 (67.1%)
- Correlation of G2 with G3: 0.905
- Correlation of study time with G3: 0.098

## Data quality
The supplied Mathematics dataset contains no missing values and no duplicate rows in this inspection. The cleaned CSV is an exported validated copy; no rows were invented or dropped.

## License and attribution
Dataset: UCI Machine Learning Repository, Student Performance. Please retain attribution to the original dataset authors and repository when reusing the data.
