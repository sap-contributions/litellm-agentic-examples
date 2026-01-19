# LiteLLM Proxy Setup Guide

This guide provides detailed instructions for running LiteLLM as a proxy server to connect SAP Generative AI Hub with any OpenAI-compatible application.

## What is the LiteLLM Proxy?

The LiteLLM proxy is a standalone server that provides an OpenAI-compatible API endpoint. It acts as a translation layer between applications expecting the OpenAI API format and SAP Generative AI Hub. This approach offers several advantages:

- **Multi-language support**: Use any programming language that can make HTTP requests
- **Centralized configuration**: Manage credentials and settings in one place
- **Easy testing**: Test integrations without modifying application code
- **Microservices friendly**: Deploy as a separate service in your architecture

## Prerequisites

- SAP AI Core with Generative AI Hub subscription
- Python 3.8 or higher
- Service key from your SAP BTP tenant

## Installation

Install LiteLLM with proxy support:

```bash
pip install "litellm[proxy]"
```

## Configuration

### Step 1: Obtain SAP Credentials

Get your service key from SAP BTP:

1. Log in to your SAP BTP cockpit
2. Navigate to your AI Core instance
3. Create or view a service key
4. Note the following values:
   - `clientid` (AICORE_CLIENT_ID)
   - `clientsecret` (AICORE_CLIENT_SECRET)
   - `url` (AICORE_AUTH_URL)
   - `serviceurls.AI_API_URL` (AICORE_BASE_URL)
   - Resource group name (AICORE_RESOURCE_GROUP)

### Step 2: Create Configuration File

Create a `config.yaml` file in your project directory:

```yaml
model_list:
  - model_name: "sap/*"
    litellm_params:
      model: "sap/*"

litellm_settings:
  drop_params: True

general_settings:
  master_key: sk-1234  # Change this to a secure key
  store_model_in_db: False

environment_variables:
  AICORE_AUTH_URL: "https://your-tenant.authentication.sap.hana.ondemand.com/oauth/token"
  AICORE_CLIENT_ID: "your-client-id"
  AICORE_CLIENT_SECRET: "your-client-secret"
  AICORE_RESOURCE_GROUP: "your-resource-group"
  AICORE_BASE_URL: "https://api.ai.your-region.cfapps.sap.hana.ondemand.com/v2"
```

**Important**: Replace the placeholder values with your actual SAP credentials.

### Configuration Parameters Explained

- **model_name**: Pattern for model names. `sap/*` allows any model with the `sap/` prefix
- **drop_params**: Removes unsupported parameters before sending to SAP GenAI Hub
- **master_key**: Authentication key for accessing your proxy (change to a secure value)
- **store_model_in_db**: Whether to persist model configurations in a database

## Running the Proxy

### Basic Usage

Start the proxy server:

```bash
litellm --config ./config.yaml
```

The proxy will start on `http://localhost:4000` by default.

### Custom Port

To run on a different port:

```bash
litellm --config ./config.yaml --port 8080
```

### Production Deployment

For production use, consider:

```bash
litellm --config ./config.yaml --port 4000 --num_workers 4
```

## Docker Deployment

### Using Docker Run

**Create a Dockerfile:**

```dockerfile
FROM python:3.12-slim

# Install LiteLLM with proxy support
RUN pip install --no-cache-dir "litellm[proxy]"

# Set working directory
WORKDIR /app

# Copy configuration file
COPY config.yaml .

# Expose the default LiteLLM proxy port
EXPOSE 4000

# Start the LiteLLM proxy server
CMD ["litellm", "--config", "./config.yaml", "--port", "4000"]
```

**Build and run the container:**

```bash
# Build the Docker image
docker build -t litellm-proxy .

# Run with environment variables from .env file
docker run -d \
  --name litellm-proxy \
  -p 4000:4000 \
  --env-file .env \
  litellm-proxy
```

**Create a `.env` file with your SAP credentials:**

```env
AICORE_AUTH_URL=https://your-tenant.authentication.sap.hana.ondemand.com/oauth/token
AICORE_CLIENT_ID=your-client-id
AICORE_CLIENT_SECRET=your-client-secret
AICORE_RESOURCE_GROUP=your-resource-group
AICORE_BASE_URL=https://api.ai.your-region.cfapps.sap.hana.ondemand.com/v2
```

**Update your `config.yaml` to use environment variables:**

```yaml
model_list:
  - model_name: "sap/*"
    litellm_params:
      model: "sap/*"

litellm_settings:
  drop_params: True

general_settings:
  master_key: sk-1234
  store_model_in_db: False

environment_variables:
  AICORE_AUTH_URL: ${AICORE_AUTH_URL}
  AICORE_CLIENT_ID: ${AICORE_CLIENT_ID}
  AICORE_CLIENT_SECRET: ${AICORE_CLIENT_SECRET}
  AICORE_RESOURCE_GROUP: ${AICORE_RESOURCE_GROUP}
  AICORE_BASE_URL: ${AICORE_BASE_URL}
```

