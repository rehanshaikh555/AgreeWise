import streamlit as st



def brand():
    st.html(
        """
        <div class="aw-brand">
            Agree<span>Wise</span>
        </div>
        """
    )


def topbar():
    st.html(
        """
        <div style="
            display:flex;
            justify-content:space-between;
            align-items:center;
            padding-bottom:1rem;
            border-bottom:1px solid #292B35;
        ">
            <div style="
                color:#71717A;
                font-size:.75rem;
            ">
                Intelligent Privacy Policy & Terms Analyzer
            </div>

            <div style="
                color:#52525B;
                font-size:.7rem;
            ">
                Understand before you agree.
            </div>
        </div>
        """
    )


def hero():
    st.html(
        """
        <div class="aw-hero">

            <div class="aw-kicker">
                <span>NO PROMPTS</span>
                &nbsp;&nbsp; MULTILINGUAL
            </div>

            <h1 class="aw-title">
                Understand before<br>
                you <span class="aw-gradient">agree.</span>
            </h1>

            <p class="aw-subtitle">
                Turn complex legal documents into clear,
                evidence-based insights - automatically.
            </p>

            <div class="aw-benefits">

                <div class="aw-benefit">
                    <span class="aw-check">✓</span>
                    No legal jargon
                </div>

                <div class="aw-benefit">
                    <span class="aw-check">✓</span>
                    Multiple languages
                </div>

                <div class="aw-benefit">
                    <span class="aw-check">✓</span>
                    Evidence-based analysis
                </div>

            </div>

        </div>
        """
    )


def document_visual():
    st.html(
        """
        <div class="aw-document-stage">

            <div class="aw-glow"></div>

            <div class="aw-insight aw-data">
                Data Collection
            </div>

            <div class="aw-insight aw-share">
                Third-party Sharing
            </div>

            <div class="aw-insight aw-rights">
                ✓ User Rights
            </div>

            <div class="aw-doc">

                <div class="aw-doc-title">
                    Privacy Policy
                </div>

                <div class="aw-line"></div>
                <div class="aw-line medium"></div>
                <div class="aw-line short"></div>

                <br>

                <div class="aw-line medium"></div>
                <div class="aw-line"></div>
                <div class="aw-line short"></div>

                <br>

                <div class="aw-line"></div>
                <div class="aw-line medium"></div>
                <div class="aw-line short"></div>

            </div>

        </div>
        """
    )


def upload_header():
    st.html(
        """
        <div class="aw-upload">

            <div class="aw-upload-icon">
                ↑
            </div>

            <div class="aw-upload-title">
                Drop your document here
            </div>

            <div class="aw-upload-subtitle">
                or choose a file below
            </div>

            <div class="aw-upload-formats">
                PDF · DOCX · TXT · PNG · JPG · JPEG
            </div>

        </div>
        """
    )


def feature_cards():
    st.html(
        """
        <div class="aw-section">

            <div class="aw-section-title">
                Why choose <span>AgreeWise?</span>
            </div>

            <div class="aw-section-subtitle">
                Understand what your documents actually say.
            </div>

        </div>
        """
    )

    columns = st.columns(4)

    cards = [
        (
            "✦",
            "Automatic Analysis",
            "No prompts required. AgreeWise finds important clauses automatically.",
            "",
        ),
        (
            "◎",
            "Multilingual",
            "Automatically detects document language and supported content.",
            "blue",
        ),
        (
            "⌕",
            "Clear Evidence",
            "Every finding will connect back to the source document.",
            "",
        ),
        (
            "✓",
            "Privacy First",
            "Designed around privacy-conscious document processing.",
            "green",
        ),
    ]

    for column, card in zip(columns, cards):
        icon, title, text, style = card

        with column:
            st.html(
                f"""
                <div class="aw-card">

                    <div class="aw-card-icon {style}">
                        {icon}
                    </div>

                    <div class="aw-card-title">
                        {title}
                    </div>

                    <div class="aw-card-text">
                        {text}
                    </div>

                </div>
                """
            )
