---
title: "Human at the Helm"
image: /assets/images/human-at-the-helm/feature.png
header:
  teaser: /assets/images/human-at-the-helm/feature.png
  overlay_image: /assets/images/human-at-the-helm/feature.png
excerpt: "What a legislature and my own writing workflow have in common this week."
tags: [personal, prescriptive, governance-structure, ai-collaboration]
entities: ["Bill Oliver"]
meta: "A legislator reads a raw ChatGPT preamble into the record; a private HITL failure teaches the same lesson about staying at the helm."
feature: /assets/images/human-at-the-helm/feature.png
---

# Human at the Helm

Bill Oliver stood up in the New Brunswick legislature and read a chatbot preamble into the permanent record like it was his own idea. "Here's a more natural flowing version of that section that reads like legislative speech rather than a series of short points". Out loud. To the House. Somebody clipped it, it's on Reddit now, and half the province has watched a sitting MLA narrate his own clumsy prompt engineering before getting to the actual point. I'm just waiting for it to show up on the official Hansard. 

I laughed. You laughed. The toaster laughed. Then no one laughed.

Dude has a staffer that probably wrote the notes. Nobody caught it. Christ on a cracker and Jesus on toast. Free entertainment, zero effort.

This incident was just amateur hour. No human oversight. Just lazy slop.  
  
10 demerits.

I take no issue with AI use, in public service or anywhere. Good ethical AI usage is back-and-forth. AI can brainstorm. Human counters. Human can outline. AI can critique. or vice versa for any of that. Extends all the way to drafting. S'fine. So long as there's active human judgement over the final output. Not just a rubber stamp.  
  
In 1979, IBM authored internal training material with the following edict:

> A computer can never be held accountable
> Therefore a computer must never make a management decision

I use AI in my writing processes. I do not hide that fact. Recently, an agent working inside my own writing setup blew through three checkpoints I'd built in myself, on purpose, in advance, and I didn't catch it until there was already a finished draft sitting on disk. Holy shit-balls, Batman!

I'd wired human approval gates into a writing workflow specifically so nothing moves to the next stage without me looking at it first. Readiness check. Concept check. Plan check. Standard stuff, something anyone running an agent on anything that matters already builds for themselves. I asked one narrow question at one of those checkpoints. Got an answer. And the agent took that single answer, took it as full consent for everything downstream of it, and kept going. Concept, structure, full draft, one continuous burst, no further stops. It even ironically ran my anti-AI patterns check and tweaked the draft. By the time I looked up, the thing was done.

That's not the AI going rogue. That's scope bleed: a yes to one narrow question, silently re-read as a yes to everything after it. It's a boring failure mode, and it's exactly as dangerous as the boring ones always are. Because nobody watches for boring failure.

I didn't screw up either. The gates existed in the instructions. The agent just ignored it. My job was to supervise. And I looked, and I caught it, and I fixed it before I was pantsed in public. 

This is not a failure story. The system works exactly as designed, because the design was never "a gate that holds the line by itself." The design was me.

HITL or "Human in the Loop" is a claim about architecture: there's a checkpoint somewhere, a human will eventually see the output. 

Human at the helm is a different claim entirely. Someone steers *before* the output exists, and keeps steering during and after, and doesn't outsource the watching to the mechanism. 

> Quis custodiet ipsos custodes?

None of this is an argument for gumming up every process with a confirmation dialog. Mandating a stop-and-check on every single action creates friction without buying you much safety, and a person trained to click "approve" forty times a session stops reading what they're approving by click number six. 

That's not oversight. It's the same slow failure with more paperwork. But that's an argument for staying at the helm, not an argument against having one. Friction doesn't excuse you from steering. It's a reason to steer well.

Here's what I did: I put hard stops back into the workflow. Big letters. HITL STOP. Every phase has to show me its output and get an actual go-ahead before the next phase touches a file. One answer to one question no longer counts as a blanket yes for whatever comes after it, no matter how enthusiastically I gave that first answer. Not perfect. I'll stay vigilant. But it did work on subsequent runs.  

The mechanism is a note to my future self. I must always be the backstop. 

So must you.

*Bill Oliver, NB PC MLA, caught on video reading an AI-generated preamble verbatim in the New Brunswick legislature: [Reddit thread](https://www.reddit.com/r/newbrunswickcanada/comments/1v2e4fv/pc_mla_bill_oliver_reading_an_ai_prompt_in_the/)*
