# deep-sparring# Deep Sparring 🤺

> **Don't just read proofs. Re-discover them.**
> A Socratic AI Companion for Deep Reading in Mathematics & ML Theory.

![License](https://img.shields.io/badge/license-MIT-blue) ![Stack](https://img.shields.io/badge/stack-Next.js_|_FastAPI_|_LLM-green)

## 📖 Why Deep Sparring?

In the age of LLMs, it's easy to paste a PDF into GPT and ask for a summary. This is efficient, but it's **"Outsourcing your Thinking"**.

Real growth in mathematics and theoretical ML comes from the struggle—the gap between seeing a theorem and understanding its proof. **Deep Sparring** is built to reclaim that intuition.

It uses AI not to give you answers, but to:
1.  **Clean the noise:** Repair broken OCR and formatting using LLM-first parsing.
2.  **Hide the answer:** Proofs are physically blurred until you are ready to reveal them.
3.  **Spar with you:** A Socratic AI tutor that answers questions with heuristics, not solutions.

## ✨ Key Features

- **🧠 Active Recall Interface:** Theorems are visible, but Proofs are blurred. You must explicitly click "Predict & Reveal" to check your intuition.
- **🔧 LLM-First Aggressive Repair:** Instead of regex, we use Large Language Models to reconstruct semantic mathematical truths from broken OCR artifacts (e.g., fixing `L [3]` to $L^3$).
- **💬 Socratic Chat:** A built-in chat interface for each theorem. The AI acts as a tutor, guiding you through specific steps without spoiling the "Aha!" moment.
- **⚡ High-Fidelity Rendering:** Full LaTeX support via KaTeX for crisp mathematical display.

## 🛠 Tech Stack

- **Frontend:** Next.js 14, Tailwind CSS, Lucide React, React Markdown (remark-math/rehype-katex).
- **Backend:** FastAPI (Python), PyMuPDF (PDF extraction).
- **AI Core:** OpenAI API (Compatible with GPT-4o, DeepSeek, etc.).

---

## 🚀 Getting Started

Follow these steps to run the project locally.

### Prerequisites

- Node.js & npm
- Python 3.8+
- An API Key (OpenAI, DeepSeek, or Moonshot)

### 1. Backend Setup

The backend handles PDF parsing and LLM interaction.

```bash
cd backend

# 1. Install dependencies
python -m pip install -r requirements.txt

# 2. Configure Environment Variables
# Create a .env file
touch .env
Open .env and add your API key:

Code snippet
OPENAI_API_KEY=sk-your-api-key-here
# Optional: If using DeepSeek or local models
# BASE_URL=[https://api.deepseek.com](https://api.deepseek.com)
Run the Server:

Bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
You should see: Application startup complete.

2. Frontend Setup

Open a new terminal for the frontend.

Bash
cd frontend

# 1. Install dependencies
npm install

# 2. Run the development server
npm run dev
Access the App: Open your browser and navigate to http://localhost:3000.

🎮 How to Use
Upload: Click the upload area and select a Math/ML paper (PDF format).

Parse: Wait for the "LLM Aggressive Repair" engine to reconstruct the theorems (approx. 10-30s).

Read & Predict:

Read the Theorem statement.

The Proof is hidden. Stop and think: How would I prove this?

Click "Predict & Reveal" to verify your intuition.

Spar:

Stuck on a specific step? Click "💬 Spar with AI".

Ask questions like: "Why is the Lipschitz assumption necessary here?"

The AI will provide hints, not answers.

🧩 Troubleshooting
"LLM Error" / "JSON Parse Error":

This usually means the model output wasn't clean JSON. The backend has auto-repair logic, but retry usually fixes it.

Ensure your API Key has sufficient quota.

Frontend shows "Connection Refused":

Ensure the Backend terminal is running and listening on port 8000.

Math symbols look weird:

The LLM inference might hallucinate LaTeX. In most cases, the aggressive repair prompt fixes this, but it depends on the model capability (GPT-4o is recommended).

📄 License
MIT License. Built for the love of Math.
