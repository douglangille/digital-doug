---
title: "Microsoft Classic vs 365 Ecosystem"
image: /assets/images/microsoft-classic-vs-365-ecosystem/204cc981-6cd2-49c6-a0f6-0340381d4961_960x640.jpeg
header:
  teaser: /assets/images/microsoft-classic-vs-365-ecosystem/204cc981-6cd2-49c6-a0f6-0340381d4961_960x640.jpeg
  overlay_image: /assets/images/microsoft-classic-vs-365-ecosystem/204cc981-6cd2-49c6-a0f6-0340381d4961_960x640.jpeg
categories:
categories: []
tags:
  - tools
  - technology
  - productivity
substack_post_id: "147751375.microsoft-classic-vs-365-ecosystem"

---

Change is hard. For everyone.

Microsoft has a hard time changing too, largely because they often have to maintain the old legacy way of doing things while striving to innovate and push the tools to more modern techniques.

[![](/assets/images/microsoft-classic-vs-365-ecosystem/edf653e0-0f1a-415d-9419-33fee24c39a8_300x266.webp)](https://substackcdn.com/image/fetch/$s_!R9wv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fedf653e0-0f1a-415d-9419-33fee24c39a8_300x266.webp)

That’s why they can often be late to market, only to eventually dominate a particular vertical.

They are the 800 pound gorilla, but chained to a boatload of bricks.

Don’t feel sorry for them tho. ‘Dem bricks are gold.

---

One example where this painfully shows up is Outlook. The underpinnings of Outlook are in the Windows Messaging System and MAPI protocol from all the way back to Windows 95. That’s 30 years of spaghetti code, bugfixes, security patches, and a whole host of 3rd party plugins. Outlook felt bloated and bound tight by its backward compatibility legacy.

[![](/assets/images/microsoft-classic-vs-365-ecosystem/4a62fac8-112a-4b39-80d9-b6d427758c8b_300x278.webp)](https://substackcdn.com/image/fetch/$s_!kMW3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a62fac8-112a-4b39-80d9-b6d427758c8b_300x278.webp)

It got to the point where Microsoft couldn’t really innovate and leverage the Microsoft 365 environment. They needed to break compatibility and start fresh.

The easiest way to do this was to build off the web version, previously known as Outlook Web Access.

For the longest time, OWA was a trimmed down version of the full-desktop client experience. Back when Exchange servers were built and maintained by individual companies and institutions, separate OWA instances were also maintained.

The move to Exchange Online and Microsoft 365 with the Microsoft Graph brought tons of opportunity to do better. And make no mistake, Microsoft had to. Its competitors were making better products, largely because they were not mired in past compatibility woes.

Here’s the sitch. We currently have two versions of Outlook for the Windows desktop.

1. Classic, based on the MAPI protocol
2. New, based on the M365 web version

The Mac variant also has a Classic/New thing going on, but the mobile and web versions are all “New”. Obviously.

---

I’m not going to spend a bunch of time on Email and Calendaring, but I’d like to spend some time on what happened to Tasks, Notes and the confusing mess that OneNote is becoming.

**So…. follow me down the rabbit-hole.**

[![](/assets/images/microsoft-classic-vs-365-ecosystem/0281a556-d5cc-4bed-8c45-7faa15733235_300x188.png)](https://substackcdn.com/image/fetch/$s_!ZkBf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0281a556-d5cc-4bed-8c45-7faa15733235_300x188.png)

---

Let’s start with Notes. It’s easier to follow the bouncing ball. Notes is a folder and object type within the Exchange Messaging Store. Each note has a title field and a memo field. The only real innovation over the years has been rich text formatting. You can access it in a couple ways:

1. In Outlook Classic under the Notes tab, which is often hidden in the navigation pane, but easily brought into view.

   [![](/assets/images/microsoft-classic-vs-365-ecosystem/e653733b-2ad1-43da-bf21-51b092881d97_212x300.webp)](https://substackcdn.com/image/fetch/$s_!PIZT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe653733b-2ad1-43da-bf21-51b092881d97_212x300.webp)
2. In the Windows Sticky Note app if you login to it with your M365 credentials. This was a Windows 10 thing where Microsoft was pushing its gawd-awful Store for everything, but it’s there in Win 11 too.
3. On the web at <https://outlook.office.com/mail/notes> and [www.onenote.com/stickynotes](https://www.onenote.com/stickynotes)
4. In OneNote under the Sticky Notes icon (mobile and desktop apps)
5. In the Microsoft 365 mobile app for iOS and Android, but is kinda wonky.
6. In the native iOS and Android Notes apps if you login using your M365 credentials (though you lose rich text, etc).

The best experience today for Outlook Notes is the Windows desktop Sticky Notes app, with an upgraded version in the Store. Otherwise, just use the web version.

IMO, the thing is pretty much pooched and obviated by other tools. We’ll talk briefly about OneNote and Loop later.

---

Okay. Tasks. So much to talk about.

Like Notes, Tasks is a folder and object type within the Exchange Message Store. And like Notes, you can access it in Outlook Classic under the navigation pane. You can also use the native Reminders/Tasks apps in iOS and Android as well.

However…

Microsoft purchased a company called Wunderlist a number of years ago and repurposed it into Microsoft To Do. This is the preferred way to access Tasks in the Exchange Message Store. There’s also additional functionality such as subtasks that aren’t exposed in the Outlook Classic interface.

[![](/assets/images/microsoft-classic-vs-365-ecosystem/eaf535a9-302c-403f-829d-9aaede4e9fa4_300x204.webp)](https://substackcdn.com/image/fetch/$s_!4zHe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feaf535a9-302c-403f-829d-9aaede4e9fa4_300x204.webp)

Microsoft To Do is integrated into the Outlook New experience.

This is the way, sayeth Microsoft.

I’ve talked about this in prior posts. The experience is really good. The addition of presenting Flagged email as Tasks in Microsoft To Do is simply brilliant.

It’s also horrid in that it allows peeps to be lazy and not extract the actual action items from email, but at least it helps tamp down the Flagged email hoard we all have and it all kinda doable. But I digress.

You can also find To Do here: <https://to-do.office.com/>

---

There’s another player on the field with respect to Tasks. It’s called Microsoft Planner. It’s needlessly confusing, but also very simple.

[![](/assets/images/microsoft-classic-vs-365-ecosystem/5dea14b3-e96f-4e75-89c2-75390e269f2c_300x300.webp)](https://substackcdn.com/image/fetch/$s_!3i7z!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5dea14b3-e96f-4e75-89c2-75390e269f2c_300x300.webp)

Planner Plans are specific kinds of project tasks lists in SharePoint. They’re basically Kanban boards that can also be viewed as lists, Gantts and calendars. Every plan is associated with a SharePoint collaborative site but a SharePoint site can contain multiple plans.

Planner is also a web and mobile app that can be used to view and work with all your ~~evil~~ plans. It’s a hub. It can be accessed via the dumbest URL ever: <https://tasks.office.com/>

Yes. Tasks can be sound at [https://to-do.microsoft.com](https://to-do.microsoft.com/) and Plans can be found at [https://tasks.microsoft.com](https://tasks.microsoft.com/). You read that right.

Anyway.

Planner tasks that you’re assigned show up in Microsoft To Do, which is handy.

---

Even more weird is that in Microsoft Teams, we have another app called Planner which combines To Do and the other thing they called Planner into a single interface. It’s awesome even if a little clunky, but I see where they’re going.

And because, why not, at some point Microsoft will be combining the old Planner hub app with Microsoft Project and calling it Project.

Whatever. Makes sense. I guess.

Like I said, change is hard for Microsoft.

[![](/assets/images/microsoft-classic-vs-365-ecosystem/efa63e9b-bfed-481e-be80-554429b7f6ab_500x239.gif)](https://substackcdn.com/image/fetch/$s_!QjBe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fefa63e9b-bfed-481e-be80-554429b7f6ab_500x239.gif)

---

The upshot is that there are Three Centres of the Productivity Universe:

1. CLASSIC MODE: Outlook Classic and OneNote for Windows Desktop
2. APPSTACK MODE: Outlook New, Microsoft To Do, OneNote and Loop
3. SUPERAPP MODE: Microsoft Teams with the integrated Planner, OneNote, and Loop

> ```
> OneNote and Loop just entered the chat.
> ```

One of the reasons folks are holding on to Outlook Classic is because of its tight integration with other desktop apps in the Office suite.

- You want mail merge to actually work? Gotta have Outlook Classic running.
- You want Send to OneNote to work reliably? Gotta have Outlook Classic.
- You want Outlook Tasks to work in OneNote? Outlook Classic AND OneNote for Windows Desktop. That’s a kicker.

[![](/assets/images/microsoft-classic-vs-365-ecosystem/e56a6ec7-0ade-474a-b04e-104cadb7e588_293x300.webp)](https://substackcdn.com/image/fetch/$s_!-znV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe56a6ec7-0ade-474a-b04e-104cadb7e588_293x300.webp)

Will this always be the case? Probably not, but it is today.

---

Now, Microsoft Loop is a whole other blog post, but in the context of what we’re talking about here, the skinny is pretty straight forward.

[![](/assets/images/microsoft-classic-vs-365-ecosystem/85489412-1984-4c37-8c5e-5f46201af326_300x300.webp)](https://substackcdn.com/image/fetch/$s_!MXHn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F85489412-1984-4c37-8c5e-5f46201af326_300x300.webp)

There is a Loop component called a Task List. It’s really a Planner Plan and thusly is surfaced in Microsoft To Do and Teams Planner.

OneNote now has the ability to have Loop Components, so that’s the more forward-looking way of integrating task management and OneNote.

---

Tune in next time when we deep dive into OneNote and Loop. It’s gonna be a trip.
