---
title: Dr. Strangebot
excerpt: "How I Learned to Stop Worrying and Love Markdown"
header:
  teaser: /assets/images/dr-strangebot/feature.png
  overlay_image: /assets/images/dr-strangebot/feature.png
tags: [personal, prescriptive, craft-authenticity, technical-infrastructure, knowledge-epistemology]
entities: []
meta: "Office formats aren't broken. You're drafting in the wrong layer. Here's what changes once you stop asking a printer to also be your desk."
feature: /assets/images/dr-strangebot/feature.png
---

# Dr. Strangebot
## Or How I Learned to Stop Worrying and Love Markdown

## Chapter 1: The Wall

I asked the chatbot to restructure a Word document. Reorder two sections, cut a paragraph, tighten the headings. Simple ask. It came back fast, confident, and wrong. The heading styles had reset halfway through. Track Changes had turned the edit into a fossil record nobody could read. A table near the bottom lost its borders. The footer vanished.

None of that was in my instructions. I asked for a restructure. I got a restructure plus collateral damage I then had to hunt down, one style inconsistency at a time, which took longer than doing the original edit by hand would have.

Fine. Word's finicky. Let's do the deck instead.

Same story, different pants. I asked the robots to tighten a PowerPoint presentation: cut two slides, rebalance the bullet density, freshen up a chart. The content came back sharp. Genuinely good structural advice, better transitions, a cleaner argument. And then I opened the actual file and found text boxes overflowing their frames, images sitting where captions used to be, half the deck still with the old theme and half wearing something else. The thinking was right. The container had come apart.

Then Excel, which is the worst of the three, and it's not close.

I had a spreadsheet with a formula that wasn't calculating right. I asked for a fix. What I got back was a description, in prose, of what the formula *should* do, which isn't the same as fixing the formula, because the model wasn't looking at the actual cell references at all. Other times it "fixed" things by handing back new values instead of new logic, which meant every cell downstream of the one it touched was now wrong in a way that wouldn't show up until someone noticed the totals didn't add up anymore. A spreadsheet is the most rigidly structured of the three formats. Everything depends on everything else by reference, so a wrong move here doesn't sit quietly in one corner. It cascades.

Three tools. Three separate frustrations. Same failure, every time: brilliant at the content, useless at the container. Ask any of them to think about what a document should say, and they're sharp. Ask them to also hold the file together while they say it, and something breaks.

I spent longer than I care to admit assuming this was a prompting problem. Better instructions. More context. A system prompt that says "preserve formatting" in increasingly desperate capital letters. None of it held for long, because I was diagnosing the wrong layer.

## Chapter 2: The Realization

A desk is where the drafting happens: messy, plain, whatever you're working on spread out where you can see all of it, change any of it, without asking permission first. A printer takes what's finished and makes it presentable for whoever needs to receive it that way. Nobody confuses the two. Nobody drafts a document by feeding blank paper through the printer and writing on the output tray.

Nobody drafts inside a finished PDF either, for the same reason. You go back to whatever made it and edit that. The PDF is the printer's job, not the desk's.

Word, PowerPoint, and Excel are stranger than a PDF, because they look like they should be desks. You type directly into them. It feels like drafting. But watch what's actually sitting underneath the words: a Word file carries style definitions, revision-tracking history, layout rules, all threaded through and around the text you can see. A PowerPoint file carries master templates, theme inheritance, exact positioning for every box and image on every slide. An Excel file carries formulas and cell references that reach across the sheet, each one depending on several others. None of that is decoration sitting politely beside your content. It's interleaved with it, cell to cell, style to paragraph, box to slide, and none of it was designed to be handed to a large language model that only reads plaintext.

So when a chatbot receives your Word doc, it doesn't actually receive the file. It receives an extraction. Plaintext pulled out, the styles and structure and cross-references mostly stripped away, because that's the only form the model can take in through a chat window. Ask it to change the words and it can. Ask it to also preserve everything that got stripped on the way in, and it's reconstructing a rulebook it was never shown, from a format so densely cross-referenced that one wrong guess about a style or a cell reference doesn't stay put. It ripples.

This is exactly why Excel breaks worse than the other two. A Word document's cross-references are mostly cosmetic, a style here, a heading level there. A spreadsheet's cross-references are the entire point. A formula like `=SUM(B2:B14)` survives the extraction fine as text. What doesn't survive is the ability to check what's actually sitting in B2 through B14, because the model was handed the formula, not the sheet. It can reason about what the formula says. It can't verify what the formula touches. So the model isn't fixing your formula. It's fixing a paraphrase of your formula, one that lost the exact thing that made it a formula.

None of this makes the model bad at the job. It's doing exactly what it's built to do: reason fluently over the plaintext in front of it. The problem sits one step earlier than the model. It's whatever handed the file over in the first place, and how much of the actual file survived that handoff. The chatbot was never bad at Word. It just can't actually use Word.

