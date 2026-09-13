import { useState } from "react";
import "./App.css";

function App() {
  const [code, setCode] = useState(
`def divide(a, b):
    return a / b`
  );

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const reviewCode = async () => {
    if (!code.trim()) return;

    setLoading(true);
    setResult(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/review", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ code }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error("Review failed");
      }

      setResult(data);
    } catch (error) {
      setResult({
        error: "Could not connect to CodeGuardian backend. Make sure FastAPI is running."
      });
    }

    setLoading(false);
  };

  return (
    <div className="app">

      <header className="navbar">
        <div className="brand">
          <div className="logo">🛡️</div>
          <div>
            <h1>CodeGuardian AI</h1>
            <p>Intelligent Multi-Agent Code Review</p>
          </div>
        </div>

        <div className="status">
          <span className="status-dot"></span>
          AI Engine Online
        </div>
      </header>

      <main className="container">

        <section className="hero">
          <div>
            <span className="badge">AI-POWERED CODE ANALYSIS</span>
            <h2>
              Write better code.<br />
              <span>Ship with confidence.</span>
            </h2>
            <p>
              CodeGuardian analyzes your code using specialized AI agents
              for bugs, security, performance and quality.
            </p>
          </div>
        </section>

        <section className="workspace">

          <div className="editor-card">
            <div className="card-header">
              <div>
                <h3>Code Input</h3>
                <p>Paste your Python code below</p>
              </div>

              <span className="language">PYTHON</span>
            </div>

            <textarea
              value={code}
              onChange={(e) => setCode(e.target.value)}
              spellCheck="false"
              placeholder="Paste your Python code here..."
            />

            <button
              className="review-button"
              onClick={reviewCode}
              disabled={loading}
            >
              {loading ? "Analyzing..." : "🔍 Review Code"}
            </button>
          </div>

          <div className="agents-card">
            <div className="card-header">
              <div>
                <h3>AI Review Agents</h3>
                <p>Specialized analysis pipeline</p>
              </div>
            </div>

            <div className="agent">
              <span>🐞</span>
              <div>
                <strong>Bug Detection</strong>
                <small>Logic & runtime issues</small>
              </div>
            </div>

            <div className="agent">
              <span>🔐</span>
              <div>
                <strong>Security Analysis</strong>
                <small>Vulnerabilities & risks</small>
              </div>
            </div>

            <div className="agent">
              <span>⚡</span>
              <div>
                <strong>Performance</strong>
                <small>Efficiency & optimization</small>
              </div>
            </div>

            <div className="agent">
              <span>✨</span>
              <div>
                <strong>Code Quality</strong>
                <small>Readability & maintainability</small>
              </div>
            </div>
          </div>

        </section>

        {loading && (
          <div className="loading">
            <div className="spinner"></div>
            <h3>CodeGuardian is reviewing your code...</h3>
            <p>Running specialized AI agents</p>
          </div>
        )}

        {result && !loading && (
          <section className="results">

            {result.error ? (
              <div className="error">
                ⚠️ {result.error}
              </div>
            ) : (
              <>
                <div className="results-header">
                  <div>
                    <span className="badge">ANALYSIS COMPLETE</span>
                    <h2>Code Review Report</h2>
                  </div>

                  <div className="severity">
                    AI Review Generated
                  </div>
                </div>

                <div className="result-grid">

                  <div className="result-card">
                    <span>🐞</span>
                    <h3>Bug Analysis</h3>
                    <p>{result.agents?.bug}</p>
                  </div>

                  <div className="result-card">
                    <span>🔐</span>
                    <h3>Security Analysis</h3>
                    <p>{result.agents?.security}</p>
                  </div>

                  <div className="result-card">
                    <span>⚡</span>
                    <h3>Performance Analysis</h3>
                    <p>{result.agents?.performance}</p>
                  </div>

                  <div className="result-card">
                    <span>✨</span>
                    <h3>Quality Analysis</h3>
                    <p>{result.agents?.quality}</p>
                  </div>

                </div>

                <div className="final-review">
                  <div className="final-title">
                    <span>🤖</span>
                    <div>
                      <h3>AI Final Review</h3>
                      <p>Synthesized by CodeGuardian</p>
                    </div>
                  </div>

                  <pre>
                    {result.final_review}
                  </pre>
                </div>

              </>
            )}

          </section>
        )}

      </main>

      <footer>
        CodeGuardian AI • Multi-Agent Code Review System
      </footer>

    </div>
  );
}

export default App;
