# Day 71: Data Exploration with Pandas

## Project Overview
An introduction to data science and exploratory data analysis using Pandas and Jupyter Notebooks. The project analyses a dataset of salaries by college major (sourced from PayScale Inc.) to answer real-world questions about earning potential, career risk, and degree group comparisons.

## Key Concepts Learned
- **Jupyter Notebooks**: Using interactive notebooks for iterative data exploration and inline output
- **DataFrame Inspection**: Loading CSV data and inspecting shape, head, tail, and null values
- **Data Cleaning**: Detecting and removing NaN rows with `isna()` and `dropna()`
- **Column Operations**: Accessing, aggregating, and computing derived columns from existing data
- **Sorting & Ranking**: Sorting DataFrames to identify top and bottom performers
- **GroupBy Analysis**: Grouping data by category to compare degree groups (STEM, HASS, Business)

## Technical Skills
- `pd.read_csv()` for loading CSV data into a DataFrame
- `df.shape`, `df.head()`, `df.tail()` for initial data inspection
- `df.isna()` for null value detection and `df.dropna()` for cleaning
- `df['column'].max()`, `.min()`, `.idxmax()`, `.idxmin()` for aggregation and index lookup
- `df.loc[]` and `df['column'][index]` for label-based and positional row access
- Column arithmetic and `.subtract()` for computing a salary spread (90th − 10th percentile)
- `df.insert()` for adding a computed column at a specific position
- `df.sort_values()` for ranking majors by spread and earning potential
- `df.groupby('Group').count()` for comparing STEM, HASS, and Business degree groups
- `pd.options.display.float_format` for formatting numeric output

## Analysis Performed

| Question | Answer |
|----------|--------|
| Highest starting salary major | Physician Assistant ($74,300) |
| Lowest starting salary major | Spanish ($34,000) |
| Highest mid-career median salary | Chemical Engineering ($107,000) |
| Lowest mid-career median salary | Education ($52,000) |
| Lowest salary spread (most predictable) | Nursing ($50,700 spread) |
| Highest salary spread (most variable) | Economics ($159,400 spread) |
| Highest earning potential (90th percentile) | Economics ($210,000) |

## Dataset
- **Source**: PayScale Inc. — `salaries_by_college_major.csv`
- **Shape**: 51 rows × 6 columns (50 majors + 1 footer row removed during cleaning)
- **Columns**: Undergraduate Major, Starting Median Salary, Mid-Career Median Salary, Mid-Career 10th Percentile Salary, Mid-Career 90th Percentile Salary, Group
- **Groups**: STEM (16 majors), HASS (22 majors), Business (12 majors)

## Project Structure
- `Data_Exploration_Jupyter_Notebooks.ipynb` - Main Jupyter Notebook with all analysis
- `salaries_by_college_major.csv` - Dataset from PayScale Inc.

## Setup
1. Create and activate a virtual environment
2. Install dependencies: `pip install pandas jupyter`
3. Launch Jupyter: `jupyter notebook`
4. Open `Data_Exploration_Jupyter_Notebooks.ipynb`
