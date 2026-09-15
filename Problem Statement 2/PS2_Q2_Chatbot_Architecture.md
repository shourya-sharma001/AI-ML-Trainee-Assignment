# Problem Statement 2 — Question 2

**Question:** What are the key architectural components to create a chatbot based on LLM? Please explain the approach on a high-level.

---

## Overview

It's easy to assume an LLM-based chatbot is basically just the LLM. In practice, the LLM is really just one piece — the part that reasons and generates text — sitting inside a larger system of supporting components that together make the whole thing reliable and useful. Below I've gone through what those pieces are.

AccuKnox already has a live product built roughly this way: AskADA, its AI Copilot, which lets users ask plain-language questions about their cloud security posture — misconfigurations, vulnerability findings, compliance status — instead of digging through dashboards manually. Since it has to answer using a customer's live data and AccuKnox's own documentation, neither of which any LLM would know from training alone, it almost certainly needs a retrieval layer backed by a vector database, plus some way to call into AccuKnox's platform for real-time data. I'll reference it a couple of times below as a concrete example rather than keeping this purely theoretical.

---

## 1. User Interface

This is just the surface the user actually types into — a chat widget on a website, a mobile app, Slack, whatever. It captures the message and shows the response. No reasoning happens here.

## 2. Input Processing

Before a message reaches the LLM, it usually gets cleaned up a bit — stripping noise, detecting language if the system is multilingual, checking for anything unsafe.

## 3. Context / Memory Management

This one's easy to overlook but matters a lot. An LLM doesn't actually remember earlier messages on its own — each call to it is essentially stateless. It's on the surrounding system to keep track of the conversation and resend the relevant parts of it along with each new message, so the model has enough context to respond sensibly. This usually breaks down into short-term memory (the current conversation) and long-term memory (things like saved preferences from earlier sessions, stored somewhere persistent).

## 4. Retrieval System (RAG)

Probably the most important piece if you want the chatbot to actually be useful for a business, not just a general-purpose assistant. An LLM only knows what it was trained on — it has no idea about a company's internal docs, recent changes, or anything proprietary.

To get around this, the system keeps a vector database of embeddings for relevant documents (I go into what that means in Question 3). When someone asks something, their question gets embedded too, and the database returns whatever stored content is closest in meaning — even if the wording is completely different. That retrieved content then gets handed to the LLM along with the original question, so the answer is grounded in something real rather than the model just guessing based on training data. This is likely how AskADA can answer something specific to a customer's environment or to AccuKnox's help docs.

## 5. The LLM

The actual model doing the reasoning (GPT, LLaMA 2, Claude, etc.) — it takes the question, the conversation history, and whatever context was retrieved, and generates a response.

## 6. Tool / Function Calling

More capable chatbots don't just talk — they can act. This happens through function calling: the LLM decides a query needs an outside action (checking a database, running a calculation, hitting an API), triggers it, and folds the result into its answer.

## 7. Output Filtering

Before the response reaches the user, it typically goes through a check for safety, tone, and formatting, so nothing inappropriate or off-brand slips through.

## 8. Logging

Conversations get logged on the backend — partly to catch misuse, partly to spot where the chatbot is falling short so it can be improved later.

---

## Flow

```
User Message
     |
     v
Input Processing (cleaning, safety check)
     |
     v
Context / Memory Management
     |
     v
Retrieval — Vector DB similarity search (RAG)
     |
     v
LLM generates a response using the question + history + retrieved context
     |
     v
Tool / Function Calling (if something external is needed)
     |
     v
Output Filtering
     |
     v
Response shown to the user
     |
     v
Logging
```

---

## A Practical Example

Let's say someone asks AskADA, "What compliance gaps do we have with the EU AI Act right now?" The Retrieval component pulls the relevant, current findings for that customer's account and any related compliance documentation — none of which any LLM would know from training. The model then turns that into a clear summary. If the person follows up with "show me the latest CNAPP metrics," Function Calling kicks in to query AccuKnox's platform APIs directly, since that data changes constantly and can't just be pre-indexed. It's a decent example of how Retrieval, the LLM, and Tool Calling actually depend on each other rather than working in isolation.
