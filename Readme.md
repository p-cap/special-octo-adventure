# Strands + Amazon Bedrock Starter

A small Python starter that runs a Strands agent with an Amazon Bedrock model and a custom word-counting tool.

## What it does

Running `main.py`:

1. Checks AWS credentials with STS and prints the account ID and caller ARN.
2. Loads model settings from `.env`.
3. Creates a Bedrock-backed Strands agent with a `count_words` tool.
4. Asks the agent to count the words in `Strands makes building agents easy` (six words).

## Prerequisites

- Python 3.13 or newer.
- `uv` for dependency management.
- AWS credentials available to Boto3.
- Access to a Bedrock model that supports tool use in your chosen AWS Region, with permission to invoke it.

The STS check verifies your AWS identity; model invocation verifies Bedrock access.

## Setup

From the project directory, install the locked dependencies:

```sh
uv sync
```

Authenticate using your AWS setup. If you use AWS CLI login:

```sh
aws login
```

For a named profile, select it in your shell before running the application:

```sh
export AWS_PROFILE=your-profile
```

Create a `.env` file in the project directory:

```dotenv
AWS_REGION=us-east-1
BEDROCK_MODEL_ID=your-bedrock-model-or-inference-profile-id
```

Replace the model placeholder with an identifier available to your account in the configured Region. `.env` is excluded from Git.

## Run

```sh
uv run main.py
```

The script prints your AWS identity, a greeting, and the agent's response to the word-count question. Model invocation uses your AWS account and may incur charges.

## Configuration

| Setting | Purpose |
| --- | --- |
| `AWS_REGION` | Region used by the Bedrock model. |
| `BEDROCK_MODEL_ID` | Model or inference profile identifier passed to `BedrockModel`. |
| `AWS_PROFILE` | Optional AWS profile; export it in your shell before running. |

The initial STS check uses `us-east-1` directly and runs **before** `.env` is loaded. Set credentials and profile selection in your shell or AWS configuration so they are available to that check.

## Customize

Edit `run_strands_agent()` in `main.py` to change the system prompt, replace the sample question, or add functions decorated with `@tool` to the agent's `tools` list.

## Troubleshooting

- **AWS credential or login errors:** Authenticate again and check the profile selected in your shell. The script stops if the STS identity check fails.
- **Missing `AWS_REGION` or `BEDROCK_MODEL_ID`:** Add both values to `.env`. The current script prints the missing key and returns without running the agent.
- **Bedrock invocation errors:** Check the model identifier, Region, model access, and permissions for the selected AWS identity.

## Project files

- `main.py` — AWS connection check, custom tool, and agent entry point.
- `pyproject.toml` — Python requirements and dependencies.
- `uv.lock` — Locked dependency versions.
- `.python-version` — Python version selected for local development.
- `.gitignore` — Excludes local configuration, environments, and generated files.
