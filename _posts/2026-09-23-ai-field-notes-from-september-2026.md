---
title: "AI Field Notes from September 2026"
date: 2026-09-23
image: /assets/images/ai-field-notes-from-september-2026/feature.png
header:
  teaser: /assets/images/ai-field-notes-from-september-2026/feature.png
  overlay_image: /assets/images/ai-field-notes-from-september-2026/feature.png
excerpt: "On Augure, Meta's Muse, and discovering it's Hermes all the way down."
tags: [personal, diagnostic]
entities: ["Cal Newport"]
meta: "Testing a Canadian sovereign AI tool and Meta's new consumer agent, Doug finds the same open-source engine running underneath both, with very different dashboards."
feature: /assets/images/ai-field-notes-from-september-2026/feature.png
---

# AI Field Notes from September 2026

I'm running a Mac without administrative rights, and when installing Augure Desktop, I was prompted to install a CUA (a Computer Use Assistant thingy) that required elevation. So I had to dig in. Actually, I had the agent itself dig in and troubleshoot itself, because I ain't got time for that shit. And it was quickly revealed that this was essentially a modified Hermes. I was expecting a Claude Cowork situation and got much more. I was taken aback.

Which is fine. No notes. Leveraging an existing open-source project is the right call for the Augure folks to make. It took some finagling to get the CUA working in userspace without giving up the farm, and as it is now, I've configured pretty strict read-only permissions on the minimum, but there's a lot of knobs and dials. Augure's command line tool is a command line tool, and the mobile tools are like every other chatbot.

For the last year or so, all of the dialogue has been around what came after chatbots, because we had chatbots for the first little while, and they did things. Then, about a year ago, we got into this whole coding harness framework thing (Claude Code, Claude Cowork, Codex, et al) where we figured out that these LLMs were actually good at coding and stuff. So we built harnesses around them so that way they would have memory and they could follow the plot and they could actually build and accumulate knowledge. The whole "second brain" gamut.

It was really good for knowledge work rather than just going and using a chat thread that had a finite context window. A coding harness in particular could keep notes as it went along. You could actually have a much longer conversation because you weren't trying to keep everything inside the chat thread itself. The agent, which is what you would talk about at this point as opposed to being a chatbot, would just keep checking the notes and refreshing itself and modifying accordingly. And that's where this whole idea of a God thread comes from: one thread to rule them all. Whereas in the old chatbot era, we had to save the context and reload a fresh chat to continue going. We would always end up having to start new chats all the time. But now with these coding harnesses, and the ones that are more tied to the productivity space, like Claude Cowork, we get this new thing: persistent context.

And now there's this other twist. Just a few months ago, we had this whole Clawdbot thing that eventually became OpenClaw and now Hermes is a thing: people are setting up these essentially coding harnesses and agents in a way to run them 24/7. They set up a MEMORY.md file to keep notes with itself, a USER.md about the human, and a SOUL.md about how the agent would behave. And then, of course, there would be the AGENTS.md, which governs its actual rules. People now can run semi-autonomously so they started giving them access to their other digital tools that impact "meat space". And that's when shit started getting scary. Running with scissors stuff.

Anyway. Where were we? Right: Augure.

So when I first looked at Augure, it was essentially as a Canadian replacement for what I was using Claude Code and Cowork for (a web tool as well).

The TL;DR is that it's a Canadian-hosted version of some post-trained models (probably Llama), at least the Tofino and Ossington ones are. The new Rosedale One is based on GLM 5. The post-training is about multilingual stuff as well as Canadian legal standards and all that jazz. The attractiveness for me is that it's sovereign.

And now, as of last week, we have this brand new consumer-facing thing from the mad engineers at Meta: Muse.

What's exciting about Muse is that it's actually a significant departure that none of the other big players are doing. Google AI Mode and Gemini don't do this. ChatGPT doesn't do this. And nothing in the Claude stack does this. But essentially, Meta, has been the first "big boy" to market with a consumer-facing 24/7, always-on personal assistant agent. 

Grok Bot is a thing too, but we don't talk about Grok here. 

Anyway, Muse is not a chatbot. It looks like a chatbot, but it is not. It is a 24/7 agent that can act in this world (well, with whatever you give it, anyway). I've been playing with Muse for the last few days and lo-and-behold, it's also just Hermes underneath.

