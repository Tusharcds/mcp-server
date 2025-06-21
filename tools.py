from langchain.tools import tool

@tool
def web_search(query: str) -> str:
    """Perform a web search and return summary."""
    return f"Search results for '{query}' (simulated)."

@tool
def echo(text: str) -> str:
    """Echo input back."""
    return text