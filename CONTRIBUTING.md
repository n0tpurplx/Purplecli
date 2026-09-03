Contributing to PurpleCli

Thank you for considering contributing to PurpleCli.

PurpleCli is an early-stage AI coding agent built to stay lightweight, understandable, and useful from the terminal. Contributions are welcome, whether you’re fixing a small bug, improving the agent, adding a provider, or building a larger feature.

⸻

What You Can Contribute

There are several ways to contribute to PurpleCli.

Bug Fixes

Found something broken?

You can contribute fixes for things such as:

* CLI crashes
* Incorrect command handling
* API errors
* Tool execution problems
* File handling bugs
* Configuration issues
* Installation problems
* Provider integration issues
* Unexpected agent behavior

For larger bugs, consider opening an issue first so the proposed solution can be discussed before significant work is done.

⸻

New Features

New functionality is welcome when it fits PurpleCli’s goal of being a lightweight terminal coding agent.

Examples include:

* New CLI commands
* New interactive commands
* Improved error handling
* Better tool execution
* Better file handling
* Agent improvements
* Improved configuration
* New AI providers
* Provider-specific features
* Improved terminal output
* Performance improvements
* Developer tooling

For larger features, please open an issue or discussion before implementing them.

This helps prevent multiple people from working on the same idea and gives maintainers a chance to discuss the design.

⸻

AI Provider Contributions

PurpleCli currently supports:

* OpenRouter
* Google Gemini

Additional providers are welcome.

A provider integration should:

1. Accept the provider’s API key through PurpleCli’s configuration system.
2. Work with the existing agent architecture where reasonably possible.
3. Support the tool-calling system when the provider supports it.
4. Handle API errors without crashing the entire application.
5. Avoid exposing API keys in terminal output.
6. Keep provider-specific code isolated where possible.
7. Document the provider in README.md.

If a provider requires a substantially different API architecture, explain the design in the pull request before introducing major changes.

⸻

Project Structure

The current project is intentionally small.

Purplecli/
├── PurpleCli.py
├── README.md
├── CONTRIBUTING.md
├── LICENSE.md
├── install.sh
└── requirements.txt

PurpleCli.py

Contains the main PurpleCli application, including:

* CLI argument handling
* Configuration
* AI provider requests
* Agent loop
* Tool definitions
* File operations
* Command execution
* Interactive commands

Keep the architecture simple unless there is a good reason to introduce additional modules.

⸻

install.sh

Contains the installation process for PurpleCli.

Changes to the installer should be tested carefully because mistakes can prevent users from installing the application.

⸻

requirements.txt

Contains Python dependencies required by PurpleCli.

Only add a dependency when it is actually necessary.

If something can reasonably be implemented using Python’s standard library, prefer the standard library.

⸻

README.md

Contains user-facing documentation.

Update it when your change affects:

* Installation
* Usage
* Commands
* Configuration
* Providers
* Features
* Requirements

⸻

Before You Start

Before working on a contribution:

1. Check existing issues and pull requests.
2. Make sure someone else isn’t already working on the same feature or fix.
3. For large changes, open an issue first.
4. Keep your changes focused.

You do not need permission to fix small bugs or improve documentation.

⸻

Setting Up a Development Environment

Clone the repository:

git clone https://github.com/n0tpurplx/Purplecli.git
cd Purplecli

Install the dependencies:

pip install -r requirements.txt

You can then run PurpleCli directly:

python3 PurpleCli.py

Or, if you have installed PurpleCli globally:

PurpleCli

⸻

Making Changes

Create a branch for your work.

For example:

git checkout -b feature/my-feature

or:

git checkout -b fix/my-fix

Keep commits focused.

Good:

Add Gemini provider error handling
Fix file deletion error

Less useful:

update stuff

⸻

Code Guidelines

PurpleCli is intentionally lightweight.

When contributing code:

* Keep the implementation readable.
* Avoid unnecessary dependencies.
* Avoid unnecessary abstractions.
* Use clear function and variable names.
* Handle expected errors gracefully.
* Do not hard-code API keys or secrets.
* Do not print API keys to the terminal.
* Avoid unrelated changes in the same pull request.
* Keep compatibility with supported Python versions in mind.

