import datetime

class Chatbot:
    """
    A simple chatbot that provides conversational responses.
    Simulates traditional LLM behavior focused on text generation.
    """
    def ask(self, prompt: str) -> str:
        prompt_lower = prompt.lower()
        if "merhaba" in prompt_lower or "selam" in prompt_lower:
            return "Merhaba! Size nasıl yardımcı olabilirim?"
        elif "nasılsın" in prompt_lower:
            return "Ben bir yapay zekayım, duygularım yok ama her zaman göreve hazırım!"
        elif "hava" in prompt_lower:
            return "Üzgünüm, şu anki hava durumu bilgisine erişimim yok."
        elif "rapor" in prompt_lower:
            return "Elbette, ne hakkında bir rapor taslağı oluşturmamı istersiniz?"
        elif "toplantı" in prompt_lower:
            return "Toplantı planlamak için bana tarih, saat ve katılımcıları söyleyebilir misiniz?"
        else:
            return "Anladım. Başka ne hakkında konuşmak istersiniz?"

class OpenWorkerAI:
    """
    A simulated OpenWorker AI that identifies and "executes" tasks
    beyond just conversational responses, demonstrating the core article concept.
    """
    def _perform_task(self, task_name: str, args: dict) -> str:
        """Simulates the execution of a specific task."""
        if task_name == "create_report_draft":
            topic = args.get("topic", "genel bir konu")
            # This is where a real OpenWorker would interface with tools/APIs to create a file
            return f"TASK EXECUTED: '{topic}' hakkında bir rapor taslağı oluşturuldu. Dosya: report_draft_{datetime.date.today()}.txt"
        elif task_name == "schedule_meeting":
            date_str = args.get("date", "yarın")
            time_str = args.get("time", "belirtilmedi")
            # This is where a real OpenWorker would interface with a calendar API
            return f"TASK EXECUTED: '{date_str} {time_str}' için bir toplantı planlandı. Katılımcılar eklenebilir."
        elif task_name == "set_reminder":
            reminder_text = args.get("text", "bir görev")
            when = args.get("when", "yakın zamanda")
            # This is where a real OpenWorker would interface with a reminder service
            return f"TASK EXECUTED: '{when}' için '{reminder_text}' hatırlatıcısı ayarlandı."
        else:
            return f"TASK FAILED: Bilinmeyen görev '{task_name}'."

    def execute_task(self, prompt: str) -> str:
        prompt_lower = prompt.lower()

        # Simplified task identification logic (in a real OpenWorker, this would be an LLM's role)
        if "rapor taslağı oluştur" in prompt_lower or "rapor hazırla" in prompt_lower:
            topic = "belirtilmemiş"
            if "hakkında" in prompt_lower:
                parts = prompt_lower.split("hakkında")
                if len(parts) > 1:
                    topic = parts[1].split("oluştur")[0].strip()
            return self._perform_task("create_report_draft", {"topic": topic})
        elif "toplantı planla" in prompt_lower or "toplantı ayarla" in prompt_lower:
            date = "yarın" 
            time = "öğleden sonra" 
            if "bugün" in prompt_lower: date = "bugün"
            if "yarın" in prompt_lower: date = "yarın"
            if "sabah" in prompt_lower: time = "sabah"
            if "öğleden sonra" in prompt_lower: time = "öğleden sonra"
            return self._perform_task("schedule_meeting", {"date": date, "time": time})
        elif "hatırlatıcı ayarla" in prompt_lower or "hatırlatıcı oluştur" in prompt_lower:
            reminder_text = "bir görev"
            when = "yakın zamanda"
            if "için" in prompt_lower:
                parts = prompt_lower.split("için")
                if len(parts) > 0:
                    reminder_text = parts[0].replace("hatırlatıcı ayarla", "").strip()
            return self._perform_task("set_reminder", {"text": reminder_text, "when": when})
        elif "hava nasıl" in prompt_lower:
            # Fallback for non-task-oriented questions
            return "Şu anki hava durumu bilgisine erişimim yok, ancak başka bir konuda yardımcı olabilirim."
        else:
            # Fallback to conversational if no task is identified
            return "Anladım. Bu bir görev komutu gibi görünmüyor, başka nasıl yardımcı olabilirim?"

# --- Demonstration ---
if __name__ == "__main__":
    print("--- Andrew Ng'in OpenWorker'ı: Görev Odaklı Yapay Zeka Örneği ---")
    print("Bu örnek, geleneksel bir sohbet robotu ile görev odaklı bir yapay zeka arasındaki farkı gösterir.\n")

    chatbot = Chatbot()
    openworker = OpenWorkerAI()

    prompts = [
        "Merhaba, nasılsın?",
        "Bana bir rapor taslağı oluşturabilir misin?",
        "Yapay zeka teknolojileri hakkında bir rapor taslağı oluştur.",
        "Yarın için bir toplantı planla.",
        "Bugün hava nasıl?",
        "E-postaları kontrol etmem için hatırlatıcı ayarla."
    ]

    for i, prompt in enumerate(prompts):
        print(f"\n--- Senaryo {i+1}: '{prompt}' ---")

        print("\n[Geleneksel Sohbet Robotu Yanıtı]:")
        # Chatbot focuses on conversational responses, often asking for more details for tasks
        print(chatbot.ask(prompt))

        print("\n[OpenWorker AI Yanıtı]:")
        # OpenWorker attempts to identify and 'execute' a task, providing a confirmation of action
        print(openworker.execute_task(prompt))
        print("-" * 50)

    print("\nÖrnek sonu.")
