.. Agentic examples LiteLLM Gen AI Hub documentation master file, created by
   sphinx-quickstart on Tue Dec  9 09:07:52 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Agentic examples for LiteLLM and SAP Gen AI Hub's documentation!
===========================================================================

The examples showcase how to easily leverage various Agent Development Kits (ADKs) via the "SAP provider" in LiteLMM.

SAP customers can access LLMs across all vendors (OpenAI, Google, Amazon, Mistral, SAP, etc.) available in the SAP Generative AI Hub.

The Sap Generative AI Hub
-------------------------
The `SAP Generative AI Hub <https://help.sap.com/docs/sap-ai-core/sap-ai-core-service-guide/large-language-models>`_
enables customers to access large language models (LLMs) from various providers e.g., Gemini, ChatGPT, Claude, Mistral
in a centralized manner.

LiteLMM
----------------
`LiteLLM <https://www.litellm.ai>`_ is an open-source library which supports 100+ LLMs from various providers.
LiteLLM acts as the bridge to use standard open-source frameworks via the OpenAI api. LiteLLM integrates with various
LLM providers. The "SAP provider" is recently added to LiteLLM to support the SAP Generative AI Hub.

.. image:: _static/LiteLLM_SAPGenAIHub.png
   :alt: LiteLLM SAP Gen AI Hub Architecture
   :width: 600px
   :align: center

**Watch the** 🎥 `Devtoberfest Talk <https://www.youtube.com/watch?v=osVV9lqm3ms>`_ 🎥 on LiteLLM & SAP Generative AI Hub.


Prerequisites
-------------
SAP AI Core Gen AI subscription via SAP BTP tenant:

https://help.sap.com/docs/sap-ai-core/sap-ai-core-service-guide/enabling-service-in-cloud-foundry

.. toctree::
   :maxdepth: 1
   :caption: Agent Framework Examples:

   _notebooks/examples/langgraph_agent.ipynb
   _notebooks/examples/crewai_litellm_lib.ipynb
   _notebooks/examples/crewai_litellm_proxy.ipynb
   _notebooks/examples/pydantic_ai_litellm_proxy.ipynb
   _notebooks/examples/google_adk.ipynb
   _notebooks/examples/openai_adk.ipynb
   _notebooks/examples/aws_strands.ipynb
   _notebooks/examples/LlamaIndex_litellm.ipynb
   _notebooks/examples/smolagents_litellm.ipynb
   _notebooks/examples/microsoft_agent_litellm_proxy.ipynb
   _notebooks/examples/agentscope_litellm.ipynb
   _notebooks/examples/ag2_litellm_proxy.ipynb
   _notebooks/proxy_set_up.ipynb

Indices and tables
==================

* :ref:`search`