Which means we can compare things.

Augure's desktop tool is like flying a helicopter. There's a lot of controls exposed to you, and the learning curve is fairly steep. It's a power user toolkit. Most normies will have to rely on the mobile tools or the website to get a more expected chatbot experience. Augure Desktop is not the same as Claude Cowork. Straight up.

But Meta's Muse by contrast, is so damned friendly and polished and clean that you would never know that behind the scenes it is extremely complex. It's friendly enough that your boomer gramma could use it. No joke. However, in order for Muse to be truly useful, you have to give it everything: the more access you give it, the better the tool responds. It's very much like a personal assistant. Meta gives you a cute little avatar you can customize and make your buddy, and you can wire it up to your mail, your calendar, your bank account. Don't do that. It can act as if it was you in the real world. That's genuinely useful, so long as you trust Meta to take care of your data. To Facebook's entrepreneurial credit, I can see how Muse can be ridiculously addictive. It's actually their best product in years, if the goal is to hook all your users on the new drug of choice.

And like Cal Newport says: these models aren't really that good, or haven't really improved that much in the last couple of years. They've made incremental improvements. The hype is off the charts. But what has changed in the last year or so in particular is the harnesses that are built around them have matured greatly, which is why we're seeing these agentic OS contraptions bubbling up.

It's been a really weird summer: all kinds of AI breakout events getting highly publicized, both for the benefit of AI companies looking for IPOs and also to stoke the flames of the doomers. I don't know what the average P-doom is, but here we are. The conversation around AI safety is starting to increase, but this AI safety stuff is really very much talking about how things are trained and how they're being used at scale. But no one's really talking as much about the other side of AI safety, like we talked about a year ago, people using AI in the Joaquin Phoenix kind of way and pathologically addicted to it. There are real social harms to using these tools all the time, making it a weird time for Facebook to release Muse.

I get the push to move towards these more immersive agentic tools, everybody trying to find a way to monetize and come up with an actual product that people want. And let me be clear, no one actually was asking for this stuff. 

For the most part, tools like Claude Code and Codex and stuff like that, the only real killer feature is actually in the programming and code development. All of the other stuff around knowledge work is YMMV territory. 

I certainly get a lot of value from a knowledge work perspective, being able to use the tools as a research assist and as a way to structure and edit my own work, though I spend quite a bit of hand-wringing and navel-gazing over what authorship looks like when AI tools are involved. I think I'm getting it figured out. 

As a raw productivity tool, it's normal technology. 

But when you look at stuff like Muse, this isn't normal. This is something else.

It's pretty muddy. Some is political, some is ethical. We all have our lines. I tend to take a managed-risk approach, the whole shadow-profile thing, but I really don't like the trite line that "people who have nothing to hide, hide nothing." And yes, it's about data brokering to advertising firms and other sentiment analysis, but criminal activity is real too: what's leaked can be used for spear-phishing, catfishing, pig-butchering, even straight-up fraud. 

Maybe the approach is to only trust the big guys, since they have security and IT departments bigger than most companies. It's kind of a gross feeling and I just threw up in my mouth a little bit, but sometimes too big to screw up is enough of a motivator. So who do I trust to protect my data more: Facebook or MyFitnessPal? Neither is the right answer. But knife to the throat, I probably trust Facebook and Google more than the smaller outfits.

There's no tidy answer or helpful "Doug recommends X" here. It's just that folks should educate themselves, follow the money, and manage their risk. Also trust your gut: if you don't trust Facebook to purchase stuff on your behalf, don't give them your credit card. However, if you're already in the Google Fitbit / Apple Watch ecosystem, what difference does it make that you give your fitness data to Meta Muse so your friendly little buddy can coach you along, and creep your wall, and silently judge your food pics on Insta.

All that said, I'm still going to use and continue to experiment with Augure because for my real work, thinking in sovereign terms is very compelling to me. But at the same time, I'm going to continue to play with Muse because it is a novel Bright Shiny Object (BSO) and my brain won't let me ignore it. It is indeed interesting and something that I think that a lot of people are going to pick up and not think twice about what they're actually doing.
