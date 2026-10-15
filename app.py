
import streamlit as st

st.set_page_config(
    page_title="Discovery Ladder",
    page_icon="D",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# DESIGN AND COLOUR SYSTEM
# -----------------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
    --page: #F7F7F3;
    --paper: #FFFFFF;
    --ink: #263329;
    --heading: #202820;
    --muted: #59665B;
    --green: #426749;
    --green-dark: #304F36;
    --line: #D9DED5;
    --soft-green: #E9EDE5;
}

.stApp {
    background: var(--page);
    color: var(--ink);
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1050px;
    padding-top: 2.5rem;
    padding-bottom: 4rem;
}

h1, h2, h3, h4 {
    font-family: 'Manrope', sans-serif !important;
    color: var(--heading) !important;
    letter-spacing: -0.035em;
}

p, li, label, .stMarkdown, .stCaption {
    color: var(--ink);
}

.hero {
    padding: 2.6rem 0 2.1rem;
    border-bottom: 1px solid var(--line);
    margin-bottom: 2.3rem;
}

.hero-title {
    font-family: 'Manrope', sans-serif;
    font-size: clamp(2.5rem, 6vw, 4.5rem);
    font-weight: 800;
    line-height: 1.06;
    letter-spacing: -0.065em;
    color: var(--heading);
    max-width: 780px;
}

.hero-description {
    font-size: 1.08rem;
    line-height: 1.8;
    color: var(--muted);
    max-width: 680px;
    margin-top: 1.2rem;
}

.eyebrow, .section-number, .evidence-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.75rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #526653 !important;
}

.eyebrow {
    margin-bottom: 0.9rem;
}

.section-number {
    margin-bottom: 0.45rem;
}

.section-intro {
    color: var(--muted) !important;
    line-height: 1.75;
    max-width: 720px;
    margin-bottom: 1.5rem;
}

.case-strip {
    background: var(--soft-green);
    color: var(--ink);
    border-left: 3px solid var(--green);
    padding: 1.1rem 1.3rem;
    margin: 1rem 0 1.5rem;
    line-height: 1.7;
}

.evidence-card {
    background: var(--paper);
    border: 1px solid var(--line);
    border-radius: 8px;
    padding: 1.2rem 1.3rem;
    min-height: 145px;
}

.evidence-card-title {
    font-family: 'Manrope', sans-serif;
    font-weight: 700;
    font-size: 1.08rem;
    color: var(--heading);
    margin: 0.7rem 0 0.55rem;
}

.evidence-card-description {
    font-size: 0.87rem;
    line-height: 1.6;
    color: var(--muted);
}

.evidence-label {
    margin-bottom: 0.7rem;
}

.small-note {
    font-size: 0.84rem;
    line-height: 1.7;
    color: var(--muted) !important;
}

.closing {
    border-top: 1px solid var(--line);
    margin-top: 2rem;
    padding-top: 1.2rem;
    color: var(--muted);
    font-size: 0.83rem;
    line-height: 1.7;
}

/* Expander panels */
div[data-testid="stExpander"] {
    border: 1px solid var(--line);
    border-radius: 8px;
    background: var(--paper);
}

div[data-testid="stExpander"] summary,
div[data-testid="stExpander"] summary p {
    color: var(--ink) !important;
}

/* Radio buttons and decision options */
div[data-testid="stRadio"] label,
div[data-testid="stRadio"] label p,
div[data-testid="stRadio"] label span,
div[data-testid="stCheckbox"] label,
div[data-testid="stCheckbox"] label p {
    color: var(--ink) !important;
}

/* Widget labels */
div[data-testid="stWidgetLabel"] p,
div[data-testid="stWidgetLabel"] label,
div[data-testid="stWidgetLabel"] {
    color: var(--ink) !important;
}

/* Dropdown control */
div[data-testid="stSelectbox"] > div > div,
div[data-baseweb="select"] > div {
    background-color: var(--paper) !important;
    border-color: #BFC9BC !important;
}

