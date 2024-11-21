from langchain_openai import ChatOpenAI
from typing import Dict
from langchain.prompts import PromptTemplate
from src.prompts import (
    COMPOSE_EMAIL_TEMPLATE,
    GRAMMAR_REVIEW_TEMPLATE,
    STYLE_REVIEW_TEMPLATE,
    EXTRACT_STYLE_TEMPLATE
)

class EmailGenerator:
    def __init__(self):
        self.primary_agent = ChatOpenAI(
            model="gpt-4",
            temperature=0.7
        )
        self.grammar_agent = ChatOpenAI(
            model="gpt-4",
            temperature=0.3
        )
        self.style_agent = ChatOpenAI(
            model="gpt-4",
            temperature=0.5
        )

    def compose_email(self, components: Dict) -> str:
        prospect_info = {
            "role": components.get("role", ""),
            "company": components.get("company", ""),
            "news": components.get("news", ""),
            "name": components.get("name", "")
        }
        
        email_style = self.extract_style(prospect_info)
        
        prompt = PromptTemplate(
            template=COMPOSE_EMAIL_TEMPLATE,
            input_variables=["subject", "hook", "problem", "credibility", "solution", "next_steps"]
        )
        
        draft = self.primary_agent.invoke(prompt.format(**components)).content
        styled = self.style_review(draft, email_style)
        final_email = self.grammar_review(styled)
        
        return final_email

    def grammar_review(self, draft: str) -> str:
        prompt = PromptTemplate(
            template=GRAMMAR_REVIEW_TEMPLATE,
            input_variables=["draft"]
        )
        return self.grammar_agent.invoke(prompt.format(draft=draft)).content

    def style_review(self, email: str, style: str) -> str:
        prompt = PromptTemplate(
            template=STYLE_REVIEW_TEMPLATE,
            input_variables=["email", "style"]
        )
        return self.style_agent.invoke(prompt.format(email=email, style=style)).content

    def extract_style(self, prospect_info: Dict) -> str:
        prompt = PromptTemplate(
            template=EXTRACT_STYLE_TEMPLATE,
            input_variables=["name", "role", "company", "news"]
        )
        
        style = self.style_agent.invoke(prompt.format(**prospect_info)).content.strip()
        
        if style not in [
            "Professional and formal",
            "Professional yet casual",
            "Enthusiastic and congratulatory",
            "Light and fun",
            "Technical and detailed"
        ]:
            return "Professional yet casual"
        
        return style
