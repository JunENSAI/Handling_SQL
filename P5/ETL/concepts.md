## 1. What is ETL?

* **E - Extract:** Getting data from a source (CSV, API, another DB).

* **T - Transform:** Cleaning, calculating, and formatting the data (Python/Pandas).

* **L - Load:** Saving the clean data into your destination (Postgres).

---

## 2. Common Transforms

Raw data is rarely perfect. Before loading to SQL, we often:

* **Handle Nulls:** `df.fillna(0)` or `df.dropna()`.

* **Fix Dates:** `pd.to_datetime(df['date_col'])`.

* **Renaming:** `df.rename(columns={'Bad Name': 'good_name'})`.

* **Data Types:** Converting strings "$100" to integers `100`.

---

## 3. The Full Script Structure

1.  **Extract:** `df = pd.read_csv('raw_data.csv')`

2.  **Transform:** `df['clean_col'] = ...`

3.  **Load:** `df.to_sql('target_table', engine, if_exists='append')`

---