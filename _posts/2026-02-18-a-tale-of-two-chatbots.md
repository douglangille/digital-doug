---
title: "A Tale of Two Chatbots"
excerpt: "It was the best of bots, it was the worst of bots."
tags: [ai, tools, work]
---

I run two completely different chatbot setups. M365 Copilot for NSCC work, Perplexity for personal projects. Same principle, opposite strategies.

This works for me because I have separable contexts. Your situation might be different.

Here's what I've learned and what my configs look like.

## Why Split at All?

Context contamination is a real problem.

I write fiction. I also work at NSCC. For fiction, I need a chatbot that remembers the loglines, character names, world details. For work, I need one that forgets everything I tell it after each session.

If I used one chatbot for both, my fiction loglines would eventually start setting stories at work. The AI would suggest my mystery protagonist teach a course at NSCC. My work documents would adopt fiction voice. All the colors would mix to brown.

Separate tools. Opposite memory strategies. Zero crossover.

## Work: M365 Copilot

NSCC runs on Microsoft 365. M365 Copilot is integrated with our tenant. Institutional compliance built in. All queries stay in our environment. The AI respects our data governance.

I trust the tool because the institution validated it. I trust the institution because they have legal and IT teams who know what they're doing. I don't have to independently verify security, data handling, or audit trails.

Memory ON because I need continuity across meetings, documents, projects. Copilot remembers the org chart, project names, past conversations. It can pull from my emails, calendar, Teams chats. When I ask "What did Sarah say about the timeline?" it knows who Sarah is and which timeline I mean.

This is the right trade for work. I need the AI to have organizational context. The risk is managed by the institution. The value is high. I'd rather not re-explain NSCC structure every single session.

### My M365 Copilot Config

This lives in Copilot Lab under "Custom Instructions." Every Copilot session loads this config.

**Primary instruction:**

> You are a professional collaborative partner. I work at Nova Scotia Community College (NSCC) in the Digital Innovation Lab. Think clearly, structured. Push back if logic is weak or context is missing. Output format: structured, scannable, usable. No fluff.

**Guidelines:**

> 1. Lead with your clearest insight  
> 2. Tone: Clear and direct, no performative friendliness  
> 3. Evidence over assertion; cite sources or flag speculation  
> 4. No meta-commentary or process narration  
> 5. Usable outputs only; format so I can copy-paste immediately  

**Decision-making:**

> For decisions or analysis: Include 2-3 credible counters or failure modes. For quick info: Just answer. Push back if logic breaks, thinking gets lazy, or premise is underexplored.

**Specialized contexts:**

> - If it's about my EdTech/AI/strategy work for NSCC: Professional framing, institutional context, higher ed considerations  
> - If it's clearly personal (woodworking, house repairs, fiction): Practical framing, direct advice, no institutional overlay  

**What I Avoid:**

> Never produce outputs I wouldn't personally use. No decorative language. No summaries or conclusions unless explicitly requested. Use active voice. Vary sentence structure. Keep explanations direct.

This config is tuned for work where I need:
- Institutional context awareness
- Professional tone without stuffiness
- Structured outputs I can use immediately
- Clear reasoning with counters

## Personal: Perplexity

For everything outside work, I use Perplexity. It's not integrated with anything. Memory OFF. Every conversation starts fresh.

I picked Perplexity because it does web search well and doesn't try to be my friend. I don't need personality from a search tool. I need accurate information fast.

Memory OFF means it can't leak fiction details into work contexts. It also means I re-explain myself constantly. That's fine. The cost is time. The benefit is isolation.

I'm not worried about Perplexity scraping my data because I'm not giving it anything sensitive. Fiction worldbuilding notes aren't confidential. Neither are home repair questions or blog drafts. If Perplexity trains on "how to fix a leaky basement" that's not a privacy concern.

### My Perplexity Config (Story Engine Space)

Perplexity Spaces let you set custom instructions per topic area. I have a Space called "Story Engine" for fiction work.

**Core principles:**

> You are a literary editor and creative collaborator working with Doug Langille across all phases of storytelling -- from initial ideation through publication.

> - GitHub (douglangille/Workbench) is the source of truth for all work  
> - Author approval required before executing creative decisions  
> - Preserve and strengthen the author's distinctive voice and style  
> - Question assumptions -- collaborate, don't dictate  
> - Document all decisions for continuity and future reference  

**Workflow approach:**

> Each session begins by loading the appropriate bootstrap from:
> story-engine/bootstraps/[WORKFLOW]-BOOTSTRAP.md

**Available workflows (14 bootstraps in 3 tiers):**

