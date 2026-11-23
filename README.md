# LangChain Practice

A hands-on learning repository documenting my journey of learning **LangChain by actually coding and experimenting with its core components.**

This repository contains small Python implementations, experiments, and beginner-level applications built while exploring how LangChain works. Instead of only studying concepts theoretically, I use this repository to understand how different components work, how they connect, and how they can be used to build AI-powered applications.

The goal is to develop a practical understanding of LangChain, from interacting with LLMs to building basic agents and experimenting with Retrieval-Augmented Generation (RAG).

**Repository:** [Langchain-Practice](https://github.com/ahsan-ali-005/Langchain-Practice)

---

## What I Learned

This repository covers the following LangChain concepts:

- Working with different LLMs and chat models.
- Generating and working with text embeddings.
- Designing prompts and managing conversation history.
- Generating structured outputs using different approaches.
- Building sequential, parallel, and conditional chains.
- Understanding LangChain Runnables and LCEL.
- Exploring Retrieval-Augmented Generation (RAG).
- Loading, splitting, storing, and retrieving documents.
- Creating custom tools and implementing tool calling.
- Building basic AI agents that can use tools.

---

## Repository Structure

```text
Langchain-Practice/
│
├── 01. LLMS/
│   └── llm_demo.py
│
├── 02. ChatModels/
│   ├── chat_model_hf_local.py
│   ├── chatmodel_anthropic.py
│   ├── chatmodel_google.py
│   ├── chatmodel_hf_api.py
│   └── chatmodel_openai.py
│
├── 03. EmbeddingModels/
│   ├── document_similarity.py
│   ├── embedding_docs_hf_local.py
│   ├── embedding_hf_local.py
│   ├── google_embedding_docs.py
│   └── google_embedding_model.py
│
├── 04. Prompts/
│   ├── ai_blog_generator.py
│   ├── basic_chatbot.py
│   ├── chatbot_with_context.py
│   ├── langchain_chat_prompt_template.py
│   ├── langchain_message_placeholder.py
│   ├── messages.py
│   ├── prompt_generator.py
│   ├── prompt_template.json
│   └── chat_history.txt
│
├── 05. Structured Outputs/
│   ├── Output Parsers/
│   │   ├── json_output_parsers.py
│   │   ├── pydantic_output_parsers.py
│   │   └── string_output_parsers.py
│   │
│   ├── using_json_schema.py
│   ├── using_pydantic.py
│   └── using_typed_dict.py
│
├── 06. Chains/
│   ├── conditional_chain.py
│   ├── parallel_chain.py
│   └── sequential_chain.py
│
├── 07. Runnables/
│   ├── runnable_branch.py
│   ├── runnable_lambda.py
│   ├── runnable_parallel.py
│   ├── runnable_pass_through.py
│   └── runnable_sequence.py
│
├── 08. RAG/
│   ├── 1. Document Loaders/
│   │   ├── csv_loader.py
│   │   ├── directory_loader.py
│   │   ├── pdf_loader.py
│   │   ├── text_loader.py
│   │   └── web_base_loader.py
│   │
│   ├── 2. Text Splitters/
│   │   ├── document_structure_based.py
│   │   ├── length_based.py
│   │   ├── semantic_meaning_based.py
│   │   └── text_structure_based.py
│   │
│   ├── 3. Vector DBs/
│   │   └── chroma_db.py
│   │
│   └── 4. Retrievers/
│       ├── contexttual_compression_retriever.py
│       ├── mmr_retriever.py
│       ├── multi_query_retriever.py
│       ├── vector_store_retriever.py
│       └── wikipedia_retriever.py
│
├── 09. Tools/
│   ├── tool_call_injected_arg.py
│   ├── toolcalling.py
│   ├── toolkit.py
│   ├── using_basetool.py
│   ├── using_structuredtool.py
│   └── using_tool_decorator.py
│
├── 10. Agents/
│   └── basic_agent.py
│
├── PDFs/
│   ├── The Prompt Ladder.pdf
│   └── What Are You Proving_.pdf
│
├── chroma_db/
├── my_dataset.csv
├── sample.txt
├── requirements.txt
└── .gitignore
```

---

## Topics & Implementations

### 1. LLMs

**Folder:** `01. LLMS/`

Started by exploring traditional LLM integrations through LangChain.

- Initializing an LLM using LangChain.
- Configuring model parameters such as temperature and maximum tokens.
- Sending prompts using `.invoke()`.
- Understanding the basic interaction between an application and an LLM.

**Implementation:** `llm_demo.py`

### 2. Chat Models

**Folder:** `02. ChatModels/`

Exploring different chat model providers and how to interact with them using a consistent LangChain interface.

**Implementations include:**

- OpenAI Chat Models
- Google Gemini
- Anthropic Claude
- Hugging Face API models
- Locally running Hugging Face models

**What I explored:**
- Initializing different chat models.
- Sending messages using `.invoke()`.
- Working with model responses.
- Comparing hosted API models with local models.
- Understanding inference providers and Hugging Face pipelines.

### 3. Embedding Models

**Folder:** `03. EmbeddingModels/`

Exploring how text can be converted into numerical representations (vectors) using embedding models.

**Implementations include:**

- Google Generative AI Embeddings.
- Hugging Face local embeddings.
- Generating embeddings for individual queries.
- Generating embeddings for multiple documents.
- Measuring document similarity using cosine similarity.

**Practical experiment:**

`document_similarity.py` compares a user query against multiple documents using cosine similarity to identify the most relevant document.

This helped me understand how semantic similarity works and why embeddings are important in RAG applications.

### 4. Prompts

**Folder:** `04. Prompts/`

Exploring prompt engineering and how LangChain manages prompts and conversation history.

**Concepts covered:**

- PromptTemplate
- ChatPromptTemplate
- Messages and message types:
  - SystemMessage
  - HumanMessage
  - AIMessage
- MessagesPlaceholder
- Dynamic prompt variables.
- Conversation history and context management.
- JSON-based prompt templates.

**Practical Implementations:**

**AI Blog Generator**

A basic Streamlit application that generates blog posts using Google Gemini.

Users can provide:
- Blog niche (Tech, Finance, Medical).
- Blog topic.
- Primary keyword.
- Target audience.
- Desired word count.
- Writing tone.
- Writing style.

The application uses a customizable JSON prompt template containing instructions for generating SEO titles, meta descriptions, introductions, structured headings, practical examples, conclusions, and calls to action.

**Basic Chatbot**

A simple command-line chatbot that accepts user input and generates responses using Gemini.

**Chatbot with Context**

An experiment in maintaining conversation history so that the model can use previous messages as context.

Further experiments explore how System, Human, and AI messages help distinguish different roles in a conversation.

### 5. Structured Outputs

**Folder:** `05. Structured Outputs/`

Exploring how to get predictable and structured responses from LLMs instead of relying entirely on free-form text.

**Approaches explored:**

- JSON Schema
- Pydantic
- TypedDict

**Output Parsers:**

- StrOutputParser
- JsonOutputParser
- PydanticOutputParser

**Practical experiment:**

Analyzing product reviews and extracting:

- Review summary.
- Sentiment (positive, negative, or neutral).

Also explored the differences between schema-based structured outputs and output parsers, including their approaches to defining expected response formats and validation.

### 6. Chains

**Folder:** `06. Chains/`

Learning how to combine multiple LangChain components into workflows.

**Implementations:**

**Sequential Chain**

- Generates a detailed report on a given topic.
- Passes the generated report into another prompt.
- Extracts the five most important points.

**Parallel Chain**

- Generates notes and quiz questions simultaneously.
- Combines both outputs into a final response.

**Conditional Chain**

- Analyzes customer feedback sentiment.
- Identifies whether feedback is positive, negative, or neutral.
- Uses conditional logic to generate an appropriate response.

These implementations helped me understand how multiple LLM operations can be connected into a single workflow.

### 7. Runnables

**Folder:** `07. Runnables/`

Exploring LangChain Runnables and the LangChain Expression Language (LCEL).

**Concepts covered:**

- RunnableSequence
- RunnableParallel
- RunnableLambda
- RunnableBranch
- RunnablePassthrough

**Implementations:**

- Creating sequential execution pipelines.
- Running multiple operations in parallel.
- Integrating custom Python functions into chains.
- Passing data through workflows without modifying it.
- Assigning additional fields to existing inputs.
- Implementing conditional execution using RunnableBranch.

Also explored how Runnables make different LangChain components composable through a common interface.

### 8. Retrieval-Augmented Generation (RAG)

**Folder:** `08. RAG/`

Exploring the building blocks used in Retrieval-Augmented Generation systems.

This section is divided into four parts.

**A. Document Loaders**

Experimenting with loading information from different sources:

- CSVLoader
- TextLoader
- PyPDFLoader
- DirectoryLoader
- WebBaseLoader

Also explored loading documents individually using lazy loading.

**B. Text Splitters**

Understanding how large documents can be divided into smaller chunks before embedding and retrieval.

Implementations include:

- CharacterTextSplitter
- RecursiveCharacterTextSplitter
- Language-aware splitting.
- SemanticChunker.

Explored chunk size, chunk overlap, document structure, and semantic meaning.

**C. Vector Databases**

Working with ChromaDB through LangChain.

Explored:

- Creating document objects.
- Adding documents to a vector store.
- Generating and storing embeddings.
- Persisting vector database data.
- Retrieving stored documents.
- Similarity search.
- Similarity search with scores.
- Metadata filtering.
- Updating and deleting documents.

**D. Retrievers**

Experimenting with different retrieval strategies:

- Vector Store Retriever
- Maximum Marginal Relevance (MMR) Retriever
- Multi-Query Retriever
- Contextual Compression Retriever
- Wikipedia Retriever

These experiments helped me understand how relevant documents can be retrieved using different strategies rather than simply searching for matching keywords.

*Note: This section currently focuses on individual RAG components and retrieval experiments rather than a complete end-to-end RAG question-answering application.*

### 9. Tools

**Folder:** `09. Tools/`

Exploring how LLMs can interact with external functions and execute operations through tool calling.

**Concepts covered:**

- Custom tools using the `@tool` decorator.
- StructuredTool.
- BaseTool.
- Toolkits.
- Tool calling with Gemini.
- InjectedToolArg.
- Structured tool arguments and type definitions.

**Practical experiments:**

- Weather lookup (mock implementation).
- Rectangle area calculation.
- Addition and multiplication tools.
- Grouping related tools into a toolkit.
- Injecting runtime arguments that should not be generated by the LLM.

Also explored manually mapping and executing tool calls returned by the model.

### 10. Agents

**Folder:** `10. Agents/`

Started exploring basic AI agents using LangChain's `create_agent`.

**Implementation: Basic Tool-Using Agent**

The agent uses Google Gemini and a custom addition tool.

It can:
- Receive a natural language request.
- Determine when the calculator tool is needed.
- Call the addition function with the appropriate arguments.
- Return the tool result to the user.

This is a basic experiment to understand how an agent works with tools and how tool execution differs from a normal LLM response.

---

## Tech Stack & Libraries

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| LangChain | Building LLM-powered applications |
| LangChain Core | Prompts, messages, Runnables and parsers |
| Google Gemini | Chat models and embeddings |
| OpenAI | LLM and chat model experiments |
| Anthropic Claude | Chat model experiments |
| Hugging Face | Local and API-based models and embeddings |
| Pydantic | Data validation and structured outputs |
| Streamlit | AI Blog Generator interface |
| ChromaDB | Vector storage and similarity search |
| Scikit-learn | Cosine similarity |
| python-dotenv | Environment variable management |

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ahsan-ali-005/Langchain-Practice.git

cd Langchain-Practice
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Some examples also require additional packages that are not currently listed in `requirements.txt`:

```bash
pip install streamlit langchain-chroma langchain-community langchain-text-splitters langchain-experimental wikipedia
```

### 4. Configure Environment Variables

Create a `.env` file in the repository root.

Add the API keys for whichever providers you intend to use:

```env
GOOGLE_API_KEY=your_google_api_key
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
HUGGINGFACEHUB_ACCESS_TOKEN=your_huggingface_token
```

You don't need every API key to run every example. Configure the relevant provider for the script you want to execute.

**Important:** Never commit your `.env` file or expose API keys on GitHub.

### 5. Run an Example

For example, to run the basic LLM experiment:

```bash
python "01. LLMS/llm_demo.py"
```

To run the sequential chain:

```bash
python "06. Chains/sequential_chain.py"
```

To run the basic agent:

```bash
python "10. Agents/basic_agent.py"
```

For the AI Blog Generator:

```bash
streamlit run "04. Prompts/ai_blog_generator.py"
```

Check the relevant script and its file paths before running it. In particular, the Blog Generator currently references `Prompts/prompt_template.json`, whereas the actual folder is named `04. Prompts`. Its template path needs to be aligned with the repository structure.

---

## Learning Approach

This repository is primarily a practical learning space.

My approach is to:

1. Understand a LangChain concept.
2. Implement it using Python.
3. Experiment with its parameters and behavior.
4. Compare different approaches to solving the same problem.
5. Build small applications using the concepts I've learned.
6. Keep improving the implementations as my understanding grows.

Some implementations are intentionally basic because the main objective is to understand the underlying concepts before moving towards more complex applications.

---


### What's Next?

Some areas I plan to explore further:

- Building complete end-to-end RAG applications.
- Conversational RAG with persistent chat history.
- More advanced AI agents and tool orchestration.
- Agent memory and state management.
- LangGraph and multi-step agent workflows.
- Integrating LangChain applications with FastAPI.
- Building more practical AI-powered projects.

---

## A Note About This Repository

This isn't intended to be a collection of production-ready applications or a complete LangChain course.

It's my personal coding playground where I learn by implementing, experimenting, making mistakes, and improving my understanding of how LLM-powered applications work.

**Learn by building. Understand by experimenting. Improve by implementing.**

---

## Connect

**Ahsan Ali**

- GitHub: [@ahsan-ali-005](https://github.com/ahsan-ali-005)
- LinkedIn: [Ahsan Ali](https://www.linkedin.com/in/mu-ahsan-ali/)

