import streamlit as st


def render_landing() -> tuple[str, object]:
    st.markdown(
        """
        <div class="aw-nav">
            <div class="aw-logo">
                <div class="aw-logo-mark">A</div>
                <span>AgreeWise</span>
            </div>
            <div style="color:#71717a;font-size:0.82rem;">
                Understand before you agree.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="aw-hero">
            <div class="aw-badge">
                Intelligent Policy Analysis
            </div>

            <h1 class="aw-title">
                Understand before<br>you agree.
            </h1>

            <p class="aw-subtitle">
                Turn complex legal documents into clear insights —
                automatically.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="aw-input-label">Paste your policy or agreement</div>',
        unsafe_allow_html=True,
    )

    pasted_text = st.text_area(
        "Policy text",
        placeholder=(
            "Paste a Privacy Policy, Terms & Conditions, "
            "Cookie Policy, or User Agreement here..."
        ),
        label_visibility="collapsed",
        key="policy_text",
    )

    st.markdown(
        """
        <div class="aw-helper">
            No prompts. No legal jargon. Just paste the text.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="aw-divider">or upload a document</div>',
        unsafe_allow_html=True,
    )

    uploaded_file = st.file_uploader(
        "Upload document",
        type=["txt", "pdf", "docx", "jpg", "jpeg", "png"],
        label_visibility="collapsed",
        key="policy_file",
    )

    st.markdown("<br>", unsafe_allow_html=True)

    analyze = st.button(
        "Analyze document →",
        type="primary",
        use_container_width=True,
    )

    st.markdown(
        """
        <div class="aw-feature">
            Privacy policies · Terms · Cookies · User agreements
        </div>
        """,
        unsafe_allow_html=True,
    )

    return pasted_text, uploaded_file if analyze else None
