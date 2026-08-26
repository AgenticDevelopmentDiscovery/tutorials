# Tutorials — Sign-Up & Schedule

Student-led peer-teaching tutorials for the course. Each tutorial is a ~15-minute talk
(plus Q&A) prepared by **up to two students**, presented during a regular class call.

- **What's available:** browse the [topic menu](topics/README.md) — 36 briefs, one file per topic.
- **Claim a topic & pick a date:** edit [SCHEDULE.md](SCHEDULE.md) (see below).
- **Check your claim:** run `python3 check_schedule.py`.
- **Have your own idea?** Pitch it — see [Proposing your own topic](#proposing-your-own-topic).

## The rules

1. **One topic per team, one team per topic.** A tutorial can be claimed by one or two
   students. Once a topic number appears in the schedule, it's taken.
2. **Calls are Mondays and Wednesdays.** There is **no call on Labor Day**
   (Monday, Sep 7, 2026) — that row is blocked out in the schedule.
3. **At most 3 tutorial slots per call day.** When a date's three slots are filled,
   pick another date.
4. **First come, first served.** The schedule file is the single source of truth.
5. The schedule is **tentative** — dates may shift with the syllabus. Your claim on a
   topic is firm; your date is a plan.

## How to claim (step by step)

1. Open the [topic menu](topics/README.md) and pick an unclaimed topic
   (anything not yet listed in [SCHEDULE.md](SCHEDULE.md) is available — the checker
   script also prints the list).
2. Read the topic's brief in [topics/](topics/) to make sure you want it.
3. Edit [SCHEDULE.md](SCHEDULE.md): find a date with a free slot and fill the cell using
   the format below.
4. Run the checker from the repo root:

   ```
   python3 check_schedule.py
   ```

   It verifies your cell format, that the topic isn't double-claimed, that no day
   exceeds 3 slots, and prints which topics and slots remain open.
5. Commit / share your edit so the claim is visible to the cohort.

### Claim format

Fill an empty **Slot** cell in the schedule table with:

```
NN · First Last & First Last
```

- `NN` is the two-digit topic number (e.g. `05`).
- Use `&` between the two presenters; a solo presenter just omits the `& ...` part.
- Example: `13 · Ada Lovelace & Grace Hopper`

## Proposing your own topic

Not seeing what you want? You can pitch a topic of your own — it just needs **vetting
before it can be claimed**:

1. Write a short proposal (a few sentences): the topic, why it matters for agentic
   development, and what the hands-on/demo would show.
2. Send it to the instructor for vetting (or raise it on a call).
3. Once approved, add a brief to [topics/](topics/) as `tutorial-NN-your-topic.md`,
   using the next unused number (37+) and the same shape as the existing briefs
   (what it is · why it matters · key ideas · hands-on/demo · connections), and add it
   to the [topic menu](topics/README.md).
4. Claim it in [SCHEDULE.md](SCHEDULE.md) like any other topic — the same rules apply
   (up to two students, one team per topic, 3 slots per day).

## Picking a good date

The suggested arc (from the [topic menu](topics/README.md)):

- **Early term (Sep):** foundations, LLM/API topics (sections 1–2).
- **Mid term (Oct):** prompting/context, retrieval, agent construction (sections 3–5).
- **Late term (Nov–Dec):** evaluation, reliability, evolutionary topics (sections 6–7).

Claim early — the good dates go first, and your write-up must be shared with the cohort
**before** you present.

## What you're committing to

From the [topic menu](topics/README.md): expand the brief into a tutorial markdown file,
share it ahead of your date, present ~15 minutes (ideally with a live demo), and field
open Q&A. Graded per the tutorial rubric — conceptual mastery first.
