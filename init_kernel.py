import os
from dotenv import load_dotenv
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.google.google_ai import GoogleAIChatCompletion, GoogleAITextEmbedding
from semantic_kernel.memory import SemanticTextMemory
from semantic_kernel.connectors.memory.chroma import ChromaMemoryStore

def init_kernel_with_google_ai():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    kernel = Kernel()

    # Adding Gemini AI model
    kernel.add_service(
        GoogleAIChatCompletion(
            gemini_model_id="gemini-1.5-pro",
            api_key=api_key,
            service_id="gemini"
        )
    )

    # Embeddings for memory storage
    embedder = GoogleAITextEmbedding(
        api_key=api_key,
        service_id="embedder",
        embedding_model_id="models/embedding-001"
    )

    kernel.add_service(embedder)

    # Restoring ChromaDB memory for caching
    memory_store = ChromaMemoryStore(persist_directory="./chroma_store")
    memory = SemanticTextMemory(storage=memory_store, embeddings_generator=embedder)

    return kernel, memory, memory_store
