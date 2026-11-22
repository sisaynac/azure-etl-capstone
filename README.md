# Azure End-to-End ETL Capstone Project

## Project Overview
This project demonstrates an end-to-end data engineering ETL pipeline using Microsoft Azure services and Power BI.

## Architecture
Data Source → Azure Blob Storage (Raw) → Azure Data Factory → Data Transformation → Azure Blob Storage (Curated) → Power BI Dashboard.

## Technologies Used
- Microsoft Azure
- Azure Blob Storage
- Azure Data Factory
- Mapping Data Flow
- Power BI
- GitHub

## Project Structure
- data/raw: Original raw dataset storage.
- data/curated: Processed and cleaned data.
- pipelines: Azure Data Factory pipeline documentation.
- scripts: Data processing scripts.
- dashboards: Power BI dashboard files.

## Pipeline Status
The Azure Data Factory pipeline was validated and successfully executed in Debug mode. The transformed output was saved in the curated storage container.

## Dashboard
The Power BI dashboard includes:
- Total Sales
- Sales by Product
- Monthly Sales Trend
- Sales Distribution by Region
- Sales Channel filter

## Author
Data Engineering Capstone Project
## Datasets

- `data/raw/retail_sales_raw.csv`: Original retail sales dataset.
- `data/curated/retail_sales_curated.csv`: Cleaned and transformed retail sales dataset.

## Project Evidence

- Azure Data Factory pipeline execution screenshot.
- Azure Blob Storage curated output screenshot.
- Power BI dashboard screenshot.
- Power BI report file.
