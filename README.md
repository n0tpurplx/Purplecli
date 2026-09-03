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
  <a href="https://github.com/n0tpurplx/Purplecli/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/n0tpurplx/Purplecli?style=for-the-badge&label=License" alt="License">
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

## About

PurpleCli is a lightweight AI coding agent that runs directly inside your terminal.

Instead of relying on a large application, web dashboard, or complicated development environment, PurpleCli gives an AI model a small set of practical tools for interacting with your project.

The agent can inspect files, read source code, create and modify files, delete files, and execute shell commands.

You tell it what you want.

It figures out what it needs to inspect, which tools it needs to use, and how to complete the task.

```text
You
 |
 v
PurpleCli
 |
 v
AI Model
 |
 +---- list_files
 |
 +---- read_file
 |
 +---- write_file
 |
 +---- delete_file
 |
 +---- run_command
 |
 v
Your Project
