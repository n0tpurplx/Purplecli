#!/usr/bin/env python3

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

VERSION = "0.1.5"

CONFIG_DIR = Path.home() / ".purplecli"
CONFIG_FILE = CONFIG_DIR / "config.json"

SYSTEM_PROMPT = """You are PurpleCli, a coding agent running in a user's terminal.

Your job is to help the user modify and work with their software project.

You have access to these tools:
- list_files
- read_file
- write_file
- delete_file
- run_command

Rules:
- Inspect files before modifying them when appropriate.
- Make precise changes.
- Never pretend a tool was executed if it was not.
- Explain important changes briefly.
- When you need to modify files, use the provided tools.
- Work inside the user's current working directory.
"""

# Plan mode state
plan_mode = False


def load_config():
    if not CONFIG_FILE.exists():
        return {}

    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}


def save_config(config):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)

    try:
        os.chmod(CONFIG_FILE, 0o600)
    except OSError:
        pass


def setup():
    print()
    print("PurpleCli Setup")
    print("---------------")
    print()
    print("Choose your AI provider:")
    print("1. OpenRouter")
    print("2. Google Gemini")
    print()

    while True:
        choice = input("Provider [1/2]: ").strip()

        if choice == "1":
            provider = "openrouter"
            break

        if choice == "2":
            provider = "gemini"
            break

        print("Please choose 1 or 2.")

    print()

    if provider == "openrouter":
        key = input("OpenRouter API key: ").strip()
    else:
        key = input("Google Gemini API key: ").strip()

    if not key:
        print("No API key entered.")
        return

    config = {
        "provider": provider,
        "api_key": key
    }

    save_config(config)

    print()
    print("✓ Provider saved.")
    print("✓ API key saved.")
    print()
    print("Setup complete.")
    print()


def list_files():
    try:
        entries = []

        for path in Path(".").iterdir():
            if path.name == ".git":
                continue

            entries.append(
                f"{'[DIR] ' if path.is_dir() else '[FILE]'} {path}"
            )

        return "\n".join(sorted(entries)) or "(empty directory)"

    except Exception as e:
        return f"Error: {e}"


def read_file(path):
    try:
        return Path(path).read_text(encoding="utf-8")
    except Exception as e:
        return f"Error reading {path}: {e}"


def write_file(path, content):
    try:
        file = Path(path)
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(content, encoding="utf-8")
        return f"Successfully wrote {path}"
    except Exception as e:
        return f"Error writing {path}: {e}"


def delete_file(path):
    try:
        file = Path(path)

        if not file.exists():
            return f"{path} does not exist."

        if file.is_dir():
            return "Refusing to delete directories."

        file.unlink()
        return f"Successfully deleted {path}"

    except Exception as e:
        return f"Error deleting {path}: {e}"


def run_command(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )

        output = ""

        if result.stdout:
            output += result.stdout

        if result.stderr:
            output += "\nSTDERR:\n" + result.stderr

        output += f"\nExit code: {result.returncode}"

        return output.strip()

    except Exception as e:
        return f"Error running command: {e}"


TOOLS = {
    "list_files": list_files,
    "read_file": read_file,
    "write_file": write_file,
    "delete_file": delete_file,
    "run_command": run_command,
}


def tool_definitions():
    return [
        {
            "type": "function",
            "function": {
                "name": "list_files",
                "description": "List files and directories in the current working directory.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "read_file",
                "description": "Read a UTF-8 text file.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string"
                        }
                    },
                    "required": ["path"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "write_file",
                "description": "Create or completely replace a UTF-8 text file.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string"
                        },
                        "content": {
                            "type": "string"
                        }
                    },
                    "required": ["path", "content"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "delete_file",
                "description": "Delete a single file.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string"
                        }
                    },
                    "required": ["path"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "run_command",
                "description": "Run a shell command in the current working directory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "command": {
                            "type": "string"
                        }
                    },
                    "required": ["command"]
                }
            }
        }
    ]


