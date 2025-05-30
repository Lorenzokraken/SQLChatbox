import sqlite3
import subprocess


DB_PATH = "co2_emissions.db"

def get_views():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='view';")
    views = [v[0] for v in cur.fetchall()]
    conn.close()
    return views

def call_ollama(prompt):
    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.stdout.decode().strip()

if __name__ == "__main__":
    views = get_views()
    print("✅ Viste trovate nel database:")
    for v in views:
        print("-", v)

    if views:
        prompt = f"""
Il database contiene le seguenti viste: {', '.join(views)}.
Scrivi una query SQL per visualizzare i primi 10 record della vista "{views[0]}".
Rispondi solo con la query.
"""
        sql = call_ollama(prompt)
        print("\n🎯 Query generata:\n", sql)
    else:
        print("⚠️ Nessuna vista trovata nel database.")
