import pandas as pd
from main import OutreachAgent
from src.email_generator import EmailGenerator

def load_prospects_from_csv(filepath: str = "src/data/train.csv") -> pd.DataFrame:
    return pd.read_csv(filepath)

def generate_outreach_email(
    prospect_name: str,
    prospect_role: str,
    company_name: str,
    company_news: str
) -> str:
    prospect_info = {
        "name": prospect_name,
        "role": prospect_role,
        "company": company_name,
        "news": company_news
    }
    
    agent = OutreachAgent()
    components = agent.generate_email_components(prospect_info)
    
    generator = EmailGenerator()
    final_email = generator.compose_email(components)
    
    return final_email

# Usage example
if __name__ == "__main__":
    # Load prospects from CSV
    prospects_df = load_prospects_from_csv()
    
    # Generate email for each prospect
    for _, row in prospects_df.iterrows():
        email = generate_outreach_email(
            prospect_name=row['Name'],
            prospect_role=row['Title'],
            company_name=row['Company'],
            company_news=row['News']
        )
        print(f"\nEmail for {row['Name']} at {row['Company']}:")
        print("-" * 50)
        print(email)
        print("-" * 50)