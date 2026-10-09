# 🚀 [Tips Hindawi](https://www.tipshindawi.com/) Internship (August–October) 2026

> 🎓 This project was built during the [**Tips Hindawi**](https://www.tipshindawi.com/) **Internship (August–October) 2026**.

## 👤 Participant

| Field            | Value                                |
| ---------------- | ------------------------------------ |
| Full Name        | Mohamed Younis Mohamed               |
| Project Name     | مدام عفاف \| Madam Afaf              |
| GitHub Username  | mohamedyounis10                      |
| Internship Batch | August–October 2026                  |
| Training Program | Large Language Models (LLMs) Program |
| Organization     | [**Edrak for Ai**](https://edrak4ai.com/en) |

---

# 📖 Project Overview

**مدام عفاف (Madam Afaf)** is an AI-powered chatbot that helps Egyptian citizens get instant, accurate information about government services — in Egyptian Arabic dialect.

The system scrapes **165 government services** from 3 official Egyptian government websites, builds a **RAG (Retrieval-Augmented Generation)** pipeline using **FAISS** vector search and **BAAI/bge-m3** embeddings, and generates grounded answers using **NileChat-3B** — an Arabic/Egyptian-dialect LLM. The frontend is a **Streamlit** app with a full RTL Arabic UI, while the backend runs on **Kaggle GPU (T4)** and is exposed via an **ngrok** tunnel.

> *"الموظفة اللي مش هتقولك فوت علينا بكرة! 😉"*

---

# ✨ Features

* 🤖 **Arabic RAG Chatbot** — answers questions about Egyptian government services using only verified, official sources (no hallucination)
* 🗣️ **Egyptian Dialect Support** — powered by NileChat-3B, understands and responds in Egyptian Arabic
* 🌐 **Real-time Web Scraping** — collects 165 services from 3 official gov.eg websites using parallel scraping (ThreadPoolExecutor)
* 📚 **Source Attribution** — every answer comes with clickable links to the official government source
* 🎨 **Full RTL Arabic UI** — Streamlit app with custom CSS for right-to-left layout, dark theme, and smooth animations
* 💰 **Zero-cost Infrastructure** — runs entirely on free-tier tools (Kaggle GPU + ngrok + Streamlit)

---

# 🛠️ Technologies Used

| Category | Technology |
|---|---|
| **LLM** | UBC-NLP/NileChat-3B (Arabic & Egyptian dialect) |
| **Embeddings** | BAAI/bge-m3 (multilingual, Arabic-optimized) |
| **Vector Store** | FAISS (in-memory, GPU-accelerated) |
| **RAG Framework** | LangChain (chunking, retrieval, prompt templates) |
| **Web Scraping** | BeautifulSoup4, Requests, ThreadPoolExecutor |
| **Deep Learning** | PyTorch, HuggingFace Transformers |
| **Frontend** | Streamlit (RTL Arabic UI with custom CSS) |
| **Backend** | FastAPI (served from Kaggle Notebook) |
| **Tunnel** | ngrok (Kaggle → local Streamlit) |
| **Compute** | Kaggle (NVIDIA T4 GPU — free tier) |
| **Language** | Python |

---

# ⚙️ Installation

### 1 — Clone the Repository

```bash
git clone https://github.com/mohamedyounis10/madam-afaf.git
cd madam-afaf
```

### 2 — Install Streamlit Dependencies

```bash
pip install streamlit requests
```

### 3 — Setup the Kaggle Notebook

1. Upload `citizen-services-rag-prototype.ipynb` to [Kaggle](https://www.kaggle.com)
2. Enable **GPU T4** — Settings → Accelerator → GPU T4
3. Enable **Internet** — Settings → Internet → On
4. Add your HuggingFace token to Kaggle Secrets as `HF_TOKEN`
5. Run All Cells (~15 minutes on first run)

### 4 — Setup ngrok

Add the following at the end of the Kaggle Notebook:

```python
from pyngrok import ngrok
ngrok.set_auth_token("YOUR_NGROK_AUTHTOKEN")
public_url = ngrok.connect(8000).public_url
print(f"API URL: {public_url}")
```

### 5 — Update API URL in `app.py`

```python
# Line 242 in app.py
API_URL = "https://YOUR-NGROK-URL.ngrok-free.app"
```

### 6 — Run the App

```bash
streamlit run app.py
```

Opens at **http://localhost:8501**

---

# 🚀 Usage

1. **Start the Kaggle Notebook** — run all cells to load the model, scrape data, build the vector store, and start the API
2. **Copy the ngrok URL** from the notebook output and paste it into `app.py`
3. **Run `streamlit run app.py`** locally
4. **Ask in Egyptian Arabic!** — type any question about Egyptian government services

**Example questions:**
```
إزاي أطلّع بطاقة رقم قومي بدل فاقد؟
عايز أجدد جواز سفري، محتاج إيه؟
ما هي المستندات المطلوبة لاكتساب الجنسية المصرية؟
إيه إجراءات استخراج بطاقة تموينية ذكية جديدة؟
```

---

# 📸 Demo

### 🖥️ App Interface

<img width="1917" height="898" alt="Screenshot 2026-10-07 001354" src="https://github.com/user-attachments/assets/5eabccb1-8e93-44c8-ad46-10ea915d6142" />

---

### 🎬 Demo Video

> *Click the thumbnail below to watch the full demo*

<a href="assets/demo.mp4">
  <img src="assets/demo.png" alt="Watch Demo Video" width="600"/>
</a>

**▶️ [Click here to watch the demo video](assets/demo.mp4)**
---

# 📈 Results

| Metric | Value |
|---|---|
| Government websites scraped | **3 official sources** |
| Total services collected | **165 services** |
| RAG chunks created | **206 chunks** |
| Web scraping time | **~10 seconds** (parallel) |
| Vector store build time | **~40 seconds** |
| Retrieval accuracy | **Top-4 most relevant chunks** |
| Total infrastructure cost | **$0** (fully free-tier) |

**Quality Highlights:**
- ✅ Accurate answers grounded exclusively in official government sources
- ✅ Refuses to answer out-of-scope questions — no hallucination
- ✅ Cites the official source URL with every answer
- ✅ Understands Egyptian Arabic dialect naturally

---

# 🔮 Future Improvements

* 📅 **Scheduled scraping** — automatically update government data periodically
* 🏛️ **More sources** — add tax authority, commercial registry, and Ministry of Labor websites
* 💾 **Persistent vector store** — save FAISS index to disk to avoid rebuilding on every session
* 🚀 **Cloud deployment** — migrate backend to Hugging Face Spaces or a cloud GPU
* 📱 **Mobile app** — build a mobile-friendly interface for easier access
* 🔄 **Streaming responses** — return answers progressively instead of waiting for full generation
* 📊 **Analytics dashboard** — track most-asked questions to improve coverage

---

# 📚 About the Internship

This project was developed as part of the [**Tips Hindawi**](https://www.tipshindawi.com/) **Internship (August–October) 2026)**, and it will be showcased on the official [Tips Hindawi](https://www.tipshindawi.com/) website.

[Tips Hindawi](https://www.tipshindawi.com/) is the internships department of [**Edrak for Ai**](https://edrak4ai.com/en), and the internship encourages participants to build real-world projects, apply practical skills, and showcase their work through GitHub.

For more information about the internship, training programs, and upcoming batches, visit the official [Tips Hindawi](https://www.tipshindawi.com/) website.

---

# 📄 License

This project is shared for educational and portfolio purposes.
