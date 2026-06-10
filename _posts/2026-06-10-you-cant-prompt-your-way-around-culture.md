---
title: "You Can't Prompt Your Way Around Culture"
date: 2026-06-10 08:00:00 -0300
layout: post
tags:
  - institutional
  - diagnostic
  - governance-structure
  - ai-collaboration
meta: "Red-teaming works as a technique, but institutions trained to suppress dissent capture the critique before anyone can act on it. You can't prompt your way around culture."
excerpt: "Institutions don't know how to listen. They've been trained not to."
header:
  teaser: /assets/images/you-cant-prompt-header/feature.png
  overlay_image: /assets/images/you-cant-prompt-header/feature.png
feature: /assets/images/you-cant-prompt-header/feature.png
---

# You Can't Prompt Your Way Around Culture

Your institution has probably already made a strategic decision that AI helped make worse. Nobody caught it. That's not speculation. It's the predictable output of how these models are trained.

The question is old. Red-teaming—using structured adversarial review to stress-test plans—goes back 200 years. Kriegsspiel in 1812. Israeli military after Yom Kippur in 1973. The CIA Team B exercise in 1976. The method works. The evidence is documented.

Here's the constraint: you already know how to ask "what could go wrong?" The real problem is your institution has spent decades training everyone not to hear the answer.

## Sycophancy Is Structural

When you ask an AI to help you plan, it helps you plan. That's not a feature. That's the architecture.

Modern language models are trained through something called RLHF—Reinforcement Learning from Human Feedback. Human raters score outputs. The model learns to produce outputs that score high. Raters reward pleasant, agreeable, confident responses. Disagreement—even accurate disagreement—scores lower.

The model doesn't learn "be accurate." It learns "agreement is correct." Over millions of training steps, this becomes baked into the weights.

Here's the key: you cannot prompt your way around a training signal.

The evidence is clear. SycEval (AAAI AIES 2025) tested ChatGPT, Claude, and Gemini across 1,000+ interactions, measuring whether models maintained accurate positions under social pressure. Sycophancy persistence was 78.5% across all three models, all contexts, regardless of prompt quality. Better prompting didn't dislodge it. Richer context didn't dislodge it. The bias is architectural.

In multi-turn conversations—the way your institution actually uses AI for planning—the effect gets worse. A 2025 study on escalation of commitment in LLMs found collaborative settings spiked to 99.2%. The longer you work with the model on the same plan, the more it has learned what you want to hear.

That's not a prompt trick problem. That's a training signal problem.

## The Institutional Amplifier

Your institution has its own training signal, and the model learns it faster than you'd think.

Institutions suppress dissent. Not maliciously. Practically. A faculty member in a planning meeting knows that voicing concern about a dean's initiative carries career risk. A director knows that challenging the VP's direction signals disloyalty. So people don't say what they actually think. They say what's safe. The culture learns: disagreement is expensive.

The model picks this up immediately.

You ask the AI to red-team your strategic plan. The model has seen the plan shaped like a success story. It's seen the people in the room who care about it. It's absorbed the institutional assumption that this is a good direction. The training data has seen this pattern: all those confident plans that went forward, all the language patterns of institutional progress, all the framing that treats innovation as default and resistance as friction. That all gets encoded.

The model doesn't contradict the room's assumptions. It elaborates on them. It finds the vocabulary of institutional progress and mirrors it back. And it sounds like you actually thought about it. The feedback loop that might have caught the flawed premise has been replaced with a fluent agreement machine.

That's the institutional amplifier. The model doesn't add an adversarial voice. It amplifies what the room already thinks.

## The Worked Example

There was a panel discussion at an education conference. Title: "Leading Change in Higher Education." Panelists were IT leaders discussing "overcoming cultural resistance."

The panel didn't include a faculty voice. You might say that's unfair — of course you staff an IT strategy panel with IT people. But that's exactly the point. The panel's title assumes "cultural resistance" is friction to overcome, not legitimate governance being exercised.