div[data-baseweb="select"] *,
div[data-testid="stSelectbox"] label {
    color: var(--ink) !important;
}

/* Dropdown menu options */
div[role="listbox"],
div[role="option"] {
    background-color: var(--paper) !important;
    color: var(--ink) !important;
}

div[role="option"] *,
div[role="listbox"] * {
    color: var(--ink) !important;
}

/* Text inputs and text areas */
.stTextInput input,
.stTextArea textarea {
    color: var(--ink) !important;
    background-color: var(--paper) !important;
    border-color: #BFC9BC !important;
    caret-color: var(--ink);
}

.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #687568 !important;
    opacity: 1;
}

/* Buttons */
div.stButton > button {
    color: #FFFFFF !important;
    background-color: var(--green);
    border: 1px solid var(--green);
    border-radius: 5px;
    font-weight: 600;
}

div.stButton > button p,
div.stButton > button span {
    color: #FFFFFF !important;
}

div.stButton > button:hover {
    background-color: var(--green-dark);
    border-color: var(--green-dark);
}

/* Links */
.stApp a {
    color: var(--green-dark) !important;
    text-decoration-thickness: 1px;
    text-underline-offset: 3px;
}

.stApp a:hover {
    color: #243E29 !important;
}

/* Progress bars and dividers */
hr {
    border-color: var(--line) !important;
}

[data-testid="stProgressBar"] > div {
    background-color: #DDE5D9;
}

[data-testid="stProgressBar"] > div > div {
    background-color: var(--green);
}

/* Feedback messages */
div[data-testid="stAlert"] p {
    color: var(--ink) !important;
}