## Chapter 3: What Source Actually Looks Like

So what does a draft look like, if a Word doc doesn't cut it? Simpler than you'd think. Plain text, markdown mostly, with a couple of close cousins worth a mention.

Markdown is what you already know how to do, minus the toolbar. A heading is a line that starts with `#`. A list is a line that starts with `-`. Bold is two asterisks around a word. That's most of it. No hidden style sheet, no revision-tracking layer, no positioning data. Just the structure sitting right there in the text, visible, readable by you and by anything else that opens the file. Take a messy Word document: inconsistent heading styles, a bulleted list that's secretly three different formats, a bold word here and there for emphasis. The markdown version of the same content is shorter, plainer, and says exactly the same thing with nothing left to break.

And then there's CSV, which matters for anyone who's ever fought with Excel. A spreadsheet is really two things stacked on top of each other: the data, and the formulas that operate on the data. CSV keeps only the first part: rows and columns, plain values, no hidden logic. Sounds like a downgrade until you remember that the hidden logic is exactly what breaks. Hand an AI a CSV and there's no invisible dependency chain for it to misread. Just the numbers, sitting in the open.

What these have in common is the same: nothing is hidden. The structure of a markdown document and the rows of a CSV file: you can see all of it just by looking at the text. There's no cross-referenced layer sitting underneath, holding the real rules somewhere you can't see them. The text *is* the rules.

That's why a model reads and writes these formats cleanly where it stumbled over Word and Excel. There's no container to misunderstand, because there's no container at all. Just the source, in the open, exactly as it is.

## Chapter 4: Beyond the Chatbot

Knowing that plaintext is the better draft format doesn't help much if the only tool you've got is a chat window and a copy-paste habit. That's most people's actual setup: open the chatbot, paste in some text, get some text back, paste it into whatever you were working on, repeat. It works, I guess. Technically. It's also you doing all the file-handling labor by hand, every single time, while the AI just handles the words in the middle. Which is kinda backwards if you think about it.

There's a layer of tools past the chat window that skips that labor. Claude Cowork, the one I actually use, doesn't require you to paste something in. It works on your actual files, in place, on your own computer. Point it at a folder and it can open what's there, change it, save it, without you ever copying a paragraph into a browser tab and copying it back out again.

Hand a tool like this your messy Word doc, and it can turn it into clean markdown, edit the markdown the way you actually want, and turn it back into a Word doc when you're done. The conversion happens as part of the tool doing its job, not as a separate chore you have to remember to run.

Treat the markdown file as your original source with provenance. The DOCX file is just an output format.

Same with sheets and decks. Work within the model's plain text format and then convert to Excel and PowerPoint.

This is, honestly, enough for most people. 

## Chapter 5: The Terminal Toolkit

There's a lot more flexibility in the terminal version these tools, and that's scary for a lot of folks: a black screen with a blinking cursor, and twenty years of folklore telling you not to touch it or you'll break something.

You won't, not from opening it. A terminal is a text box. That's the whole secret. You type a line, you press enter, it does exactly and only what that line says, and it's got no more mystery to it than the search bar you already use forty times a day. It just answers in actions instead of links. Typos here mostly do what typos anywhere do: nothing, or an error message telling you it didn't understand. The command line does have real "running with scissors" moments, a tool with file access doing something you didn't mean for it to do, and those deserve your attention. But that's the same caution you'd give someone with a mouse and a delete key, not some special hazard unique to the black screen. You will get things wrong sometimes. So does everyone. That's not a sign you're not technical enough. It's what week one looks like for literally everybody.

Right now, many large language models have command line interfaces (CLIs). Claude Code is the most talked-about, and the one I use most of the time. The French company Mistral has one called Vibe that I like too. This is the lineup as of this writing, and it's probably a different lineup by the time you're reading it, because this corner of the field reshuffles every few months. What doesn't change as fast: basically, a CLI tool is an AI that lives in your terminal, reads and edits your actual files directly, and can reach for tools on your system itself when the job calls for it. You can use it like a chatbot and feel like a hacker. It's way more than that though. It's closer to the AI collaborator that Big Tech touts: something that can decide a file needs converting, converts it, and keeps working, without you standing in the middle relaying instructions between two separate programs.

A few tools you just ask the CLI tool to set up for you:

* Pandoc takes a markdown file and turns it into almost anything else: Word, ePUB, HTML, you name it. 
* Microsoft's markitdown runs the other direction, taking messy Office files and pulling clean markdown back out of them, doing properly what a chat window's extraction does badly: preserving structure on the way out instead of stripping it. 
* Python is a scripting language that specializes in doing a lot of things with plaintext and other document formats.

