# JavaScript/TypeScript Examples

This guide demonstrates how to use SAP Generative AI Hub with JavaScript and TypeScript applications through the LiteLLM proxy. Since the proxy provides an OpenAI-compatible API, any JavaScript library that supports OpenAI can work with SAP GenAI Hub.

## Prerequisites

- LiteLLM proxy running and configured (see [PROXY_SETUP.md](PROXY_SETUP.md))
- Node.js 16 or higher
- npm or yarn package manager

## Setup

### 1. Start the LiteLLM Proxy

Ensure your LiteLLM proxy is running:

```bash
litellm --config ./config.yaml
```

The proxy should be accessible at `http://localhost:4000`.

### 2. Install Dependencies

Choose your preferred framework and install the necessary packages.

## Using OpenAI SDK

The official OpenAI SDK works directly with the LiteLLM proxy.

### Installation

```bash
npm install openai
```

### JavaScript Example

```javascript
const OpenAI = require('openai');

const client = new OpenAI({
  apiKey: 'sk-1234', // Your proxy master key
  baseURL: 'http://localhost:4000'
});

async function main() {
  const completion = await client.chat.completions.create({
    model: 'sap/gpt-4',
    messages: [
      { role: 'user', content: 'Explain quantum computing in simple terms.' }
    ]
  });

  console.log(completion.choices[0].message.content);
}

main();
```

### TypeScript Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'sk-1234', // Your proxy master key
  baseURL: 'http://localhost:4000'
});

async function main(): Promise<void> {
  const completion = await client.chat.completions.create({
    model: 'sap/gpt-4',
    messages: [
      { role: 'user', content: 'Explain quantum computing in simple terms.' }
    ]
  });

  console.log(completion.choices[0].message.content);
}

main();
```

## Using LangChain.js

LangChain.js is a popular framework for building LLM applications in JavaScript/TypeScript.

### Installation

```bash
npm install @langchain/openai @langchain/core
```

### Basic Chat Example

```typescript
import { ChatOpenAI } from "@langchain/openai";

const model = new ChatOpenAI({
  modelName: "sap/gpt-4",
  openAIApiKey: "sk-1234", // Your proxy master key
  configuration: {
    baseURL: "http://localhost:4000",
  },
});

const response = await model.invoke("What is the capital of France?");
console.log(response.content);
```

### Streaming Example

```typescript
import { ChatOpenAI } from "@langchain/openai";

const model = new ChatOpenAI({
  modelName: "sap/gpt-4",
  openAIApiKey: "sk-1234",
  configuration: {
    baseURL: "http://localhost:4000",
  },
  streaming: true,
});

const stream = await model.stream("Write a short poem about AI.");

for await (const chunk of stream) {
  process.stdout.write(chunk.content);
}
```

### Agent with Tools Example

```typescript
import { ChatOpenAI } from "@langchain/openai";
import { AgentExecutor, createOpenAIFunctionsAgent } from "langchain/agents";
import { pull } from "langchain/hub";
import { Calculator } from "@langchain/community/tools/calculator";

const model = new ChatOpenAI({
  modelName: "sap/gpt-4",
  openAIApiKey: "sk-1234",
  configuration: {
    baseURL: "http://localhost:4000",
  },
});

const tools = [new Calculator()];
const prompt = await pull("hwchase17/openai-functions-agent");

const agent = await createOpenAIFunctionsAgent({
  llm: model,
  tools,
  prompt,
});

const agentExecutor = new AgentExecutor({
  agent,
  tools,
});

const result = await agentExecutor.invoke({
  input: "What is 25 * 4 + 10?",
});

console.log(result.output);
```

### RAG (Retrieval-Augmented Generation) Example

```typescript
import { ChatOpenAI } from "@langchain/openai";
import { OpenAIEmbeddings } from "@langchain/openai";
import { MemoryVectorStore } from "langchain/vectorstores/memory";
import { Document } from "@langchain/core/documents";
import { createStuffDocumentsChain } from "langchain/chains/combine_documents";
import { ChatPromptTemplate } from "@langchain/core/prompts";

// Initialize model
const model = new ChatOpenAI({
  modelName: "sap/gpt-4",
  openAIApiKey: "sk-1234",
  configuration: {
    baseURL: "http://localhost:4000",
  },
});

// Initialize embeddings (using OpenAI embeddings through proxy)
const embeddings = new OpenAIEmbeddings({
  openAIApiKey: "sk-1234",
  configuration: {
    baseURL: "http://localhost:4000",
  },
});

// Create documents
const docs = [
  new Document({ pageContent: "LangChain is a framework for building LLM applications." }),
  new Document({ pageContent: "SAP Generative AI Hub provides enterprise LLM access." }),
  new Document({ pageContent: "LiteLLM acts as a bridge between frameworks and providers." }),
];

// Create vector store
const vectorStore = await MemoryVectorStore.fromDocuments(docs, embeddings);

// Create retrieval chain
const prompt = ChatPromptTemplate.fromTemplate(`
Answer the question based on the following context:

Context: {context}

Question: {question}
`);

const chain = await createStuffDocumentsChain({
  llm: model,
  prompt,
});

