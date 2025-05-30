from flask import Flask, render_template, request, jsonify, redirect, send_from_directory
import sqlite3
import os
from sql_ollama import call_ollama_sql, get_schema_for_prompt, describe_database
import subprocess
from flask import request


app = Flask(__name__)       # Flask app instance
DB_PATH = "db/data.db"      # Path to your SQLite database file



def execute_sql_query(query):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    try:
        cur.execute(query)
        rows = cur.fetchall()
        columns = [desc[0] for desc in cur.description]
        return {"columns": columns, "rows": rows}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conn.close()


@app.route("/")     # Route per la home page
def index():            
    db_name = request.args.get("db_name")       # Ottengo il nome del database dalla query string
    return render_template("index.html", success=request.args.get("success") == "1", db_name=db_name)   # Renderizzo la home page

@app.route("/schema-tree")
def schema_tree():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
    tables = [row[0] for row in cur.fetchall()]
    result = {}
    for t in tables:
        cur.execute(f"PRAGMA table_info({t})")
        result[t] = [col[1] for col in cur.fetchall()]
    conn.close()
    return jsonify(result)
from sql_ollama import describe_database  # aggiungi se non l’hai già

# def describe_database():
#     schema = get_schema_for_prompt()
#     prompt = f"""Analizza il seguente schema SQLite e descrivilo in massimo 2 righe in italiano. Spiega sinteticamente a cosa serve il database.

# Schema:
# {schema}

# Risposta:"""

#     result = subprocess.run(
#         ["ollama", "run", "llama3"],
#         input=prompt.encode(),
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE
#     )

#     if result.stderr:
#         print("❌ Errore da Ollama (descrizione):", result.stderr.decode())

#     return result.stdout.decode().strip()


# Route per gestire le domande
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")
    print("📩 Domanda ricevuta:", question)

    if question.strip().lower().startswith(("select", "create", "insert", "update", "delete", "with")):
        sql_query = question
    else:
        sql_query = call_ollama_sql(question)

    print("🧠 Query generata:", sql_query)

    try:
        result = execute_sql_query(sql_query)
        print("🪵 Risultato:", result)
        return jsonify({"query": sql_query, "result": result})
    except Exception as e:
        return jsonify({"error": str(e), "query": sql_query})


@app.route("/upload-db", methods=["POST"])
def upload_db():
    file = request.files["dbfile"]
    if file:
        os.makedirs("db", exist_ok=True)  # aggiungi questa riga
        filename = "data.db"
        filepath = os.path.join("db", filename)
        file.save(filepath)
        return redirect(f"/?success=1&db_name={file.filename}")
    return redirect("/")



@app.route("/delete-db", methods=["POST"])  #   # Route per gestire la cancellazione del database
def delete_db():
    try:
        os.remove("db/data.db")
    except:
        pass
    return redirect("/")

@app.route("/db-description")
def db_description():
    description = describe_database()
    return jsonify({"description": description})



if __name__ == "__main__": 
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)