# Agentic Examples for SAP Generative AI Hub
The examples below showcase how to use different agentic frameworks with the SAP provider via LiteLMM.
Users can access LLMs across all vendors (OpenAI, Google, Amazon, Mistral, SAP, ...) available in the Generative AI Hub.
Each framework example is described in a separate jupyter notebook.

📚 **[View Online documentation](https://sap-contribution.github.io/litellm-agentic-examples/)** 📚

## Prerequisites
- [AI Core Gen AI subscription via BTP tenant.](https://help.sap.com/docs/sap-ai-core/sap-ai-core-service-guide/enabling-service-in-cloud-foundry)
- Install latest Litellm (including SAP provider).

## 1. Langgraph
* [langgraph_agent notebook](langgraph_example/langgraph_agent.ipynb)

## 2. CrewAI
* [crewai_litellm_lib notebook](crewai_example/crewai_litellm_lib.ipynb)
* [crewai_litellm_proxy notebook](crewai_example/crewai_litellm_proxy.ipynb)

## 3. PydanticAI
* [pydanticai_litellm notebook](pydanticai_example/pydanticai_litellm.ipynb)

## 4. Google ADK
* [google_adk notebook](google_adk_example/google_adk.ipynb)

## 5. OpenAI ADK
* [openai_adk.py](openai_adk_example/openai_adk.ipynb)

## 6. AWS
* [aws_strands notebook](aws_strands_example/aws_strand.ipynb)

## 7. LlamaIndex
* [Llamaindex_litellm notebook](Llamaindex_example/Llamaindex_litellm.ipynb)

## 8. smolagents
* [smolagents_litellm notebook](smolagents_example/smolagents_litellm.ipynb)

## 9. MSFT Agent Framework
* [msft_agent_litellm notebook](msft_agent_example/msft_agent_litellm.ipynb)

## 10. Agentscope
* [agentscope_litellm notebook](agentscope_example/agentscope_litellm.ipynb)

## 11. AG2
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