// Retrieve and answer
const relevantDocs = await vectorStore.similaritySearch("What is LiteLLM?");
const response = await chain.invoke({
  context: relevantDocs,
  question: "What is LiteLLM?",
});

console.log(response);
```

## Using Vercel AI SDK

The Vercel AI SDK provides a streamlined interface for building AI applications.

### Installation

```bash
npm install ai
```

### Example

```typescript
import { openai } from '@ai-sdk/openai';
import { generateText } from 'ai';

const result = await generateText({
  model: openai('sap/gpt-4', {
    baseURL: 'http://localhost:4000',
    apiKey: 'sk-1234',
  }),
  prompt: 'Explain the concept of machine learning.',
});

console.log(result.text);
```

## Using Anthropic SDK (for Claude models)

If you're using Claude models through SAP GenAI Hub, you can use the Anthropic SDK.

### Installation

```bash
npm install @anthropic-ai/sdk
```

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: 'sk-1234', // Your proxy master key
  baseURL: 'http://localhost:4000',
});

const message = await client.messages.create({
  model: 'sap/claude-3-sonnet',
  max_tokens: 1024,
  messages: [
    { role: 'user', content: 'Hello, Claude!' }
  ],
});

console.log(message.content);
```

## Environment Variables

For production applications, use environment variables for configuration:

```typescript
import { ChatOpenAI } from "@langchain/openai";

const model = new ChatOpenAI({
  modelName: process.env.MODEL_NAME || "sap/gpt-4",
  openAIApiKey: process.env.LITELLM_API_KEY,
  configuration: {
    baseURL: process.env.LITELLM_BASE_URL || "http://localhost:4000",
  },
});
```

Create a `.env` file:

```env
LITELLM_API_KEY=sk-1234
LITELLM_BASE_URL=http://localhost:4000
MODEL_NAME=sap/gpt-4
```

## Error Handling

Implement proper error handling for production applications:

```typescript
import { ChatOpenAI } from "@langchain/openai";

const model = new ChatOpenAI({
  modelName: "sap/gpt-4",
  openAIApiKey: "sk-1234",
  configuration: {
    baseURL: "http://localhost:4000",
  },
});

async function chat(message: string): Promise<string> {
  try {
    const response = await model.invoke(message);
    return response.content as string;
  } catch (error) {
    if (error instanceof Error) {
      console.error('Error calling LLM:', error.message);
      
      // Handle specific error types
      if (error.message.includes('401')) {
        throw new Error('Authentication failed. Check your API key.');
      } else if (error.message.includes('404')) {
        throw new Error('Model not found. Check your model name.');
      } else if (error.message.includes('timeout')) {
        throw new Error('Request timed out. Try again later.');
      }
    }
    throw error;
  }
}
```

## Next.js Integration

Example of using SAP GenAI Hub in a Next.js API route:

```typescript
// app/api/chat/route.ts
import { ChatOpenAI } from "@langchain/openai";
import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  try {
    const { message } = await req.json();

    const model = new ChatOpenAI({
      modelName: "sap/gpt-4",
      openAIApiKey: process.env.LITELLM_API_KEY,
      configuration: {
        baseURL: process.env.LITELLM_BASE_URL,
      },
    });

    const response = await model.invoke(message);

    return NextResponse.json({ 
      response: response.content 
    });
  } catch (error) {
    console.error('Error:', error);
    return NextResponse.json(
      { error: 'Failed to process request' },
      { status: 500 }
    );
  }
}
```

## Express.js Integration

Example of using SAP GenAI Hub in an Express.js application:

```typescript
import express from 'express';
import { ChatOpenAI } from "@langchain/openai";

const app = express();
app.use(express.json());

const model = new ChatOpenAI({
  modelName: "sap/gpt-4",
  openAIApiKey: process.env.LITELLM_API_KEY,
  configuration: {
    baseURL: process.env.LITELLM_BASE_URL,
  },
});

app.post('/api/chat', async (req, res) => {
  try {
    const { message } = req.body;
    const response = await model.invoke(message);
    res.json({ response: response.content });
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ error: 'Failed to process request' });
  }
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

## Best Practices

1. **Use Environment Variables**: Never hardcode API keys or URLs
2. **Implement Retry Logic**: Handle transient failures gracefully
3. **Add Timeouts**: Set appropriate timeout values for your use case
4. **Monitor Usage**: Track API calls and costs
5. **Cache Responses**: Cache frequent queries to reduce API calls
6. **Handle Errors**: Provide meaningful error messages to users
7. **Rate Limiting**: Implement rate limiting to prevent abuse

## Additional Resources

- [LangChain.js Documentation](https://js.langchain.com/)
- [OpenAI Node.js SDK](https://github.com/openai/openai-node)
- [Vercel AI SDK](https://sdk.vercel.ai/)
- [LiteLLM Proxy Documentation](https://docs.litellm.ai/docs/simple_proxy)

## Support

For JavaScript/TypeScript specific issues:
- Check the framework's documentation
- Ensure the LiteLLM proxy is running and accessible
- Verify your configuration matches the examples above
