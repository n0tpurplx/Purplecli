# PurpleCli

<p align="center">
  <strong>A lightweight AI coding agent for your terminal.</strong>
</p>

<p align="center">
  <a href="https://github.com/n0tpurplx/Purplecli">
    <img src="https://img.shields.io/github/stars/n0tpurplx/Purplecli?style=for-the-badge&logo=github&label=Stars" alt="GitHub Stars">
  </a>
  <a href="https://github.com/n0tpurplx/Purplecli/issues">
    <img src="https://img.shields.io/github/issues/n0tpurplx/Purplecli?style=for-the-badge&logo=github&label=Issues" alt="GitHub Issues">
  </a>
  <a href="https://github.com/n0tpurplx/Purplecli/blob/main/LICENSE.md">
    <img src="https://img.shields.io/badge/License-PAL%20v1.0-7C3AED?style=for-the-badge" alt="PAL v1.0">
  </a>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Status-Early%20Development-8A2BE2?style=for-the-badge" alt="Status">
</p>

<p align="center">
  <a href="#installation">Installation</a>
  &nbsp;&bull;&nbsp;
  <a href="#usage">Usage</a>
  &nbsp;&bull;&nbsp;
  <a href="#features">Features</a>
  &nbsp;&bull;&nbsp;
  <a href="#configuration">Configuration</a>
  &nbsp;&bull;&nbsp;
  <a href="#roadmap">Roadmap</a>
</p>

---

## Table of Contents

