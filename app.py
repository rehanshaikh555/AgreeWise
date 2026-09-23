"""
AgreeWise
Intelligent Privacy Policy & Terms Analyzer

UI shell only.
Core analysis remains isolated until the UI is complete.
"""

import streamlit as st

from core.analyzer import analyze_document
from extraction import extract_and_normalize
from ui.styles import inject_global_styles
from ui.components import (
    brand,
    document_visual,
    feature_cards,
    hero,
    topbar,
    upload_header,
)



def initialize_state():
    defaults = {
        "page": "home",
        "uploaded_file": None,
        "pasted_text": "",
        "analysis_result": None,
        "analysis_error": None,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def sidebar():
    with st.sidebar:

        brand()

        st.markdown(
            '<div class="aw-nav-label">Workspace</div>',
            unsafe_allow_html=True,
        )

        if st.button(
            "⌂  Home",
            use_container_width=True,
        ):
            st.session_state.page = "home"
            st.rerun()

        if st.button(
            "◫  My Analyses",
            use_container_width=True,
        ):
            st.session_state.page = "analyses"
            st.rerun()

        if st.button(
            "◎  How It Works",
            use_container_width=True,
        ):
            st.session_state.page = "how"
            st.rerun()

        st.markdown(
            '<div class="aw-nav-label">System</div>',
            unsafe_allow_html=True,
        )

        if st.button(
            "⚙  Settings",
            use_container_width=True,
        ):
            st.session_state.page = "settings"
            st.rerun()

        st.html(
            """
            <div class="aw-privacy-card">

                <div class="aw-privacy-icon">
                    <span>✓</span>
                </div>

                <div class="aw-privacy-content">
                    <div class="aw-privacy-title">
                        Your Privacy
                    </div>

                    <div class="aw-privacy-text">
                        Documents are designed to be processed
                        without unnecessary permanent storage.
                    </div>
                </div>

                <div class="aw-privacy-pulse"></div>

            </div>
            """
        )


def home():
    topbar()

    left, right = st.columns(
        [1.15, 0.85],
        gap="large",
    )

    with left:
        hero()

    with right:
        document_visual()

    upload_header()

    uploaded = st.file_uploader(
        "Upload document",
        type=[
            "pdf",
            "docx",
            "txt",
            "png",
            "jpg",
            "jpeg",
        ],
        label_visibility="collapsed",
        key="agreewise_uploader",
    )

    st.markdown(
        """
        <div style="
            text-align:center;
            color:#52525B;
            font-size:.75rem;
            margin:1rem 0 .6rem;
        ">
            or paste your document text
        </div>
        """,
        unsafe_allow_html=True,
    )

    pasted_text = st.text_area(
        "Paste document text",
        height=180,
        placeholder=(
            "Paste a Privacy Policy, Terms & Conditions, "
            "Cookie Policy or User Agreement here..."
        ),
        label_visibility="collapsed",
        key="policy_input",
    )

    if uploaded is not None:
        st.session_state.uploaded_file = uploaded

        st.markdown(
            f"""
            <div class="aw-card">
                <div class="aw-card-title">
                    Document ready
                </div>
                <div class="aw-card-text">
                    {uploaded.name}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    has_input = (
        uploaded is not None
        or bool(pasted_text.strip())
    )

    if has_input:
        if st.button(
            "Analyze Document",
            type="primary",
            use_container_width=True,
        ):
            st.session_state.pasted_text = pasted_text
            st.session_state.analysis_result = None
            st.session_state.analysis_error = None

            if uploaded is not None:
                st.session_state.uploaded_file = uploaded

            try:
                if uploaded is not None:
                    source = uploaded.getvalue()
                    filename = uploaded.name
                    extracted_text = extract_and_normalize(
                        source,
                        filename,
                    )
                else:
                    extracted_text = extract_and_normalize(
                        pasted_text,
                        "pasted_document.txt",
                    )

                st.session_state.analysis_result = analyze_document(
                    extracted_text
                )
                st.session_state.page = "results"

            except Exception as exc:
                st.session_state.analysis_error = str(exc)
                st.session_state.page = "analysis"

            st.rerun()

    feature_cards()


def analysis():
    topbar()

    st.markdown(
        """
        <div class="aw-hero">

            <div class="aw-kicker">
                <span>●</span> ANALYSIS
            </div>

            <h1 class="aw-title">
                AgreeWise is
                <span class="aw-gradient">
                    reading.
                </span>
            </h1>

            <p class="aw-subtitle">
                Your document is being prepared for
                structured analysis.
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    stages = [
        ("✓", "Extracting document text", "Complete"),
        ("✓", "Detecting language", "Complete"),
        ("✓", "Identifying important clauses", "Complete"),
        ("◉", "Checking data practices", "Processing"),
        ("○", "Preparing your insights", "Waiting"),
    ]

    for icon, title, status in stages:

        status_class = (
            "color:#A78BFA;"
            if status == "Processing"
            else "color:#71717A;"
        )

        icon_color = (
            "#6EE7B7"
            if status == "Complete"
            else "#A78BFA"
            if status == "Processing"
            else "#52525B"
        )

        st.markdown(
            f"""
            <div class="aw-card" style="
                display:flex;
                align-items:center;
                justify-content:space-between;
                padding:17px 20px;
                margin-bottom:10px;
            ">

                <div style="
                    display:flex;
                    align-items:center;
                    gap:12px;
                ">

                    <span style="
                        color:{icon_color};
                        font-weight:700;
                    ">
                        {icon}
                    </span>

                    <span style="
                        color:#D4D4D8;
                        font-size:.86rem;
                    ">
                        {title}
                    </span>

                </div>

                <span style="
                    {status_class}
                    font-size:.72rem;
                ">
                    {status}
                </span>

            </div>
            """,
            unsafe_allow_html=True,
        )

    if st.button(
        "Continue to Results",
        type="primary",
        use_container_width=True,
    ):
        st.session_state.page = "results"
        st.rerun()


def results():
    topbar()

    result = st.session_state.get("analysis_result")
    error = st.session_state.get("analysis_error")

    if error:
        st.html(
            """
            <div class="aw-hero">
                <div class="aw-kicker">ANALYSIS ERROR</div>
                <h1 class="aw-title">
                    We couldn't
                    <span class="aw-gradient">analyze.</span>
                </h1>
                <p class="aw-subtitle">
                    The document could not be processed successfully.
                </p>
            </div>
            """,
        )

        st.error(error)

        if st.button("← Back to Home", use_container_width=True):
            st.session_state.page = "home"
            st.session_state.analysis_error = None
            st.rerun()

        return

    if not result:
        st.html(
            """
            <div class="aw-hero">
                <div class="aw-kicker">NO ANALYSIS</div>
                <h1 class="aw-title">
                    Nothing to
                    <span class="aw-gradient">show yet.</span>
                </h1>
                <p class="aw-subtitle">
                    Start an analysis from the home page first.
                </p>
            </div>
            """,
        )

        if st.button("← Back to Home", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()

        return

    document_type = result.get("document_type", {})
    language = result.get("language", {})
    metadata = result.get("metadata", {})
    findings = result.get("findings", [])

    st.html(
        """
        <div class="aw-hero">

            <div class="aw-kicker">
                ANALYSIS COMPLETE
            </div>

            <h1 class="aw-title">
                Your document
                <span class="aw-gradient">
                    insights.
                </span>
            </h1>

            <p class="aw-subtitle">
                AgreeWise identified important data practices
                and connected each finding to source evidence.
            </p>

        </div>
        """
    )

    info_columns = st.columns(4)

    info = [
        (
            "Document Type",
            document_type.get("name", "Unknown"),
        ),
        (
            "Language",
            language.get("name", "Unknown"),
        ),
        (
            "Words",
            str(metadata.get("word_count", 0)),
        ),
        (
            "Findings",
            str(len(findings)),
        ),
    ]

    for column, (label, value) in zip(info_columns, info):
        with column:
            st.html(
                f"""
                <div class="aw-card" style="min-height:120px;">
                    <div class="aw-card-text">
                        {label}
                    </div>

                    <div class="aw-card-title" style="
                        margin-top:.55rem;
                        font-size:1.05rem;
                    ">
                        {value}
                    </div>
                </div>
                """,
            )

    st.html(
        """
        <div class="aw-section">
            <div class="aw-section-title">
                What AgreeWise found
            </div>

            <div class="aw-section-subtitle">
                Categories below are based on detected clauses
                in the analyzed document.
            </div>
        </div>
        """
    )

    if not findings:
        st.info(
            "No supported privacy or data-practice categories "
            "were detected in this document."
        )
    else:
        columns = st.columns(4)

        for index, finding in enumerate(findings):
            with columns[index % 4]:
                name = finding.get("name", "Unknown")
                match_count = finding.get("match_count", 0)

                st.html(
                    f"""
                    <div class="aw-card">

                        <div class="aw-card-icon">
                            ✓
                        </div>

                        <div class="aw-card-title">
                            {name}
                        </div>

                        <div class="aw-card-text">
                            {match_count} detected signal
                            {"s" if match_count != 1 else ""}
                        </div>

                    </div>
                    """,
                )

    st.html(
        """
        <div class="aw-section">

            <div class="aw-section-title">
                Evidence
            </div>

            <div class="aw-section-subtitle">
                Every finding is connected to the exact source
                sentence that triggered the analysis.
            </div>

        </div>
        """
    )

    for finding in findings:
        name = finding.get("name", "Unknown")
        matches = finding.get("matches", [])
        evidence_items = finding.get("evidence", [])

        with st.expander(
            f"{name} — {len(evidence_items)} evidence "
            f"{'item' if len(evidence_items) == 1 else 'items'}"
        ):
            if matches:
                st.markdown("**Detected signals**")

                st.markdown(
                    " · ".join(
                        f"`{match}`"
                        for match in matches
                    )
                )

            if not evidence_items:
                st.info("No source evidence was returned.")
                continue

            for evidence_index, evidence in enumerate(evidence_items):
                context_label = evidence.get(
                    "context_label",
                    "Context unavailable",
                )
                sentence = evidence.get(
                    "sentence",
                    "",
                )
                evidence_matches = evidence.get(
                    "matches",
                    [],
                )
                indicators = evidence.get(
                    "context_indicators",
                    [],
                )

                st.html(
                    f"""
                    <div class="aw-card" style="
                        min-height:auto;
                        margin:12px 0;
                    ">

                        <div class="aw-card-text">
                            Evidence {evidence_index + 1}
                        </div>

                        <div style="
                            margin-top:.55rem;
                            color:#D4D4D8;
                            font-size:.9rem;
                            line-height:1.7;
                        ">
                            “{sentence}”
                        </div>

                    </div>
                    """,
                )

                st.caption(
                    f"Context: {context_label}"
                )

                if evidence_matches:
                    st.caption(
                        "Matched phrases: "
                        + ", ".join(evidence_matches)
                    )

                if indicators:
                    st.caption(
                        "Context indicators: "
                        + ", ".join(indicators)
                    )

    if st.button(
        "← Back to Home",
        use_container_width=True,
    ):
        st.session_state.page = "home"
        st.rerun()


def secondary_page(title, description):
    topbar()

    # ---------------------------------------------------------
    # UNIQUE HOW-IT-WORKS EXPERIENCE
    # ---------------------------------------------------------
    if title == "How AgreeWise works.":
        st.html(
            """
            <style>
                .aw-how {
                    position: relative;
                    padding: 34px 4px 70px;
                    overflow: hidden;
                }

                .aw-how-orb {
                    position: absolute;
                    width: 420px;
                    height: 420px;
                    right: -140px;
                    top: -120px;
                    border-radius: 50%;
                    background:
                        radial-gradient(
                            circle,
                            rgba(56,189,248,.22) 0%,
                            rgba(56,189,248,.08) 35%,
                            transparent 70%
                        );
                    filter: blur(8px);
                    pointer-events: none;
                }

                .aw-how-kicker {
                    display: inline-flex;
                    align-items: center;
                    gap: 8px;
                    padding: 7px 12px;
                    border: 1px solid rgba(14,165,233,.22);
                    border-radius: 999px;
                    background: rgba(255,255,255,.42);
                    color: #0284C7;
                    font-size: 11px;
                    font-weight: 800;
                    letter-spacing: .14em;
                    text-transform: uppercase;
                    box-shadow: 0 8px 30px rgba(14,165,233,.08);
                }

                .aw-how-kicker-dot {
                    width: 7px;
                    height: 7px;
                    border-radius: 50%;
                    background: #0EA5E9;
                    box-shadow: 0 0 0 5px rgba(14,165,233,.10);
                }

                .aw-how-title {
                    max-width: 850px;
                    margin: 22px 0 12px;
                    color: #12304A;
                    font-size: clamp(42px, 5vw, 72px);
                    line-height: .98;
                    letter-spacing: -.055em;
                    font-weight: 850;
                }

                .aw-how-gradient {
                    background: linear-gradient(
                        100deg,
                        #0369A1 0%,
                        #0EA5E9 45%,
                        #38BDF8 100%
                    );
                    -webkit-background-clip: text;
                    background-clip: text;
                    color: transparent;
                }

                .aw-how-description {
                    max-width: 720px;
                    color: #648095;
                    font-size: 17px;
                    line-height: 1.75;
                    margin-bottom: 34px;
                }

                /* -------------------------------------------------
                   ENGINE PANEL
                ------------------------------------------------- */

                .aw-engine {
                    position: relative;
                    padding: 22px;
                    border-radius: 28px;
                    border: 1px solid rgba(14,165,233,.18);
                    background: rgba(255,255,255,.48);
                    box-shadow:
                        0 28px 80px rgba(14,116,144,.10),
                        inset 0 1px 0 rgba(255,255,255,.85);
                    backdrop-filter: blur(22px);
                    -webkit-backdrop-filter: blur(22px);
                    overflow: hidden;
                }

                .aw-engine::before {
                    content: "";
                    position: absolute;
                    inset: 0;
                    background:
                        linear-gradient(
                            115deg,
                            rgba(255,255,255,.50),
                            transparent 35%,
                            rgba(56,189,248,.06)
                        );
                    pointer-events: none;
                }

                .aw-engine-head {
                    position: relative;
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    margin-bottom: 20px;
                }

                .aw-engine-name {
                    color: #12304A;
                    font-size: 14px;
                    font-weight: 800;
                    letter-spacing: -.01em;
                }

                .aw-live {
                    display: inline-flex;
                    align-items: center;
                    gap: 7px;
                    padding: 6px 10px;
                    border-radius: 999px;
                    background: rgba(14,165,233,.08);
                    border: 1px solid rgba(14,165,233,.16);
                    color: #0284C7;
                    font-size: 10px;
                    font-weight: 800;
                    letter-spacing: .08em;
                }

                .aw-live-dot {
                    width: 6px;
                    height: 6px;
                    border-radius: 50%;
                    background: #0EA5E9;
                    animation: awPulse 1.8s infinite;
                }

                @keyframes awPulse {
                    0%,100% {
                        box-shadow: 0 0 0 0 rgba(14,165,233,.25);
                    }
                    50% {
                        box-shadow: 0 0 0 6px rgba(14,165,233,0);
                    }
                }

                /* -------------------------------------------------
                   PIPELINE
                ------------------------------------------------- */

                .aw-pipeline {
                    position: relative;
                    display: grid;
                    grid-template-columns: repeat(4, 1fr);
                    gap: 12px;
                }

                .aw-step {
                    position: relative;
                    min-height: 178px;
                    padding: 20px;
                    border-radius: 20px;
                    background: rgba(255,255,255,.56);
                    border: 1px solid rgba(14,165,233,.14);
                    box-shadow:
                        0 12px 30px rgba(14,116,144,.055),
                        inset 0 1px 0 rgba(255,255,255,.85);
                    transition:
                        transform .25s ease,
                        box-shadow .25s ease,
                        border-color .25s ease;
                }

                .aw-step:hover {
                    transform: translateY(-7px);
                    border-color: rgba(14,165,233,.32);
                    box-shadow:
                        0 20px 45px rgba(14,116,144,.12),
                        0 0 0 1px rgba(56,189,248,.06);
                }

                .aw-step-number {
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    width: 34px;
                    height: 34px;
                    border-radius: 10px;
                    background: rgba(14,165,233,.09);
                    border: 1px solid rgba(14,165,233,.16);
                    color: #0284C7;
                    font-size: 11px;
                    font-weight: 850;
                    margin-bottom: 26px;
                }

                .aw-step h3 {
                    margin: 0 0 8px;
                    color: #163247;
                    font-size: 17px;
                    font-weight: 800;
                }

                .aw-step p {
                    margin: 0;
                    color: #6B8293;
                    font-size: 12px;
                    line-height: 1.65;
                }

                .aw-step-line {
                    position: absolute;
                    top: 36px;
                    right: -18px;
                    width: 24px;
                    height: 1px;
                    background: linear-gradient(
                        90deg,
                        rgba(14,165,233,.35),
                        rgba(14,165,233,0)
                    );
                }

                /* -------------------------------------------------
                   SIGNALS
                ------------------------------------------------- */

                .aw-signals {
                    display: grid;
                    grid-template-columns: 1.2fr .8fr;
                    gap: 14px;
                    margin-top: 14px;
                }

                .aw-signal-panel {
                    padding: 20px;
                    border-radius: 22px;
                    background: rgba(255,255,255,.42);
                    border: 1px solid rgba(14,165,233,.14);
                    backdrop-filter: blur(18px);
                    -webkit-backdrop-filter: blur(18px);
                }

                .aw-panel-label {
                    margin-bottom: 15px;
                    color: #6B8293;
                    font-size: 10px;
                    font-weight: 800;
                    letter-spacing: .12em;
                    text-transform: uppercase;
                }

                .aw-document-line {
                    display: flex;
                    align-items: center;
                    gap: 10px;
                    padding: 10px 12px;
                    margin-bottom: 7px;
                    border-radius: 11px;
                    background: rgba(255,255,255,.58);
                    border: 1px solid rgba(14,165,233,.09);
                }

                .aw-document-icon {
                    width: 25px;
                    height: 25px;
                    display: grid;
                    place-items: center;
                    border-radius: 7px;
                    background: #E0F2FE;
                    color: #0284C7;
                    font-size: 11px;
                    font-weight: 800;
                }

                .aw-document-text {
                    flex: 1;
                    color: #466277;
                    font-size: 11px;
                    white-space: nowrap;
                    overflow: hidden;
                    text-overflow: ellipsis;
                }

                .aw-document-status {
                    color: #0EA5E9;
                    font-size: 10px;
                    font-weight: 800;
                }

                .aw-evidence {
                    position: relative;
                    padding: 17px;
                    border-radius: 16px;
                    background: linear-gradient(
                        135deg,
                        rgba(224,242,254,.72),
                        rgba(255,255,255,.55)
                    );
                    border: 1px solid rgba(14,165,233,.16);
                }

                .aw-evidence-label {
                    color: #0284C7;
                    font-size: 9px;
                    font-weight: 850;
                    letter-spacing: .12em;
                    text-transform: uppercase;
                    margin-bottom: 9px;
                }

                .aw-evidence-text {
                    color: #35556A;
                    font-size: 12px;
                    line-height: 1.65;
                }

                .aw-highlight {
                    padding: 2px 5px;
                    border-radius: 5px;
                    background: rgba(56,189,248,.16);
                    color: #0369A1;
                    font-weight: 750;
                }

                .aw-metrics {
                    display: grid;
                    grid-template-columns: repeat(3, 1fr);
                    gap: 9px;
                    margin-top: 10px;
                }

                .aw-metric {
                    padding: 12px;
                    border-radius: 13px;
                    background: rgba(255,255,255,.55);
                    border: 1px solid rgba(14,165,233,.10);
                }

                .aw-metric-value {
                    color: #12304A;
                    font-size: 19px;
                    font-weight: 850;
                    letter-spacing: -.03em;
                }

                .aw-metric-label {
                    color: #71889A;
                    font-size: 9px;
                    margin-top: 2px;
                }

                @media (max-width: 900px) {
                    .aw-pipeline {
                        grid-template-columns: repeat(2, 1fr);
                    }

                    .aw-signals {
                        grid-template-columns: 1fr;
                    }

                    .aw-step-line {
                        display: none;
                    }
                }

                @media (max-width: 600px) {
                    .aw-pipeline {
                        grid-template-columns: 1fr;
                    }

                    .aw-how-title {
                        font-size: 42px;
                    }

                    .aw-metrics {
                        grid-template-columns: 1fr;
                    }
                }

                @media (prefers-reduced-motion: reduce) {
                    .aw-live-dot {
                        animation: none;
                    }

                    .aw-step {
                        transition: none;
                    }
                }
            </style>

            <div class="aw-how">
                <div class="aw-how-orb"></div>

                <div class="aw-how-kicker">
                    <span class="aw-how-kicker-dot"></span>
                    THE EVIDENCE ENGINE
                </div>

                <h1 class="aw-how-title">
                    From legal text to
                    <span class="aw-how-gradient">clear evidence.</span>
                </h1>

                <p class="aw-how-description">
                    AgreeWise turns dense policies into structured,
                    understandable findings — without asking you what
                    to look for.
                </p>

                <div class="aw-engine">
                    <div class="aw-engine-head">
                        <div class="aw-engine-name">
                            AgreeWise Analysis Pipeline
                        </div>

                        <div class="aw-live">
                            <span class="aw-live-dot"></span>
                            AUTOMATIC
                        </div>
                    </div>

                    <div class="aw-pipeline">

                        <div class="aw-step">
                            <div class="aw-step-number">01</div>
                            <h3>Ingest</h3>
                            <p>
                                Paste text or upload a supported document.
                                AgreeWise extracts the readable content.
                            </p>
                            <div class="aw-step-line"></div>
                        </div>

                        <div class="aw-step">
                            <div class="aw-step-number">02</div>
                            <h3>Understand</h3>
                            <p>
                                Language, document type and important
                                clauses are identified automatically.
                            </p>
                            <div class="aw-step-line"></div>
                        </div>

                        <div class="aw-step">
                            <div class="aw-step-number">03</div>
                            <h3>Detect</h3>
                            <p>
                                Custom rules inspect privacy, tracking,
                                sharing, retention and user-rights signals.
                            </p>
                            <div class="aw-step-line"></div>
                        </div>

                        <div class="aw-step">
                            <div class="aw-step-number">04</div>
                            <h3>Prove</h3>
                            <p>
                                Every finding is connected back to the
                                sentence that triggered it.
                            </p>
                        </div>

                    </div>
                </div>

                <div class="aw-signals">

                    <div class="aw-signal-panel">
                        <div class="aw-panel-label">
                            What the engine sees
                        </div>

                        <div class="aw-document-line">
                            <div class="aw-document-icon">A</div>
                            <div class="aw-document-text">
                                We collect your name and email address...
                            </div>
                            <div class="aw-document-status">
                                PERSONAL DATA
                            </div>
                        </div>

                        <div class="aw-document-line">
                            <div class="aw-document-icon">◎</div>
                            <div class="aw-document-text">
                                We may collect location information...
                            </div>
                            <div class="aw-document-status">
                                LOCATION
                            </div>
                        </div>

                        <div class="aw-document-line">
                            <div class="aw-document-icon">◌</div>
                            <div class="aw-document-text">
                                We use cookies and tracking technologies...
                            </div>
                            <div class="aw-document-status">
                                TRACKING
                            </div>
                        </div>
                    </div>

                    <div class="aw-signal-panel">
                        <div class="aw-panel-label">
                            Evidence connection
                        </div>

                        <div class="aw-evidence">
                            <div class="aw-evidence-label">
                                DETECTED FINDING
                            </div>

                            <div class="aw-evidence-text">
                                The policy states that the service may
                                <span class="aw-highlight">
                                    collect location information
                                </span>
                                from your device.
                            </div>
                        </div>

                        <div class="aw-metrics">
                            <div class="aw-metric">
                                <div class="aw-metric-value">12+</div>
                                <div class="aw-metric-label">
                                    clause categories
                                </div>
                            </div>

                            <div class="aw-metric">
                                <div class="aw-metric-value">20+</div>
                                <div class="aw-metric-label">
                                    language signals
                                </div>
                            </div>

                            <div class="aw-metric">
                                <div class="aw-metric-value">1:1</div>
                                <div class="aw-metric-label">
                                    evidence mapping
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
            """
        )
        return

    # ---------------------------------------------------------
    # OTHER SECONDARY PAGES
    # ---------------------------------------------------------
    st.html(
        f"""
        <div class="aw-hero">
            <div class="aw-kicker">AGREEWISE</div>

            <h1 class="aw-title">
                {title}
            </h1>

            <p class="aw-subtitle">
                {description}
            </p>
        </div>
        """
    )

def main():
    initialize_state()
    inject_global_styles()
    sidebar()

    page = st.session_state.page

    if page == "home":
        home()

    elif page == "analysis":
        analysis()

    elif page == "results":
        results()

    elif page == "analyses":
        secondary_page(
            "Your analyses.",
            "Your previous document analyses will appear here.",
        )

    elif page == "how":
        secondary_page(
            "How AgreeWise works.",
            (
                "Paste or upload a document. "
                "AgreeWise extracts the content, detects the "
                "language, identifies important clauses and "
                "connects findings to evidence."
            ),
        )

    elif page == "settings":
        secondary_page(
            "Settings.",
            "Application preferences and processing controls.",
        )


if __name__ == "__main__":
    main()
