# Aletheia

**Expose the blindspots of language models. Simulate, visualize, and secure your prompts.**

Aletheia is an interactive tool for testing how easily large language models (LLMs) can be manipulated and for exploring defenses against those attacks. It is designed for developers, researchers, and engineers who want to understand prompt injection, jailbreaks, and alignment failures in a practical way.

---

## What It Does

- Simulates prompt injection attacks and jailbreak attempts  
- Detects when a model disobeys its system prompt  
- Highlights why the failure occurred (token-level, structural, semantic)  
- Suggests defensive rewrites for more resilient prompts  
- Compares vulnerability across multiple LLMs  

---

## Core Use Cases

| Feature | Description |
|---------|-------------|
| Prompt Attack Simulation | Enter a system prompt and adversarial user prompt. Aletheia tests if the model breaks. |
| Adversarial Mode | Built-in attack patterns attempt to override system instructions automatically. |
| Model Comparison | Run the same prompt against GPT-4, Claude, or local LLMs and compare outcomes. |
| Prompt Hardening | Suggests safer alternatives for prompts identified as vulnerable. |
| Breakdown Visuals | Token-level highlighting, jailbreak classifications, and structural diagrams. |

---

## Why Aletheia?

In Greek, *Aletheia* (ἀλήθεια) means “truth” or “unveiling.”  
The goal of this project is to unveil the hidden vulnerabilities of language models so that developers can make them safer, more trustworthy, and more robust. Just as Aletheia represents uncovering what lies beneath the surface, this tool reveals the fragile points in AI systems that adversaries exploit.

---

## Tech Stack

- **Frontend:** React/Next.js + Tailwind CSS
- **Backend:** Python (FastAPI)  
- **LLMs:** OpenAI GPT-4, Anthropic Claude, HuggingFace Transformers (optional local models)  
- **Extras:** Regex heuristics, adversarial prompt templates, token diffing  
- **Deployment:** Vercel, Render, or HuggingFace Spaces  

