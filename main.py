import asyncio
from init_kernel import init_kernel_with_google_ai
from agents.extraction_agent import ExtractionAgent
from agents.processing_agent import GeminiAgent
from agents.email_agent import EmailAgent
import json

async def main():
    file_path = "Prescription_Notes/Prescription_JohnDoe.txt"
    # file_path = "Prescription_Notes/Prescription_Rocky.jpg"

    # Initialize Semantic Kernel & ChromaDB Memory
    kernel, memory, memory_store = init_kernel_with_google_ai()

    # Initialize Agents
    extractor = ExtractionAgent()
    gemini_agent = GeminiAgent(kernel, memory, memory_store)
    email_agent = EmailAgent()

    # Extract Text from File
    extracted_text = extractor.extract_content(file_path, "txt")
    # extracted_text = extractor.extract_content(file_path, "image")

    # Process Instructions with Gemini
    instructions, time_actions = await gemini_agent.process_content(extracted_text)

    # Convert actions to JSON format
    time_actionsJson = json.loads(time_actions)

    print("Instructions:\n", instructions)
    print("\n⏰ Time-based actions extracted:\n", time_actionsJson)

    # Schedule reminders & send emails
    await email_agent.schedule_reminders(time_actionsJson, kernel)

if __name__ == "__main__":
    asyncio.run(main())
