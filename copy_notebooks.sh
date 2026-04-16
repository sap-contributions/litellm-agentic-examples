#!/bin/bash

# Script to copy notebooks to docs/source/_notebooks for Sphinx build

# Create the _notebooks directory if it doesn't exist
mkdir -p docs/source/_notebooks/examples/

# Copy all notebooks to the _notebooks directory, preserving structure
echo "Copying notebooks to docs/source/_notebooks..."

# Copy each example directory
cp -r langgraph_example/*.ipynb docs/source/_notebooks/examples/
cp -r crewai_example/*.ipynb docs/source/_notebooks/examples/
cp -r pydantic_ai_example/*.ipynb docs/source/_notebooks/examples/
cp -r google_adk_example/*.ipynb docs/source/_notebooks/examples/
cp -r openai_adk_example/*.ipynb docs/source/_notebooks/examples/
cp -r aws_strands_example/*.ipynb docs/source/_notebooks/examples/
cp -r LlamaIndex_example/*.ipynb docs/source/_notebooks/examples/
cp -r smolagents_example/*.ipynb docs/source/_notebooks/examples/
cp -r microsoft_agent_example/*.ipynb docs/source/_notebooks/examples/
cp -r agentscope_example/*.ipynb docs/source/_notebooks/examples/
cp -r ag2_example/*.ipynb docs/source/_notebooks/examples/
# Copy PROXY_SETUP.md and fix code block language for Sphinx
sed 's/```env/```bash/g' PROXY_SETUP.md > docs/source/_notebooks/PROXY_SETUP.md

# Copy JAVASCRIPT_EXAMPLES.md and fix code block language for Sphinx
sed 's/```env/```bash/g' JAVASCRIPT_EXAMPLES.md > docs/source/_notebooks/JAVASCRIPT_EXAMPLES.md

# Copy README.md and fix paths for Sphinx:
sed -e 's|!\[LiteLLM_SAPGenAIHub\.png\](docs/source/_static/LiteLLM_SAPGenAIHub\.png)|<img src="_static/LiteLLM_SAPGenAIHub.png" alt="LiteLLM SAP GenAI Hub Architecture" />|g' \
    -e 's|(langgraph_example/|(_notebooks/examples/|g' \
    -e 's|(crewai_example/|(_notebooks/examples/|g' \
    -e 's|(pydantic_ai_example/|(_notebooks/examples/|g' \
    -e 's|(google_adk_example/|(_notebooks/examples/|g' \
    -e 's|(openai_adk_example/|(_notebooks/examples/|g' \
    -e 's|(aws_strands_example/|(_notebooks/examples/|g' \
    -e 's|(LlamaIndex_example/|(_notebooks/examples/|g' \
    -e 's|(smolagents_example/|(_notebooks/examples/|g' \
    -e 's|(microsoft_agent_example/|(_notebooks/examples/|g' \
    -e 's|(agentscope_example/|(_notebooks/examples/|g' \
    -e 's|(ag2_example/|(_notebooks/examples/|g' \
    -e 's|(PROXY_SETUP.md)|(_notebooks/PROXY_SETUP.md)|g' \
    -e 's|(JAVASCRIPT_EXAMPLES.md)|(_notebooks/JAVASCRIPT_EXAMPLES.md)|g' \
    -e 's|(./DOCUMENTATION_SETUP.md)|(https://github.com/sap-contributions/litellm-agentic-examples/blob/main/DOCUMENTATION_SETUP.md)|g' \
    README.md > docs/source/_notebooks/README.md

echo "Notebooks, README, and supporting docs copied successfully!"
