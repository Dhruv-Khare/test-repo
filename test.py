except json.JSONDecodeError:
        logger.error(f"Could not parse Gemini response: {raw[:200]}")
        return "Review complete.", []
