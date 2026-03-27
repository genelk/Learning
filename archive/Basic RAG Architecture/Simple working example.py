# rag_simple.py
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# Load docs
loader = TextLoader("my_docs.txt")
documents = loader.load()

# Split
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)

# Embed and store
embeddings = OpenAIEmbeddings()
db = Chroma.from_documents(chunks, embeddings)

# Create QA chain
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    retriever=db.as_retriever()
)

# Query
answer = qa.run("What is the main topic of the document?")
print(answer)
