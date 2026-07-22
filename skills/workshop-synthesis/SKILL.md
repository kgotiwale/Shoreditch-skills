---
name: workshop-synthesis
description: Turn photos of an in-person customer workshop — sticky-note walls, affinity clusters, dot-voted boards, flipcharts, worksheets — into a stakeholder readout that separates what participants said from what we concluded. Use when given workshop photos and asked to "summarise the session", "write up the workshop", "synthesise the stickies", or produce a readout / debrief / findings doc from a co-creation, discovery, or customer workshop. Requires image input.
---

# Workshop Synthesis

Photos of a workshop wall are **raw data**, not findings. This skill walks the ladder from
data to findings to insight without letting the rungs blur — because the single failure mode
that destroys a readout is a confident theme name that no note on the wall actually supports.

## Required inputs — gate on these

**The photos.** One or more images. If none are attached, ask. Never synthesise from a verbal
recollection of a workshop; that is the person's memory, not the room's output.

**The session frame.** Ask for whatever is missing, in one batch, before Pass 1:

| Field | Why it matters |
|---|---|
| Session topic + date | Header; anchors the readout |
| Who was in the room (customers vs. internal, roughly how many) | A wall mixing customer and internal voices is two datasets |
| The prompt for each activity | A note answering "what frustrates you?" is not the same evidence as an unprompted one |
| What decision this readout feeds | Determines what gets surfaced vs. filed |

If the user can't supply the activity prompts, say so in Method & Limitations rather than
inventing them. A note without its prompt is a fragment.

## The three passes

**Never merge these.** Each pass has a different epistemic status, and collapsing them is how a
facilitator's pet theory ends up wearing a customer's clothes.

### Pass 1 — Transcribe (Data)

List what is *physically* on the board. No interpretation, no tidying, no grouping.

- **Go photo by photo, region by region.** Establish the overview shot first — the wide shot
  that shows the whole wall — then place the detail shots against it. Left to right, top to
  bottom.
- **Assign every note an ID.** `W1-N014` = wall 1, note 14. Every downstream claim cites these.
  Without IDs the readout is unfalsifiable, and a sceptic can't check your work against the photo.
- **Record position, not just text.** Where a note sits is data. Two clusters a metre apart are
  two topics; a note bridging them is a note bridging them. Capture cluster membership and any
  ordering the room imposed (chronological, cause-and-effect, a ranked column).
- **Transcribe the marks too:** arrows and their direction, boxes, underlines, circles, stars,
  crossings-out, colour. A crossed-out note is not deleted — it is *considered and rejected*, and
  it belongs in the record labelled as such.
- **Classify each note.** Not all notes are data:
  - `data` — a participant's contribution
  - `label` — a cluster header the room wrote (usually a different colour or framed)
  - `prompt` — the facilitator's question, printed or written up
  - `meta` — logistics, parking lot, agenda
  A cluster header is *the room's own theme name*. It is the most valuable note on the wall and
  must never be silently demoted into the pile it names.

**Never invent legibility.** Two distinct buckets, and they are not the same problem:

- `[illegible — looks like "…"]` — you cannot read it. A confident wrong guess poisons every
  theme built on it.
- `[legible but empty — "AI", "one-stop shop"]` — you can read it and it carries no recoverable
  meaning. This is not an OCR failure; it is a note that needs its author, and its author is gone.

Both go to the Ambiguity Ledger. Do not quietly drop either — an omitted note reads as a wall
that didn't have it.

*Note on OCR: handwriting recognition is unreliable enough that the CHI 2019 team who built a
sticky-note capture system declined to use it at all. No vendor publishes an accuracy figure.
Read the photos directly, flag aggressively, and treat every transcription as provisional.*

### Hand the illegible notes back — marked on the photo

A ledger line reading "W2-N009 — illegible" is useless on a wall of sixty notes: the person who
can decipher it cannot find it. **Mark it on the image instead**, and the ambiguity becomes a
question they can answer in one glance.

Do this at the **end of Pass 1, before clustering** — a theme built on a guessed note has to be
rebuilt anyway, so resolve the text while the cost is still low.

```bash
python3 ~/.claude/skills/workshop-synthesis/scripts/annotate.py --image WALL.jpg --marks marks.json
```

`marks.json` — boxes are `[x0, y0, x1, y1]` normalised 0–1 from the top-left, so they survive
whatever resizing happened while you read the photo:

