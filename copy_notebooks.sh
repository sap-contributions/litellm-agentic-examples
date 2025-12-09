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
cp proxy_set_up.ipynb docs/source/_notebooks/

echo "Notebooks copied successfully!"
