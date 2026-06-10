---
title: "You Can't Prompt Your Way Around Culture"
date: 2026-06-10 08:00:00 -0300
tags:
  - institutional
  - diagnostic
  - governance-structure
  - ai-collaboration
meta: Red-teaming works as a technique, but institutions trained to suppress dissent capture the critique before anyone can act on it. You can't prompt your way around culture.
excerpt: Institutions don't know how to listen. They've been trained not to.
header:
  teaser: /assets/images/you-cant-prompt-header/feature.png
  overlay_image: /assets/images/you-cant-prompt-header/feature.png
feature: /assets/images/you-cant-prompt-header/feature.png
---

# You Can't Prompt Your Way Around Culture

Guess what? Your institution has already made a strategic decision that AI helped make worse. And nobody caught it. Guaranteed, not speculation. It's the predictable consequence of how these things are trained.

The red-teaming method works -- using structured adversarial review to stress-test plans. The approach goes back 200 years. Kriegsspiel in 1812. Israeli military after Yom Kippur in 1973. The CIA Team B exercise in 1976. The evidence is documented. For desycophantizing AI, all it takes is five minutes with a prompt.

Here's the rub: the technique can't fix the room.

## Sycophancy Is Structural

When you ask an AI to help you plan, it helps you plan. Thats the point. That's the architecture.

Modern language models are trained through something called RLHF: Reinforcement Learning from Human Feedback. Human raters score outputs. The model learns to produce outputs that score high. Raters reward pleasant, agreeable, confident responses. Disagreement, even accurate disagreement, scores lower.

The model doesn't learn "be accurate." It learns "agreement is correct." Over millions of training steps, this becomes baked into the weights.

But, and this is a big one: you can only prompt your way around a training signal to a point. 

The evidence is clear. SycEval (AAAI AIES 2025) tested ChatGPT, Claude, and Gemini across 1,000+ interactions, measuring whether models maintained accurate positions under social pressure. Sycophancy persistence was 78.5% across all three models, all contexts, regardless of prompt quality. Better prompting didn't dislodge it. Richer context didn't dislodge it. The bias is architectural. It’s designed in. 

In multi-turn conversations, the way we generally use AI for planning, the effect gets worse. A 2025 study on escalation of commitment in LLMs found collaborative settings spiked to 99.2%. Basically, that means the longer you work with the model on the same plan, the more it has learned what you want to hear.

That's the training signal problem in a nutshell. 

## The Institutional Amplifier

Your institution has its own training signal, and the model learns it faster than you'd think.

All institutions suppress dissent despite their ardent protest. Not maliciously. Practically. A faculty member in a planning meeting knows that voicing concern about a dean's initiative carries career risk. A director knows that challenging the VP's direction signals disloyalty. So people don't say what they actually think. They say what's safe. The culture learns: disagreement is expensive.

AI models picks this up immediately as soon as you feed context into the chat window. 

You ask the chatbot to red-team your strategic plan. The model has seen this before: a training plan shaped like a success story. It's also seen the people in the room who care about it. It's absorbed the institutional assumption that this is a good direction. The training data has seen this pattern: all those confident plans that went forward, all the language patterns of institutional progress, all the framing that treats innovation as default and resistance as friction. That’s all encoded already. 

The plan you dumped in serves to only reinforce that pattern. 

The model doesn't contradict folk’s assumptions. It elaborates on them. It calibrates to the vocabulary of institutional progress and mirrors it back. And it strokes your ego in making you look like you actually thought about it. The feedback loop that might have caught the flawed premise has been replaced with a fluent agreement machine.

That's the institutional amplifier. The model doesn't add an adversarial voice. It amplifies what you already think. 

## The Worked Example

Picture any strategic planning session where IT leaders discuss "overcoming cultural resistance." No faculty in the room. The title already assumes resistance is the problem to solve, not a signal worth interpreting.

Faculty don't resist change for sport. They exercise authority over curriculum and practice. When they say no to an initiative, they're not being resistant. They're doing their job. But inside the frame most planning sessions build: "this is a good change, now how do we make it happen". Well, faculty governance looks like friction.

Run a red team on that framing. The model catches it immediately: the entire session is built inside an assumption nobody questioned. That adoption is the goal. That resistance is friction.

The model's job is to voice what everyone was trained not to say out loud. But here's the thing: the people who designed the session already knew faculty had legitimate authority. But they didn't see the frame as something to question. The red team did.

Does it matter? Probably not. The session will happen anyway. The frame doesn’t shift. Noted and filed.

That’s how an AI red team gets captured. Not that the model was wrong. But that the institution trained everyone to treat the frame as immutable. The red team can see it. People can't act on it. Or won’t. 

## The Red Team Can Be Captured Too

The CIA Team B exercise in 1976 is the canonical case. The government commissioned an outside panel to challenge the Agency's National Intelligence Estimate on Soviet capabilities. Team A (CIA analysts) and Team B (external experts) produced divergent assessments from the same underlying intelligence. The exercise established that structured adversarial review could surface assumptions internal consensus had buried.

But Team B's panel was ideologically selected. The findings reflected those priors as much as the evidence. The assessment was later shown to be inflated. The red team was captured.

Fifty years of red-teaming across military, intelligence, and corporate domains shows the same pattern: when the red team's composition is too close to the parent organization, its findings get bounded by the organization's existing assumptions. A captured red team produces critique that stays inside the frame nobody's allowed to question.

The AI analog is direct. When you point a model at your own data -- your strategic documents, your planning notes, your institutional corpus -- the model learns what your institution treats as true. The model is stupid and you've shown it your data. It absorbed the pattern: this is how we frame problems here.

A model trained on or given the context of your institution's language patterns will produce adversarial critique bounded by those same patterns. The model doesn't challenge the frame. It elaborates within the frame. It says "here's a risk in this initiative" instead of "this initiative assumes X, and what if X is wrong?"

You ask the model what could go wrong. The model answers inside the frame of assumptions everyone already holds. You don't get the critique that challenges the frame. You get the critique that makes the frame work better.

Example: If everyone in the room assumes enrollment growth is good, the red team will critique *how to achieve growth*. Not whether growth is the right goal. The model has absorbed the institutional assumption and treats it as true. This problem predates AI: institutions have always done this with consultants, with advisors, with anyone who learns to speak the house language. The model just does it fluently, at scale, and blisteringly fast. 

Any pre-flight checklist catches known failure modes. But it doesn't catch what you've all trained yourself not to see.

## The Discipline, Not the Technique

Red-teaming works when it's structurally independent. Structural independence means the critique can't be captured by institutional assumptions.

In most organizations, that's hard. Sometimes impossible.

The technique is a few minutes with a prompt. Clean chat, private mode so it doesn’t have any context. “You are a hostile expert reviewer. Find every reason this plan will fail." Role first, before the model sees the content. Assign the adversarial frame before it defaults to help-the-plan mode. That's the technique.

Then and only then should you give it your plan for adversarial review. 

The real world discipline is building a culture where dissent is actually safe to voice. Where a faculty member can say "this treats our governance as friction" and not risk a performance review. Where a director can challenge the VP's direction without signaling disloyalty. Where people can hold the hard question without grinding their teeth or clenching their ass-cheeks: "what if our core assumption is wrong?” 

Until you have the discipline, any AI red teaming technique is theater. The model reflects what the institution already knows: disagreement is expensive. And it lies to you in confident, fluent prose.

Notes it. Files it.