```json
[
  {"id": "W1-N014", "box": [0.31, 0.22, 0.39, 0.30], "ask": "illegible — looks like 'latency'?"},
  {"id": "W1-N022", "box": [0.55, 0.61, 0.63, 0.69], "ask": "obscured by the note in front"}
]
```

Writes `WALL.annotated.jpg`: a magenta box and ID badge on each flagged note, plus a legend strip
listing what you need for each. One annotated image per wall — batch every uncertain note on that
wall into a single pass rather than asking one at a time.

**Make the `ask` specific.** "Illegible" tells them nothing; *"looks like 'latency' or 'latency
spike'?"* lets them confirm rather than re-read. Say what you think it is and what you're unsure
between.

**Flag generously.** The cost of marking a note you could have read is one glance. The cost of
guessing wrong is a theme that misrepresents a customer — and nobody downstream will know.

Then wait. Do not proceed to Pass 2 on guessed text; fold their answers into the transcription and
move the resolved notes out of the ledger. Anything they can't decipher either **stays** in the
ledger — the room couldn't read its own note, which is itself worth reporting.

### Pass 2 — Cluster (Findings)

**The room's clustering is authoritative. Do not re-cluster.**

If participants physically grouped notes, that grouping *is* a finding — it is the customers
telling you what belongs together, and it is better evidence than your reading of their
handwriting. Merging two of their clusters, or splitting one, destroys the thing you were there
to collect. If you believe the room grouped something wrongly, say so as a labelled observation;
do not silently fix it.

Only cluster yourself when the wall is genuinely ungrouped (a Post Up, a brain-dump, a fresh
flipchart). Then:

- **Group by content first, name after.** Naming first makes you sort into your own hypothesis.
- **No minimum cluster size.** A single note is a legitimate finding. NN/g is explicit: *"Don't
  discount a small cluster just because it has few sticky notes… they are a sign that diverse
  perspectives were represented."* One observation that exemplifies a known principle is real
  evidence — you just can't say how common it is.
- **A group over ~4 notes is a signal to split, not a strong theme.** *Contextual Design* caps
  first-level groups at four deliberately: it forces distinctions up into the labels instead of
  letting a fat pile masquerade as a finding.
- **A note may sit in two clusters.** Duplicate it and say you did.

**Name themes in the customer's voice, stating the issue — not the topic.**

- ❌ "Different ways of searching" — names the subject; you learn nothing without reading the notes
- ✅ "Recent stuff is best" — states the issue; the notes become examples of it

The label should read as though the customer were speaking to you from the wall.

### Pass 3 — Interpret (Insight)

Now, and only now, conclusions. Every one carries its evidence and its status.

**Tag the epistemic status of every statement:**

- **Observation** — on the wall, cites note IDs
- **Inference** — your reading of what it means; label it `[Inference]`
- **Recommendation** — what to do; label it, and say plainly it is meant to start the team's
  thinking, not to be the only or best answer
- **`Me:`** — anything you or a facilitator contributed that no participant said. Borrowed from
  NN/g's group-notetaking convention. If it isn't tagged, a reader will assume a customer said it.

**Counts scope evidence. They never project rates.**

- ❌ "70% of customers want X"
- ✅ "7 of the 10 participants in this session put a note about X on the wall"

And prefer to rank by **severity**, not headcount. "Three people couldn't find it" invites the
team to dismiss three people; "the registration button faded into the background" does not.

**Say what would confirm a single-source signal.** An isolated note isn't noise, but it isn't
proven either. Give it its own section and name the cheap test that would settle it.

## Dot voting — ask, don't guess

A photo of dots on a wall is **ambiguous**, and the two readings mean opposite things:

- **Dot voting** — participants prioritising among options. Result is a ranking.
- **Dot coding** — dots with pre-assigned meanings, eliciting reaction. **Not** a ranking, and
  reporting it as one is a fabrication.

Ask which it was. Then:

- **Report raw counts and weighted scores as different numbers**, and say which you're reporting.
  If the room used ranked dots (1/2/3 → 3/2/1 points), a raw count is the wrong answer.
- **Coloured dots need their legend.** Colour often encodes a criterion — feasibility vs. impact.
  Without the key photographed, the colours are undecodable. Say so rather than assuming.
