# Outreach Agentic LLM

An intelligent framework using LangChain and OpenAI for generating personalized cold outreach emails.

## Quick Start

1. Create a virtual environment and install requirements:

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

2. Create a `.env` file and add your OpenAI API key:
```bash
OPENAI_API_KEY=your_key_here
```

3. Run the example script:
```bash
python src/usage_example.py
```

## Next steps
- Perplexity can be used to parse for features, like the style maybe should be extracted with perplexity. 

- Obvious personalization based on a shallow information is not good we should dig deeper.
- More information should be used to draft the email.  see the TODOs in the main.py file.

- I only used gpt4, did not extensively experiment

- For the real vs fake sounding maybe we should train a discriminative model, that would be a good way to get metrics out of this (LLMs are not reliable)