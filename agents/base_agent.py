from config.env import * 

# === Core Agent Class ===
class CourtroomAgent:
    def __init__(self, name: str, system_prompt: str, model: str = "llama3-8b-8192"):
        self.name = name
        self.system_prompt = system_prompt.strip()
        self.history: list[dict[str, str]] = []
        self.client = Groq(api_key=key)
        self.model = model

    def _format_prompt(self, user_msg: str) -> list[dict[str, str]]:
        messages = [{"role": "system", "content": self.system_prompt}]
        messages.extend(self.history)
        messages.append({"role": "user", "content": user_msg})
        return messages

    def respond(self, user_msg: str, **gen_kwargs) -> str:
        messages = self._format_prompt(user_msg)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7,
            max_tokens=512,
            **gen_kwargs
        )
        answer = response.choices[0].message.content.strip()
        self.history.append({"role": "user", "content": user_msg})
        self.history.append({"role": "assistant", "content": answer})
        return answer