/* Captions */
.stCaption, [data-testid="stCaptionContainer"] {
    color: var(--muted) !important;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# HEADER
# -----------------------------

st.markdown("""
<div class="hero">
    <div class="eyebrow">An exploration of AI, genetics and evidence</div>
    <div class="hero-title">Discovery is not a prediction.</div>
    <div class="hero-description">
        A model can identify a pattern. A researcher has to work out
        what it means. Follow a real genetic discovery and explore
        the evidence that turns a possible clue into a scientific claim.
    </div>
</div>
""", unsafe_allow_html=True)


# -----------------------------
# 01 — THE PROCESS
# -----------------------------

st.markdown(
    '<div class="section-number">01 / THE PROCESS</div>',
    unsafe_allow_html=True
)

st.header("From clue to conclusion")

st.markdown("""
<div class="section-intro">
The process is rarely a straight line. Researchers move between
ideas, data and experiments, revising their explanations when the
evidence demands it.
</div>
""", unsafe_allow_html=True)

stages = [
    ("01", "Prediction", "A possible pattern is identified."),
    ("02", "Hypothesis", "A testable explanation is proposed."),
    ("03", "Experiment", "Evidence is collected to test it."),
    ("04", "Conclusion", "The results are evaluated.")
]

cols = st.columns(4)

for col, (number, title, description) in zip(cols, stages):
    with col:
        st.markdown(f"""
        <div class="evidence-card">
            <div class="evidence-label">{number}</div>
            <div class="evidence-card-title">{title}</div>
            <div class="evidence-card-description">{description}</div>
        </div>
        """, unsafe_allow_html=True)

st.write("")

stage_choice = st.selectbox(
    "Look closer at a stage",
    ["Prediction", "Hypothesis", "Experiment", "Conclusion"]
)

stage_details = {
    "Prediction": (
        "A prediction points to something worth investigating.",
        "What data was used? How reliable is the method? Could another "
        "explanation produce the same pattern?"
    ),
    "Hypothesis": (
        "A hypothesis explains how or why a finding might occur.",
        "Can the explanation be tested? What result would support it, "
        "and what result would challenge it?"
    ),
    "Experiment": (
        "An experiment or further analysis tests a specific claim.",
        "Does the method measure what researchers want to know? "
        "Are there suitable controls or alternative explanations?"
    ),
    "Conclusion": (
        "A conclusion should match the strength of the evidence.",
        "Do different kinds of evidence agree? Has the finding been "
        "replicated? What remains uncertain?"
    )
}

explanation, question = stage_details[stage_choice]

st.markdown(f"**{explanation}**")
st.write(question)

st.divider()


# -----------------------------
# 02 — THE RNU4-2 CASE
# -----------------------------

st.markdown(
    '<div class="section-number">02 / RESEARCH CASE</div>',
    unsafe_allow_html=True
)

st.header("A clue in an overlooked part of the genome")

st.markdown("""
<div class="section-intro">
In 2024, independent research teams linked variants in RNU4-2
to a neurodevelopmental disorder. Their work showed why researchers
need to look beyond the familiar parts of the genome.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="case-strip">
    <strong>The question:</strong> How can a change in a small RNA gene
    be connected to a person's condition — and what evidence makes
    that connection convincing?
</div>
""", unsafe_allow_html=True)

st.subheader("Why RNU4-2 was different")

st.write("""
Many genetic tests focus on protein-coding genes. RNU4-2 does not
encode a protein. It produces U4 small nuclear RNA, which is part
of the spliceosome — the machinery cells use to process RNA.
""")

st.write("""
Researchers identified disease-associated variants in RNU4-2.
One team also examined RNA sequencing data and found evidence of
abnormal RNA splicing. This helped connect the genetic finding
to a possible biological effect.
""")

st.markdown("""
<div class="small-note">
Scientific distinction: the original RNU4-2 studies used genomic
analysis and experimental evidence. They are not examples of AI
discovering the gene. This project explores how computational
predictions can support investigations like these.
</div>
""", unsafe_allow_html=True)

st.write("")

st.markdown(
    "[Read the original Nature paper]"
    "(https://www.nature.com/articles/s41586-024-07773-7)"
    " · "
    "[Read the independent Nature Medicine paper]"
    "(https://www.nature.com/articles/s41591-024-03085-5)"
)

st.divider()


# -----------------------------
# 03 — EVIDENCE DESK
# -----------------------------

st.markdown(
    '<div class="section-number">03 / EVIDENCE DESK</div>',
    unsafe_allow_html=True
)

st.header("What does the evidence actually tell us?")

st.markdown("""
<div class="section-intro">
Choose a file to examine one part of the research. Each answers
a different question; none should be interpreted in isolation.
</div>
""", unsafe_allow_html=True)

evidence_file = st.radio(
    "Evidence files",
    [
        "01  Genetic pattern",
        "02  Biological mechanism",
        "03  Experimental evidence",
        "04  Limits of the finding"
],
    label_visibility="collapsed"
)

if evidence_file == "01  Genetic pattern":
    st.markdown("#### A pattern across affected individuals")

    st.write("""
    Researchers found variants in a specific region of RNU4-2 in
    people with neurodevelopmental disorders. In one Nature study,
    a recurrent single-base insertion was particularly common among
    the affected individuals studied.
    """)

    st.markdown("**What this supports**")
    st.write(
        "The repeated genetic pattern gives researchers a strong "
        "reason to investigate whether the variants are related to the disorder."
    )

    st.markdown("**What it cannot show by itself**")
    st.write(
        "A pattern alone does not fully explain how a variant affects "
        "cells or establish every detail of the disease mechanism."
    )

elif evidence_file == "02  Biological mechanism":
    st.markdown("#### From genetic change to biological effect")

    st.write("""
    U4 small nuclear RNA is part of the spliceosome, which helps remove
    introns from pre-messenger RNA. Changes to this system can alter
    how RNA is processed.
    """)

    st.markdown("**What this supports**")
    st.write(
        "A biologically plausible explanation for how variants could "
        "affect cellular processes."
    )

    st.markdown("**What researchers still need**")
    st.write(
        "Evidence that connects the proposed mechanism to the observed "
        "condition, while considering other possible explanations."
    )

elif evidence_file == "03  Experimental evidence":
    st.markdown("#### Testing what happens to RNA")

    st.write("""
    The Nature team examined RNA sequencing data and reported
    abnormal splicing patterns associated with RNU4-2 variants.
    This offered evidence that the genetic changes affected RNA processing.
    """)

    st.markdown("**Why this matters**")
    st.write(
        "The researchers were not relying on a genetic association alone. "
        "They also investigated a biological effect consistent with their explanation."
    )

    st.markdown("**A useful distinction**")
    st.write(
        "An experiment can strengthen a claim, but results still need "
        "to be interpreted in context and alongside other evidence."
    )

elif evidence_file == "04  Limits of the finding":
    st.markdown("#### What should we be careful about?")

    st.write("""
    A strong scientific claim depends on the full body of evidence,
    not one statistic or one experiment. Different studies may examine
    different groups, methods and questions.
    """)

    st.markdown("**Questions a researcher should ask**")
    st.write("- Do independent studies support the finding?")
    st.write("- Does the biological evidence fit the genetic results?")
    st.write("- Which conclusions are supported, and which remain uncertain?")

st.divider()


# -----------------------------
# 04 — RESEARCH DECISION
# -----------------------------

st.markdown(
    '<div class="section-number">04 / YOUR DECISION</div>',
    unsafe_allow_html=True
)

st.header("Suppose AI finds the next clue.")

st.write("""
A model flags a genetic variant and predicts that it may disrupt
RNA splicing. You are on the research team. What do you do next?
""")

decision = st.radio(
    "Your next move",
    [
        "Report that the variant causes the disease.",
        "Discard the prediction because AI is not reliable.",
        "Investigate the prediction using relevant genetic and experimental evidence."
    ],
    key="decision",
    label_visibility="collapsed"
)

if st.button("Review decision"):
    if decision.startswith("Investigate"):
        st.success("The strongest next step is to investigate.")

        st.write("""
        The prediction helps prioritise a question. Researchers can then
        examine supporting genetic evidence, investigate possible biological
        effects, and assess alternative explanations. The appropriate tests
        depend on the specific claim being evaluated.
        """)

    elif decision.startswith("Report"):
        st.warning("The conclusion goes further than the evidence.")

        st.write("""
        A model's prediction does not establish that a variant causes
        a disease. Further evidence is needed to assess the claim.
        """)

    else:
        st.warning("You may be discarding a useful lead.")

        st.write("""
        AI predictions can be useful when treated critically. The goal
        is neither to trust nor dismiss a model automatically, but to
        test whether its prediction holds up.
        """)

st.divider()


# -----------------------------
# 05 — FIELD NOTES
# -----------------------------

st.markdown(
    '<div class="section-number">05 / FIELD NOTES</div>',
    unsafe_allow_html=True
)

st.header("What would convince you?")

st.write("""
Imagine you have a genetic clue, a possible biological explanation,
and one experiment supporting it. What would you want to know before
accepting the conclusion?
""")

reflection = st.text_area(
    "Your notes",
    placeholder="What evidence would you look for next, and why?",
    height=120,
    label_visibility="collapsed"
)

if st.button("Keep field note"):
    if reflection.strip():
        st.session_state["field_note"] = reflection.strip()
        st.success("Field note saved for this session.")
    else:
        st.warning("Write a note before saving.")

if "field_note" in st.session_state:
    st.markdown("**Your saved field note**")
    st.write(st.session_state["field_note"])


# -----------------------------
# FOOTER
# -----------------------------

st.markdown("""
<div class="closing">
    DISCOVERY LADDER · An educational Replicate exploring computational
    predictions, genetics and scientific evidence.<br>
    This project is for learning and is not a diagnostic tool.
</div>
""", unsafe_allow_html=True)