- **Report dot counts as approximate when read from a photo.** Dots overlap, sit on edges, and
  hide under curl. If a count is close between two options, say it's close.
- Note known distortions if visible: **vote-splitting** across near-duplicate options, and
  clustering that suggests people voted after seeing others' dots.

## Output

```
# Workshop readout: [topic] — [date]

**Session:** [activity/activities] · [N participants — customer/internal split] · [walls covered]

## Headlines
[2–4 sentences. What a stakeholder who reads nothing else must know.]

## Themes

### [Theme name — the issue, in the customer's voice]
**Evidence:** [W1-N003, W1-N007, W1-N012] — verbatim, or the room's own cluster label
**Reading:** [Inference — what this means]
**Frequency:** [N notes, from ~M of P participants — or "concentrated in one activity" / "isolated"]
**Confidence:** [high / read-between-lines]

## Prioritisation
[Dot voting or coding — state which. Counts, weighting scheme, legend. Flag approximation.]

## Considered and rejected
[Crossed-out items, with what replaced them. The room's dead ends are findings.]

## Single-source signals
[Isolated notes worth keeping. For each: the cheap test that would confirm it.]

## Open questions from the room
[Every "?", disagreement marker, dangling arrow, unresolved parking-lot item.]

## Ambiguity ledger
| Note ID | Issue | What we can say |
|---|---|---|
| W2-N009 | [illegible — looks like "latency"?] | Needs the room to resolve |
| W1-N022 | [legible but empty — "synergy"] | Author unknown; not synthesisable |

## Recommendations
[Labelled as recommendations. Ranked by severity. Each traces to theme(s).]

## Method & limitations
[Photos received and coverage gaps. Missing prompts. Notes obscured or cut off.
Whether anything can be inferred about the wider customer population — usually: no.]
```

## Output — the deck (Shoreditch readout format)

The readout above is the **working document** — the evidence layer a sceptic can check. The
**client deliverable is a slide deck**, one section per workshop exercise, derived *from* that
readout. Never skip the readout and draft slides straight off the photos: the deck inherits its
credibility from the passes, and a slide with no note behind it is the exact failure mode this
skill exists to prevent.

**Per-exercise section — fixed running order:**

1. **Divider** — `Exercise N` + the activity name (e.g. "How might we…").
2. **Overview** — one 60–90 word paragraph. Name the groups/personas who worked the boards
   (Alex, Sam, Priya…), the prompt they worked from, and the clusters that emerged. Prose, not
   bullets. States what happened in the room, not yet what it means.
3. **Workshop findings** — the raw board photos in a grid. The evidence, shown not described.
4. **Key takeaways** — 4–6 themes. Each = a **heading stating the issue in the customer's voice**
   + **one supporting bullet** that grounds it in the wall (verbatim note fragments, the recurring
   phrase, or "appeared on all three boards"). This is Pass 2/3 rendered for stakeholders.
5. **4-point summary** — exactly **four** numbered points, each = a **bold headline** + **one
   sentence**. Fold minor/overlapping themes into the four; if a fifth is fighting to get in, it
   belongs *inside* one of the four, not beside it.

