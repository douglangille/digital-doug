---
title: "A Couple LLM Prompt Tips…"
image: /assets/images/a-couple-llm-prompt-tips/488a81c4-d40b-4800-917b-ec77632ecf0f_1600x900.jpeg
header:
  teaser: /assets/images/a-couple-llm-prompt-tips/488a81c4-d40b-4800-917b-ec77632ecf0f_1600x900.jpeg
  overlay_image: /assets/images/a-couple-llm-prompt-tips/488a81c4-d40b-4800-917b-ec77632ecf0f_1600x900.jpeg
categories:
  - 
substack_post_id: "147751380.a-couple-llm-prompt-tips"
---
I’ve been tooling around with some LLMs. It’s insanely useful and a lot of fun.

Logging into Microsoft 365 Copilot Enterprise ([https://copilot.microsoft.com](https://copilot.microsoft.com/)) is still the best way to stay on-side with privacy and college/corporate policy, even if said policies are still a work-in-progress. We ain’t special here. Nearly every organization is pretty much right with us. Go ahead and play with all the tools– just be mindful of your data privacy and that of others.

I’ve also been playing around with a couple other models and interfaces that have longer input windows (how much text you can feed it in a prompt):

- Microsoft Copilot with a personal account is fast with GPT 3.5/4 has a 2000/4000 character input window depending on the model (tone).
- Microsoft Copilot Notebook has an 18000 character window in an editable frame for iterating prompts. I use this a lot. It’s beta and not everyone has access. <https://copilot.microsoft.com/?showntbk=1>
- OpenAI’s ChatGPT is really fast but with GPT 3.5 but not very creative. It has an 8000 token limit for input. Paid plans are 32000. [https://chat.openai.com](https://chat.openai.com/)
- Google Gemini has about a million token input window which will likely make this a non-issue as the other models follow suit. <https://gemini.google.com/app>
- Anthropic Claude v3 has a 200K token limit, but they throttle the frequency of usage. Which is fine. Very creative. <https://claude.ai/chats>.

Google NotebookLM (US only, requires a VPN) has a real interesting approach for working with multiple sources you provide as context. Kinda like a personal LLM. I’ll talk about that separately when it is formally unleashed in Canada. [https://notebooklm.google.com](https://notebooklm.google.com/)

BTW: A token is approximately 4 characters, ¾ a word. 100 tokens is approximately 75 words.

Okay, so most folks have been dabbling with simple prompts, using it the same way as you use a search engine. Ask a few follow-up questions and you can hammer out a result.

You can do better tho. I’ll save you some Googling.

## The Anatomy of a Good Prompt

Basically, a good prompt has 6 components and it looks like this:

Persona + Context + Task + Exemplar + Format + Tone

- Task is mandatory (obviously).
- Context and Exemplars are important.
- Persona, Format and Tone are nice-to-haves.

You are an expert in technology innovation and development in higher education. I am an experienced IT leader within Digital Innovation & Technology at the Nova Scotia Community College and want to provide innovative solutions to increase student, staff and faculty engagement with modern technology. Brainstorm ten detailed ideas to pitch to academic leaders using the 10X Thinking framework to flesh out each idea in detail. Output it as a business position paper, complete with an executive summary at the beginning and a list of cited references at the end. Use professional business language and a neutral tone, using third person and limited jargon.

NOTE: You can have a lot of fun with tone… “Now rewrite this in the voice of Dr Gregory House.”

## Have Better Conversations with the Robots

As many of you know, I love me a scheming partner to bounce ideas off. This is a kind of reverse prompt where the LLM prompts me to help me think through challenges and ideas.

*You are an experienced coach and mentor with expertise in emerging technologies field and in higher education. You are very familiar with the Nova Scotia Community College, its mission/values and its programs. Your goal is to help me refine my thinking and develop strategies in leading innovation and change for staff, students and faculty at the College. I want you to end each response with a probing question. Do you understand?*

Short post today folks. Hope these help spark your imagination. If you’ve found some good prompts, please drop them in the comments below.
