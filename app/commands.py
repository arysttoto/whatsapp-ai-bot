class CommandHandler:
    def __init__(self):
        self.commands = {
            "help": self.help,
            "start": self.start,
        }

    def parse_and_execute(self, message, user_id): 
        if not message.startswith("/"):
            return None  # Not a command
        parts = message[1:].split()
        command = parts[0].lower()
        args = parts[1:]
        handler = self.commands.get(command)
        if handler:
            return handler(args, user_id)
        else:
            return "Unknown command. Type /help for available commands."

    def help(self, args, user_id):
        return "Available commands: /help, /start"

    def start(self, args, user_id):
        return f"Hello, user {user_id}! Welcome to the WhatsApp AI bot."
