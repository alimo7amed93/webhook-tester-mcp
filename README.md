# 🚀 Webhook Tester MCP Server

A powerful and modular FastMCP server for interacting with webhook-test.com, designed to automate and manage Webhook tokens (URLs), inspect incoming requests, and perform analytics — all without writing custom API integrations.

Built with the FastMCP framework to expose modular tools and resources, this project enables webhook observability, automated testing via Claude.

## 📦 Features & Use Cases

- Create and manage webhooks
- Fetch webhook payloads
- Delete webhooks
- Testable via Claude structured prompts

## ⚙️ Setup

1. Clone the repo
2. Install dependencies `pip install -r requirements.txt`
3. Configure `.env`

## 🧪 Testing Using Claude

- Configure Claude Desktop to use the local server by editing your claude_desktop_config.json file:

``` 
{
    "mcpServers": {
      "webhook-tester-mcp": {
        "command": "fastmcp",
        "args": ["run", "{{fullPath}}\\Webhook-test_mcp\\server.py"]
      }
    }
  } 
```

## 📄 License
This project is licensed under the [MIT License](https://mit-license.org/).