def openrouter_request(messages, config):
    import requests

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openrouter/free",
            "messages": messages,
            "tools": tool_definitions(),
            "tool_choice": "auto"
        },
        timeout=120
    )

    response.raise_for_status()
    return response.json()


def gemini_request(messages, config):
    import requests

    # Gemini's OpenAI-compatible endpoint lets us use the
    # same agent/tool architecture as OpenRouter.
    response = requests.post(
        "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
        headers={
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gemini-2.5-flash",
            "messages": messages,
            "tools": tool_definitions(),
            "tool_choice": "auto"
        },
        timeout=120
    )

    response.raise_for_status()
    return response.json()


def ask_ai(messages, config):
    if config["provider"] == "openrouter":
        return openrouter_request(messages, config)

    if config["provider"] == "gemini":
        return gemini_request(messages, config)

    raise RuntimeError("Unknown provider.")


def execute_tool(name, arguments):
    if name not in TOOLS:
        return f"Unknown tool: {name}"

    try:
        return TOOLS[name](**arguments)
    except Exception as e:
        return f"Tool error: {e}"


def agent(user_message, config):
    global plan_mode
    
    # Build system prompt with optional plan mode instruction
    system_content = SYSTEM_PROMPT
    if plan_mode:
        system_content += "\n\nPLAN MODE: Before taking any actions, you must first create a detailed plan. Output the plan clearly, then proceed step by step."
    
    messages = [
        {
            "role": "system",
            "content": system_content
        },
        {
            "role": "user",
            "content": user_message
        }
    ]

    while True:
        try:
            response = ask_ai(messages, config)
        except Exception as e:
            print(f"\nAPI error: {e}")
            return

        choice = response["choices"][0]
        message = choice["message"]

        tool_calls = message.get("tool_calls")

        messages.append(message)

        if not tool_calls:
            content = message.get("content", "")
            print()
            if plan_mode:
                print(f"[Plan] PurpleCli: {content}")
            else:
                print(f"PurpleCli: {content}")
            print()
            return

        for tool_call in tool_calls:
            function = tool_call["function"]
            name = function["name"]

            try:
                arguments = json.loads(function["arguments"])
            except json.JSONDecodeError:
                arguments = {}

            print(f"→ {name}({', '.join(arguments.keys())})")

            result = execute_tool(name, arguments)

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call["id"],
                    "content": result
                }
            )


def main():
    global plan_mode
    
    parser = argparse.ArgumentParser(
        prog="PurpleCli",
        description="PurpleCli - a lightweight AI coding agent."
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"PurpleCli {VERSION}"
    )

    parser.add_argument(
        "-S",
        "--setup",
        action="store_true",
        help="Configure your AI provider and API key."
    )
    
    parser.add_argument(
        "--plan",
        action="store_true",
        help="Start with plan mode enabled."
    )

    args = parser.parse_args()

    if args.setup:
        setup()
        return

    config = load_config()

    if not config.get("provider") or not config.get("api_key"):
        print("PurpleCli has not been configured yet.")
        print()
        print("Run:")
        print("  PurpleCli --setup")
        print()
        return

    # Set plan mode from CLI flag
    if args.plan:
        plan_mode = True

    print(f"PurpleCli {VERSION}")
    if plan_mode:
        print("Plan mode: ON")
    print(f"Provider: {config['provider']}")
    print("Type /help for commands. Type /exit to quit.")
    print()

    while True:
        try:
            prompt = "[PLAN] > " if plan_mode else "> "
            user_input = input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            print()
            break

        if not user_input:
            continue

        if user_input in ("/exit", "/quit"):
            break

        if user_input == "/help":
            print()
            print("/help   Show this help")
            print("/exit   Exit PurpleCli")
            print("/plan   Toggle plan mode")
            print()
            continue

        if user_input == "/plan":
            plan_mode = not plan_mode
            if plan_mode:
                print()
                print("Plan mode activated. Run /plan again to end plan mode.")
                print()
            else:
                print()
                print("Plan mode deactivated.")
                print()
            continue

        agent(user_input, config)


if __name__ == "__main__":
    main()
