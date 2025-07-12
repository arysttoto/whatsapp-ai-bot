# WhatsApp AI Bot Boilerplate

A production-ready Flask boilerplate for building WhatsApp bots powered by OpenAI's GPT models. This boilerplate provides a solid foundation for creating intelligent WhatsApp chatbots with proper error handling, logging, and modular architecture.

## 🚀 Features

- **WhatsApp Business API Integration**: Complete webhook handling and message sending
- **OpenAI GPT Integration**: AI-powered responses using OpenAI's ChatCompletion API
- **Modular Architecture**: Clean separation of concerns with dedicated modules
- **Error Handling**: Comprehensive error handling with retry mechanisms
- **Logging**: Structured logging with file and console output
- **Command System**: Extensible slash command system for user interactions
- **Configuration Management**: Environment-based configuration with dotenv
- **Production Ready**: Proper error handling, logging, and modular design

## 📁 Project Structure

```
whatsapp-ai-bot/
├── app/
│   ├── __init__.py          # Flask app factory and configuration
│   ├── whatsapp.py          # WhatsApp Business API client
│   ├── ai.py               # OpenAI integration client
│   ├── routes.py           # Webhook endpoints
│   ├── commands.py         # Command processing system
│   ├── config.py           # Configuration management
│   ├── errors.py           # Custom exception classes
│   ├── ai_prompts.py       # AI prompt templates
│   └── main.py             # Application entry point
├── logs/                   # Application logs
├── tests/                  # Test files
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd whatsapp-ai-bot
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```env
   # WhatsApp Business API Configuration
   WHATSAPP_API_URL=https://graph.facebook.com/v17.0
   WHATSAPP_WEBHOOK_VERIFY_TOKEN=your_webhook_verify_token
   WHATSAPP_ACCESS_TOKEN=your_whatsapp_access_token
   WHATSAPP_PHONE_NUMBER_ID=your_phone_number_id
   
   # OpenAI Configuration
   OPENAI_API_KEY=your_openai_api_key
   OPENAI_MODEL=gpt-3.5-turbo
   OPENAI_TEMPERATURE=0.7
   ```

## 🚀 Quick Start

1. **Run the development server**:
   ```bash
   python app/main.py
   ```

2. **Set up WhatsApp webhook**:
   - Deploy your application to a public URL (e.g., using ngrok for local development)
   - Configure your WhatsApp Business API webhook to point to your application's root endpoint
   - Use the `WHATSAPP_WEBHOOK_VERIFY_TOKEN` as the verification token

3. **Test the bot**:
   Send a message to your WhatsApp Business number and receive AI-powered responses!

## 📚 Architecture Overview

### Core Components

#### 1. **Application Factory (`app/__init__.py`)**
- Creates and configures the Flask application
- Sets up logging, error handlers, and dependency injection
- Registers blueprints and services

#### 2. **WhatsApp Client (`app/whatsapp.py`)**
- Handles all WhatsApp Business API communication
- Manages webhook verification and message sending
- Extracts messages from webhook payloads

#### 3. **AI Client (`app/ai.py`)**
- Integrates with OpenAI's GPT models
- Generates contextual responses to user messages
- Handles API errors and retries

#### 4. **Webhook Routes (`app/routes.py`)**
- Processes incoming WhatsApp webhooks
- Handles both verification (GET) and message delivery (POST)
- Orchestrates message processing flow

#### 5. **Command System (`app/commands.py`)**
- Processes slash commands (e.g., `/help`, `/start`)
- Extensible framework for adding new commands
- User-specific command handling

### Data Flow

1. **Message Reception**: WhatsApp sends webhook to your endpoint
2. **Message Extraction**: `WhatsAppClient.unpack_messages()` extracts message content
3. **AI Processing**: `AIClient.generate_reply()` generates response using GPT
4. **Message Sending**: `WhatsAppClient.send_message()` sends response back to user

## 🔧 Customization

### Adding New Commands

Extend the `CommandHandler` class in `app/commands.py`:

```python
def __init__(self):
    self.commands = {
        "help": self.help,
        "start": self.start,
        "weather": self.weather,  # New command
    }

def weather(self, args, user_id):
    """Get weather information for a location."""
    location = " ".join(args) if args else "default location"
    return f"Weather for {location}: Sunny and 25°C"
```

### Customizing AI Prompts

Modify the prompt templates in `app/ai_prompts.py`:

```python
customer_service_prompt = """
You are a helpful customer service representative for {company_name}.
Always be polite, professional, and solution-oriented.

Customer message: "{message_text}"
Your response:
"""
```

### Adding New Message Types

Extend the webhook handler in `app/routes.py` to handle different message types:

```python
for message in messages:
    if message.get("type") == "text":
        # Handle text messages
        parsed_message = message["text"]["body"]
        reply_message = current_app.ai_client.generate_reply(parsed_message)
    elif message.get("type") == "image":
        # Handle image messages
        reply_message = "I received your image!"
    # Add more message type handlers
```

## 🧪 Testing

Run the test suite:

```bash
python -m pytest tests/
```

## 📝 Logging

The application logs to both console and file (`logs/app.log`). Log levels include:
- **INFO**: General application flow
- **WARNING**: Non-critical errors (permission errors, validation errors)
- **ERROR**: Critical errors and exceptions

## 🚀 Production Deployment

### Using Gunicorn

```bash
pip install gunicorn
gunicorn app.main:app --bind 0.0.0.0:8000 --workers 4
```

### Using Docker

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["gunicorn", "app.main:app", "--bind", "0.0.0.0:8000"]
```

## 🔒 Security Considerations

- **Environment Variables**: Never commit API keys to version control
- **Webhook Verification**: Always verify webhook tokens
- **Input Validation**: Validate all incoming messages
- **Rate Limiting**: Implement rate limiting for production use
- **HTTPS**: Use HTTPS in production for webhook endpoints

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For issues and questions:
1. Check the documentation in the code comments
2. Review the error logs in `logs/app.log`
3. Open an issue on GitHub

## 🔗 Related Resources

- [WhatsApp Business API Documentation](https://developers.facebook.com/docs/whatsapp)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python-dotenv Documentation](https://pypi.org/project/python-dotenv/)