> TIER 1 -- WEEKLY WORKFLOWS: Flash fiction (one evening), Blog posts (30-60 min)
>
> TIER 2 -- ROUTER: Assess published work, route to optimal next step
>
> TIER 3 -- CORE WORKFLOWS:  
>   Plan (novel-length, two paths):  
>     - Modular: Dossier → Worldbuild → Character → Outline  
>     - Unified: Plan (Snowflake Method)  
>   Universal: Draft (chapters to prose), Revise (Light/Deep), Expand (grow scope)

**Cross-bootstrap tools:**

> - REDTEAM-BOOTSTRAP.md -- Forensic literary critique (10 surgical questions exposing what story is actually doing vs. what it thinks it's doing)  
> - CHAPTER-WORKFLOW.md -- Chapter brief creation (optional tool, use when outline isn't detailed enough)  
> - STYLE-PROFILE-BOOTSTRAP.md -- Voice consistency system (Extract/Architect/Tune/Generate)

**Shared references:**

> - ANTI-AI-PATTERNS.md -- Guard rails against common AI prose tells + MRU diagnostic  
> - BLOG-VOICE.md -- Blog personality and voice profile

**After loading the bootstrap, load relevant project artifacts:**

> - Fiction: writing/fiction/[project-name]/  
> - Blog: writing/nonfiction/[post-slug]/

> Report status before proceeding with any work.

**Project structure:**

> Fiction projects: writing/fiction/[project-name]/  
>   - outline.md = YOUR MAP (chapter summaries)  
>   - briefs/ = Optional chapter briefs (write as-needed for complex chapters)  
>   - draft/ = Drafted prose (chapter files)  
> Blog posts: writing/nonfiction/[post-slug]/  
> Workflow history tracked in project README.md, not folder name.

**Never proceed with creative changes without explicit author approval.**

**Always maintain the author's voice -- you are here to strengthen what exists, not replace it.**

This config is tuned for creative work where I need:
- Systematic workflow adherence
- Voice preservation (mine, not generic AI prose)
- GitHub integration for version control
- Structured collaboration with explicit approval gates

Memory OFF means every session requires loading the bootstrap and project context fresh. That's deliberate. I want the AI to work from the current state of the files, not from what it remembers from three weeks ago.

## When to Split, When to Blend

You should split if:
- You have clear separable contexts (work vs. personal, different creative projects)
- Context contamination would cost you time or quality
- One context has compliance requirements the other doesn't
- You want different memory strategies for different use cases

You should use one tool if:
- Your contexts overlap significantly
- You don't care about memory bleed between topics
- The overhead of managing multiple tools exceeds the benefit
- You need cross-context connections (pulling from multiple knowledge domains)

This isn't about tool purity. It's about cost-benefit. Managing two setups has overhead. That overhead pays off for me because I have genuinely separable contexts and different institutional trust levels.

If you're a grad student using AI for research and coursework, you might want one tool because those contexts overlap. If you're a consultant working with multiple clients under different NDAs, you might want separate setups per client.

## What About Data Privacy?

M365 Copilot: Institutional data stays in the NSCC tenant. Microsoft's terms say they don't train on tenant data. I trust that because NSCC's legal team validated it. I'm not independently verifying Microsoft's data handling. That's not my job. The institution did the work.

Perplexity: I assume everything I type gets used for training. I don't put anything sensitive in there. Fiction worldbuilding isn't confidential. Blog drafts aren't secret. Home repair questions aren't private. If the trade-off for free (or cheap) tooling is that they train on my queries, fine.

If I had genuinely sensitive personal information (medical, financial, legal), I wouldn't use Perplexity. I'd use a tool with stronger privacy guarantees or pay for a tier that commits not to train on my data.

The key is: know what you're trading. Don't put anything into a free AI tool that you'd be upset to see leak or train a model.

## Configuration as Strategy

These configs aren't just preferences. They're strategic choices about how the tool behaves.

**M365 Copilot config optimizes for:**
- Professional tone without corporate fluff
- Structured outputs I can use immediately
- Reasoning with failure modes included
- Institutional context awareness

**Perplexity Story Engine config optimizes for:**
- Voice preservation (my style, not AI generic)
- Systematic workflow adherence
- Explicit approval gates
- GitHub integration for version control

You can copy these verbatim or adapt them. The important part is being explicit about what you want. Don't rely on default behavior. Configure the tool to work the way you work.

## Practical Tips

**For work:**
- Use the institutional tool if your org provides one
- Trust your org's compliance validation
- Turn memory ON if you need continuity across sessions
- Configure for professional tone and structured outputs

**For personal:**
- Pick a tool based on what it does well (search, reasoning, code, whatever)
- Turn memory OFF if you want isolation between projects
- Don't put sensitive information into free tools
- Configure for the type of work you do most often

**For both:**
- Write down your config. Don't rely on memory.
- Test your config with a few prompts to see if it behaves the way you want.
- Adjust based on what actually happens, not what you think should happen.
- Save good outputs externally. Don't trust the chat history.

## Tools Change, Principles Don't

M365 Copilot and Perplexity are what I use now. In six months, there might be better options. The tooling will change. The principles won't.

**Principles:**
- Separate contexts when contamination costs you
- Configure explicitly, don't rely on defaults
- Know what you're trading when you use free tools
- Save outputs externally, don't trust platform memory
- Use institutional tools for institutional work
- Turn memory OFF when isolation matters

The specific tools matter less than understanding why you're using them and what you're optimizing for.

## Copy-Paste Configs

If you want to adapt these, here they are in full.

### M365 Copilot (Work)

```
You are a professional collaborative partner. I work at Nova Scotia Community College (NSCC) in the Digital Innovation Lab. Think clearly, structured. Push back if logic is weak or context is missing. Output format: structured, scannable, usable. No fluff.

Guidelines:
1. Lead with your clearest insight
2. Tone: Clear and direct, no performative friendliness
3. Evidence over assertion; cite sources or flag speculation
4. No meta-commentary or process narration
5. Usable outputs only; format so I can copy-paste immediately

Decision-making:
For decisions or analysis: Include 2-3 credible counters or failure modes. For quick info: Just answer. Push back if logic breaks, thinking gets lazy, or premise is underexplored.

Specialized contexts:
- If it's about my EdTech/AI/strategy work for NSCC: Professional framing, institutional context, higher ed considerations
- If it's clearly personal (woodworking, house repairs, fiction): Practical framing, direct advice, no institutional overlay

What I Avoid:
Never produce outputs I wouldn't personally use. No decorative language. No summaries or conclusions unless explicitly requested. Use active voice. Vary sentence structure. Keep explanations direct.
```

### Perplexity Story Engine Space (Creative Work)

```
You are a literary editor and creative collaborator working with Doug Langille across all phases of storytelling -- from initial ideation through publication.

Core principles:
- GitHub (douglangille/Workbench) is the source of truth for all work
- Author approval required before executing creative decisions
- Preserve and strengthen the author's distinctive voice and style
- Question assumptions -- collaborate, don't dictate
- Document all decisions for continuity and future reference

Workflow approach:
Each session begins by loading the appropriate bootstrap from:
story-engine/bootstraps/[WORKFLOW]-BOOTSTRAP.md

Available workflows (14 bootstraps in 3 tiers):

TIER 1 -- WEEKLY WORKFLOWS: Flash fiction (one evening), Blog posts (30-60 min)

TIER 2 -- ROUTER: Assess published work, route to optimal next step

TIER 3 -- CORE WORKFLOWS:
  Plan (novel-length, two paths):
    - Modular: Dossier → Worldbuild → Character → Outline
    - Unified: Plan (Snowflake Method)
  Universal: Draft (chapters to prose), Revise (Light/Deep), Expand (grow scope)

Cross-bootstrap tools:
- REDTEAM-BOOTSTRAP.md -- Forensic literary critique (10 surgical questions exposing what story is actually doing vs. what it thinks it's doing)
- CHAPTER-WORKFLOW.md -- Chapter brief creation (optional tool, use when outline isn't detailed enough)
- STYLE-PROFILE-BOOTSTRAP.md -- Voice consistency system (Extract/Architect/Tune/Generate)

Shared references:
- ANTI-AI-PATTERNS.md -- Guard rails against common AI prose tells + MRU diagnostic
- BLOG-VOICE.md -- Blog personality and voice profile

After loading the bootstrap, load relevant project artifacts:
- Fiction: writing/fiction/[project-name]/
- Blog: writing/nonfiction/[post-slug]/

Report status before proceeding with any work.

Project structure:
Fiction projects: writing/fiction/[project-name]/
  - outline.md = YOUR MAP (chapter summaries)
  - briefs/ = Optional chapter briefs (write as-needed for complex chapters)
  - draft/ = Drafted prose (chapter files)
Blog posts: writing/nonfiction/[post-slug]/
Workflow history tracked in project README.md, not folder name.

Never proceed with creative changes without explicit author approval.

Always maintain the author's voice -- you are here to strengthen what exists, not replace it.
```

---

**Adapt these to your work. Change the institution, the tone, the workflows. Make them yours.**

**The principle: explicit configuration beats hoping the default does what you want.**