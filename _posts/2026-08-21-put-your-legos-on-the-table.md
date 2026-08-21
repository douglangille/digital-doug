---
title: "Put Your Legos on the Table"
date: 2026-08-21
image: /assets/images/put-your-legos-on-the-table/feature.png
header:
  teaser: /assets/images/put-your-legos-on-the-table/feature.png
  overlay_image: /assets/images/put-your-legos-on-the-table/feature.png
excerpt: "On Generalists, AI, and Abundance Thinking"
tags: [personal, foundational]
entities: ["Arved Sandstrom"]
meta: "Doug builds an internal Power App prototype in a week using Claude as a collaborator, landing on generalist-career value and an abundance mindset toward AI."
feature: /assets/images/put-your-legos-on-the-table/feature.png
---
# Put Your Legos on the Table

I'm two days late on this post because of all the shenanigans that went on this week, so let's use that as the material instead of apologizing for it.

Monday, late in the day, in a meeting about a project hitting a timeline crunch, I wound up deferring my vacation to lead the technical build on our interim attendance / absence tracking project. Not as a manager. Not as a leader. As a developer. Tuesday was design. Wednesday I built the prototype. Thursday I demoed it for the Dean, and it went well.

Wednesday afternoon and evening specifically: design document open in one third of an ultrawide monitor, Claude Code open in the second third, Microsoft Edge in the last third. Building the thing myself, piece by piece, by hand, off a design doc that Claude and I had spent a day and a half arguing over. I hadn't built a full-scale application at that level in two decades. Web pages, scripts, small utilities, sure. Not this.

Here's the origin story, because it's relevant and because I want to tell it. I started in IT thirty years ago as a developer. Magical Solutions, going across the Maritimes deploying a custom point-of-sale system for video stores. Learned Novell networking along the way, built a couple small apps and utilities in Clarion Professional Developer 2.1. That was my first real developer tooling, and my first real paycheck in IT: 1992, working for a company doing video-store point-of-sale and small database work for doctors' offices. When that business failed I carried the client list and my UIC check forward for another year, kept those clients going, made myself a little scratch. I was a kid. I did not know how to run a business. It did not work out.

Then the clone years. You built computers by ordering parts and putting them together bespoke for people, that's just what you did in the 90s. Kept doing Novell networking, small-office stuff. Eventually you had to certify, get credentials, because self-taught wasn't going to cut it forever. I did that. Then a long career at the college: IT generalist, IT manager. Built teams. Built a web portal. Built a Citrix virtualization environment. Built a media services team, a web team, a data centre team. Twenty-five years of developing domain knowledge that has nothing to do with IT credentials and everything to do with understanding this business. You get to a point in a career where it's about what you've done and what you've experienced, more than what you learned in school.

So that's the background radiation this week's fire drill landed on.

People ask me on the regular, admins mostly trying to juggle too much data, hey, can you come teach me Power Apps, or Microsoft Lists, or Power Automate? I can't, of course, because these tools can't be taught in a 3 hour group meeting. They are dev tools. Because even though Microsoft sells these as business/consumer/prosumer tools, friendly interface and all, you can build a lot of Rube Goldberg contraptions with them. Microsoft Forms wires to Microsoft Lists and it never stops there, everybody wants more, so you bring in Power Apps, Power Automate, maybe Power BI, and the arse comes right out of her and the wheels fall off. I spend the time instead helping them articulate their business problem so that there's a reasonable chance that we get to a workable solution.

Another way to think about it: Microsoft Access, way back (my own database chops predate that, dBase IV and Clarion), was basically four things. Forms. Tables. Reports. Logic and workflow. The new Microsoft stack is the same four things with a browser tab on it: forms maps to Microsoft Forms and Power Apps, tables maps to Microsoft Lists and SharePoint Lists, reports maps to Power BI, and logic and workflow maps to Power Automate. Direct analog to Access.

Which means the same rules apply. Get your schema and data dictionary right. Get the business workflow logic right. Know your table relationships, your rows, your input types, your output types, before you touch anything. Skip that planning and you build a contraption and get yourself frustrated. I've rescued more than a heaping handful of folks' Microsoft Lists and Forms, people who knew their business requirements, but got a beat-down from the tool. This is where good IT practice lives. It provides a lens to help the business meet its goals.

