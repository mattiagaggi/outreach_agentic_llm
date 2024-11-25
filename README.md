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

You can edit the data in `src/data/train.csv` to test your own prospects.

## Next steps

- More information should be used to draft the email.  see the TODOs in the main.py file.
Without this I would not do a proper evaluation as we need this info.


- Perplexity can be used to parse for the missing info that we need, like the style, the problem statement etc maybe should be extracted with perplexity. 

- Obvious personalization based on a shallow information is not good we should dig deeper.

- I only used gpt4, did not extensively experiment.

- For the real vs fake sounding maybe we should train a discriminative model, that would be a good way to get metrics out of this (LLMs are not reliable). It would be also a good way to actually do incremental improvements to the email generation.

- Any next step I give you now is not great as it should come from the user feedback