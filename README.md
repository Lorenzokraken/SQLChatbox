# 🧠 SQL Chatbox AI

Un'applicazione web interattiva che ti permette di porre domande in linguaggio naturale su un database SQLite, generando automaticamente le query SQL grazie all'integrazione con LLM (Large Language Models) come LLaMA o Gemini.

---

## 🔍 Funzionalità principali

- 📥 **Upload del database**: carica un file `.db` SQLite personalizzato
- 💬 **Domande in linguaggio naturale**: digita domande come “Mostra le emissioni di CO₂ per nazione nel 2002”
- 🧠 **Generazione automatica della query SQL** tramite un LLM (locale o API)
- 🧾 **Visualizzazione tabellare dei risultati**
- 📊 **Grafici interattivi**: genera grafici a linee o a torta direttamente dal risultato della query

---

## 🛠 Requisiti

- Python 3.11+
- Flask
- Plotly (per i grafici)
- SQLite
- Un modello LLM accessibile (es. [Ollama](https://ollama.com/) o Google Gemini)

---

## ▶️ Avvio dell'app

```
# Installazione delle dipendenze
pip install -r requirements.txt

# Avvio del server Flask
python app.py
Poi visita http://localhost:5000 nel browser.
```
📦 Struttura del progetto
```
SQLChatbox/
│
├── app.py                  # Backend Flask
├── sql_ollama.py           # Funzione che chiama il modello LLM
├── templates/
│   └── index.html          # Interfaccia utente
├── static/
│   └── style.css           # (opzionale) Stili CSS
├── db/
│   └── data.db             # Database di esempio
├── uploads/                # (opzionale) Per gestire file caricati
└── README.md
```

🤖 LLM supportati
Puoi integrare:
```
Ollama in locale (ollama run llama3)

Altri modelli Open Source con output testuale in SQL
```
📈 Esempi di domande supportate
"Mostra le top 5 nazioni per emissioni nel 2002"

"Visualizza le emissioni medie per continente"

"Grafico delle emissioni di CO₂ negli ultimi 10 anni"

📬 Contribuisci
Pull Request e feedback benvenuti!
Inizia aprendo una issue o forka il progetto!