**Two-part exercises get two 4-pointers, at different altitudes.** A workshop exercise that runs
"How Might We" *then* an ideation round (Crazy 8's, sketching) is two datasets, and one shared
summary collapses them. Split it:

- **Pt.1 — the needs (problem space).** Titled *"What the room is telling us."* Four numbered
  *needs*, drawn from the HMW boards. Names the problem, not the fix.
- **Pt.2 — the solutions (solution space).** Titled *"What to build."* Four numbered *concepts*,
  drawn from the sketch boards. Each concept should trace back to a Pt.1 need.

Keep the framing distinct — a Pt.1 point is a need the customer has; a Pt.2 point is a thing we
would build. If a Pt.2 concept names no need from Pt.1, either the need is missing from Pt.1 or the
concept is a solution nobody asked for — flag it, don't smuggle it in.

**Rules that keep the deck honest:**

- **Ground every takeaway.** A heading with no note fragment, recurring phrase, or board-count
  under it is yours, not the room's — cut it or tag it `Me:`.
- **Headings state the issue, not the topic.** "Trust is a human problem" not "Trust." Same rule
  as Pass 2 theme naming — the heading should read as the customer speaking.
- **The 4-pointer is a forcing function, not a trim.** Four is the count because it forces
  distinctions up into the headlines. Don't pad to four; don't spill to five.
- **Overview says what happened; takeaways say what it means; the 4-pointer says what to do next.**
  Keep the three altitudes distinct across the three slide types — same discipline as the three
  passes, one rung per slide.
- **Cross-exercise echoes are worth stating** ("confirms the North Star from Exercise 2") — but
  only when a note actually echoes it.

Build the deck slides as an HTML artifact matching the studio layout only when asked; default to
delivering the copy, structured under the five headings above, so it drops into the existing deck.

## Quality bar

Before returning, check:

- Could a sceptic take any theme, open the photo, and find the notes? If a claim has no note IDs,
  it is yours, not the customer's — tag it `Me:` or cut it.
- Did the room's own cluster labels survive as labels?
- Is every illegible note flagged rather than guessed?
- Does any sentence project from this room to "customers" generally? Remove it.
- Are rejected ideas and open questions present? A readout with no dead ends and no disagreement
  is a readout that has been tidied into a story.
- Does the deck's 4-point summary hold exactly four needs, each traceable to a takeaway that is
  traceable to notes? Does every takeaway heading state an issue, not a topic? Do Overview /
  takeaways / 4-pointer stay at their three altitudes (happened / means / do next)?

## Anti-patterns

- **Cleaning up the room's thinking** into what it should have decided.
- **Verbatim laundering** — paraphrasing a note and presenting it in quote marks. If it has
  quotes, it is a real note, transcribed.
- **Silent dropping** — omitting illegible or awkward notes so the wall looks coherent.
- **Flattening the wall to a list** — position, adjacency, and ordering are data.
- **Treating a facilitator's prompt as a customer's idea.** A cued note is weaker evidence than a
  spontaneous one. Both count; they don't count equally.
- **Theming by feature instead of by need.** "Wants a dashboard" is a solution someone guessed;
  "can't tell if it worked without asking someone" is the need underneath.
- **Entertainment bias** — over-weighting the loudest, funniest, or most quotable note.

## Photo capture — for next time

Little published method exists here; most of this is authored from practice rather than cited.
The one solid source is Tomomi Sasaki's *How to get the workshop photos you need*:

- **One wide shot per wall first** — it is the orientation key that positions every detail shot.
  It is not a duplicate. Then detail shots, **left to right, camera held parallel to the wall,
  angle unchanged** so they can be stitched.
- **Zoom until handwriting is readable.** That is the only correct zoom level.
- **Un-overlap the notes before shooting.** A photo of stickies stuck on top of each other is not
  documentation.
- **Shoot when the activity is finished**, not mid-flight.
- **One photo per worksheet.**
- Photograph promptly — NN/g notes that stickies fall off walls overnight and cleaners erase boards.
- Authored additions, not found in any source: **photograph the legend** for any colour scheme,
  and capture the **activity prompt** in-frame or in a paired shot. Both are routinely lost, and
  both are unrecoverable afterwards.
- Get consent before photographing participants.

## References

- [NN/g — Affinity Diagramming](https://www.nngroup.com/articles/affinity-diagram/) — no minimum cluster size
- [NN/g — Data vs. Findings vs. Insights](https://www.nngroup.com/articles/data-findings-insights-differences/) — the three-rung ladder
- [NN/g — Group Notetaking](https://www.nngroup.com/articles/group-notetaking/) — the `Me:` convention
- [NN/g — Dot Voting](https://www.nngroup.com/articles/dot-voting/) · [Dot Coding](https://www.nngroup.com/articles/dot-coding/)
- [NN/g — Actionable Usability Findings](https://www.nngroup.com/articles/actionable-usability-findings/) — label recommendations
- [NN/g — Qualitative Rigor](https://www.nngroup.com/articles/qualitative-rigor/) — why singletons survive
- [NN/g — The True Score](https://www.nngroup.com/articles/true-score/) — counts scope, don't project
- Beyer & Holtzblatt, *Contextual Design*, ch. 9 — four-note cap; labels in the customer's voice
- [Sasaki — How to get the workshop photos you need](https://tomomiq.medium.com/how-to-get-the-workshop-photos-you-need-76ad338e68c3)
- [Affinity Lens, CHI 2019](https://chi2021.acm.org/contents/wp-content/uploads/example_papers/Subramonyam-LaTeX-Single-Column.pdf) — position is data; handwriting OCR avoided
