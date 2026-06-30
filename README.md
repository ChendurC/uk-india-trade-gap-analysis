# 🇬🇧 UK–India Trade Gap Analysis

> **What does the UK buy from the world that India isn't supplying enough of?**

This project analyses $400B+ of UK import data to identify the largest product categories where India holds less than 5% market share — and quantifies the opportunity gap.

Built as a portfolio project targeting Data Analyst / Data Engineer roles in the UK.

---

## 📊 Live Dashboards
- **Tableau Dashboard:** [View on Tableau Public](https://public.tableau.com/app/profile/chendur.murugan.cheran/viz/Uk-IndiaTrade/Dashboard1)
- **Streamlit App:** Run locally (see below)

---

## 🔍 Key Finding

The UK imports **$400.7B** of goods annually. India supplies only **$12.5B** of that — leaving a **$388.2B gap**. The three biggest under-represented categories:

| Category | UK Imports | India's Share |
|---|---|---|
| Automobiles & Vehicles | $62.5B | 0.16% |
| Machinery & Computers | $58.3B | 1.37% |
| Electrical Equipment | $42.1B | 1.43% |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python & Pandas | Data pipeline & cleaning |
| Streamlit & Plotly | Interactive web dashboard |
| Tableau | Advanced visualisations |
| Git & GitHub | Version control & portfolio |

---

## 🚀 How to Run

**1. Clone the repo**
```bash
git clone https://github.com/ChendurC/uk-india-trade-gap-analysis
cd uk-india-trade-gap-analysis
```

**2. Install dependencies**
```bash
pip install pandas streamlit plotly requests
```

**3. Generate the data**
```bash
python pipeline/fetch_data.py
```

**4. Launch the dashboard**
```bash
streamlit run dashboard/app.py
```

---

## 💡 Insights

- **Automobiles**: India has a massive manufacturing base (Tata, Mahindra) but exports almost no cars to the UK. The 2025 India-UK FTA could change this.
- **Pharmaceuticals**: India already supplies ~5% but given its generic drug dominance, this is still underweight.
- **Clothing & Apparel**: India's highest market share (8.76%) — yet Bangladesh and China still dominate. FTA tariff cuts could shift this significantly.

---

## 👤 Author

**Chendur Murugan Cheran** — MSc Business Analytics, University of Exeter  
Previously: Software Engineer @ IQVIA (2.7 years)  
[LinkedIn](https://linkedin.com/in/chendurmurugan) | [GitHub](https://github.com/chendurmurugan)

---

*Data source: UN Comtrade & UK ONS Trade Statistics (2023)*