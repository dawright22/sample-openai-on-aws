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

This directory contains a Jupyter notebook (`Getting_Started_Guide_Bedrock.ipynb`) that demonstrates four use cases for running OpenAI's GPT-OSS models (`gpt-oss-120b` and `gpt-oss-20b`) on Amazon Bedrock.

## Use Cases

### 1. OpenAI SDK Integration

Use the familiar OpenAI Python SDK, pointed at Bedrock's OpenAI-compatible endpoint. This requires no code changes if you already use the OpenAI SDK.

* Chat completions (non-streaming and streaming)
* Function calling with tool use

### 2. Amazon Bedrock InvokeModel API

Direct low-level access to Bedrock's `InvokeModel` and `InvokeModelWithResponseStream` APIs via `boto3`.

* Non-streaming inference
* Streaming with time-to-first-token measurement
* Tool use with manual request/response handling

### 3. Amazon Bedrock Converse API

A unified, model-agnostic interface that works across all Bedrock-hosted models without code changes.

* Synchronous inference with reasoning trace extraction
* Streaming via `converse_stream`
* Tool use with Bedrock's native `toolSpec` format

### 4. Reasoning Use Cases

Demonstrations of complex reasoning tasks using the Chat Completions API:

* **Exponential growth** — compound growth calculations over time
* **Kinematics** — multi-phase motion analysis and distance computation
* **Scientific problem solving** — projectile physics with step-by-step derivation
* **System design** — scalable architecture reasoning (URL shortener)

## Prerequisites

* Python 3.9+
* AWS account with Bedrock model access enabled for `openai.gpt-oss-120b-1:0` and/or `openai.gpt-oss-20b-1:0` in `us-west-2`
* A Bedrock API key

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
export OPENAI_BASE_URL="https://bedrock-runtime.us-west-2.amazonaws.com/openai/v1"
```

Or update the values directly in the notebook's configuration cell.

### 5. Open the notebook

```bash
jupyter notebook Getting_Started_Guide_Bedrock.ipynb
```

Or open the file in VS Code and select the `Python (.venv bedrock-gptoss)` kernel from the kernel picker (top-right of the notebook).

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
