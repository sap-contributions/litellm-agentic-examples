# LiteLLM Agentic Examples for SAP Generative AI Hub

[![Documentation](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://sap-contributions.github.io/litellm-agentic-examples/)

Build AI agents with SAP Generative AI Hub using your favorite open-source frameworks. This repository provides practical examples showing how to integrate popular agentic frameworks with SAP's enterprise AI platform through LiteLLM.

## What You'll Find Here

This repository demonstrates how to:
- Connect various open-source agent frameworks to SAP Generative AI Hub
- Use both library-based and proxy-based integration approaches
- Build production-ready AI agents with enterprise-grade LLM access
- Leverage multiple LLM providers (OpenAI, Google, Amazon, Mistral, SAP, and more) through a single interface

**Missing a framework?** We welcome contributions! If you'd like to add an example for a framework not listed here, please open a pull request.

## Understanding the Components

### SAP Generative AI Hub

[SAP Generative AI Hub](https://help.sap.com/docs/sap-ai-core/generative-ai/generative-ai-hub?locale=en-US) is SAP's enterprise platform for accessing large language models. It provides centralized access to LLMs from multiple providers including OpenAI, Google, Amazon, Mistral, and SAP's own models, with built-in governance, security, and compliance features.

### LiteLLM

[LiteLLM](https://www.litellm.ai) is an open-source library that provides a unified interface for 100+ LLM providers. It translates requests into provider-specific formats, allowing you to use any LLM with a standardized OpenAI-compatible API.

### The Integration

Most open-source agent frameworks are designed to work with OpenAI's API. LiteLLM acts as a bridge, translating OpenAI-style requests to work with SAP Generative AI Hub. This means you can use any framework that supports OpenAI with SAP's enterprise LLM platform, without modifying the framework's code.

![LiteLLM_SAPGenAIHub.png](docs/source/_static/LiteLLM_SAPGenAIHub.png)

## Framework Support Overview

The following table shows which frameworks are included in this repository, their integration methods, and example notebooks:

| Framework | Description | Library | Proxy | Notebook Examples                                                                                       |
|-----------|-------------|---------|-------|---------------------------------------------------------------------------------------------------------|
| **LangGraph** | Low-level orchestration framework for building stateful, multi-agent applications using graph-based control flow with cyclic capabilities. Trusted by companies like Klarna, Replit, and Elastic for production deployment with built-in debugging via LangSmith. | ✓ | ✓ | [Library](langgraph_example/langgraph_agent.ipynb)                                                      |
| **CrewAI** | Lean Python framework built from scratch for creating autonomous AI agents with role-based architecture. Features high-level simplicity with low-level control, supporting 100,000+ certified developers and claiming 5.76x faster execution in certain cases. | ✓ | ✓ | [Library](crewai_example/crewai_litellm_lib.ipynb),  [Proxy](crewai_example/crewai_litellm_proxy.ipynb) |
| **PydanticAI** | Type-safe agent framework by the Pydantic team with sophisticated dependency injection, durable execution for long-running workflows, and automatic self-correction where validation errors enable real-time learning from mistakes. Supports MCP and A2A protocols. | - | ✓ | [Proxy](pydantic_ai_example/pydantic_ai_litellm_proxy.ipynb)                                            |
| **Google ADK** | Flexible, model-agnostic framework powering agents in Google products like Agentspace. Supports Python, Go, and Java with workflow agents for predictable pipelines, pre-built tools, and MCP tools integration optimized for Gemini and the Google ecosystem. | ✓ | ✓ | [Library](google_adk_example/google_adk.ipynb)                                                          |
| **OpenAI Agents SDK** | Lightweight, production-ready Python framework with minimal abstractions, featuring four core primitives: agents, handoffs, guardrails, and sessions. Provider-agnostic supporting 100+ LLMs with automatic Pydantic-powered schema generation and built-in tracing. | ✓ | ✓ | [Library](openai_adk_example/openai_adk.ipynb)                                                          |
| **AWS Strands** | Model-driven SDK taking advantage of state-of-the-art models' capabilities to plan and execute. Used in production by AWS teams including Amazon Q Developer and AWS Glue, with support for thousands of MCP servers and multi-agent primitives including A2A protocol. | ✓ | ✓ | [Library](aws_strands_example/aws_strands.ipynb)                                                        |
| **LlamaIndex** | Data orchestration framework with enterprise-grade document parsing supporting 90+ file types. Features event-driven Workflows for multi-step agentic systems and 300+ integration packages working seamlessly with various LLM, embedding, and vector store providers. | ✓ | ✓ | [Library](LlamaIndex_example/LlamaIndex_litellm.ipynb)                                                  |
| **smolagents** | Minimalist framework by Hugging Face with ~1,000 lines of core code, specializing in code agents that write and execute Python snippets. Features sandboxed execution environments and achieves ~30% reduction in LLM calls compared to standard tool-calling methods. | ✓ | ✓ | [Library](smolagents_example/smolagents_litellm.ipynb)                                                  |
| **Microsoft Agent Framework** | Comprehensive .NET and Python framework combining AutoGen's abstractions with Semantic Kernel's enterprise features. Introduces graph-based architecture with workflows for explicit control, checkpointing for long-running processes, and comprehensive monitoring integration. | - | ✓ | [Proxy](microsoft_agent_example/microsoft_agent_litellm_proxy.ipynb)                                    |
| **AgentScope** | Agent-oriented framework with native asynchronous execution support for realtime interruption and customized handling. Prioritizes transparency with no deep encapsulation, making all operations visible and controllable. Includes AgentScope Studio for visual multi-agent system management. | ✓ | ✓ | [Library](agentscope_example/agentscope_litellm.ipynb)                                                  |
| **AG2** | Open-source framework (formerly AutoGen) with open governance under AG2AI organization. Features core agents like ConversableAgent for seamless communication, supports multi-agent conversation patterns, and introduces FSM/Stateflow for structured state management. | - | ✓ | [Proxy](ag2_example/ag2_litellm_proxy.ipynb)                                                            |

### Integration Types

- **Library Integration**: Uses LiteLLM as a Python library directly in your code. The framework calls LiteLLM functions, which handle the communication with SAP Generative AI Hub.

- **Proxy Integration**: Runs LiteLLM as a standalone server that mimics the OpenAI API. Your framework connects to this local proxy server, which forwards requests to SAP Generative AI Hub. This approach enables multi-language support.

## Getting Started

### Prerequisites

- [SAP AI Core with Generative AI Hub subscription](https://help.sap.com/docs/sap-ai-core/sap-ai-core-service-guide/enabling-service-in-cloud-foundry) via SAP BTP tenant
- Python 3.8 or higher
- LiteLLM library (latest version includes SAP provider support)

> **Note:** While Python 3.8+ is supported, Python 3.12 or higher is recommended for optimal performance and compatibility.

### Installation

```bash
pip install litellm
```

For proxy-based integration:
```bash
pip install "litellm[proxy]"
```

### Basic Workflow

1. **Set up credentials**: Obtain your SAP AI Core service key from your BTP tenant
2. **Choose integration method**: Decide between library or proxy approach based on your needs
3. **Configure connection**: Set up LiteLLM with your SAP credentials
4. **Select a framework**: Choose from the examples below
5. **Build your agent**: Follow the notebook examples to create your AI agent

## Running LiteLLM as a Proxy

The proxy approach runs LiteLLM as a standalone server, making it accessible to any application that can make HTTP requests. This is particularly useful for multi-language support (e.g., JavaScript, Go) and microservices architectures.

The proxy mimics the OpenAI API, allowing any OpenAI-compatible client to connect to SAP Generative AI Hub by pointing it to the local proxy URL.

**For detailed instructions on configuring and running the proxy, including Docker setup, please see the [LiteLLM Proxy Setup Guide](PROXY_SETUP.md).**


## Multi-Language Support

Because LiteLLM can run as a proxy server with an OpenAI-compatible API, you're not limited to Python. Any language that can make HTTP requests can use SAP Generative AI Hub through the LiteLLM proxy.

### JavaScript/TypeScript Example

Here's how to use LangChain.js with the LiteLLM proxy:

```typescript
import { ChatOpenAI } from "@langchain/openai";

const model = new ChatOpenAI({
  modelName: "sap/gpt-4",
  openAIApiKey: "sk-1234", // Your proxy master key
  configuration: {
    baseURL: "http://localhost:4000", // LiteLLM proxy URL
  },
});

const response = await model.invoke("Hello, how are you?");
console.log(response.content);
```

Learn more with our [JavaScript/TypeScript examples](JAVASCRIPT_EXAMPLES.md).


## Contributing

We welcome contributions! If you'd like to add an example for a framework not listed here:

1. Fork the repository
2. Create a new directory following the naming pattern: `framework_name_example/`
3. Include both a Jupyter notebook and Python script
4. Add clear documentation explaining the integration
5. Update this README with your framework in the comparison table
6. Submit a pull request

## Additional Resources

- [Online Documentation](https://sap-contributions.github.io/litellm-agentic-examples/)
- [Devtoberfest Talk: LiteLLM & SAP GenAI Hub](https://www.youtube.com/watch?v=osVV9lqm3ms)
- [LiteLLM Documentation](https://docs.litellm.ai/)
- [SAP AI Core Documentation](https://help.sap.com/docs/sap-ai-core)
- [SAP Generative AI Hub Documentation](https://help.sap.com/docs/sap-ai-core/generative-ai)

## Note for Maintainers

### Cleanup Notebooks Before Commit

Clear cell outputs and metadata using the `.pre-commit-config.yaml`.

Installation:
```bash
python3 -m venv env
source env/bin/activate
python3 -m pip install pre-commit nbstripout
```

Manual run:
```bash
pre-commit run --all-files
```

Skip hooks temporarily:
```bash
git commit -m "Message" --no-verify
```

### Update Documentation via Sphinx

The documentation is automatically built and deployed via GitHub Actions on each push to the main branch. To build the documentation locally, follow the instructions in our [Documentation Setup Guide](./DOCUMENTATION_SETUP.md).
