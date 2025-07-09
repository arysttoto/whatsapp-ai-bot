class RetryableError(Exception):
    """Raise this to trigger a WhatsApp retry via 503 response"""
    pass
