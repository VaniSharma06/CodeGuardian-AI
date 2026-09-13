# 🛡️ CodeGuardian AI

## AI-Powered Multi-Agent Code Review Platform

CodeGuardian AI is a full-stack AI-powered code review platform that analyzes Python source code using a combination of **static analysis, specialized AI agents, and Generative AI**.

The system automatically reviews code for **bugs, security vulnerabilities, performance issues, and code-quality problems**, then combines the findings into a unified AI-generated review.

---

## 🚀 Why CodeGuardian AI?

Traditional code review can be time-consuming and inconsistent.

CodeGuardian AI provides an automated review pipeline where different AI agents specialize in different aspects of software quality.

```text
                    Python Source Code
                           │
                           ▼
                  ┌─────────────────┐
                  │  Static Analyzer│
                  │   Python AST    │
                  └────────┬────────┘
                           │
                           ▼
              ┌─────────────────────────┐
              │    Multi-Agent Layer    │
              ├─────────────────────────┤
              │ 🐞 Bug Detection Agent  │
              │ 🔐 Security Agent       │
              │ ⚡ Performance Agent    │
              │ ✨ Quality Agent        │
              └────────────┬────────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │  AI Synthesizer │
                  └────────┬────────┘
                           │
                           ▼
                 Final Review Report
                           │
                           ▼
                  React Dashboard

✨ Key Features
🤖 Multi-Agent AI Code Review

Specialized AI agents independently analyze different aspects of submitted code.

🐞 Bug Detection — identifies potential logical and runtime issues
🔐 Security Analysis — detects potentially unsafe operations and vulnerabilities
⚡ Performance Analysis — identifies inefficient algorithms and operations
✨ Code Quality Analysis — reviews readability, structure, naming, and maintainability
🧠 AI Synthesizer — combines all findings into a unified final review
🔎 Static Code Analysis

Uses Python's Abstract Syntax Tree (AST) to perform deterministic source-code analysis.

Current checks include:

Function detection
Missing function documentation
print() usage
Dangerous eval() usage
Nested loops
Basic structural analysis
🧠 Generative AI

Google Gemini is used to provide intelligent reasoning and recommendations beyond predefined static-analysis rules.

🌐 Interactive Web Dashboard

A React-based dashboard allows users to:

Enter Python code
Submit it for analysis
Monitor the review process
View specialized agent reports
Read the final AI-generated review
🔄 Full-Stack Architecture

The project connects:

React Frontend
      ↓
FastAPI REST API
      ↓
Static Analyzer + AI Agents
      ↓
Google Gemini
      ↓
Final Review
      ↓
React Dashboard
🏗️ System Architecture
                         ┌─────────────────────┐
                         │      USER CODE      │
                         │       Python        │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   FastAPI Backend   │
                         └──────────┬──────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                    ▼                               ▼
          ┌──────────────────┐           ┌────────────────────┐
          │  Static Analyzer │           │    AI Agents       │
          │   Python AST     │           │                    │
          └────────┬─────────┘           │ 🐞 Bug Agent       │
                   │                     │ 🔐 Security Agent  │
                   │                     │ ⚡ Performance     │
                   │                     │ ✨ Quality Agent   │
                   │                     └─────────┬──────────┘
                   │                               │
                   └──────────────┬────────────────┘
                                  ▼
                       ┌─────────────────────┐
                       │   AI Synthesizer    │
                       │   Final AI Review   │
                       └──────────┬──────────┘
                                  │
                                  ▼
                       ┌─────────────────────┐
                       │   React Dashboard   │
                       └─────────────────────┘

🔄 How It Works
1. Code Submission

The user enters Python source code through the React dashboard.

The frontend sends the code to the FastAPI backend through the /review API endpoint.

2. Static Analysis

The backend parses the submitted Python source code using Python's AST module.

This allows CodeGuardian AI to identify predefined structural patterns without relying entirely on an AI model.

Python Code
     ↓
Python AST
     ↓
Static Analysis
     ↓
Static Findings
3. Specialized AI Agents

The code is analyzed by multiple specialized AI agents.

🐞 Bug Detection Agent

Focuses on:

Logical errors
Runtime risks
Incorrect assumptions
Potential failure cases
🔐 Security Agent

Focuses on:

Unsafe functions
Input handling
Injection risks
Hardcoded secrets
Security weaknesses
⚡ Performance Agent

Focuses on:

Inefficient loops
Nested iterations
Repeated calculations
Algorithmic inefficiencies
Data-structure choices
✨ Quality Agent

Focuses on:

Readability
Naming
Structure
Documentation
Maintainability
Best practices
4. AI Synthesis

The individual agent reports are passed to an AI synthesizer.

The synthesizer creates a consolidated report containing:

Summary
Severity
Bugs
Security issues
Performance issues
Quality improvements
Recommendations


🛠️ Technology Stack

Backend
Technology	Purpose
Python	Core programming language
FastAPI	REST API backend
Pydantic	Request validation
Python AST	Static code analysis
Uvicorn	Development server
AI
Technology	Purpose
Google Gemini	Generative AI analysis
Multi-Agent Architecture	Specialized code review
AI Synthesizer	Final report generation
Frontend
Technology	Purpose
React	User interface
Vite	Frontend development/build tool
JavaScript	Frontend logic
CSS	Dashboard styling
Development
PyCharm
Git
GitHub
npm
REST APIs


📁 Project Structure

CodeGuardian-AI/
│
├── agents/
│   ├── bug_agent.py
│   ├── security_agent.py
│   ├── performance_agent.py
│   ├── quality_agent.py
│   └── synthesizer.py
│
├── analyzers/
│   └── code_analyzer.py
│
├── services/
│   └── gemini_service.py
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── main.jsx
│   │   └── index.css
│   │
│   ├── package.json
│   └── vite.config.js
│
├── main.py
├── .env
├── .gitignore
└── README.md


🔌 API
GET /

Returns a welcome response and confirms that the backend is running.

Example:

{
  "message": "Welcome to CodeGuardian AI!"
}
POST /review

Analyzes submitted Python source code.

Example Request
{
  "code": "def divide(a, b):\n    return a / b"
}
Response

The API returns:

Status
│
├── Static Analysis
│
├── Bug Agent
│
├── Security Agent
│
├── Performance Agent
│
├── Quality Agent
│
└── Final AI Review
🧪 Example
Input
def check(data):
    for x in data:
        for y in data:
            print(eval(x))
Potential Findings

CodeGuardian AI can identify concerns including:

Nested-loop performance
Unsafe eval() usage
Potential security weaknesses
Code-quality improvements

The findings from the specialized agents are then combined by the AI synthesizer.

⚙️ Installation
Prerequisites

Make sure you have:

Python 3.10+
Node.js
npm
Git
Google Gemini API key
1. Clone the Repository
git clone https://github.com/VaniSharma06/CodeGuardian-AI.git
cd CodeGuardian-AI
2. Create a Virtual Environment
python -m venv .venv
Windows
.venv\Scripts\activate
3. Install Backend Dependencies
pip install fastapi uvicorn google-genai python-dotenv
🔑 Environment Configuration

Create a .env file in the project root:

GEMINI_API_KEY=your_api_key_here

Never commit your real API key to GitHub.

The repository's .gitignore is configured to exclude .env.

▶️ Run the Backend

From the project root:

uvicorn main:app --reload

Backend:

http://127.0.0.1:8000

FastAPI documentation:

http://127.0.0.1:8000/docs
💻 Run the Frontend

Open another terminal:

cd frontend
npm install
npm run dev

Frontend:

http://localhost:5173
🔗 Frontend–Backend Communication
┌─────────────────────┐
│   React Frontend    │
│   localhost:5173    │
└──────────┬──────────┘
           │
           │ HTTP POST
           ▼
┌─────────────────────┐
│   FastAPI Backend   │
│  127.0.0.1:8000     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Static Analyzer   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│     AI Agents       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    Gemini API       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Final AI Review   │
└─────────────────────┘

🎯 Engineering Highlights

This project demonstrates practical experience with:

Multi-agent AI architecture
Generative AI integration
Prompt engineering
Python AST processing
Static code analysis
REST API development
FastAPI
React
Frontend-backend integration
CORS configuration
API request validation
Environment-variable management
Modular software architecture
Git and GitHub

📐 Design Principles

CodeGuardian AI follows a modular architecture where each component has a clear responsibility.

analyzers/
    ↓
Static code analysis

agents/
    ↓
Specialized AI reasoning

services/
    ↓
External AI service integration

main.py
    ↓
API orchestration

frontend/
    ↓
User interface

This separation makes the system easier to maintain, test, and extend.

🔮 Future Enhancements

GitHub Integration
Repository analysis
Pull Request reviews
Automated review comments
Diff-based code analysis
Advanced Code Analysis
Code complexity scoring
Code quality scoring
Duplicate-code detection
Dependency analysis
More AST-based rules
AI Improvements
Automatic code-fix suggestions
Explainable recommendations
Context-aware reviews
Support for additional programming languages
Developer Experience
Review history
Exportable reports
User authentication
Team dashboards
CI/CD integration
📊 Project Highlights
Area	Implementation
AI Architecture	Multi-Agent System
Static Analysis	Python AST
Backend	FastAPI
Frontend	React + Vite
AI Model	Google Gemini
API	REST
Security	Security-focused AI analysis
Performance	Performance-focused AI analysis
Code Quality	Dedicated quality agent
Version Control	Git + GitHub

🧠 Learning Outcomes

Through this project, the following concepts were implemented:

Designing modular AI systems
Working with Generative AI APIs
Building specialized AI agents
Combining deterministic analysis with AI reasoning
Creating REST APIs
Connecting React applications with Python backends
Handling API requests and responses
Managing environment variables securely
Structuring a full-stack software project
Using Git and GitHub for project version control

🚀 Project Vision

CodeGuardian AI aims to demonstrate how Generative AI and traditional software-engineering techniques can work together to build intelligent developer tools.

Instead of relying on a single AI prompt, the system distributes code-review responsibilities across specialized agents and uses an AI synthesis layer to produce a consolidated review.

Analyze → Detect → Explain → Improve
👩‍💻 Author
Vani Sharma

Computer Science & Engineering Student

GitHub:
https://github.com/VaniSharma06

⭐ Support

If you find CodeGuardian AI interesting, consider giving the repository a ⭐ on GitHub.

📜 License

This project is intended for educational and portfolio purposes.






