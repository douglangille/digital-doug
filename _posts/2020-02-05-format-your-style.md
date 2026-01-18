---
title: "Format Your Style"
image: /assets/images/format-your-style/e35be88a-afa4-4328-ba73-afb8a6cf6e9a_580x386.jpeg
header:
  teaser: /assets/images/format-your-style/e35be88a-afa4-4328-ba73-afb8a6cf6e9a_580x386.jpeg
  overlay_image: /assets/images/format-your-style/e35be88a-afa4-4328-ba73-afb8a6cf6e9a_580x386.jpeg
categories:
  - 
excerpt: "Long live Comic Papyrus"
substack_post_id: "141217720.format-your-style"
tags:
  - productivity
  - tools
  - creativity
---
Okay. So the last two weeks, we’ve been on a plain text kick and then did the markdown thing. This week, I’m going to wrap this topic up.

[![05c78b3b-6ab1-459d-869e-0dd937fc85ba](/assets/images/format-your-style/c7755316-1331-42cc-86ca-3bacc2893f57_500x211.gif "05c78b3b-6ab1-459d-869e-0dd937fc85ba")](https://substackcdn.com/image/fetch/$s_!BYDQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7755316-1331-42cc-86ca-3bacc2893f57_500x211.gif)

We’ve already established that plain text is a great sustainable, future-proof and portable document format and that markdown provides enough text formatting to convey the semantic meaning of document structure beyond the words themselves.

It’s a great way to manage the “source code” of your creative works.

**Of course, life isn’t lived in black-and-white and plain text isn’t the final presentation.**

[![f54d2013-4cf6-46bb-b34a-1312160a5a13](/assets/images/format-your-style/1fe4cd78-9875-4f0f-a571-b19ce0c38ccb_480x278.gif "f54d2013-4cf6-46bb-b34a-1312160a5a13")](https://substackcdn.com/image/fetch/$s_!B2oV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1fe4cd78-9875-4f0f-a571-b19ce0c38ccb_480x278.gif)

There are many tools that are used to convert markdown-formatted plain text to other formats. Most of the apps out there use Pandoc in the background to do the heavy lifting. [Pandoc](https://pandoc.org/) is free.

The command:

`pandoc -o fancydoc.html fancydoc.txt`

…will convert the plain text document fancydoc.txt to a web page fancydoc.html.

This command:

`pandoc -o fancydoc.docx fancydoc.txt`

…will result in a Microsoft Word document.

You can even make an ebook using Pandoc if you feel so inclined.

Anyway, the idea is that markdown can convert to a web or Word document rather readily. And just about anything else.

**How is this possible? Are you some sort of wizard?**

**Glad you asked.** No, I am not but take this little ditty:

```
# Title

## Chapter 1

Call me *Ishmael*.

> A dude **walks** into a ***bar***.

* one
* two
* three
```

Here’s how pandoc converts it to HTML:

```
<h1>Title</h1>
<h2>Chapter 1</h2>
<p>Call me <em>Ishmael</em>.</p>
<blockquote>
<p>A dude <strong>walks</strong> into a <strong><em>bar</em></strong>.</p>
</blockquote>
<ul>
<li>one</li>
<li>two</li>
<li>three</li>
</ul>
```

[![b142139a-1eee-4624-a77e-17b629415b07](/assets/images/format-your-style/a7b2c4aa-c79d-4ade-8608-69cd5f7e1814_350x400.png "b142139a-1eee-4624-a77e-17b629415b07")](https://substackcdn.com/image/fetch/$s_!K44o!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa7b2c4aa-c79d-4ade-8608-69cd5f7e1814_350x400.png)

You’ll quickly notice how much more readable markdown is as source-code over HTML. Which is the whole reason markdown was created in the first place– a one-to-one element conversion to HTML.

**Now…**

You can style the HTML using a thing called CSS (yeah, call acronyms anonymous). I won’t make you all bleary-eyed with code, but essentially, you can style elements and classes to look differently. For example, you can make all first-level headers in the font Comic Sans, make all strongly-emphasized text become red and put a grey background behind quoted/blocked text. You do you. I won’t judge. Much.

The separation of semantic content from presentation is pretty important to how the web works.

If you want to chat more about HTML and CSS, I’d be only too happy to do such. But to be honest, that’s the jam of the Digitial Products and Experience team. They could talk about this stuff all day.

**So finally, now let’s look at Microsoft Word.**

I converted the snippet above to Word and it looks like this:

[![](/assets/images/format-your-style/d5f7ac30-a504-45e0-8a7e-973152a52c76_735x566.png)](https://substackcdn.com/image/fetch/$s_!du94!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd5f7ac30-a504-45e0-8a7e-973152a52c76_735x566.png)

You’ll notice all the semantic structure came across and were styled in that oh-so-unique Microsoft way. Take a look at the other screengrab. You’ll see how the markdown formatting became Word styles.

What’s important here to remember is that you should always be using Word styles for the semantic/structural elements of your document– headings, blocked text, etc.

The reasons are many, but here are three:

1. **Accessibility** for screen readers and stuff. I mentioned this last week, but it bears repeating. If your document is semantically well-structured, then the screen readers will have an easier time.
2. **Theming**. If you’re using Word’s style functionality, then you can use the themes stuff under the Design ribbon. And, yes, you can define your own theme design. This is pretty much the same as the CSS styling for HTML documents.
3. **Tables of Contents** link to Microsoft heading styles… automagically.

[![](/assets/images/format-your-style/551edbdd-96b3-4bae-a6af-fddf0d9caabf_757x680.png)](https://substackcdn.com/image/fetch/$s_!e1fm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F551edbdd-96b3-4bae-a6af-fddf0d9caabf_757x680.png)

[![](/assets/images/format-your-style/da99ff2e-f64d-45fc-ac6d-4ad245c53dd4_1114x685.png)](https://substackcdn.com/image/fetch/$s_!8TWZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fda99ff2e-f64d-45fc-ac6d-4ad245c53dd4_1114x685.png)

**So that’s it for now.**

If you can tweak how you layout your Word documents so that you use styles, you’ll save yourself a lot of headache and possibly heartache.
