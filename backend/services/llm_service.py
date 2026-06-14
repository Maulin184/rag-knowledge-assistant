from groq import Groq

from backend.config import (
    LLM_MODEL,
    MAX_TOKENS,
    TEMPERATURE
)

class LLMService:

    def __init__(
        self,
        api_key: str
    ):

        self.client = Groq(
            api_key=api_key
        )

    def build_prompt(
        self,
        chat_history_text,
        question: str,
        context: str
    ) -> str:
        
        return f"""
        You are a helpful AI assistant.

        Use the conversation history.

        Answer the question only from the provided context.

        If the answer is not available in the context,
        say:

        "I could not find the answer in the provided documents."

        Conversation History:
        {chat_history_text}

        Context:
        {context}

        Question:
        {question}

        Answer:
        """ 

    def generate_answer(
        self,
        question,
        context,
        chat_history=None
    ) -> str:
        
        chat_history_text = (
            self.format_chat_history(
                chat_history
            )
)

        prompt = self.build_prompt(
            chat_history_text,
            question,
            context
        )

        response = (
            self.client.chat.completions.create(
                model=LLM_MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=TEMPERATURE,
                max_completion_tokens=MAX_TOKENS
            )
        )

        return (
            response.choices[0]
            .message
            .content
        )
    
    def format_chat_history(
        self,
        messages
    ):

        if not messages:
            return ""

        history = []

        for message in messages:

            role = (
                message["role"]
                .capitalize()
            )

            content = (
                message["content"]
            )

            history.append(
                f"{role}: {content}"
            )

        return "\n".join(
            history
        )