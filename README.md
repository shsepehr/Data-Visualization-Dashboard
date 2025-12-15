# Data Visualization Dashboard

## Description
This tool generates interactive and static charts from CSV datasets using Python.  
Great for data analysis, reporting, and visualization of numeric trends.

## Features
- Histograms, KDE plots
- Line charts, scatter plots (can be added)
- Supports multiple numeric columns
- Generates separate PNG files per column

## Installation
pip install -r requirements.txt


## Usage
1. Place your CSV file (`sample_data.csv`)  
2. Run:
python dashboard.py

3. Outputs:
- PNG files for each numeric column (e.g., `sales_hist.png`, `profit_hist.png`)

## Example
Input CSV:


id,sales,profit
1,100,20
2,200,50
3,150,30
4,300,80

Outputs:  
`sales_hist.png`, `profit_hist.png`  

## Tech Stack
- Python
- Pandas
- Matplotlib
- Seaborn
- Plotly