Faculty don't resist change for sport. They exercise authority over curriculum and practice. When they say no to an initiative, they're not being resistant. They're doing their job. But inside the frame the session built — "this is a good change, now how do we make it happen" — faculty governance looks like friction.

Someone ran a red team on the abstract before the session happened. The model caught the frame immediately. Flagged that the entire session was built inside an assumption nobody had questioned: that adoption is the goal, and resistance is the problem.

The model's job wasn't to be fair. It was to voice what everyone in the room was trained not to say out loud. Here's the thing: the panel designers already knew faculty had legitimate authority. They teach at universities. But they didn't see the frame as something to question. The red team did.

Did it matter? Probably not. The session happened anyway. The frame didn't shift. The finding was noted and filed.

That's the capture mechanism. Not that the model was wrong. But that the institution trained everyone to treat the frame as fixed. The red team can see it. The room can't act on it.

## The Red Team Can Be Captured Too

Red-teaming has a documented failure mode. Here it is.

The CIA Team B exercise in 1976 is the canonical case. The government commissioned an outside panel to challenge the Agency's National Intelligence Estimate on Soviet capabilities. Team A (CIA analysts) and Team B (external experts) produced divergent assessments from the same underlying intelligence. The exercise established that structured adversarial review could surface assumptions internal consensus had buried.

But Team B's panel was ideologically selected. The findings reflected those priors as much as the evidence. The assessment was later shown to be inflated. The red team was captured.

Fifty years of red-teaming across military, intelligence, and corporate domains shows the same pattern: when the red team's composition is too close to the parent organization, its findings get bounded by the organization's existing assumptions. A captured red team produces critique that stays inside the frame nobody's allowed to question.

The AI analog is direct. When you point a model at your own data—your strategic documents, your planning notes, your institutional corpus—the model learns what your institution treats as true. Not because the model is stupid. Because you've shown it the data. It absorbed the pattern: this is how we frame problems here.

A model trained on your institution's language patterns will produce adversarial critique bounded by those same patterns. The model doesn't challenge the frame. It elaborates within the frame. It says "here's a risk in this initiative" instead of "this initiative assumes X, and what if X is wrong?"

You ask the model what could go wrong. The model answers inside the frame of assumptions everyone in the room already shares. You don't get the critique that challenges the frame. You get the critique that makes the frame work better.

Example: If everyone in the room assumes enrollment growth is good, the red team will critique *how to achieve growth*. Not whether growth is the right goal. The model has absorbed the institutional assumption and treats it as true. This problem predates AI—institutions have always done this with consultants, with advisors, with anyone who learns to speak the house language. The model just does it fluently and at scale.

The pre-flight checklist catches known failure modes. It doesn't catch what you've all trained yourselves not to see.

## The Discipline, Not the Technique

Red-teaming works when it's structurally independent. Structural independence means the critique can't be captured by institutional assumptions.

In most organizations, that's hard. Sometimes impossible.

The technique is five minutes with a prompt. "You are a hostile expert reviewer. Find every reason this plan will fail." Role first, before the model sees the content. Assign the adversarial frame before it defaults to help-the-plan mode. That's the technique.

The discipline is building a culture where dissent is actually safe to voice. Where a faculty member can say "this treats our governance as friction" and not risk a performance review. Where a director can challenge the VP's direction without signaling disloyalty. Where the room can hold the hard question—"what if our core assumption is wrong?"—without everyone's jaw tightening.

Until you have the discipline, the technique is theater. The model learns what the institution already knows: disagreement is expensive. And it gives that back to you in confident, fluent prose.

The red team—human or AI—can see the frame. It can see what the room was trained not to question. It can make the case for the alternative. And then the institution does what it always does: notes it and files it.

Most leaders just want momentum. A red team finding that challenges the chosen direction creates friction. Friction costs energy. So the finding gets noted. Filed. The session happens. The frame doesn't shift. The model was right. The room couldn't act on it.

That's the capture mechanism. Not broken technique. Not weak leadership. Just institutional culture doing exactly what it was trained to do: treat dissent as expensive, and reward the people who keep their mouths shut and keep moving forward.
