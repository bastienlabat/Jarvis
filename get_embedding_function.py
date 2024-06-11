from langchain_community.embeddings.ollama import OllamaEmbeddings

def get_embedding_function():
    #there are tons and tons of options here I am just picking this one cause it's common af
    embeddings = OllamaEmbeddings(model='nomic-embed-text')

    return embeddings
