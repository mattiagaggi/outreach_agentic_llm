from langchain_openai import ChatOpenAI
from typing import Dict
from dotenv import load_dotenv
from src.prompts import SUBJECT_TEMPLATE, HOOK_TEMPLATE, PROBLEM_TEMPLATE

load_dotenv()

class OutreachAgent:
    def __init__(self):
        self.model = ChatOpenAI(
            model="gpt-4",
            temperature=0.7
        )
        
    def generate_email_components(self, prospect_info: Dict) -> Dict:
        components = {
            'subject': self._generate_subject(prospect_info),
            'hook': self._generate_hook(prospect_info),
            'problem': self._generate_problem_statement(prospect_info),
            'credibility': self._generate_credibility(prospect_info),
            'solution': self._generate_solution(prospect_info),
            'next_steps': self._generate_next_steps(prospect_info)
        }
        return components
        
    def _generate_subject(self, prospect_info: Dict) -> str:
        return self.model.invoke(SUBJECT_TEMPLATE.format(**prospect_info)).content
        
    def _generate_hook(self, prospect_info: Dict) -> str:
        return self.model.invoke(HOOK_TEMPLATE.format(**prospect_info)).content
        
    def _generate_problem_statement(self, prospect_info: Dict) -> str:
        return self.model.invoke(PROBLEM_TEMPLATE.format(**prospect_info)).content
        
    def _generate_credibility(self, prospect_info: Dict) -> str:
        # TODO: Add credibility template
        return "Our credibility statement"
        
    def _generate_solution(self, prospect_info: Dict) -> str:
        # TODO: Add solution template
        return "Our solution description"
        
    def _generate_next_steps(self, prospect_info: Dict) -> str:
        # TODO: Add next steps template
        return "Suggested next steps"