Together they're the two-way door between the Office world and the plaintext world, the actual build step, source to output and back. Why bother with this instead of letting Cowork handle it quietly in the background? Control. You can convert forty files in one command instead of one at a time. You can ask the CLI tool to script it so it happens the same way every time. You're not depending on one company's tool continuing to offer that feature next year. 

Back to the Excel example, the formula that broke, the values that cascaded wrong. Export the relevant sheet to CSV, point the CLI tool at it. Or better yet, have it put together a python script to parse and find the problem. It can open the actual file. Read the actual rows. See exactly what's there instead of guessing at a structure it can only half perceive through a chat box. The fix works here, not because the model got smarter, but because you finally gave it better tools.

Just a tip from the trenches: don't forget to test the script on a copy of the file. 

## Chapter 6: Where You Actually Write

I experimented with more text editors than I should admit. Notes apps are notorious for promising to organize thinking and mostly organized procrastination. Every switch costs a week of re-setting-up before you throw in the towel and move on.

There are two standouts for me that I use. And they're free.

Obsidian is where you write when the work is mostly documents: notes, drafts, thinking that needs to sit next to other thinking. Markdown is the native format, not a mode it grudgingly supports. Files link to each other. Nothing about it asks you to leave plaintext to do the thing plaintext is good at.

VSCode is where you write when the work is everything else: code, configuration, the kind of file that isn't primarily prose. It's also a convenient place to have a terminal prompt right next to the files you're working on, all sitting in the same window, so you're not context-switching between three separate apps to get one thing done.

Pick based on what you're mostly doing, not based on which one wins some abstract feature contest. Documents, Obsidian. Everything else, VSCode. Plenty of people end up with both open at once, and that's fine. Don't be a tool zealot.

One warning, because it's the trap I fall into: both of these tools have a bottomless rabbit hole of plugins, themes, and settings, and it is entirely possible to spend more time tuning your editor than using it. That's not a productivity system. That's a new hobby. Set a minimal config once. Stop touching it. The whole point of these tools is to help you get out of your own way. Don't build a new way to get in it.

## Chapter 7: When You Still Convert Back

None of this means abandoning Word, Excel, or PowerPoint. It means being deliberate about when you leave plaintext instead of fighting the tool by accident.

The Word case is the clearest one. You draft in markdown, you get to a version worth sharing, and then someone else needs to mark it up: comments in the margin, changes tracked, the whole apparatus of institutional review. Nobody in your team is keen on reviewing a markdown diff. Track Changes is the actual shared surface for that kind of work, because everyone already knows how to use it. So you convert, hand it to the people who need to touch it that way, and that's fine. Use the right tool for the right job. Draft in markdown where it's clean, convert at the point where another human needs the tool they already know.

Excel is a different shape of the same idea, and it's worth being blunt about it: your formulas are not leaving Excel, and they shouldn't. A formula is logic. CSV only holds values. Round-trip a spreadsheet through CSV and the logic doesn't survive the trip. You'd get numbers back with no memory of how they were calculated. So the actual pattern isn't "replace Excel." It's "keep the formulas where formulas live, and export only the slice you want an AI to look at." Two jobs. Two formats. No shame in either one.

PowerPoint is the one people get wrong in a different direction, and it's worth pausing on. People treat a deck as though the thinking happens inside it. It doesn't. A slide deck is output, same category as a Word doc, just with letterboxing and popcorn. The actual content, the argument, the sequence, the story a good deck needs to tell, is exactly the kind of thing that belongs in plaintext first. Draft that structure as a document, hand a well-built document to an AI with real storytelling guidance, and it can generate the deck *from* that source. Decks are rarely genuinely collaborative in the Track Changes sense anyway, one owner, the occasional round of feedback, so there's not much reason to draft inside one at all. There's a bigger question boiling on the stove: whether a deck is even the right output when a one-page infographic would do more with less production overhead. That's a different post, for a different day.

Sovereignty over your source was never about refusing every output format. It's about choosing the conversion point on purpose, instead of discovering it by accident when Track Changes turns into a fossil record.

## Chapter 8: The Printer and the Desk

Word, PowerPoint, Excel. I still use all three, most weeks. What changed isn't the tools. It's what I ask them to be.

They were never bad at their jobs. A finished document, a polished deck, a working spreadsheet: Word, PowerPoint, and Excel are good at exactly that, better than plaintext will ever be, because that's the job they were built for. I'm just not asking a printer to be a desk.

A desk is where the drafting happens: messy, plain, structure visible, nothing hidden that can break when you're not looking. A printer takes what's finished and makes it presentable for whoever needs to receive it that way: a colleague who wants Track Changes, a room that wants a deck, a formula that needs to stay a formula. Both jobs matter. 

The worrying doesn't stop because Word got better at working with AI, or because Excel finally learned to explain itself. It stops because I stopped asking them to. Draft where nothing's hidden. Convert when someone else needs the finished version. That's the whole thing.
