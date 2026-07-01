---
title: Elbows Up and AI
excerpt: What the Fable 5 shutdown actually taught me about digital sovereignty, and why "buy Canadian" is messier than the slogan.
header:
  teaser: /assets/images/elbows-up-and-ai/feature.png
  overlay_image: /assets/images/elbows-up-and-ai/feature.png
tags:
- institutional
- diagnostic
- governance-structure
- technical-infrastructure
- ai-collaboration
entities: []
meta: The essay argues that Canadian AI-sovereignty anxiety conflates fear of the technology with fear of American jurisdiction, and that corporate structure, not server location, is what actually determines sovereignty.
feature: /assets/images/elbows-up-and-ai/feature.png
---

# Elbows Up and AI

Early June, I was at AUCTC running two AI sessions. One on red-teaming, one on AI literacy. During the red-teaming demo I pulled up Fable 5 for the first time, mostly to show people how a frontier model handles an adversarial prompt. It was good. Better than I expected. I made a mental note to go play with it properly when I got home.

Couple days later I went back. Gone.

Not "down for maintenance" gone. Gone gone. The thing had launched on June 9. By the evening of the 12th it was dead. Three days of public life. What happened is that on Friday the 12th, at 5:21pm, the US government handed Anthropic an export control directive: kill access to Fable 5 and Mythos 5 for every foreign national, everywhere, immediately. The stated reason was a jailbreak somebody found. No specifics. No timeline. No appeal. Anthropic said publicly they thought the order was a mistake and they'd fight it. Didn't matter. The plug came out of the wall that same evening.

So there I was, having just spent a day teaching people to think critically about AI, watching a tool I'd used in front of a room vanish because a government I don't vote for decided it should. I'm an AI enthusiast. I am not AI-pilled. But digital sovereignty is literally part of my day job, and even I got caught flat-footed, because in the moment all the policy language burns off and you're left with one fact: the tool is gone and you didn't get a say.

Happy Canada Day.

## "Elbows Up" Has Two Meanings

The slogan's right. The thinking behind it is mushy.

"Elbows up," applied to AI, means buy Canadian. It also means buy anything that isn't American. Those are not the same shopping list, and pretending they are is how you end up with a strategy that feels patriotic and accomplishes nothing.

The Carney government launched "AI for All" on June 4. Two billion dollars, three pillars (trust, opportunity, sovereignty), a promise to keep Canadian data and compute and traffic inside Canadian borders, a national supercomputer, a quarter-million jobs by 2031. Good intentions, real money, the right instinct.

Eight days later, Fable went dark. The strategy had no answer for that, because the day-the-Americans-pull-the-plug scenario wasn't anywhere in it. You can write a beautiful sovereignty strategy and still have no plan for the actual sovereignty event when it lands on a Friday evening with no warning.

That's not me dunking on the intent. The intent is correct. But a sovereignty plan that doesn't survive contact with the thing it's supposed to protect you from is a press release with better production values.

## The PATRIOT Act Problem Nobody Wants To Talk About

This should bother you more than it does. "Canadian servers" is a marketing phrase. Corporate structure is the law.

The Fable shutdown was an export-control order. It cut access *off*. The laws below reach *in* and pull data out. When the hand on the leash is American, it can yank either end. Choke the supply or empty your drawers, your call which scares you more.

Two American statutes do the quiet, heavy lifting that most of the Canadian AI conversation skates right past. The PATRIOT Act lets US intelligence agencies demand data from US companies without a warrant, without telling the customer, and without caring one bit where the data physically sits. The CLOUD Act, from 2018, goes further: any company under US jurisdiction can be ordered to cough up data anywhere on Earth. And "under US jurisdiction" is a generous net. Incorporated there, doing business there, owned by a US parent, or leaned on by US investors. Subsidiaries included.

It does not matter where the server lives. It matters who owns the company.

Microsoft said this themselves, under oath, at a French Senate hearing. Their own French subsidiary admitted it could not guarantee that French data, stored in France, sold as a French sovereign product, was safe from US authorities. The sovereign branding didn't survive its own lawyers.

Gartner made the same point at a session in Dartmouth last week, and they put a useful frame on it. Sovereignty isn't one thing, it's three layers. Data sovereignty (where the bytes live). Operational sovereignty (who runs the platform). Technological sovereignty (who controls the actual model). "Canadian servers" buys you the bottom shelf. The CLOUD Act reaches right into the middle one and helps itself.

And while we're being honest: Canada is no choirboy here. We're negotiating our own CLOUD Act agreement with the Americans to grease cross-border data requests. David Fraser, the Halifax privacy lawyer who's forgotten more about this than most of us will ever learn, has been sounding alarms about Bill C-22, our homegrown lawful-access bill that would force Canadian providers to build government interception right into their plumbing. So "sovereignty from whom, exactly" is a fair shot. But it's an argument for doing this properly, not for throwing up your hands. We can hold both: be patriotic, and admit we leave the back door unlocked too.

