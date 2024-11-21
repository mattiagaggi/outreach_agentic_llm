SUBJECT_TEMPLATE = """
Given the following prospect information, create a compelling subject line:
Prospect Name: {name}
Company: {company}
Role: {role}
Recent News: {news}

Generate a brief, subject line (max 7 words) that does not sound generated by a LLM but it is as human sounding as possible. No buzzwords or exclamation marks, just a normal subject line the same you would use in a normal email.
"""

HOOK_TEMPLATE = """
Create a personalized hook based on the following information:
Prospect Name: {name}
Company: {company}
Role: {role}
Recent News: {news}

Create a short, engaging hook that references their recent news or achievement. 
Keep it conversational and authentic.
"""

PROBLEM_TEMPLATE = """
Create a concise problem statement for:
Prospect Name: {name}
Company: {company}
Role: {role}
Recent News: {news}

Describe the key problem that our solution addresses, relevant to their industry.
"""

COMPOSE_EMAIL_TEMPLATE = """
Compose a cold outreach email using these components:
Subject: {subject}
Hook: {hook}
Problem: {problem}
Credibility: {credibility}
Solution: {solution}
Next Steps: {next_steps}

Requirements:
- Keep it under 50 words
- Minimize comma usage
- Make it conversational
- Be direct and clear
"""

GRAMMAR_REVIEW_TEMPLATE = """Review and correct this email for grammar while maintaining its message:
{draft}"""

STYLE_REVIEW_TEMPLATE = """Review this email maintaining a {style} style.

Style Guidelines for {style}:
- If "Professional and formal": Use traditional business language, be courteous and reserved
- If "Professional yet casual": Balance professionalism with conversational tone
- If "Enthusiastic and congratulatory": Include genuine excitement and praise
- If "Light and fun": Include appropriate humor while maintaining professionalism
- If "Technical and detailed": Focus on precision and industry-specific terminology

Original email:
{email}

Please revise while maintaining the determined style. Also don't use typical words that come out of LLMs and make sure it is the most natural sounding as possible"""

EXTRACT_STYLE_TEMPLATE = """Determine the most appropriate email style based on:

Prospect Name: {name}
Prospect Role: {role}
Company: {company}
Recent News: {news}

Choose ONE of these styles (return ONLY the style name):
- Professional and formal
- Professional yet casual
- Enthusiastic and congratulatory
- Light and fun
- Technical and detailed

If information is missing, default to "Professional yet casual"."""