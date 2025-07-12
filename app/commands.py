"""
Command Processing System

This module provides a command handler for processing slash commands in
WhatsApp messages. It allows users to interact with the bot using
predefined commands like /help and /start.

The command system supports:
- Slash command parsing and execution
- Extensible command registration
- User-specific command handling
- Help system for available commands

Example:
    handler = CommandHandler()
    response = handler.parse_and_execute("/help", "user123")
"""

class CommandHandler:
    """
    Handler for processing slash commands in WhatsApp messages.

    This class manages the parsing and execution of user commands that
    start with a forward slash (/). It provides a framework for adding
    new commands and handling user interactions.

    Attributes:
        commands (dict): Mapping of command names to handler functions
    """

    def __init__(self):
        """
        Initialize command handler with default commands.

        Registers built-in commands including help and start commands.
        Additional commands can be added by extending the commands dictionary.
        """
        self.commands = {
            "help": self.help,
            "start": self.start,
        }

    def parse_and_execute(self, message, user_id): 
        """
        Parse and execute slash commands from user messages.

        Extracts command name and arguments from messages starting with '/',
        then executes the corresponding handler function if found.

        Args:
            message (str): The user's message text
            user_id (str): Unique identifier for the user

        Returns:
            str or None: Response message from command execution, or None
                        if message is not a command

        Example:
            >>> handler.parse_and_execute("/help", "user123")
            "Available commands: /help, /start"
            >>> handler.parse_and_execute("Hello", "user123")
            None
        """
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
        """
        Display available commands to the user.

        Args:
            args (list): Command arguments (unused for help command)
            user_id (str): User requesting help

        Returns:
            str: List of available commands
        """
        return "Available commands: /help, /start"

    def start(self, args, user_id):
        """
        Welcome new users to the bot.

        Args:
            args (list): Command arguments (unused for start command)
            user_id (str): User starting the bot

        Returns:
            str: Welcome message for the user
        """
        return f"Hello, user {user_id}! Welcome to the WhatsApp AI bot."