- [About](#about)
- [Features](#features)
- [429 Note](#429-note)
- [Installation](#installation)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [CLI Options](#cli-options)
- [Interactive Commands](#interactive-commands)
- [AI Providers](#ai-providers)
- [Configuration](#configuration)
- [Tools](#tools)
- [Agent Architecture](#agent-architecture)
- [Project Structure](#project-structure)
- [Security](#security)
- [Development](#development)
- [Extending PurpleCli](#extending-purplecli)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Bug Reports](#bug-reports)
- [License](#license)
- [Status](#status)
- [Credits](#credits)

---

## About

PurpleCli is a lightweight AI coding agent designed to run directly inside your terminal.

It connects an AI model to your local project and gives the model a set of tools for working with files and executing commands.

Instead of only generating code, PurpleCli can inspect your project, understand existing files, make changes, run commands, and continue working based on the results.

```text
                         USER
                           |
                           v
                    +-------------+
                    |  PurpleCli  |
                    +-------------+
                           |
                           v
                    +-------------+
                    |  AI Provider |
                    +-------------+
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
        File Tools     Shell Tools   Project Data
             |             |             |
             +-------------+-------------+
                           |
                           v
                     YOUR PROJECT
```

PurpleCli is intentionally small and focuses on providing a simple foundation for an AI-powered terminal coding agent.

---

## Features

### AI Coding Agent

PurpleCli uses an agent loop that allows the AI to interact with your project instead of simply returning generated code.

The model can decide when it needs to inspect files, modify files, remove files, or execute commands.

### File Management

PurpleCli currently provides tools for:

- Listing files and directories
- Reading files
- Creating files
- Replacing file contents
- Deleting individual files

### Shell Execution

The agent can execute shell commands in the current working directory.

This allows PurpleCli to work with existing development tools and project workflows.

For example, the agent can potentially:

- Run tests
- Run scripts
- Install dependencies
- Inspect project state
- Build applications
- Execute development commands

### Multiple AI Providers

PurpleCli currently supports:

- OpenRouter
- Google Gemini

The provider can be selected through the setup command.

### Tool Calling

The AI can request tools when it needs them.

A typical interaction looks like this:

```text
User
 |
 v
AI analyzes request
 |
 v
AI requests tool
 |
 v
PurpleCli executes tool
 |
 v
Tool result returned
 |
 v
AI continues
 |
 v
Final response
```

### Plan Mode

PurpleCli includes a plan mode that instructs the AI to create a detailed plan before taking any actions. This can be useful for complex tasks where you want to review the approach before execution.

You can toggle plan mode at any time with the `/plan` command, or start PurpleCli with plan mode enabled using the `--plan` flag.

### Lightweight

PurpleCli is built around a relatively small Python codebase.

There is no requirement for a large framework or complicated application stack.

### Terminal First

PurpleCli runs directly from your command line.

There is no web dashboard required to use the core agent.

---

## 429 Note

You might experience an error like:

```bash
  API Error: 429 Client error: to many requests for url:
```

Please do NOT report this as a bug. receiving this error means that you are being rate limited or that your daily/weekly usage limit or you RPM (Requests per minute) have been maxed out. This is NOT a bug this is simply AI providers limiting how much you can use their tools.

---

## Installation

### Installation Notes

You will need to have "requests" installed, as the installer currently does not do this for you!

Install it using:

```bash
  pip install requests
```

### Quick Install

Install PurpleCli using the installation script:

```bash
curl -fsSL https://raw.githubusercontent.com/n0tpurplx/Purplecli/main/install.sh | sh
```

After installation:

```bash
PurpleCli
```

If the command is not immediately available, restart your terminal or make sure the installation directory is included in your `PATH`.

### Manual Installation

Clone the repository:

```bash
git clone https://github.com/n0tpurplx/Purplecli.git
```

Enter the project:

```bash
cd Purplecli
```

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Run PurpleCli:

```bash
python3 PurpleCli.py
```

---

## Requirements

PurpleCli requires:

- Python 3.x
- Internet access
- An API key from a supported AI provider

Python dependencies are listed in:

```text
requirements.txt
```

---

## Getting Started

After installing PurpleCli, configure your AI provider:

```bash
PurpleCli --setup
```

You will be asked to select a provider:

```text
PurpleCli Setup
---------------

Choose your AI provider:
1. OpenRouter
2. Google Gemini

Provider [1/2]:
```

Select your provider and enter the corresponding API key.

Once setup is complete, start PurpleCli:

```bash
PurpleCli
```

You should see something similar to:

```text
PurpleCli 0.1.5
Provider: openrouter
Type /help for commands. Type /exit to quit.

>
```

You can now describe what you want the agent to do.

For example:

```text
> Create a Python script that prints Hello World
```

Or:

```text
> Inspect this project and tell me how it works
```

Or:

```text
> Find the bug in main.py and fix it
```

---

## Usage

Start PurpleCli with:

```bash
PurpleCli
```

Once inside the agent, type your request after the `>` prompt.

PurpleCli sends the request to your configured AI provider and allows the model to use its available tools.

### Example

```text
> Add a README section explaining how this project works
```

The agent may inspect the project first:

```text
→ list_files()
→ read_file(path)
```

It can then make the required changes:

```text
→ write_file(path, content)
```

If it needs to verify something, it can execute a command:

```text
→ run_command(command)
```

The process continues until the model returns a final response.

### Another Example

```text
> Find all Python files in this project and explain what each one does
```

PurpleCli can inspect the directory, read the relevant files, and provide the requested explanation.

---

## CLI Options

PurpleCli currently provides the following command-line options:

| Option | Description |
| --- | --- |
| `-h`, `--help` | Show the help message |
| `-v`, `--version` | Show the PurpleCli version |
| `-S`, `--setup` | Configure an AI provider and API key |
| `--plan` | Start with plan mode enabled |

### Help

```bash
PurpleCli --help
```

### Version

```bash
PurpleCli --version
```

Example:

```text
PurpleCli 0.1.5
```

### Setup

```bash
PurpleCli --setup
```

This starts the interactive provider configuration.

---

## Interactive Commands

Inside PurpleCli, the following commands are currently available:

| Command | Description |
| --- | --- |
| `/help` | Show available interactive commands |
| `/exit` | Exit PurpleCli |
| `/quit` | Exit PurpleCli |
| `/plan` | Toggle plan mode |

### Exit

Either of the following commands exits PurpleCli:

```text
/exit
```

or:

```text
/quit
```

You can also exit using `Ctrl+C` or EOF input.

### Plan Mode

PurpleCli includes a plan mode that instructs the AI to create a detailed plan before taking any actions. This can be useful for complex tasks where you want to review the approach before execution.

You can toggle plan mode at any time with the `/plan` command, or start PurpleCli with plan mode enabled using the `--plan` flag.

---

## AI Providers

PurpleCli currently supports two AI providers.

### OpenRouter

OpenRouter provides access to AI models through a unified API.

Select OpenRouter during setup:

```text
Provider [1/2]: 1
```

PurpleCli currently requests:

```text
openrouter/free
```

through the OpenRouter API.

### Google Gemini

Google Gemini can be selected during setup:

```text
Provider [1/2]: 2
```

PurpleCli currently uses:

```text
gemini-2.5-flash
```

through Google's OpenAI-compatible API endpoint.

### Adding Providers

Additional providers may be added in future versions.

See [Extending PurpleCli](#extending-purplecli) for information about the provider architecture.

---

## Configuration

PurpleCli stores its configuration in the user's home directory.

```text
~/.purplecli/config.json
```

The configuration contains the selected provider and API key.

A configuration file may look like:

```json
{
  "provider": "openrouter",
  "api_key": "your-api-key"
}
```

The configuration file is created automatically when setup is completed.

PurpleCli attempts to restrict the configuration file permissions to the current user where supported by the operating system.

### Changing Providers

To change your provider or API key, run:

```bash
PurpleCli --setup
```

You can select a different provider and enter a new API key.

### API Keys

Do not share your configuration file publicly.

Do not commit it to Git.

Do not post your API key in:

- GitHub issues
- Pull requests
- Screenshots
- Logs
- Public repositories

If an API key is accidentally exposed, revoke it through the relevant provider immediately.

---

## Tools

PurpleCli currently provides five tools to the AI agent.

### `list_files`

Lists files and directories in the current working directory.

```text
list_files()
```

The `.git` directory is excluded from the listing.

### `read_file`

Reads a UTF-8 text file.

```text
read_file(path)
```

### `write_file`

Creates or completely replaces a UTF-8 text file.

```text
write_file(path, content)
```

Parent directories are created automatically when necessary.

### `delete_file`

Deletes a single file.

```text
delete_file(path)
```

Directory deletion is intentionally refused.

### `run_command`

Executes a shell command inside the current working directory.

```text
run_command(command)
```

The command's output and exit code are returned to the agent.

---

## Agent Architecture

PurpleCli uses a simple tool-calling agent loop.

```text
                    User
                     |
                     v
              System Prompt
                     |
                     v
                AI Provider
                     |
                     v
                 Tool Call?
                /          \
              No            Yes
              |              |
              v              v
        Final Response   Execute Tool
                             |
                             v
                       Tool Result
                             |
                             v
                        AI Provider
                             |
                             v
                         Continue
```

The agent continues requesting and executing tools until the model returns a final response without additional tool calls.

### Message Flow

PurpleCli starts the conversation with:

1. The system prompt.
2. The user's request.

The model then responds with either:

- A final response.
- One or more tool calls.

When a tool call is returned, PurpleCli executes it and adds the result back into the conversation.

The model can then use that information to continue working.

### Why This Architecture?

The architecture is intentionally simple.

PurpleCli does not attempt to build a huge abstraction layer between the model and the user's terminal.

Instead, the model gets a small, clearly defined set of operations that it can use to interact with the project.

---

## Project Structure

```text
Purplecli/
├── PurpleCli.py
├── README.md
├── CONTRIBUTING.md
├── LICENSE.md
├── install.sh
└── requirements.txt
```

### `PurpleCli.py`

The main PurpleCli application.

Contains:

- CLI argument handling
- Configuration
- AI provider integrations
- Agent loop
- Tool definitions
- File operations
- Shell command execution
- Interactive commands

### `README.md`

The main project documentation.

### `CONTRIBUTING.md`

Contribution guidelines for developers working on PurpleCli.

### `LICENSE.md`

The project's licensing terms under the PURPLE ACTION LICENSE (PAL) v1.0.

### `install.sh`

The installation script used by the quick installation command.

### `requirements.txt`

Python dependencies required by PurpleCli.

---

## Security

PurpleCli has access to powerful local operations, including file modification and shell command execution.

Treat AI-generated actions with the same caution you would use when running commands manually.

### PurpleCli Can

The current toolset allows the agent to:

- Read files
- Write files
- Delete files
- Execute shell commands

### Protect Sensitive Files

Avoid running PurpleCli in directories containing sensitive information unless you understand what files the agent can access.

Be especially careful with:

- API keys
- Passwords
- SSH keys
- Environment files
- Private configuration
- Authentication tokens
- Personal data

### API Keys

PurpleCli stores provider API keys locally in:

```text
~/.purplecli/config.json
```

Do not commit this file to a public repository.

### Reporting Vulnerabilities

If you discover a security vulnerability in PurpleCli, do not publicly disclose sensitive exploit details before the issue can be addressed.

Report security issues through the project's designated security reporting process.

---

## Development

Clone the repository:

```bash
git clone https://github.com/n0tpurplx/Purplecli.git
```

Enter the project:

```bash
cd Purplecli
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run PurpleCli:

```bash
python3 PurpleCli.py
```

### Basic Checks

Check the help output:

```bash
python3 PurpleCli.py --help
```

Check the version:

```bash
python3 PurpleCli.py --version
```

Run setup:

```bash
python3 PurpleCli.py --setup
```

### Development Philosophy

PurpleCli is intentionally lightweight.

When developing new functionality:

- Prefer simple solutions.
- Avoid unnecessary dependencies.
- Keep functions focused.
- Keep provider-specific logic isolated.
- Handle expected errors gracefully.
- Avoid unnecessary abstractions.
- Do not expose secrets.
- Keep the CLI easy to understand.

---

## Extending PurpleCli

PurpleCli is designed so that additional providers and tools can be added without completely redesigning the application.

### Adding an AI Provider

A provider integration generally requires:

1. A provider request function.
2. Provider selection during setup.
3. Provider handling inside `ask_ai()`.
4. Any required model configuration.
5. Appropriate error handling.
6. Documentation in the README.

Provider integrations should use the existing agent architecture where reasonably possible.

### Adding a Tool

A new tool generally requires:

1. A Python function implementing the operation.
2. An entry in the `TOOLS` dictionary.
3. A corresponding function definition in `tool_definitions()`.
4. Appropriate argument handling.
5. Error handling.

For example:

```python
def example_tool(value):
    return f"Received: {value}"
```

The tool then needs to be registered with the tool system so the AI can call it.

### Tool Design

Tools should be:

- Predictable
- Focused
- Clearly described
- Safe where reasonably possible
- Easy for the model to understand

Avoid creating tools that duplicate functionality already provided by existing tools unless there is a clear benefit.

---

## Roadmap

PurpleCli is currently in early development.

The roadmap may change as the project evolves.

### Agent Improvements

Potential improvements include:

- Better context management
- Improved multi-step reasoning
- More reliable tool execution
- Better handling of long tasks
- Improved recovery from failed tool calls
- More advanced project awareness

### Provider Improvements

Potential provider improvements include:

- More AI providers
- Better provider configuration
- Provider-specific capabilities
- Improved API error handling
- Model selection

### CLI Improvements

Potential CLI improvements include:

- Better terminal output
- More interactive commands
- Improved command history
- Improved configuration management
- Better status information
- Improved error messages

### Tooling Improvements

Potential tooling improvements include:

- More project inspection tools
- Safer command execution
- Better file operations
- Search tools
- Project structure analysis
- Test execution helpers

### Developer Experience

Potential developer experience improvements include:

- Better automated testing
- Better documentation
- Improved installation
- Easier development setup
- More contribution tooling

---

## Contributing

Contributions are welcome.

There are many ways to contribute to PurpleCli, including:

- Bug fixes
- New features
- AI provider integrations
- Tool improvements
- Agent improvements
- Documentation
- Testing
- Performance improvements
- Installation improvements
- Error handling improvements

For complete contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

### Before Contributing

For small fixes and documentation changes, you can generally get started immediately.

For larger features or architectural changes, consider opening an issue first to discuss the idea.

This helps avoid duplicated work and gives the project maintainers a chance to provide feedback before significant implementation work begins.

---

## Bug Reports

Found a bug?

Open an issue on GitHub:

[Open a GitHub Issue](https://github.com/n0tpurplx/Purplecli/issues)

When reporting a bug, include:

- What you were trying to do
- What happened
- What you expected to happen
- Your operating system
- Your Python version
- Your PurpleCli version
- Relevant error output
- Steps to reproduce the problem

### Do Not Include Secrets

Never include:

- API keys
- Passwords
- Authentication tokens
- Private keys
- Personal credentials
- Sensitive personal information

Remove sensitive information from logs before posting them publicly.

---

## License

PurpleCli is licensed under the:

**PURPLE ACTION LICENSE (PAL) v1.0**

PAL permits:

- Personal use
- Commercial use
- Modification
- Forking
- Creation of derivative works
- Redistribution with attribution
- Building commercial software using PurpleCli

The license requires proper attribution when redistributing the project's code and prohibits misrepresenting the original work as your own.

See the complete license in [LICENSE.md](LICENSE.md).

---

## Status

PurpleCli is currently in:

**Early Development**

The project is functional, but its architecture, features, and APIs may change significantly between releases.

Expect breaking changes while PurpleCli develops toward a more stable release.

---

## Credits

PurpleCli was created and is maintained by:

**n0tpurplx**

Contributors are credited through the project's contribution history.

As the project grows, significant contributors may also be listed in an `AUTHORS.md` file.

---

## Links

- [GitHub Repository](https://github.com/n0tpurplx/Purplecli)
- [Issues](https://github.com/n0tpurplx/Purplecli/issues)
- [Contributing](CONTRIBUTING.md)
- [License](LICENSE.md)

---

<p align="center">
  <strong>PurpleCli</strong><br>
  A lightweight AI coding agent for your terminal.
</p>
