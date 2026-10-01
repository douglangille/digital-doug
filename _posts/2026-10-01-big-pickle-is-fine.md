---
title: "Big Pickle Is Fine"
date: 2026-10-01
image: /assets/images/free-agent-stack/feature.png
header:
  teaser: /assets/images/free-agent-stack/feature.png
  overlay_image: /assets/images/free-agent-stack/feature.png
excerpt: "You don't need a chainsaw to carve a roast."
tags: [personal, prescriptive]
entities: ["Tiago Forte"]
meta: "Doug argues a free OpenCode model pointed at an Obsidian vault gets most second-brain users most of the way there, no subscription needed."
feature: /assets/images/free-agent-stack/feature.png
---

# Big Pickle Is Fine

My algorithm feeds are chock full of AI junk that falls in two camps: 

1. The Anti-AI Army who hate this stuff and grasp on to any and every reason to reject the technology, even if that means siding with conspiracy theorists and fallacious argument. There's truth in a lot of it, but there's also a lot of crackpot BS.
2. The AI-pilled who seem to want to foist this tech on everyone else, citing its inevitability as the reason to be first. The premise is somewhere between suspect and false and it's sending folks down garden paths and dangerous places.

And then there are the pragmatists. They see the potential value of the tools, hate the industry and its [weird-ass philosophies](https://en.wikipedia.org/wiki/Effective_altruism), but... Don't want to be left behind in an economy that's shifting.

Somewhere in there is a group of people who want to do the whole Tiago Forte "second brain" thing with [Obsidian](https://obsidian.md), but do not want to commit to a subscription tool like Claude Code or OpenAI Codex or anything like that. They want something a little more free-ish. The good news is I think these folks could get away with using OpenCode and its free model toolkit pointed at Obsidian. You can get most of the way there without spending a dime.

I make no bones about [fan-girling over Obsidian and Markdown](https://digital.douglangille.ca/app-apocalypse-starter-kit/) as a note-taking app and durable file format. I wrote about this a couple weeks ago. But the short version is that you point the app (Obsidian) at a folder on your computer that has your notes in human-readable formatted (Markdown) plain text files. Okay, great, we have a folder full of plain text notes, but what do you do with it when you want to use AI with these files? 

So, this is what we're doing. We are going to point the robots at your notes. Specifically we're talking about [OpenCode](https://opencode.ai).

You can think of OpenCode as like an open source alternative to Claude Cowork/Code or ChatGPT Work/Codex. There's a desktop app and then there's a terminal application. You can use whatever makes sense for you. You'll get similar results. The big difference between what you see in OpenCode versus the Big Boys is the model choice. For example, with Claude, you're basically tied to Anthropic's models. With OpenCode, you can use any number of model providers. Sure, Claude might be a more mature tool, but to be honest, OpenCode is more than adequate for nearly every one of my use cases.

OpenCode pays the bills with paid services Zen and Go. The models offered are vetted to work well with OpenCode and is price competitive.

If you really don't want to spend a dime, the OpenCode project includes a handful of free Zen models they make available without a subscription.

I've tried and tested a slew of the other free-ish offerings and I won't bore you with the sad journey, but haven't found anything better. I even tried hosting a local model on my own hardware, but my computer isn't beefy enough to do such, and the price of hardware these days makes it cost prohibitive. I have better things to spend $5,000 on.

The biggest complaint and objection about using free models is that they collect some of your data, your inputs and your outputs, and send them back to the mothership to train future models or to do future post-training.

The whole idea of worrying about your outputs and inputs being used for training data is the wrong lens. You can choose what context you give it. If you are giving the AI personal information, your hopes and dreams and stuff like that, then maybe you should think about that. You should think about your social media use too, for the same reason. Jussayin. I find it so weird that folks are wigged out about their AI chats being used for product improvement while feeding the TikTok and Insta algorithms like a bunch of apple-drunk squirrels on an acorn bender. 

Use the tools, but treat them like postcards. I wouldn't put anything there that you wouldn't want to be used to embarrass you somewhere in the future. The risk isn't training data. It never was. The likelihood that the next-token predictor is going to spit out a string of an individual's personal deets has always been implausibly small. It's non-zero, but it's not the risk I'd lose sleep over.

The real risk is when you give these things unrestricted access to your computer. That's the threat vector.

That and your work data. And personally identifiable information. Follow your employer's AI usage and data handling policies. 

You finish getting your Obsidian vault set up, and you make that first file: your `about-me` file: how you think, what you do, what is important to you and what isn't, how you work, what good looks like. Don't get fancy. Bullets are fine. Dictating a ramble into the file is also fine.

Then go to the [OpenCode website and download the app](https://opencode.ai/download). There's instructions for Windows or Mac or Linux or whatever you happen to be using. I like the Terminal app, but the Desktop app is great too. Six of one, half dozen the other.

When you fire it up, point OpenCode only at the folder where you have your Obsidian notes. If you're feeling extra cautious, make an AI-only folder inside Obsidian and point the OpenCode agent at it. It's best practice even once you get more miles under your belt and know what you're doing.

It will ask you if it needs to traverse outside of that folder before it does anything else. If you say yes, it can definitely run low-level commands for you without asking again (that's the point). And all of those shell commands can do pretty dangerous things. There's caps on the scissors most of the time, but you can take them off and then go running gleefully and delete all your precious notes. So maybe make a backup once in a while. You do backups right? 

Once you have an agent chat session open pointed at that directory, you're actually good to start. The default model is the free OpenCode Zen model: Big Pickle. If you're in a rush go ahead and configure a provider and pick a model with the opencode `/connect` and `/models` commands.

We'll come back to models in a bit.

Your first prompt in OpenCode in your Obsidian vault should look something like this: 

```
You're in an Obsidian Vault. read the about-me file to get started. Your goal is to setup Obsidian as a space for both the human and the agent to work together. Interview the user with smart one at a time questions, starting with the biggest decisions first. The user's answers will direct your questioning, but remain on task. If you are unsure, ask the user. Do not make assumptions and push back as needed. When you are 100% confident you have a full understanding of the requirements, present the plan to the user. The user approves the final plan before you implement.
```

The agent will ask you some questions about who you are and how you'd like to work if you haven't answered them already. And then it will propose the structure. And you can tweak it. And you can go edit the files yourself, because they're just your text files. You can see everything.

There are a gazillion frameworks for this, and you can watch 17,000 YouTube videos about how to set up a Second Brain in Obsidian. Don't fall for the trap. None of it really matters. None of the systems on YouTube are *your* system. The takeaway idea is: don't try and build this yourself. This is good work for a robot to do.

Now, about models.

One way to think about it is the model is an engine of a car and the harness is the steering wheel, the transmission, the drivetrain, the body. An engine by itself doesn't do much. You have to put it in something for it to do anything useful. And hopefully the human is driving the goddamn thing with enough coffee on board to keep it between the mustard and the mayo.

* ChatGPT is the harness. GPT-5.6 is the model.
* Claude Code is the harness. Sonnet 5.5 is the model. 
* OpenCode is the harness. Big Pickle is the default model.

Despite the name "code" peppered on all these products, I actually do precious little coding. Most of my AI time is working with documents, data and content. And it's become very clear that, over the last year especially, the model choice has very little to do with the quality of the output.

"New & Improved" doesn't mean the previous model is "Old & Inadequate".

It's not the models that do the fancy stuff anyway, it's the harness itself that takes action. Your skill in using them matters. You'd be surprised how far you can get if you slow down and stop treating these things like magic black boxes where you say: "Create this awesome thing. Make no mistakes."

What makes a harness better? If it has a model that does reasoning, can search the web, and a way to manage the context window.

Context window?

No worries. I got you.

So a context window is essentially how much of the conversation, both the input and the output and the thinking, that the model can keep in its head via the harness at any given time. Bigger is better but only to a point. Some models have a million token context window, but in practical terms you can only use half of it before it starts forgetting stuff in the middle. Don't get sucked into the spec bullshit because what's advertised ain't always reality. The heuristic that I find useful is to keep it under 500K for a million token model. And when you only have a 200K model, keep it to 100. Anything after that, it starts to get mushy.

All the newer harnesses can show you a percentage of the context window in use. 

The fact that they can save the keeper outputs to a file to reuse as inputs helps dramatically. This is what makes these agent tools better than pure chatbots.

I continue to be really surprised at how well the lesser known models perform. Even the slate of free models in OpenCode are fine for almost all of the work you're doing. If you're getting it to read an article and summarize it for you, or getting it to edit notes you made in Obsidian, Big Pickle is good. You don't need a chainsaw to carve a roast.

Now, if you want it to write for you based on an outline you developed with a free model, then you _might_ want a better model. But you probably shouldn't. Get the model to help you build the outline. Help you test the facts and check the web, search for things, verify what's going on, do all of that skeleton work. And then once you have a good skeleton, go write the damn thing yourself based on the prep. 

At least then it's better work, in your words, and the Anti-AI Army might leave you alone.