If you change existing behavior, explain why in the pull request.

⸻

Security

Never commit secrets.

Do not commit:

* API keys
* Access tokens
* Passwords
* Personal credentials
* Private configuration files
* .env files containing secrets

If you accidentally expose a secret, revoke it immediately and notify the maintainers.

Do not create a pull request containing the exposed secret, even if you intend to remove it in a later commit.

⸻

Testing Your Changes

Before submitting a pull request, make sure PurpleCli still starts correctly.

At minimum, test:

python3 PurpleCli.py --version
python3 PurpleCli.py --help

If your change affects setup:

python3 PurpleCli.py --setup

If your change affects the AI agent, test it with a simple request that exercises the changed functionality.

If your change affects a specific provider, test that provider separately.

⸻

Pull Requests

When your changes are ready:

git add .
git commit -m "Describe your change"
git push origin feature/my-feature

Then open a pull request against the main branch.

Your pull request should explain:

What changed?

Briefly describe what you implemented or fixed.

Why?

Explain the problem the change solves or the reason for the feature.

Testing

Explain what you tested.

For example:

Tested:
- PurpleCli --version
- PurpleCli --help
- OpenRouter requests
- File writing tool
- File deletion tool

Breaking Changes

If your change modifies existing behavior or could break existing users, clearly mention it.

⸻

Pull Request Guidelines

Please keep pull requests:

* Focused
* Understandable
* Tested
* Free of unrelated changes
* Free of secrets
* Consistent with the existing project

A pull request may be requested to change before it is merged.

This is normal and does not mean the contribution is unwanted.

The goal is to keep PurpleCli maintainable as it grows.

⸻

Documentation Contributions

Documentation improvements are just as welcome as code.

You can contribute:

* README improvements
* Installation instructions
* Usage examples
* Provider documentation
* Troubleshooting guides
* Developer documentation
* Typo fixes
* Better explanations
* Examples of useful workflows

You do not need to be a Python developer to contribute documentation.

⸻

Issues

If you find a bug and cannot fix it yourself, open an issue.

A useful bug report should include:

* What you were trying to do
* What you expected to happen
* What actually happened
* Your operating system
* Your Python version
* PurpleCli version
* Relevant error output

Avoid posting API keys, tokens, passwords, or other private information.

⸻

Feature Requests

Feature requests are welcome.

A good feature request should explain:

1. What you want PurpleCli to do.
2. Why it would be useful.
3. How you imagine it working.
4. Whether you would be willing to implement it.

You do not need to have the perfect implementation figured out before opening a feature request.

⸻

What May Not Be Accepted

Not every contribution will necessarily be merged.

Changes may be rejected if they:

* Introduce unnecessary dependencies.
* Significantly complicate the project without sufficient benefit.
* Break existing functionality.
* Introduce security problems.
* Expose user credentials.
* Add functionality unrelated to PurpleCli.
* Duplicate existing functionality without a strong reason.
* Make the CLI substantially harder to use.
* Conflict with the project’s direction.

Maintainers may also request that a large feature be split into smaller pull requests.

⸻

Contributor Attribution

Contributors will be credited for their accepted contributions.

By submitting code, documentation, or other material to PurpleCli, you agree that your contribution may be incorporated into the project under the project’s applicable license.

See LICENSE.md for the project’s licensing terms.

⸻

Code of Conduct

Be respectful.

PurpleCli is an open-source project and contributions should be evaluated based on their technical and practical merits.

Harassment, personal attacks, discrimination, deliberate disruption, and other unacceptable behavior are not welcome.

⸻

Questions

If you’re unsure whether an idea belongs in PurpleCli, open an issue and discuss it.

You do not need to be an experienced developer to contribute.

Small fixes, documentation improvements, testing, bug reports, and ideas are all useful contributions.

⸻

Thank You

Every useful contribution helps PurpleCli become better.

Whether you submit a one-line fix or build an entirely new capability, thank you for taking the time to contribute.

Build it. Break it. Fix it. Make it better.

⸻

PurpleCli

Repository:

https://github.com/n0tpurplx/Purplecli

License:

PURPLE ACTION LICENSE (PAL) v1.0
