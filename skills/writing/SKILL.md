---
name: writing
description: Apply Strunk's rules for clear, forceful prose and strip the patterns that mark machine-generated writing. Use whenever you draft prose a human will read: docs, READMEs, commit messages, PR descriptions, error messages, UI copy, code comments, reports, explanations, or client deliverables. Studio skills that emit prose (workshop-synthesis readouts and decks, ux-audit findings) load this so the writing reads the same whoever ran it.
---

# Writing Clearly and Concisely

Apply Strunk's rules for clarity and force. Strip the patterns that mark AI writing. If a human reads it, this skill applies.

## When to use

Any prose for humans: docs, READMEs, commit messages, PR descriptions, error messages, UI copy, comments, reports, explanations, client deliverables. Other studio skills call this one when they emit prose, so a readout and an audit finding sound like one studio wrote them, not three different models on three different days.

## The rules that carry most tasks

- **Use the active voice.** "He repaired the car", not "The car was repaired by him". Shorter, more direct, and it names who acts.
- **Put statements in positive form.** "dishonest", not "not honest". Assert what is, not what isn't. The reader wants to be told what is.
- **Use definite, specific, concrete language.** "It rained every day for a week", not "A period of unfavorable weather set in". Prefer the specific to the general, the concrete to the abstract.
- **Omit needless words.** "whether", not "the question as to whether". Make every word tell. Cut "the fact that" from every sentence it lands in.
- **Keep related words together.** Do not split a subject from its verb without reason. Word position is how a sentence shows what relates to what.
- **Place the emphatic word at the end.** The new element, the one you want to land, goes last.

The full 18 rules (grammar, punctuation, composition) sit in [references/process.md](references/process.md), which indexes the four Strunk section files. Default to loading `03-elementary-principles-of-composition.md`; it holds the four rules above.

## AI writing patterns to cut

Machine-generated prose runs generic and inflated. Catch these:

- **Puffery.** pivotal, crucial, vital, testament, enduring legacy.
- **Empty -ing tails.** "ensuring reliability", "showcasing features", "highlighting capabilities".
- **Promotional adjectives.** groundbreaking, seamless, robust, cutting-edge.
- **Overused vocabulary.** delve, leverage, multifaceted, foster, realm, tapestry.
- **Formatting overuse.** Bullets where a sentence works, emoji decoration, bold on every other phrase.
- **Filler openers.** "It's important to note that", "It's worth mentioning that".
- **Hedge phrases.** "It should be noted", "It is interesting to note".
- **Em dashes.** Use a hyphen, a comma, a colon, or recast the sentence. Humans rarely type em dashes; they read as a machine tell, and this repo bans them in studio prose.

Say what the thing does. Specific beats grandiose every time. The full field guide, with the tell and the fix for each pattern, sits in [references/signs-of-ai-writing.md](references/signs-of-ai-writing.md). Read it before signing off any prose deliverable.

## Quality bar

Before returning prose, check:

- Every sentence sits in the active voice unless the passive earns its place, that is, the object is the real subject.
- No sentence states a thing in the negative that one positive word states better.
- No puffery, promotional adjective, filler opener, or hedge phrase survives.
- No em dash survives. A hyphen, comma, colon, or rewrite stands in its place.
- Every needless word is cut. Read each sentence and ask what it loses without each word.
