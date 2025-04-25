import httpx
from mcp.server.fastmcp import FastMCP
from utils.config import get_env_variable

API_KEY = get_env_variable("WEBHOOK_TESTER_API_KEY")
BASE_URL = get_env_variable("WEBHOOK_TESTER_BASE_URL")
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

mcp = FastMCP(
    "Webhook Tester MCP",
    base_url="http://localhost:8000"
    )

@mcp.resource("get_webhook_payloads/{webhook_id}")
def get_webhook_payloads(webhook_id: str) -> dict:
    url = f"{BASE_URL}/webhooks/{webhook_id}"
    response = httpx.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json().get("payloads", [])

@mcp.tool("create_new_webhook")
def create_new_webhook(title: str, response_code: str = "200", content_type: str = "application/json", payload: str = "{}", response_delay: int = 0) -> dict:
    url = f"{BASE_URL}/webhooks"
    data = {
        "title": title,
        "response_code": response_code,
        "content_type": content_type,
        "payload": payload,
        "response_delay": response_delay
    }
    response = httpx.post(url, headers=HEADERS, json=data)
    response.raise_for_status()
    return response.json()

@mcp.tool("list_all_webhooks")
def list_all_webhooks() -> dict:
    url = f"{BASE_URL}/webhooks"
    response = httpx.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

@mcp.tool("get_webhook_details")
def get_webhook_details(webhook_id: str) -> dict:
    url = f"{BASE_URL}/webhooks/{webhook_id}"
    response = httpx.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

@mcp.tool("delete_webhook")
def delete_webhook(webhook_id: str) -> dict:
    url = f"{BASE_URL}/webhooks/{webhook_id}"
    response = httpx.delete(url, headers=HEADERS)
    response.raise_for_status()
    return {"status": "deleted", "webhook_id": webhook_id}


if __name__ == "__main__":
    mcp.run()