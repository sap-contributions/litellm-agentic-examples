# Agentic Examples for SAP Generative AI Hub

[![Documentation](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://sap-contributions.github.io/litellm-agentic-examples/)

[//]: # ([![License]&#40;https://img.shields.io/github/license/sap-contributions/litellm-agentic-examples&#41;]&#40;LICENSE&#41;)

The examples showcase how to easily use different agentic frameworks with the "SAP provider" via LiteLLM.

SAP customers can access LLMs across all vendors (OpenAI, Google, Amazon, Mistral, SAP, ...) available in the SAP Generative AI Hub.

📚 **[View Online documentation](https://sap-contributions.github.io/litellm-agentic-examples/)** 📚

🎥 **[Watch Video Tutorial](https://www.youtube.com/watch?v=osVV9lqm3ms)** 🎥

## Sap Generative AI Hub
The [SAP Generative AI Hub](https://help.sap.com/docs/sap-ai-core/sap-ai-core-service-guide/large-language-models)
enables customers to access large language models (LLMs) from various providers e.g., Gemini, ChatGPT, Claude, Mistral, ...,
in a centralized manner.

## LiteLMM
[LiteLLM](https://www.litellm.ai) is an opensource library which supports 100+ LLMs from various providers.
LiteLLM acts as the bridge to use standard open-source frameworks via the OpenAI api. LiteLLM integrates with various
LLM providers. The "SAP provider" is recently added to LiteLLM to support the SAP Generative AI Hub.

![LiteLLM_SAPGenAIHub.png](docs/source/_static/LiteLLM_SAPGenAIHub.png)

## Prerequisites
- [SAP AI Core Gen AI subscription via SAP BTP tenant.](https://help.sap.com/docs/sap-ai-core/sap-ai-core-service-guide/enabling-service-in-cloud-foundry)
- Install latest Litellm (includes SAP provider).

## Examples Overview
The following examples include python code and jupyter notebooks to demonstrate the integration step by step.

### 1. Langgraph
* [langgraph_agent notebook](langgraph_example/langgraph_agent.ipynb)

### 2. CrewAI
* [crewai_litellm_lib notebook](crewai_example/crewai_litellm_lib.ipynb)
* [crewai_litellm_proxy notebook](crewai_example/crewai_litellm_proxy.ipynb)

### 3. PydanticAI
* [pydanticai_litellm_proxy notebook](pydantic_ai_example/pydantic_ai_litellm_proxy.ipynb)

### 4. Google ADK
* [google_adk notebook](google_adk_example/google_adk.ipynb)

### 5. OpenAI ADK
* [openai_adk notebook](openai_adk_example/openai_adk.ipynb)

### 6. AWS
* [aws_strands notebook](aws_strands_example/aws_strands.ipynb)

### 7. LlamaIndex
* [Llamaindex_litellm notebook](Llamaindex_example/Llamaindex_litellm.ipynb)

### 8. smolagents
* [smolagents_litellm notebook](smolagents_example/smolagents_litellm.ipynb)

### 9. Microsoft Agent Framework
* [microsoft_agent_litellm_proxy notebook](microsoft_agent_example/microsoft_agent_litellm_proxy.ipynb)

### 10. Agentscope
* [agentscope_litellm notebook](agentscope_example/agentscope_litellm.ipynb)

### 11. AG2
* [ag2_litellm notebook](ag2_example/ag2_litellm_proxy.ipynb)


## Note for Maintainers of these examples

### Cleanup Notebooks before Commit
Clear cell outputs and metadata using the ".pre-commit-config.yaml".
Installation procedure:
```bash
python3 -m venv env
source env/bin/activate
python3 -m pip install pre-commit nbstripout
```
Manual run:
```bash
pre-commit run --all-files
```
Skip Hooks temporarily:
```bash
git commit -m "Message" --no-verify
```

### Update Documentation via Sphinx
The documentation is automatically built and deployed via GitHub Actions on each push to the main branch.
To build the documentation locally, follow the instructions in [DOCUMENTATION_SETUP.md](./DOCUMENTATION_SETUP.md).
