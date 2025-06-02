import sqlite3
import subprocess

DB_PATH = "db/data.db"

def get_schema_for_prompt():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
    tables = [row[0] for row in cur.fetchall()]
    if not tables:
        return "Non posso aiutarti con questa domanda"

    schema = ""
    for t in tables:
        cur.execute(f"PRAGMA table_info({t})")
        cols = cur.fetchall()
        if not cols:
            continue
        col_defs = ", ".join(f"{col[1]} {col[2]}" for col in cols)
        schema += f"{t}({col_defs})\n"
    conn.close()
    return schema

def call_ollama_sql(natural_question):
    schema = get_schema_for_prompt()
    if schema == "Non posso aiutarti con questa domanda":
        return schema

    prompt = f"""
Sei un assistente SQL specializzato in SQLite. 
Hai accesso allo schema del database qui sotto. 
Il tuo compito è GENERARE UNA QUERY SQL VALIDA (e solo la query!) per rispondere alla domanda dell’utente.

Segui queste regole:
- Usa solo i nomi di tabelle e colonne che vedi nello schema.
- Se la domanda parla di "vendite", considera le tabelle con quantità o prezzi (es: invoice_items).
- Evita di inventare tabelle, colonne o join inesistenti.
- NON AGGIUNGERE COMMENTI, spiegazioni o testo fuori dalla query.
- Se trovi nella domanda "quanto" ha venduto o "quanto" ha emesso mostra sempre il valore.

esempio di query:
-- Quali sono i 7 paesi che hanno emesso piu co2 nel 2007 e quanto hanno emesso.
SELECT c.name, e.co2
FROM countries c
JOIN emissions e ON c.country_id = e.country_id
WHERE e.year = 2007
ORDER BY e.co2 DESC
LIMIT 10;


Schema del database:
{schema}

Domanda:
{natural_question}
"""


    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    if result.stderr:
        print("❌ Errore da Ollama:", result.stderr.decode())

    output = result.stdout.decode().strip()
    cleaned = output.replace("```sql", "").replace("```", "").strip()

    if not cleaned.lower().startswith(("select", "insert", "update", "delete", "with", "create")):
        return "SELECT 'Non posso aiutarti con questa domanda: output non valido.';"

    return cleaned


def describe_database():
    schema = get_schema_for_prompt()
    prompt = f"""Analizza lo schema SQLite qui sotto e scrivi una breve descrizione del database in **italiano**, in massimo 2 righe.

Schema:
{schema}

Descrizione in italiano:"""

    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    if result.stderr:
        print("❌ Errore da Ollama (descrizione):", result.stderr.decode())

    return result.stdout.decode().strip()
