# JSON Query Engine

A simple Python-based query engine for querying JSON datasets using SQL-like syntax.

## Run

```bash
python cli.py
```

## Query Syntax

```sql
SELECT field WHERE condition
```

## Examples

```sql
SELECT title WHERE release_year > 2020
```

```sql
SELECT country WHERE release_year == 2021
```

```sql
SELECT rating WHERE release_year < 2019
```

## Dataset

Uses the Netflix Kaggle dataset converted into JSON format.
