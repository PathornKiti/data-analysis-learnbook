# Peer review guide

Reviewing someone else's project teaches you as much as building your own. Be **kind, specific and useful**.

## Ground rules
* Review the **work**, not the person. Describe what you saw ("I couldn't tell which dataset was used"), not what they are ("sloppy").
* Be specific: point at a file, a chart, a sentence.
* For every problem, suggest one **concrete improvement**.
* Name at least **two strengths**. They're real, and the author needs to know what to keep.

## Step 1: Fresh-clone test (15 minutes)
Without asking the author for help, follow their README in a **new folder and a new virtual environment**.
- [ ] I could install the dependencies using only the README
- [ ] `python run_analysis.py` (or the command they documented) ran without errors
- [ ] The results I got match the numbers in their README/report
- [ ] `pytest` passes
- [ ] `python projects/check_project.py <their project>` shows no ❌

If something failed, copy the exact error message. That is gold for the author.

## Step 2: Read the report (15 minutes)
- [ ] After the summary alone, I can say what the question was and what they found
- [ ] Every chart has a title that states a message, labelled axes and units
- [ ] Estimates come with intervals; sample sizes are given; effect sizes are discussed
- [ ] The claims are no stronger than the evidence (no unsupported "causes", "proves")
- [ ] The limitations section names *specific* risks (not just "more data would help")
- [ ] I'd be comfortable with the ethics checklist as written

## Step 3: Read the code (15 minutes)
- [ ] Logic lives in `src/` modules; the notebook mostly imports and tells the story
- [ ] Functions are small, have docstrings, and don't modify their inputs
- [ ] I found no copy-pasted blocks that should be a function
- [ ] The tests check things that matter (formulas, edge cases), not just that code runs
- [ ] Seeds are set; paths are relative

## Feedback form

**Project / author:**   **Reviewer:**

1. **Two strengths** (specific):
2. **The single most important thing to improve** (and how):
3. **One claim I'm not convinced by**, and what evidence would convince me:
4. **One test I'd add** (what bug would it catch?):
5. **Something I learned from this project:**
6. **The error messages / places I got stuck** during the fresh-clone test:

## Receiving feedback
* Read it all before reacting. Thank the reviewer.
* Sort suggestions into **must fix** (it breaks or misleads), **should fix** (clarity), **could fix** (taste).
* If you disagree, that's fine, but make sure it's because you *understood* the point, and consider whether a stranger would be confused in the same way.
