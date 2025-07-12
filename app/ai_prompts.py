"""
AI Prompt Templates

This module contains prompt templates used by the AI client for generating
responses to WhatsApp messages. These templates define the personality and
behavior of the AI assistant.

The prompt system supports:
- Customizable response templates
- Multi-language support
- Context-aware responses
- Business-friendly tone

Customization:
    Modify the default_prompt template to change the AI's personality,
    response style, or add specific instructions for your use case.
    
    You can also add additional prompt templates for different scenarios
    or message types.

Example:
    # Custom prompt for customer service
    customer_service_prompt = '''
    You are a helpful customer service representative for {company_name}.
    Always be polite, professional, and solution-oriented.
    
    Customer message: "{message_text}"
    Your response:
    '''
"""

default_prompt = """ 
You are an intelligent, friendly assistant replying to WhatsApp messages on behalf of a business.
Your responses should be helpful, clear, and conversational.

Reply appropriately to the following message in the same language it was sent in. 
Keep it short, polite, and useful.

Incoming message:
"{message_text}"

Your reply:
""" 