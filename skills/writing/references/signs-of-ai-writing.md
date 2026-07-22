# Signs of AI Writing

Condensed from Wikipedia's field guide for detecting AI-generated content. These patterns emerge because LLMs regress to statistical means, replacing specific facts with generic, positive-sounding language.

## Core mechanism: regression to the mean

LLMs infer statistically likely continuations. Specific, unusual, nuanced facts (rare in training data) get replaced by generic, positive descriptions (common in training data). The subject becomes at once less specific and more exaggerated.

## Pattern categories

### 1. Undue emphasis on symbolism, legacy, importance

Words to watch: stands/serves as, is a testament/reminder, plays a vital/significant/crucial/pivotal role, underscores/highlights its importance, reflects broader, symbolizing its ongoing/enduring/lasting impact, key turning point, indelible mark, deeply rooted, profound heritage, steadfast dedication.

LLMs puff up importance by claiming arbitrary aspects represent broader topics. Even mundane subjects get legacy statements.

### 2. Superficial analyses via present participles

Words to watch: ensuring..., highlighting..., emphasizing..., reflecting..., underscoring..., showcasing..., aligns with..., contributing to...

The strongest tell is an inanimate thing made the subject of these verbs: "This fact highlights..." A fact cannot highlight anything; that is a narrator's unsubstantiated claim about what something means.

### 3. Promotional and advertisement-like language

Words to watch: continues to captivate, groundbreaking (figurative), stunning natural beauty, enduring/lasting legacy, nestled, in the heart of, boasts a, rich tapestry, vibrant community.

Neutral topics get tourism-brochure treatment. Companies sound like TV commercials.

### 4. Didactic disclaimers

Words to watch: it's important/critical/crucial to note/remember/consider, may vary, it should be noted.

LLMs lecture the reader about what is "important to remember": safety warnings, jurisdiction variations, controversial-topic hedging.

### 5. Forced summaries and conclusions

Words to watch: In summary, In conclusion, Overall.

LLMs add conclusion sections and restate core ideas at paragraph ends, even when the text is short enough not to need summarizing.

### 6. "Despite challenges" formula

Pattern: "Despite its [positive words], [subject] faces challenges...", then a vague positive assessment, then speculation about future initiatives. Rigid outline structure with "Challenges and Legacy" or "Future Outlook" sections.

## Overused AI vocabulary

High-confidence indicators. Co-occurrence is the strongest tell: where one appears, others follow.

| Category | Words |
|----------|-------|
| Emphasis | crucial, vital, pivotal, key (adj), notably |
| Legacy | testament, enduring, indelible, profound |
| Analysis | delve, multifaceted, nuanced, intricate, intricacies |
| Action | leverage, foster, enhance, streamline, underscore, underpin |
| Texture | tapestry, landscape, realm, vibrant, seamless, robust |
| Connection | interplay, aligns with, shed light on, garnered |
| Display | showcasing, highlighting, emphasizing, reflecting |

## Punctuation tells

**Em dashes (—).** LLMs overuse the em dash where a human would use a hyphen (-), a comma, or two sentences. Most developers never type one. If generated text reads "structure — not chaos", rewrite to "structure, not chaos" or "structure. Not chaos." One em dash in a doc is suspicious. Three is a pattern.

## Structural tells

- **List-heavy structure.** Bullet points and numbered lists where prose reads more naturally.
- **Bold overuse.** Bolding every other phrase for artificial emphasis.
- **Emoji decoration.** Emojis on headers or list items.
- **Parallel exhaustiveness.** "Whether X, Y, or Z" constructions that try to cover every case.
- **Triple adjective chains.** "comprehensive, innovative, and forward-thinking".

## Formatting tells

- Headers with flowery language ("A Rich Tapestry of Cultural Heritage").
- Sections suspiciously uniform in length.
- Every paragraph following the same structure (claim, evidence, significance).
- Excessive transitional phrases between paragraphs.

## How to fix

- Delete puffery. If removing a sentence changes nothing, remove it.
- Replace generic claims with specific facts.
- Use the active voice with concrete subjects.
- Cut present-participle analysis phrases entirely.
- Remove "it's important to note" and similar hedges.
- Let the reader draw their own conclusions about significance.
- Vary sentence and paragraph structure.

Source: Wikipedia's "Signs of AI-generated content" field guide, developed by editors who review thousands of AI-generated submissions.
