---
title: OpenAI GPT-OSS Models on Amazon Bedrock
description: Getting started guide and use cases for running OpenAI GPT-OSS models on Amazon Bedrock using three API approaches and reasoning examples
ms.date: 2026-05-21
ms.topic: tutorial
keywords:
  - amazon bedrock
  - openai
  - gpt-oss
  - python
  - jupyter
estimated_reading_time: 5
---

## Overview

This repository contains a practical playbook for running OpenAI GPT-OSS models on Amazon Bedrock from Jupyter notebooks. It includes end-to-end examples for configuration, inference, streaming, tool use, and reasoning tasks using both Bedrock-native APIs and OpenAI-compatible APIs.

## Playbook Contents

| File | Purpose |
|---|---|
| `Getting_Stated_guide.ipynb` | Main getting-started notebook with setup and core Bedrock/OpenAI-compatible examples |
| `OSS_Agents_With_OpenAI_Compatible_Endpoint.ipynb` | Agent workflows using OpenAI-compatible Bedrock endpoints |
| `agentic_workflow_with_langchain.ipynb` | Agentic patterns and orchestration with LangChain |
| `demo_gpt_oss_research.ipynb` | Additional GPT-OSS experimentation and demos |
| `base-imgs/` | Supporting images used by notebooks |

## Use Cases

### 1. OpenAI SDK Integration

Use the familiar OpenAI Python SDK, pointed at Bedrock's OpenAI-compatible endpoint. This requires no code changes if you already use the OpenAI SDK.

* Chat completions (non-streaming and streaming)
* Function calling with tool use

## Prerequisites

* Python 3.9+
* AWS account with Bedrock model access enabled for `openai.gpt-oss-120b-1:0` and/or `openai.gpt-oss-20b-1:0` in `us-west-2`
* A Bedrock API key
* Jupyter support in your environment (VS Code notebooks or Jupyter Lab)

## Setup

### 1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -U boto3 openai strands-agents ipython ipykernel
```

### 3. Register the kernel with Jupyter

```bash
python -m ipykernel install --user --name bedrock-gptoss --display-name "Python (.venv bedrock-gptoss)"
```

### 4. Configure AWS credentials

Set your Bedrock API key before running the notebook:

```bash
export AWS_BEARER_TOKEN_BEDROCK="<your-bedrock-api-key>"
export OPENAI_API_KEY="<your-bedrock-api-key>"
export OPENAI_BASE_URL="https://bedrock-mantle.us-west-2.api.aws/v1"
```

Or set values directly in the notebook configuration cell.

### 5. Open the notebook

```bash
jupyter notebook Getting_Stated_guide.ipynb
```

Or open the file in VS Code and select the `Python (.venv bedrock-gptoss)` kernel from the kernel picker (top-right of the notebook).

## Recommended Execution Order

To avoid state-related notebook errors, run setup cells in order:

1. Install dependencies
2. Import modules (including `import os`)
3. Configure environment variables
4. Run model invocation examples

If you skip cells and see missing-name errors, run all previous setup cells and re-run the current cell.

## IAM Permissions Required

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream"
      ],
      "Resource": "*"
    }
  ]
}
```

## Model IDs

| Model | ID | Parameters | Best For |
|---|---|---|---|
| GPT-OSS 120b | `openai.gpt-oss-120b-1:0` | 120B | Complex reasoning, agentic tasks |
| GPT-OSS 20b | `openai.gpt-oss-20b-1:0` | 20B | Faster inference, cost-effective tasks |
