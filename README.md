# Indian Retail Sales — GenAI-Powered Insights Dashboard
### AI-powered analytics pipeline that generates business insights from Indian retail sales data using an LLM (Groq/Llama) and visualizes them in Power BI.
## Overview
An analytics pipeline that automatically generates written business insights from retail sales data using a Large Language Model (LLM),
displayed alongside an interactive Power BI dashboard — instead of relying on manual report writing.
## Dataset
15,000 retail transactions across 20 Indian cities (2024–2025), covering Electronics, Groceries, Apparel, Home & Kitchen, and Beauty & 
Personal Care categories. Includes order date, city/state, category, pricing, discounts, payment mode, and store type (Online/In-Store).
## Pipeline
1.Data validation (EDA) — checked for nulls, duplicates, and distribution sanity (quantities, discounts, prices) before analysis.
2.Summary statistics — computed monthly revenue trend, top/bottom performing cities, category-wise performance, and flagged anomalous months using z-score deviation.
3.LLM insight generation — summary stats (not raw data) sent to Llama 3 via the Groq API to produce a business-ready executive summary covering trend, anomalies, category/geo insights, and a recommendation.
4.Visualization — Power BI dashboard combining KPI cards, a monthly trend line, top-cities bar chart, category pie chart, and the AI-generated narrative side by side.
## Files
Indian_retail_sales.csv -	Raw dataset (15,000 transactions)

Summary_for_llm.txt	- Pre-computed summary statistics fed to the LLM

Generate_insights_groq.ipypy	- Script that calls the Groq API to generate the executive summary

Indian_Retail_AI_Dashboard.pbix - Power BI dashboard with visuals + AI insight
## Tools
Python (pandas), Groq API (Llama 3), Power BI
## Key takeaway
Sending curated summary statistics to the LLM — rather than raw row-level data — produced more accurate, cost-efficient 
results and avoided hallucinated figures, since every number the model referenced was grounded in the pre-computed summary.
## Sample Output
"Total monthly revenue swung sharply from a low of ₹11.99M in Aug-24 to a peak of ₹20.60M in Nov-25, delivering an overall 56% rise in the 24-month horizon. 
The year-over-year (YoY) trajectory is volatile: after a modest 1.5% rise in Feb-24, sales fell 12.9% in Jun-24 (₹12.61M) before surging 39% in Oct-24 (₹19.75M). 
Oct-24 and Nov-24 align with the post-Diwali and early-holiday shopping surge, when discretionary spending on electronics and apparel traditionally spikes." 
