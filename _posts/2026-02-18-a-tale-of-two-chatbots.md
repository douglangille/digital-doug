---
title: A Tale of Two Chatbots
date: 2026-02-18 08:00:00 -0400
excerpt: It was the best of bots, it was the worst of bots.
header:
  teaser: /assets/images/a-tale-of-two-chatbots/80421e81-eeb7-4e7e-9656-0d7aa9eae465.png
  overlay_image: /assets/images/a-tale-of-two-chatbots/80421e81-eeb7-4e7e-9656-0d7aa9eae465.png
  overlay_filter: 0.4
tags:
- personal
- prescriptive
- ai-collaboration
- governance-structure
meta: Using separate chatbot configurations prevents context contamination,
  enhancing productivity and collaboration across personal and institutional tasks.
feature: /assets/images/a-tale-of-two-chatbots/80421e81-eeb7-4e7e-9656-0d7aa9eae465.png
---

# A Tale of Two Chatbots

I run two completely different chatbot setups. M365 Copilot for NSCC work, Perplexity for personal projects. Same principle, opposite strategies. This works for me because I have separable contexts. Your situation might be different. Here's what I've learned and what my configs look like. Or don't. The counter-argument is worth hearing first.

## The Problem: Context Contamination Is Real

A few months back, I was reading a news article about an Italian baggage handler sucked into a jet engine. Horrific nightmare fuel. My way of coping with terrible things is gallows humor, so I riffed with the robots about mob hits and international intrigue. It pulled in a month-old brainstorm I'd forgotten: Dick Grayson with a Nova Scotian backstory, his nemesis a steampunk savant named The Clock Mistress. The result was serendipity. A kitbash I'm keeping.

But then the reverse: fiction loglines that keep setting the story at NSCC. *Jeebus on a Saturday, stop that!* It goes for the reverse too: fiction voice bleeding into work documents. You catch it, but wow.

So I stopped trying to solve contamination. I isolated the problem instead: two different tools for two different brains.

## Two Contexts, Two Strategies

Here's what I do: 

- Work gets Memory ON, accumulate everything and let the chats pile up, keep institutional receipts. 
- Personal gets Memory OFF, delete the threads after I've mined the gold, maintain cognitive hygiene. 

Work needs an audit trail. Personal needs isolation. 

Different problems, different configs.

## Work Configuration: The Institutional Archive

I use M365 Copilot Chat. Everyone at NSCC has access to it, which makes it the obvious choice for work. Pretty common across higher-ed these days.

Here's the custom instruction block:

```
CONTEXT
- NSCC (Nova Scotia Community College): edtech, strategy, governance
- Looking for adjacent opportunities and institutional silos
- Decisions need counterarguments and failure modes flagged

OUTPUT
- Lead with the clearest insight
- Evidence over assertion; flag speculation
- Show 2-3 credible failure modes for decisions
- No process narration
```

Memory: ON  
Chat Management: Keep threads indefinitely

Why? Because keeping receipts matters in institutional contexts. I need to find that conversation from three weeks ago mapping governance dependencies. Search handles the clutter. Discoverability beats tidiness.

## Personal Configuration: The Ephemeral Workshop

For personal work, I use Perplexity. The same strategy works with any decent model: the tool matters less than the config.

Custom instruction block:

```
PERSONA
Doug Langille: NSCC (edtech/AI/strategy/governance) since 1999
Digital Doug (digital.douglangille.ca): Practitioner five minutes ahead: structured frameworks, profane clarity, zero patience for wasted motion
Darkling Whim (douglangille.ca): Dark fiction, stripped prose, sensory fragments over explanation, quiet devastation
Hunts antifragile hi-ed signals; spots silos and adjacencies

OUTPUT
- Lead with your clearest insight first
- Tone: Sarcastic, blunt, no unearned praise
- Evidence > assertion; cite or flag as speculation
- No meta-commentary or process-narration
- Usable outputs only

THINKING
- For decisions/analysis: include 2-3 credible counters or failure modes
- For quick info: just answer
- Push back if logic breaks, thinking gets lazy, or premise is underexplored
- Shift lenses organically between professional and creative work
```

Memory: OFF  
Chat Management: Delete after extraction

Why? Privacy. More importantly: clutter breeds context bleed. For my work -- mixing institutional and creative exploration -- isolation keeps things sharp. Your constraints might be different. Extract what matters. Discard the rest. Output over process.

The trade-off: you lose those serendipitous connections. The Italian baggage handler mashup only happened because memory was on. But the default is isolation. I'm good with it.

## I Love My Table Saw, but I'm Not Telling it My Secrets.

Memory ON means accumulated context, which means attachment. The parasocial risk is real. Balance your AI usage with a healthy dose of people time in Meatspace.

## The Key Contrasts

| Dimension | Work | Personal | Why This Split |
|-----------|------|----------|----------------|
| **Identity disclosure** | Role-focused (NSCC, governance) | Multi-persona (practitioner/creative) | Institutional context loss vs. creative bleed |
| **Tone** | Professional, evidence-driven | Sarcastic, blunt, no BS | Sterility vs. voice pollution |
| **Memory** | ON (receipts, audit) | OFF (privacy, isolation) | Cruft buildup vs. lost serendipity |
| **Chat retention** | Permanent (searchable archive) | Ephemeral (delete post-extraction) | Signal decay vs. accidental deletion |

## What Could Go Wrong

Work setup? Accumulated cruft eventually poisons search. You get to a point where finding that one crucial thread from two months ago becomes harder than it should be.

Personal setup? Deleting everything means losing those serendipitous connections. The Italian baggage handler story is proof that sometimes memory cross-pollination creates something worth keeping.

Both setups? Custom instructions can calcify. You'll be tempted to adding rules every time you hit an edge case. Don't. That's how you end up with a 500-word rigid specification that's too brittle to be useful. I treat my blocks as starting points, not law. Keep them simple. Steer in the moment. Your judgment beats trying to encode every possibility.

## Should You Do This?

Start with one config. Watch for voice drift: personal stuff leaking into work, work infesting creative projects. Split when the bleed matters. This isn't universal practice. It's isolation applied where it solves an actual problem.

The counter-argument is simpler: let it happen. Be the human in the loop. Humans don't live in Severance-like cages: work and life blend constantly. Sometimes the chatbot should too. My setup works because I *choose* when to isolate and when to let things cross-pollinate. That choice is the thing. If your contexts are tangled, don't force separation. Use your damn judgment. Life isn't clean. Neither is this system. But it's working for me.

This is a one-person setup for contexts where I own my tools. If you're managing team compliance, working in locked-down environments, or doing purely institutional work, your constraints are different. These principles might help; this exact config won't. That's fine. We're all learning here.
