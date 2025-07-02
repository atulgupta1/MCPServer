# 🧠 MCP Server: Multi-Tool AI Agent Using LangGraph + LangChain + Groq

This project demonstrates how to create a **multi-tool AI agent** using:

- 🧩 **LangGraph** for agent orchestration
- 🔗 **LangChain** for tool integration
- ⚙️ **MCP Adapters** for local and remote tool execution (via `stdio` and HTTP)
- ⚡ **Groq LLMs** for blazing-fast reasoning
- 🌐 A simple math tool (`mathserver.py`) and a mock weather tool

---

## 📦 Requirements

- Python 3.10+
- Virtual environment (`.venv`) created in the project folder
- GROQ API key (see `.env`)

Install dependencies:

```bash
.venv\Scripts\activate
pip install -r requirements.txt
🔑 Setup
Create .env file with your Groq key:

ini
Copy
Edit
GROQ_API_KEY=your_groq_key_here
Ensure your virtual environment is activated:

bash
Copy
Edit
.venv\Scripts\activate
Start the MCP-compatible weather tool server:

Assumes it's running locally at http://127.0.0.1:8000/mcp
Use FastAPI or Flask based mock server.

bash
Copy
Edit
python weather_server.py
Run the AI agent:

bash
Copy
Edit
python client.py
🧮 Tools Used
1. Math Tool (stdio)
Launched from mathserver.py

Communicates via stdin/stdout

Handles basic math (currently only +)

2. Weather Tool (HTTP)
Responds to queries like: "What is the weather in California?"

Return mock data like "It's always raining" or real data if extended

🧠 Example Prompts
text
Copy
Edit
what's (3+5)*12?
what is the weather in California?
🛠 File Structure
graphql
Copy
Edit
MCP Server/
│
├── .venv/                  # Virtual environment
├── client.py               # Main agent entrypoint
├── mathserver.py           # MCP math tool (stdio)
├── weather_server.py       # Optional: HTTP weather tool (FastAPI)
├── .env                    # Contains GROQ_API_KEY
├── requirements.txt        # Dependencies
└── README.md               # You're here!
🧰 Troubleshooting
TypeError: 'AIMessage' object is not subscriptable
➜ Use .content instead of ['messages'][-1]['content']:

python
Copy
Edit
print("math response:", math_response.content)
RuntimeError: Event loop is closed
➜ Harmless on Windows — suppressed in __main__ block

🚀 Future Ideas
Add more tools (e.g. Wikipedia, calculator, unit converter)

Handle multiple arithmetic operations

Stream agent responses

Deploy as a local assistant or API

👨‍💻 Author
Atul Gupta


🪄 License
MIT License – use freely, attribute respectfully.

yaml
Copy
Edit

---

Let me know if you want me to generate a `requirements.txt`, or add `weather_server.py` FastAPI stub too.