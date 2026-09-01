"""
Auto-Insights Generator for Indian Retail Sales Dashboard (FREE version using Groq)
-------------------------------------------------------------------------------------
Reads pre-computed summary stats and asks an LLM (via Groq's free API) to write
a plain-English executive summary with trends, anomalies, and recommendations --
the kind of narrative you'd normally write by hand for a Power BI / Excel report.

Groq free tier: no credit card required, 14,400 requests/day limit.
"""

import os
from groq import Groq

# ---- 1. Set up the client ----
# Option A (recommended): set an environment variable before running:
#   Windows (cmd):      set GROQ_API_KEY=gsk_xxxx
#   Windows (PowerShell): $env:GROQ_API_KEY="gsk_xxxx"
#   Mac/Linux:           export GROQ_API_KEY=gsk_xxxx
# Then the line below picks it up automatically.
client = Groq()  # reads GROQ_API_KEY from environment

# Option B (quick testing only -- do NOT commit this to GitHub):
# client = Groq(api_key="gsk_your-key-here")


# ---- 2. Load the summary stats we generated earlier ----
with open("summary_for_llm.txt", "r") as f:
    summary_text = f.read()


# ---- 3. Build the prompt ----
prompt = f"""You are a senior data analyst preparing commentary for a business
dashboard on Indian retail sales (2024-2025). Below is a statistical summary
of the data -- monthly revenue trend, top/bottom cities, category performance,
and flagged anomalous months.

{summary_text}

Write an executive summary for a business audience (200-250 words) with these
sections:
1. Overall Trend -- describe the general revenue pattern over the two years
2. Key Anomalies -- explain the flagged months, referencing likely real-world
   causes (e.g. festive season, monsoon slowdown) where plausible
3. Category & Geography Insights -- what stands out about product categories
   and city performance
4. Recommendation -- one specific, actionable suggestion for the business

Reference actual numbers from the summary. Avoid generic filler statements.
Write in a confident, analyst tone suitable for a leadership audience.
"""


# ---- 4. Call the API ----
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",  # free, high-quality model on Groq
    max_tokens=600,
    messages=[{"role": "user", "content": prompt}]
)

insight_text = response.choices[0].message.content

# ---- 5. Save output so it can feed into Power BI / Excel ----
with open("insight_report.txt", "w") as f:
    f.write(insight_text)

print("=== GENERATED INSIGHT ===\n")
print(insight_text)
print("\n\nSaved to insight_report.txt")
