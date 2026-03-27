import openai
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

class ProductionRAG:
    def __init__(self):
        # Vector database
        self.pc = Pinecone(api_key="xxx")
        self.index = self.pc.Index("company-docs")
        
        # Embedding model
        self.embedder = SentenceTransformer('all-mpnet-base-v2')
        
        # LLM
        self.client = openai.OpenAI(api_key="xxx")
    
    def index_document(self, doc_id, text):
        """Add document to vector DB"""
        # Chunk document
        chunks = self.chunk_text(text, chunk_size=500)
        
        # Create embeddings
        for i, chunk in enumerate(chunks):
            embedding = self.embedder.encode(chunk).tolist()
            
            # Store in vector DB
            self.index.upsert(vectors=[{
                'id': f'{doc_id}_{i}',
                'values': embedding,
                'metadata': {'text': chunk, 'doc_id': doc_id}
            }])
    
    def query(self, question, top_k=3):
        """Query with RAG"""
        # Embed question
        question_embedding = self.embedder.encode(question).tolist()
        
        # Retrieve relevant chunks
        results = self.index.query(
            vector=question_embedding,
            top_k=top_k,
            include_metadata=True
        )
        
        # Build context from retrieved chunks
        context = "\n\n".join([
            match['metadata']['text'] 
            for match in results['matches']
        ])
        
        # Generate answer with LLM
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Answer based only on the provided context."},
                {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
            ]
        )
        
        return response.choices[0].message.content
    
    def chunk_text(self, text, chunk_size=500, overlap=50):
        """Split text into overlapping chunks"""
        words = text.split()
        chunks = []
        for i in range(0, len(words), chunk_size - overlap):
            chunk = ' '.join(words[i:i + chunk_size])
            chunks.append(chunk)
        return chunks
```

### **What Interviewers Would Ask:**

- "Explain how RAG works at a high level"
- "What chunking strategies have you used and why?"
- "How do you choose chunk size and overlap?"
- "What vector databases have you worked with?" (Pinecone, Weaviate, Chroma, FAISS)
- "How do you handle RAG for multiple document types?" (PDF, HTML, etc.)
- "What's your approach to evaluating RAG quality?"
- "How do you optimize retrieval accuracy?"
- "Explain the difference between embeddings and LLM generation"

### **Beginner Project (1 Weekend):**
```
Build a simple "Ask Questions About Your Documents" app:
1. Get OpenAI API key (free trial)
2. Install: pip install langchain openai chromadb
3. Load 3-5 text documents (company policies, Wikipedia articles, etc.)
4. Chunk them (500 chars per chunk)
5. Create embeddings and store in ChromaDB
6. Build query function
7. Test asking questions

Total time: 4-8 hours