## The Cohere Question

Cohere is the Canadian AI story Ottawa wants on the front page. Founded in Toronto, globally respected, enterprise-grade. The new Bell deal is the showpiece: 220 million dollars, 2,304 Nvidia Grace Blackwell GPUs humming away in Merritt, BC, the flagship of something called the Canadian Sovereign AI Alliance.

I want to believe it. I genuinely do.

Then I look at who owns it. Nvidia. AMD. Salesforce Ventures. Cisco. All American, all incorporated south of the line. A billion and a half raised, offices in New York and San Francisco, a Series E in flight, an announced merger with a German outfit that would create a combined entity valued at twenty billion dollars, pending regulatory approval.

The servers are in Merritt. The money is in Santa Clara.

Minority investors with no operational control aren't the same as a US parent company. But it absolutely complicates the sovereign story, and "complicated" is not the word being printed on the banner. Canadian-founded still counts for something. It just isn't a synonym for sovereign, and nobody pitching this deal is offering you the narrower definition where the claim actually holds up. They're letting you fill in the flattering blanks yourself.

## What Actually Exists

Two options worth your attention. Neither is a clean win, and I'd rather tell you that than sell you a flag.

Augure is the one to watch. Small Quebec shop, launched in February. Canadian-owned, no US investors, no US parent, every byte processed on Montreal servers, at least as far as their own disclosures go. Watch the disclosures, not the homepage. Their models (Ossington 4 and Tofino 2.5, named for a Toronto street and a chunk of the BC coast, which is a nice touch) are trained on Canadian law, federal and provincial tax, Quebec French. Law 25 compliant out of the box. They built it for the people who genuinely cannot afford to get this wrong: lawyers, therapists, healthcare, defence.

It's small. The model quality hasn't been stress-tested against the frontier stuff, and there's no CLI yet, which means I can't drop it into a terminal and actually work the way I work. They've got a developer API. If they ship a proper command-line harness, the story changes overnight and Augure goes from compliance tool to daily driver. I'm rooting for them, with my eyes open.

Then there's Mistral, which isn't Canadian at all. It's French. EU AI Act, GDPR, no US parent, no CLOUD Act reach. The Vibe CLI is a real coding agent, terminal-native, runs the same class of work I throw at Claude Code, and I use it for exactly that. It works.

Yes, I hear it: France has spies too. The EU has its own data-access laws. Fair. But the EU AI Act has actual enforcement behind it, GDPR demands judicial oversight that American national security letters simply don't, and, bluntly, France isn't threatening to annex anybody this month. The risk from US jurisdiction isn't a thought experiment, it's the news. That's not me hating America. I'm just reading the room.

## The Category Error

This is the part I keep chewing on. A lot of Canadian AI anxiety is two completely different fears wearing the same Canadian tuxedo.

Fear one: AI is going to gut jobs, hoover up value, flatten our culture, and cook the planet. And inference, not training, eats 80 to 90 percent of AI's energy, so moving the data centre to Merritt doesn't shave the bill one watt. That's a fear about the technology itself.

Fear two: American big tech is going to own our data, run our infrastructure, and treat access to our tools as a geopolitical lever to yank whenever it suits them. That's a fear about who's in charge.

They rhyme. They are not the same song. If your fear is the second one, Mistral and Augure are genuine answers. If it's the first one, a server in Montreal does precisely nothing for you, because the displacement and the extraction and the water bill happen no matter whose flag is on the rack.

Canada doesn't get to skip its own homework here either. I talk about equity of access every time I do the AI literacy stuff, because it's the part that doesn't trend. Half of First Nations households still don't hit the basic internet service target.

**You cannot build "AI for All" on top of an internet for some.**

The strategy at least names this, which is more than the last one managed. Whether it delivers is a wholly separate bet.

Elbows up has to be an equity play, not just a sovereignty play. We try. We are not there. Both of those things are true and a real socialist gets to say so on Canada Day without spilling his wobbly pop.

## So What Does Sovereignty Actually Mean?

I'm proudly Canadian and genuinely into this stuff. I use Claude every day. And Gemini. And Perplexity. And Mistral. I'm trialing Augure. None of that is clean. But it's honest, and honest is where the argument has to live.

The whole Fable "charlie foxtrot" was the useful slap. Sovereignty isn't a question of where the data centre sits. It's whether you can keep working when somebody else's government pulls the cord for reasons that have sweet fuck all to do with you.

Before you trust a tool, ask who owns it. Not where the servers are. Who owns the company, where they're incorporated, who's behind the money. That one question tells you more than every "sovereign AI" press release stacked end to end.

But we're finally asking the right questions, in public, with our elbows where they belong. For this country, on this day, that'll do.

Joyeux Canada Day.