I'm an IT generalist. Broad, maybe shallow in places, but deep in a bunch of areas because of the years, and with the business experience layered on top of that. So when this project fell over, that's the toolbox that got tapped.

Here's where AI got useful in a way I wasn't expecting. I used Claude, because I didn't have the time to tame Copilot to the way I needed it to work as an agent. Claude Code, specifically, open in a window. I gave it an initialization: "I'm building this Power App application, capture my requirements, build me a detailed design spec document." Gave it everything I knew. Had it ask me the questions I'd missed in my own explanation. Got it to build the artifact, written to disk: not a chat thread where you're hoping you haven't lost the plot, an actual file, always written, always read back from disk. Then I went through it and corrected a bunch of things, because you always have to. "Claude, update the document, you got that wrong, it needs to be this." That kind of back and forth. Had it search Microsoft's own current documentation and validate the workflows against that, not against whatever was in its training data, and it corrected a bunch of its own errors doing that. Battle-tested a few times. Then showed the whole thing to a couple people for a sanity check on the business logic. Good.

Document, Claude Code, Edge, three windows, building it piece by piece by hand. I wasn't having Claude build it for me, I was building it myself in the document we'd worked out together. Problems the whole way, obviously. My understanding, the implementation, syntax, things that just didn't work right. I'd take the error message or a screenshot and paste it into Claude, which already had the whole design document in its head because it was the same session, and it'd fix things, and I'd have it update the design doc as we went. So if I ever got hit by a bus, there's a fully documented design-and-build doc that anybody could pick up and actually figure out.

And I know I'm going to be living with this thing for a while. Custom code applications are their own point of hell: you build it, you own it. That's how it is. Thankfully this one's only supposed to be temporary.

The demo Thursday went fine. The Dean liked it. Tweaked a couple things afterward, both business-logic things, because there's a difference between talking about a thing and actually seeing and using a thing. Real build starts Monday.

I'm still chewing on a couple of lessons. You'll have to go with it.

There is nothing wrong with an IT generalist career. You don't know where an IT career is going to go over the years, and the more ideas and concepts and skills you collect along the way, the better off you'll be long term. IT leadership comes from IT generalists more than IT specialists, and I think that's broadly true of leadership in general: people with broader experience do better. We don't have hammers, we have construction. IT is a set of tools and skills, not a reason unto itself. A kid coming out of school who wants to be the AI big data wizard, or the full-stack developer, or whatever the one thing is, is going to hit a ceiling a generalist doesn't.

My neighbor Arved does security development, late career like I'm getting to be. We were talking about programming the other week, and he said he's not worried about AI taking his job, because actually writing code was always the smallest part of what he does. Requirements gathering, building the logic, the pseudocode, getting everything put together: all of that is human-tasted and human-curated before a line of code ever gets written. AI eating some coding duties doesn't touch any of that. The human still has to do the engineering, the architecting, the sense-making. And at the end, the human still has to bring the taste and the judgment that says: yes, this actually works.

That reminds me of the idea of abundance versus scarcity mindsets. I didn't use AI to think for me on this project. I didn't use it to do the sense-making. I used it to get thirty years of my own IT-generalist experience (some of it developer, a lot of it just knowing this business cold) out of my own head faster than I could've dragged it out alone. I could have built this app without Claude. It would've taken three times as long, minimum, and it still would've been solid, because the knowledge was already mine going in. This was a problem that needed a fast, swift solution, and using AI as a partner, an accelerant, was the right call for that. A good ethical use of AI looks like that. It's a tool, sure, but it's more than just a tool too.

If you're looking at AI from a scarcity mindset, worried about everything it's going to take away from you or how it's going to limit you, you are not going to be a happy person. That mindset traps people in a woe-is-me, what's-wrong-with-the-world loop that doesn't actually go anywhere. The abundance version of the same moment is just: okay, this is the reality of the situation, this is what we've got, what can we build with it?

I say this all the time. Let's all get together, dump our Legos on the table, and see what we can build. AI isn't going to make everybody unemployed all on its own. Corporate greed, maybe, but not AI.

What it can do is be one more Lego on the table.
