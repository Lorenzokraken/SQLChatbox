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
- Ollama 3

---
Scarica e installa Ollama.
https://ollama.com/download

Se non ha una buona GPU apri il cmd e digita:
ollama run llama3
set OLLAMA_NO_GPU=1

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

Puoi usare modelli Open Source/a pagamento con output testuale in SQL
Cambia la struttura di sql_ollama per ricevere dati dalla tua api-key piuttosto che dal serve ollama
```


Avviato Flask ti troverai qui sul Localhost: 
![Screenshot 2025-05-24 143548](https://github.com/user-attachments/assets/9ba69e62-716f-42d4-bc21-4a2fd6efa419)

Carica un database e ricevi uno schema del database con una descrizione dettagliata:
![Screenshot 2025-06-02 182519](https://github.com/user-attachments/assets/ee83579a-568d-4560-8ebf-75070d3c9c43)
![Screenshot 2025-05-24 143805](https://github.com/user-attachments/assets/24d6955c-2428-4943-953c-0b253c3076e4)
Scrivi quello che vorresti visulizzare/modificare dal database cercando di essere più chiaro possibile. 
![Immagine 2025-06-02 191956](https://github.com/user-attachments/assets/ed9eaebd-b6fc-437d-bfb2-5b48bfe1e25a)
Ollama genererà un Query SQL e ti mostrerà i campi che ti interessano:
![Screenshot 2025-06-02 192010](https://github.com/user-attachments/assets/f7e0e766-a784-483f-9439-a49cd7a7fa0e)
Genera grafici (Torta, Barre, Linee)
![Immagine 2025-06-02 192146](https://github.com/user-attachments/assets/4f18f270-0111-4cf9-8544-e7437049f05a)



📬 Contribuisci
Pull Request e feedback benvenuti!
Inizia aprendo una issue o forka il progetto!