### Using Docker Compose

**Create a `docker-compose.yml` file:**

```yaml
version: '3.8'

services:
  litellm-proxy:
    build: .
    container_name: litellm-proxy
    ports:
      - "4000:4000"
    env_file:
      - .env
    volumes:
      - ./config.yaml:/app/config.yaml:ro
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:4000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

**Start the service:**

```bash
# Start the proxy in detached mode
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the service
docker-compose down
```

**Alternative: Using pre-built image (if available):**

```yaml
version: '3.8'

services:
  litellm-proxy:
    image: python:3.12-slim
    container_name: litellm-proxy
    command: >
      sh -c "pip install --no-cache-dir 'litellm[proxy]' &&
             litellm --config /app/config.yaml --port 4000"
    ports:
      - "4000:4000"
    env_file:
      - .env
    volumes:
      - ./config.yaml:/app/config.yaml:ro
    working_dir: /app
    restart: unless-stopped
```

## Testing the Proxy

### Using curl

Test the proxy with a simple request:

```bash
curl http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "sap/gpt-4",
    "messages": [
      {
        "role": "user",
        "content": "Hello, how are you?"
      }
    ]
  }'
```

### Using Python

```python
import openai

client = openai.OpenAI(
    api_key="sk-1234",  # Your proxy master key
    base_url="http://localhost:4000"
)

response = client.chat.completions.create(
    model="sap/gpt-4",
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

print(response.choices[0].message.content)
```

## Available Models

Most common SAP Generative AI Hub models are supported, including:

- `sap/gpt-5`
- `sap/claude-4.5-sonnet`
- `sap/gemini-pro`

To list available models:

```bash
curl http://localhost:4000/v1/models \
  -H "Authorization: Bearer sk-1234"
```

## Troubleshooting

### Connection Errors

**Problem**: Cannot connect to the proxy

**Solutions**:
- Verify the proxy is running: Check terminal output
- Confirm the port is correct: Default is 4000
- Check firewall settings: Ensure the port is not blocked

### Authentication Errors

**Problem**: 401 Unauthorized responses

**Solutions**:
- Verify your master key matches the config file
- Check SAP credentials are correct in `config.yaml`
- Ensure your SAP AI Core subscription is active

### Model Not Found

**Problem**: Model not available errors

**Solutions**:
- Verify the model name format: Should be `sap/model-name`
- Check your SAP subscription includes the requested model
- List available models using the `/v1/models` endpoint

### Timeout Errors

**Problem**: Requests timing out

**Solutions**:
- Check your network connection to SAP services
- Verify SAP AI Core service is operational
- Increase timeout settings in your client application

## Security Considerations

### Production Deployment

For production use:

1. **Change the master key**: Use a strong, randomly generated key
2. **Use environment variables**: Don't commit credentials to version control
3. **Enable HTTPS**: Use a reverse proxy (nginx, Caddy) for SSL/TLS
4. **Restrict access**: Use firewall rules to limit who can access the proxy
5. **Monitor usage**: Implement logging and monitoring

### Environment Variables

Instead of hardcoding credentials in `config.yaml`, use environment variables:

```yaml
environment_variables:
  AICORE_AUTH_URL: ${AICORE_AUTH_URL}
  AICORE_CLIENT_ID: ${AICORE_CLIENT_ID}
  AICORE_CLIENT_SECRET: ${AICORE_CLIENT_SECRET}
  AICORE_RESOURCE_GROUP: ${AICORE_RESOURCE_GROUP}
  AICORE_BASE_URL: ${AICORE_BASE_URL}
```

Then set them in your shell:

```bash
export AICORE_AUTH_URL="https://..."
export AICORE_CLIENT_ID="..."
export AICORE_CLIENT_SECRET="..."
export AICORE_RESOURCE_GROUP="..."
export AICORE_BASE_URL="https://..."
```

## Advanced Configuration

### Multiple Model Configurations

Configure different models with specific settings:

```yaml
model_list:
  - model_name: "sap-gpt4"
    litellm_params:
      model: "sap/gpt-4"
      max_tokens: 4096

  - model_name: "sap-claude"
    litellm_params:
      model: "sap/claude-3-sonnet"
      max_tokens: 8192
```

### Logging Configuration

Enable detailed logging:

```yaml
litellm_settings:
  set_verbose: True
  json_logs: True
```

## Additional Resources

- [LiteLLM Proxy Documentation](https://docs.litellm.ai/docs/simple_proxy)
- [SAP AI Core Documentation](https://help.sap.com/docs/sap-ai-core)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)

## Support

For issues specific to:
- **LiteLLM**: Open an issue on the [LiteLLM GitHub repository](https://github.com/BerriAI/litellm)
- **SAP Generative AI Hub**: Contact SAP support or consult the [SAP Community](https://community.sap.com/)
