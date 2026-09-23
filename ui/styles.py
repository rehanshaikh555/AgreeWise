import streamlit as st



def inject_global_styles():
    st.markdown(
        """
        <style>

        .stApp {
            background: #09090B;
            color: #F7F7FA;
        }

        .block-container {
            max-width: 1400px;
            padding-top: 2rem;
            padding-bottom: 4rem;
        }

        [data-testid="stSidebar"] {
            background: #0D0E12;
            border-right: 1px solid #292B35;
        }

        [data-testid="stSidebar"] .block-container {
            padding: 1.5rem 1rem;
        }

        .aw-brand {
            font-size: 1.45rem;
            font-weight: 800;
            letter-spacing: -0.04em;
            color: #F7F7FA;
            margin-bottom: 2rem;
        }

        .aw-brand span {
            color: #A78BFA;
        }

        .aw-nav-label {
            color: #626574;
            font-size: .68rem;
            font-weight: 700;
            letter-spacing: .12em;
            text-transform: uppercase;
            margin: 1.5rem 0 .55rem;
        }

        .aw-hero {
            padding: 2.5rem 0 2rem;
        }

        .aw-kicker {
            color: #A78BFA;
            font-size: .72rem;
            font-weight: 800;
            letter-spacing: .14em;
            text-transform: uppercase;
            margin-bottom: 1.2rem;
        }

        .aw-kicker span {
            color: #6EE7B7;
            margin-right: .35rem;
        }

        .aw-title {
            font-size: 3.8rem;
            font-weight: 800;
            line-height: 1.02;
            letter-spacing: -.055em;
            color: #F7F7FA;
            margin: 0;
        }

        .aw-gradient {
            background: linear-gradient(
                90deg,
                #A78BFA,
                #818CF8
            );
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .aw-subtitle {
            color: #A7A8B3;
            font-size: 1.04rem;
            line-height: 1.7;
            max-width: 620px;
            margin-top: 1.2rem;
        }

        .aw-benefits {
            display: flex;
            flex-wrap: wrap;
            gap: .9rem 1.4rem;
            margin-top: 1.7rem;
        }

        .aw-benefit {
            color: #A7A8B3;
            font-size: .82rem;
        }

        .aw-check {
            color: #A78BFA;
            font-weight: 800;
            margin-right: .35rem;
        }

        .aw-document-stage {
            position: relative;
            min-height: 420px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .aw-glow {
            position: absolute;
            width: 300px;
            height: 300px;
            border-radius: 50%;
            background: rgba(124, 58, 237, .13);
            filter: blur(55px);
        }

        .aw-doc {
            position: relative;
            width: 285px;
            min-height: 355px;
            padding: 2rem 1.6rem;
            background: #15161B;
            border: 1px solid #292B35;
            border-radius: 18px;
            box-shadow: 0 30px 80px rgba(0,0,0,.35);
            transform: rotate(2deg);
        }

        .aw-doc-title {
            color: #F7F7FA;
            font-size: .92rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
        }

        .aw-line {
            height: 6px;
            width: 100%;
            border-radius: 99px;
            background: #292B35;
            margin-bottom: .65rem;
        }

        .aw-line.medium {
            width: 78%;
        }

        .aw-line.short {
            width: 52%;
        }

        .aw-insight {
            position: absolute;
            z-index: 2;
            padding: .55rem .75rem;
            border-radius: 10px;
            background: #15161B;
            border: 1px solid #343642;
            color: #D4D4D8;
            font-size: .72rem;
            box-shadow: 0 12px 30px rgba(0,0,0,.25);
        }

        .aw-data {
            top: 18%;
            left: 4%;
        }

        .aw-share {
            top: 47%;
            right: 0;
        }

        .aw-rights {
            bottom: 14%;
            left: 7%;
        }

        .aw-upload {
            text-align: center;
            padding: 2rem;
            background: #15161B;
            border: 1px dashed #343642;
            border-radius: 18px;
            margin-top: 1rem;
        }

        .aw-upload-icon {
            color: #A78BFA;
            font-size: 1.7rem;
            margin-bottom: .65rem;
        }

        .aw-upload-title {
            color: #F7F7FA;
            font-weight: 700;
            font-size: 1rem;
        }

        .aw-upload-subtitle {
            color: #71717A;
            font-size: .82rem;
            margin-top: .35rem;
        }

        .aw-upload-formats {
            color: #52525B;
            font-size: .7rem;
            margin-top: .8rem;
        }

        .aw-section {
            margin-top: 3rem;
            margin-bottom: 1.2rem;
        }

        .aw-section-title {
            color: #F7F7FA;
            font-size: 1.35rem;
            font-weight: 750;
        }

        .aw-section-title span {
            color: #A78BFA;
        }

        .aw-section-subtitle {
            color: #71717A;
            font-size: .82rem;
            margin-top: .4rem;
        }

        .aw-card {
            background: #15161B;
            border: 1px solid #292B35;
            border-radius: 18px;
            padding: 1.35rem;
            min-height: 165px;
        }

        .aw-card-icon {
            color: #A78BFA;
            font-size: 1.15rem;
            margin-bottom: 1rem;
        }

        .aw-card-icon.blue {
            color: #818CF8;
        }

        .aw-card-icon.green {
            color: #6EE7B7;
        }

        .aw-card-title {
            color: #F7F7FA;
            font-size: .92rem;
            font-weight: 700;
        }

        .aw-card-text {
            color: #71717A;
            font-size: .76rem;
            line-height: 1.6;
            margin-top: .55rem;
        }

        .stButton > button {
            border-radius: 12px;
            min-height: 42px;
            border: 1px solid #292B35;
            background: #15161B;
            color: #D4D4D8;
        }

        .stButton > button:hover {
            border-color: #6D5BD0;
            color: #F7F7FA;
        }

        [data-testid="stSidebar"] .stButton > button {
            text-align: left;
            background: transparent;
            border: 0;
        }

        [data-testid="stFileUploader"] {
            background: transparent;
        }

        @media (max-width: 900px) {
            .aw-title {
                font-size: 3rem;
            }

            .aw-document-stage {
                min-height: 350px;
            }
        }


        /* =========================================================
           AGREEWISE DYNAMIC MOTION LAYER
           ========================================================= */

        /* Hide Streamlit chrome so the product owns the interface */
        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        header {
            background: transparent !important;
        }

        /* Ambient page motion */
        .stApp {
            overflow-x: hidden;
        }

        .stApp::before {
            content: "";
            position: fixed;
            width: 520px;
            height: 520px;
            top: -220px;
            right: -160px;
            border-radius: 50%;
            background: radial-gradient(
                circle,
                rgba(139, 92, 246, .10) 0%,
                rgba(139, 92, 246, .035) 35%,
                transparent 72%
            );
            pointer-events: none;
            z-index: 0;
            animation: awAmbient 9s ease-in-out infinite alternate;
        }

        @keyframes awAmbient {
            from {
                transform: translate3d(0, 0, 0) scale(1);
                opacity: .65;
            }
            to {
                transform: translate3d(-45px, 35px, 0) scale(1.12);
                opacity: 1;
            }
        }

        /* Hero entrance */
        .aw-hero {
            animation: awHeroIn .75s cubic-bezier(.16, 1, .3, 1) both;
        }

        .aw-kicker {
            animation: awFadeUp .55s .05s ease both;
        }

        .aw-title {
            animation: awFadeUp .7s .12s cubic-bezier(.16, 1, .3, 1) both;
        }

        .aw-subtitle {
            animation: awFadeUp .7s .22s ease both;
        }

        .aw-benefits {
            animation: awFadeUp .7s .32s ease both;
        }

        @keyframes awHeroIn {
            from {
                opacity: 0;
                transform: translateY(18px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes awFadeUp {
            from {
                opacity: 0;
                transform: translateY(12px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Animated Agree gradient */
        .aw-gradient {
            background-size: 200% 200%;
            animation: awGradient 4s ease infinite;
        }

        @keyframes awGradient {
            0% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
            100% {
                background-position: 0% 50%;
            }
        }

        /* Floating document */
        .aw-document-stage {
            animation: awStageIn .9s .12s cubic-bezier(.16, 1, .3, 1) both;
        }

        .aw-doc {
            animation: awDocumentFloat 5s ease-in-out infinite;
            transform-origin: center center;
        }

        @keyframes awStageIn {
            from {
                opacity: 0;
                transform: translateX(22px) scale(.97);
            }
            to {
                opacity: 1;
                transform: translateX(0) scale(1);
            }
        }

        @keyframes awDocumentFloat {
            0%, 100% {
                transform: translateY(0) rotate(1deg);
            }
            50% {
                transform: translateY(-9px) rotate(-.4deg);
            }
        }

        /* Ambient document glow */
        .aw-glow {
            animation: awGlow 3.5s ease-in-out infinite;
        }

        @keyframes awGlow {
            0%, 100% {
                opacity: .42;
                transform: scale(.96);
            }
            50% {
                opacity: .8;
                transform: scale(1.05);
            }
        }

        /* Floating insight badges */
        .aw-insight {
            animation: awInsightFloat 4.5s ease-in-out infinite;
            transition:
                transform .25s ease,
                border-color .25s ease,
                background .25s ease,
                box-shadow .25s ease;
        }

        .aw-data {
            animation-delay: -.8s;
        }

        .aw-share {
            animation-delay: -2.2s;
        }

        .aw-rights {
            animation-delay: -3.4s;
        }

        @keyframes awInsightFloat {
            0%, 100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-7px);
            }
        }

        @media (hover: hover) and (pointer: fine) {
            .aw-insight:hover {
                transform: translateY(-5px) scale(1.035);
                border-color: rgba(139, 92, 246, .45);
                background: rgba(21, 22, 27, .96);
                box-shadow: 0 12px 30px rgba(0, 0, 0, .25);
            }
        }

        /* Document text scanning effect */
        .aw-line {
            position: relative;
            overflow: hidden;
        }

        .aw-line::after {
            content: "";
            position: absolute;
            inset: 0;
            width: 45%;
            background: linear-gradient(
                90deg,
                transparent,
                rgba(139, 92, 246, .18),
                transparent
            );
            transform: translateX(-120%);
            animation: awScan 3.2s ease-in-out infinite;
        }

        .aw-line.medium::after {
            animation-delay: .65s;
        }

        .aw-line.short::after {
            animation-delay: 1.15s;
        }

        @keyframes awScan {
            0%, 55% {
                transform: translateX(-120%);
            }
            75%, 100% {
                transform: translateX(250%);
            }
        }

        /* Upload interaction */
        .aw-upload {
            transition:
                transform .25s ease,
                border-color .25s ease,
                background .25s ease,
                box-shadow .25s ease;
        }

        @media (hover: hover) and (pointer: fine) {
            .aw-upload:hover {
                transform: translateY(-3px);
                border-color: rgba(139, 92, 246, .55) !important;
                background: rgba(139, 92, 246, .035) !important;
                box-shadow: 0 18px 45px rgba(0, 0, 0, .22);
            }

            .aw-upload:hover .aw-upload-icon {
                transform: translateY(-4px) scale(1.08);
            }
        }

        .aw-upload-icon {
            transition: transform .25s ease;
        }

        /* Feature card stagger */
        .aw-card {
            animation: awCardIn .6s cubic-bezier(.16, 1, .3, 1) both;
            transition:
                transform .25s ease,
                border-color .25s ease,
                box-shadow .25s ease,
                background .25s ease;
        }

        .aw-card:nth-child(1) {
            animation-delay: .08s;
        }

        .aw-card:nth-child(2) {
            animation-delay: .16s;
        }

        .aw-card:nth-child(3) {
            animation-delay: .24s;
        }

        .aw-card:nth-child(4) {
            animation-delay: .32s;
        }

        @keyframes awCardIn {
            from {
                opacity: 0;
                transform: translateY(15px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @media (hover: hover) and (pointer: fine) {
            .aw-card:hover {
                transform: translateY(-5px);
                border-color: rgba(139, 92, 246, .30);
                box-shadow: 0 18px 40px rgba(0, 0, 0, .22);
                background: #18191F;
            }
        }

        /* Sidebar navigation */
        [data-testid="stSidebar"] .stButton > button {
            transition:
                transform .2s ease,
                background .2s ease,
                border-color .2s ease,
                color .2s ease;
        }

        @media (hover: hover) and (pointer: fine) {
            [data-testid="stSidebar"] .stButton > button:hover {
                transform: translateX(3px);
                border-color: rgba(139, 92, 246, .28);
                background: rgba(139, 92, 246, .07);
            }
        }

        /* Primary buttons */
        .stButton > button {
            transition:
                transform .2s ease,
                box-shadow .2s ease,
                border-color .2s ease;
        }

        @media (hover: hover) and (pointer: fine) {
            .stButton > button:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 25px rgba(0, 0, 0, .2);
            }
        }

        /* Respect accessibility preferences */
        @media (prefers-reduced-motion: reduce) {
            *,
            *::before,
            *::after {
                animation-duration: .01ms !important;
                animation-iteration-count: 1 !important;
                scroll-behavior: auto !important;
                transition-duration: .01ms !important;
            }
        }


        /* =========================================================
           DYNAMIC PRIVACY CARD
           ========================================================= */

        .aw-privacy-card {
            position: relative;
            display: flex;
            align-items: flex-start;
            gap: 11px;
            margin-top: 2rem;
            padding: 14px;
            min-height: 74px;
            overflow: hidden;
            border: 1px solid #292B35;
            border-radius: 16px;
            background: linear-gradient(
                135deg,
                rgba(139, 92, 246, .10),
                #15161B 55%,
                rgba(21, 22, 27, .96)
            );
            animation: awPrivacyIn .65s cubic-bezier(.16, 1, .3, 1) both;
            transition:
                transform .25s ease,
                border-color .25s ease,
                box-shadow .25s ease;
        }

        @keyframes awPrivacyIn {
            from {
                opacity: 0;
                transform: translateY(12px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .aw-privacy-card::before {
            content: "";
            position: absolute;
            width: 120px;
            height: 120px;
            top: -75px;
            right: -45px;
            border-radius: 50%;
            background: radial-gradient(
                circle,
                rgba(139, 92, 246, .18),
                transparent 68%
            );
            animation: awPrivacyOrb 4s ease-in-out infinite;
            pointer-events: none;
        }

        @keyframes awPrivacyOrb {
            0%, 100% {
                transform: translate(0, 0) scale(.85);
                opacity: .45;
            }
            50% {
                transform: translate(-14px, 16px) scale(1.15);
                opacity: .95;
            }
        }

        .aw-privacy-icon {
            position: relative;
            z-index: 2;
            width: 31px;
            height: 31px;
            min-width: 31px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 9px;
            color: #C4B5FD;
            background: rgba(139, 92, 246, .13);
            border: 1px solid rgba(139, 92, 246, .28);
            font-size: 13px;
            font-weight: 800;
            animation: awPrivacyPulse 2.8s ease-in-out infinite;
        }

        @keyframes awPrivacyPulse {
            0%, 100% {
                box-shadow: 0 0 0 0 rgba(139, 92, 246, 0);
            }
            50% {
                box-shadow:
                    0 0 0 6px rgba(139, 92, 246, .045),
                    0 0 20px rgba(139, 92, 246, .10);
            }
        }

        .aw-privacy-content {
            position: relative;
            z-index: 2;
            min-width: 0;
        }

        .aw-privacy-title {
            color: #F5F7FB;
            font-weight: 700;
            font-size: 13px;
            margin-bottom: 5px;
        }

        .aw-privacy-text {
            color: #858693;
            font-size: 11px;
            line-height: 1.55;
        }

        /* =========================================================
           MORE ACTIVE DOCUMENT VISUAL
           ========================================================= */

        .aw-document-stage {
            animation:
                awStageIn .9s .12s cubic-bezier(.16, 1, .3, 1) both,
                awStageFloat 7s 1s ease-in-out infinite;
        }

        @keyframes awStageFloat {
            0%, 100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-5px);
            }
        }

        .aw-doc {
            animation:
                awDocumentFloat 5s ease-in-out infinite,
                awDocumentBreath 3.8s ease-in-out infinite;
        }

        @keyframes awDocumentBreath {
            0%, 100% {
                box-shadow:
                    0 25px 70px rgba(0, 0, 0, .34),
                    0 0 0 rgba(139, 92, 246, 0);
            }
            50% {
                box-shadow:
                    0 30px 75px rgba(0, 0, 0, .40),
                    0 0 35px rgba(139, 92, 246, .07);
            }
        }

        /* Independent badge movement */
        .aw-data {
            animation:
                awDataFloat 4.2s ease-in-out infinite,
                awBadgeIn .7s .35s cubic-bezier(.16, 1, .3, 1) both;
        }

        .aw-share {
            animation:
                awShareFloat 5.1s .4s ease-in-out infinite,
                awBadgeIn .7s .5s cubic-bezier(.16, 1, .3, 1) both;
        }

        .aw-rights {
            animation:
                awRightsFloat 4.7s .8s ease-in-out infinite,
                awBadgeIn .7s .65s cubic-bezier(.16, 1, .3, 1) both;
        }

        @keyframes awDataFloat {
            0%, 100% {
                transform: translate(0, 0);
            }
            50% {
                transform: translate(-5px, -9px);
            }
        }

        @keyframes awShareFloat {
            0%, 100% {
                transform: translate(0, 0);
            }
            50% {
                transform: translate(6px, -7px);
            }
        }

        @keyframes awRightsFloat {
            0%, 100% {
                transform: translate(0, 0);
            }
            50% {
                transform: translate(-4px, 8px);
            }
        }

        @keyframes awBadgeIn {
            from {
                opacity: 0;
                scale: .88;
            }
            to {
                opacity: 1;
                scale: 1;
            }
        }

        /* Moving scan beam */
        .aw-doc::after {
            content: "";
            position: absolute;
            left: 0;
            right: 0;
            top: 0;
            height: 1px;
            background: linear-gradient(
                90deg,
                transparent,
                rgba(167, 139, 250, .75),
                transparent
            );
            box-shadow: 0 0 14px rgba(139, 92, 246, .25);
            animation: awDocumentScan 4.5s ease-in-out infinite;
            pointer-events: none;
        }

        @keyframes awDocumentScan {
            0%, 15% {
                top: 5%;
                opacity: 0;
            }
            25% {
                opacity: .85;
            }
            70% {
                opacity: .85;
            }
            85%, 100% {
                top: 92%;
                opacity: 0;
            }
        }

        /* =========================================================
           UPLOAD AREA
           ========================================================= */

        .aw-upload {
            position: relative;
            overflow: hidden;
        }

        .aw-upload::before {
            content: "";
            position: absolute;
            top: 0;
            left: -45%;
            width: 35%;
            height: 100%;
            background: linear-gradient(
                90deg,
                transparent,
                rgba(139, 92, 246, .045),
                transparent
            );
            transform: skewX(-18deg);
            animation: awUploadSweep 5s ease-in-out infinite;
            pointer-events: none;
        }

        @keyframes awUploadSweep {
            0%, 35% {
                left: -45%;
            }
            70%, 100% {
                left: 125%;
            }
        }

        .aw-upload-icon {
            animation: awUploadIcon 2.4s ease-in-out infinite;
        }

        @keyframes awUploadIcon {
            0%, 100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-5px);
            }
        }

        /* =========================================================
           REDUCED MOTION
           ========================================================= */

        @media (prefers-reduced-motion: reduce) {
            .aw-privacy-card,
            .aw-privacy-icon,
            .aw-privacy-card::before,
            .aw-document-stage,
            .aw-doc,
            .aw-data,
            .aw-share,
            .aw-rights,
            .aw-doc::after,
            .aw-upload::before,
            .aw-upload-icon {
                animation: none !important;
            }
        }


        /* =========================================================
           AGREEWISE — RED + WHITE EXPERIMENTAL THEME
           ========================================================= */

        .stApp {
            background: #FFFFFF !important;
            color: #C1121F !important;
        }

        .block-container {
            background: #FFFFFF !important;
        }

        [data-testid="stSidebar"] {
            background: #C1121F !important;
            border-right: 1px solid #C1121F !important;
        }

        [data-testid="stSidebar"] .block-container {
            background: #C1121F !important;
        }

        /* Sidebar brand */
        .aw-brand {
            color: #FFFFFF !important;
        }

        .aw-brand span {
            color: #FFFFFF !important;
        }

        .aw-nav-label {
            color: rgba(255,255,255,.65) !important;
        }

        /* Sidebar buttons */
        [data-testid="stSidebar"] .stButton > button {
            color: #FFFFFF !important;
            background: transparent !important;
            border-color: transparent !important;
        }

        [data-testid="stSidebar"] .stButton > button:hover {
            color: #C1121F !important;
            background: #FFFFFF !important;
            border-color: #FFFFFF !important;
        }

        /* Topbar */
        .aw-topbar,
        .aw-topbar * {
            color: #C1121F !important;
        }

        /* Hero */
        .aw-kicker {
            color: #C1121F !important;
        }

        .aw-kicker span {
            color: #C1121F !important;
        }

        .aw-title {
            color: #C1121F !important;
        }

        .aw-gradient {
            color: #C1121F !important;
            background: none !important;
            -webkit-text-fill-color: #C1121F !important;
        }

        .aw-subtitle {
            color: #C1121F !important;
        }

        .aw-benefit {
            color: #C1121F !important;
        }

        .aw-check {
            color: #C1121F !important;
        }

        /* Document visual */
        .aw-document-stage {
            background: #FFFFFF !important;
        }

        .aw-doc {
            background: #FFFFFF !important;
            border: 2px solid #C1121F !important;
            box-shadow:
                0 25px 70px rgba(193,18,31,.18),
                0 0 35px rgba(193,18,31,.10) !important;
        }

        .aw-doc-title {
            color: #C1121F !important;
        }

        .aw-line {
            background: #C1121F !important;
            opacity: .22 !important;
        }

        .aw-insight {
            color: #C1121F !important;
            background: #FFFFFF !important;
            border: 2px solid #C1121F !important;
            box-shadow: 0 8px 25px rgba(193,18,31,.15) !important;
        }

        .aw-glow {
            background: radial-gradient(
                circle,
                rgba(193,18,31,.20),
                transparent 70%
            ) !important;
        }

        /* Upload */
        .aw-upload {
            background: #FFFFFF !important;
            border: 2px dashed #C1121F !important;
            color: #C1121F !important;
        }

        .aw-upload:hover {
            background: #FFF5F5 !important;
            border-color: #C1121F !important;
            box-shadow: 0 18px 45px rgba(193,18,31,.15) !important;
        }

        .aw-upload-icon,
        .aw-upload-title {
            color: #C1121F !important;
        }

        .aw-upload-subtitle,
        .aw-upload-formats {
            color: #C1121F !important;
            opacity: .65;
        }

        /* Feature section */
        .aw-section-title {
            color: #C1121F !important;
        }

        .aw-section-title span {
            color: #C1121F !important;
        }

        .aw-section-subtitle {
            color: #C1121F !important;
            opacity: .7;
        }

        .aw-card {
            background: #FFFFFF !important;
            border: 2px solid #C1121F !important;
            color: #C1121F !important;
            box-shadow: 0 12px 35px rgba(193,18,31,.08) !important;
        }

        .aw-card:hover {
            background: #C1121F !important;
            color: #FFFFFF !important;
            box-shadow: 0 18px 45px rgba(193,18,31,.20) !important;
        }

        .aw-card-icon {
            color: #C1121F !important;
            background: #FFFFFF !important;
            border-color: #C1121F !important;
        }

        .aw-card-title,
        .aw-card-text {
            color: inherit !important;
        }

        /* Privacy card */
        .aw-privacy-card {
            background: #FFFFFF !important;
            border: 2px solid #FFFFFF !important;
        }

        .aw-privacy-icon {
            color: #C1121F !important;
            background: #FFFFFF !important;
            border-color: #C1121F !important;
        }

        .aw-privacy-title,
        .aw-privacy-text {
            color: #C1121F !important;
        }

        /* Buttons */
        .stButton > button {
            background: #C1121F !important;
            color: #FFFFFF !important;
            border: 2px solid #C1121F !important;
        }

        .stButton > button:hover {
            background: #FFFFFF !important;
            color: #C1121F !important;
            border-color: #C1121F !important;
        }

        /* Inputs */
        textarea,
        input,
        [data-baseweb="select"] > div {
            background: #FFFFFF !important;
            color: #C1121F !important;
            border-color: #C1121F !important;
        }

        /* File uploader */
        [data-testid="stFileUploader"] {
            color: #C1121F !important;
        }

        /* Streamlit links */
        a {
            color: #C1121F !important;
        }

        /* Red scan effect */
        .aw-doc::after {
            background: linear-gradient(
                90deg,
                transparent,
                rgba(193,18,31,.9),
                transparent
            ) !important;
            box-shadow: 0 0 18px rgba(193,18,31,.35) !important;
        }

        /* Red ambient animation */
        .stApp::before {
            background: radial-gradient(
                circle,
                rgba(193,18,31,.10) 0%,
                rgba(193,18,31,.035) 35%,
                transparent 72%
            ) !important;
        }

        /* Selection */
        ::selection {
            background: #C1121F !important;
            color: #FFFFFF !important;
        }


        /* =========================================================
           AGREEWISE — SOFT RED GLASSMORPHISM THEME
           ========================================================= */

        :root {
            --aw-red: #E86F7A;
            --aw-red-light: #F4A3AA;
            --aw-red-soft: #FCECEF;
            --aw-red-dark: #9F3F49;
            --aw-text: #54252A;
            --aw-muted: #8E686D;
            --aw-white: rgba(255, 255, 255, .72);
            --aw-border: rgba(232, 111, 122, .22);
        }

        /* Page */
        .stApp {
            background:
                radial-gradient(
                    circle at 85% 10%,
                    rgba(244, 163, 170, .20),
                    transparent 30%
                ),
                radial-gradient(
                    circle at 10% 85%,
                    rgba(232, 111, 122, .10),
                    transparent 28%
                ),
                #FFF9FA !important;
            color: var(--aw-text) !important;
        }

        .block-container {
            background: transparent !important;
        }

        /* =========================================================
           SIDEBAR GLASS
           ========================================================= */

        [data-testid="stSidebar"] {
            background:
                linear-gradient(
                    145deg,
                    rgba(252, 236, 239, .92),
                    rgba(255, 255, 255, .72)
                ) !important;
            border-right: 1px solid var(--aw-border) !important;
            backdrop-filter: blur(22px);
            -webkit-backdrop-filter: blur(22px);
            box-shadow: 8px 0 35px rgba(159, 63, 73, .06);
        }

        [data-testid="stSidebar"] .block-container {
            background: transparent !important;
        }

        .aw-brand {
            color: var(--aw-text) !important;
        }

        .aw-brand span {
            color: var(--aw-red) !important;
        }

        .aw-nav-label {
            color: var(--aw-red-dark) !important;
            opacity: .65;
        }

        [data-testid="stSidebar"] .stButton > button {
            color: var(--aw-text) !important;
            background: transparent !important;
            border: 1px solid transparent !important;
            border-radius: 12px !important;
        }

        [data-testid="stSidebar"] .stButton > button:hover {
            color: var(--aw-red-dark) !important;
            background: rgba(255, 255, 255, .60) !important;
            border-color: var(--aw-border) !important;
            box-shadow: 0 8px 25px rgba(159, 63, 73, .07);
        }

        /* =========================================================
           TOPBAR
           ========================================================= */

        .aw-topbar,
        .aw-topbar * {
            color: var(--aw-muted) !important;
        }

        /* =========================================================
           HERO
           ========================================================= */

        .aw-kicker {
            color: var(--aw-red) !important;
        }

        .aw-kicker span {
            color: var(--aw-red) !important;
        }

        .aw-title {
            color: var(--aw-text) !important;
        }

        .aw-gradient {
            color: var(--aw-red) !important;
            background: none !important;
            -webkit-text-fill-color: var(--aw-red) !important;
        }

        .aw-subtitle {
            color: var(--aw-muted) !important;
        }

        .aw-benefit {
            color: var(--aw-muted) !important;
        }

        .aw-check {
            color: var(--aw-red) !important;
        }

        /* =========================================================
           GLASS DOCUMENT
           ========================================================= */

        .aw-document-stage {
            background: transparent !important;
        }

        .aw-doc {
            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,.86),
                    rgba(255,247,248,.66)
                ) !important;
            border: 1px solid rgba(255,255,255,.85) !important;
            box-shadow:
                0 30px 70px rgba(159,63,73,.10),
                inset 0 1px 0 rgba(255,255,255,.95),
                0 0 45px rgba(232,111,122,.08) !important;
            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);
        }

        .aw-doc-title {
            color: var(--aw-text) !important;
        }

        .aw-line {
            background: var(--aw-red-light) !important;
            opacity: .38 !important;
        }

        .aw-insight {
            color: var(--aw-red-dark) !important;
            background: rgba(255,255,255,.58) !important;
            border: 1px solid rgba(255,255,255,.90) !important;
            box-shadow:
                0 12px 30px rgba(159,63,73,.09),
                inset 0 1px 0 rgba(255,255,255,.95) !important;
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
        }

        .aw-insight:hover {
            background: rgba(255,255,255,.82) !important;
            border-color: rgba(232,111,122,.35) !important;
        }

        .aw-glow {
            background:
                radial-gradient(
                    circle,
                    rgba(232,111,122,.16),
                    rgba(244,163,170,.08),
                    transparent 70%
                ) !important;
        }

        /* =========================================================
           UPLOAD GLASS
           ========================================================= */

        .aw-upload {
            background: rgba(255,255,255,.54) !important;
            border: 1px dashed rgba(232,111,122,.38) !important;
            color: var(--aw-text) !important;
            box-shadow:
                0 18px 45px rgba(159,63,73,.06),
                inset 0 1px 0 rgba(255,255,255,.90);
            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);
        }

        .aw-upload:hover {
            background: rgba(255,255,255,.78) !important;
            border-color: var(--aw-red) !important;
            box-shadow:
                0 20px 50px rgba(159,63,73,.10),
                0 0 30px rgba(232,111,122,.08) !important;
        }

        .aw-upload-icon,
        .aw-upload-title {
            color: var(--aw-red-dark) !important;
        }

        .aw-upload-subtitle,
        .aw-upload-formats {
            color: var(--aw-muted) !important;
        }

        /* =========================================================
           FEATURE GLASS CARDS
           ========================================================= */

        .aw-section-title {
            color: var(--aw-text) !important;
        }

        .aw-section-title span {
            color: var(--aw-red) !important;
        }

        .aw-section-subtitle {
            color: var(--aw-muted) !important;
        }

        .aw-card {
            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,.74),
                    rgba(255,248,249,.54)
                ) !important;
            border: 1px solid rgba(255,255,255,.88) !important;
            color: var(--aw-text) !important;
            box-shadow:
                0 16px 40px rgba(159,63,73,.07),
                inset 0 1px 0 rgba(255,255,255,.92);
            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);
        }

        .aw-card:hover {
            background: rgba(255,255,255,.88) !important;
            border-color: rgba(232,111,122,.30) !important;
            color: var(--aw-text) !important;
            box-shadow:
                0 22px 50px rgba(159,63,73,.11),
                0 0 28px rgba(232,111,122,.07) !important;
        }

        .aw-card-icon {
            color: var(--aw-red) !important;
            background: rgba(252,236,239,.72) !important;
            border-color: rgba(232,111,122,.20) !important;
        }

        .aw-card-title,
        .aw-card-text {
            color: var(--aw-text) !important;
        }

        .aw-card-text {
            color: var(--aw-muted) !important;
        }

        /* =========================================================
           PRIVACY GLASS
           ========================================================= */

        .aw-privacy-card {
            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,.68),
                    rgba(252,236,239,.55)
                ) !important;
            border: 1px solid rgba(255,255,255,.90) !important;
            box-shadow:
                0 14px 35px rgba(159,63,73,.07),
                inset 0 1px 0 rgba(255,255,255,.95);
            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);
        }

        .aw-privacy-icon {
            color: var(--aw-red) !important;
            background: rgba(252,236,239,.80) !important;
            border-color: rgba(232,111,122,.22) !important;
        }

        .aw-privacy-title {
            color: var(--aw-text) !important;
        }

        .aw-privacy-text {
            color: var(--aw-muted) !important;
        }

        /* =========================================================
           BUTTONS
           ========================================================= */

        .stButton > button {
            background: linear-gradient(
                135deg,
                #E86F7A,
                #D95C68
            ) !important;
            color: #FFFFFF !important;
            border: 1px solid rgba(255,255,255,.45) !important;
            box-shadow:
                0 8px 24px rgba(159,63,73,.16),
                inset 0 1px 0 rgba(255,255,255,.22);
        }

        .stButton > button:hover {
            background: linear-gradient(
                135deg,
                #ED7B85,
                #E06470
            ) !important;
            color: #FFFFFF !important;
            box-shadow:
                0 12px 30px rgba(159,63,73,.20),
                0 0 22px rgba(232,111,122,.12);
        }

        /* =========================================================
           INPUTS / TEXTAREA
           ========================================================= */

        textarea,
        input,
        [data-baseweb="select"] > div {
            background: rgba(255,255,255,.70) !important;
            color: var(--aw-text) !important;
            border-color: rgba(232,111,122,.20) !important;
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
        }

        textarea:focus,
        input:focus {
            border-color: rgba(232,111,122,.55) !important;
            box-shadow: 0 0 0 3px rgba(232,111,122,.08) !important;
        }

        /* =========================================================
           AMBIENT RED LIGHT
           ========================================================= */

        .stApp::before {
            background:
                radial-gradient(
                    circle,
                    rgba(232,111,122,.13) 0%,
                    rgba(244,163,170,.055) 38%,
                    transparent 72%
                ) !important;
            animation: awAmbient 9s ease-in-out infinite alternate;
        }

        /* Selection */
        ::selection {
            background: var(--aw-red) !important;
            color: #FFFFFF !important;
        }


        /* =========================================================
           AGREEWISE — SKY BLUE GLASSMORPHISM THEME
           ========================================================= */

        :root {
            --aw-blue: #38BDF8;
            --aw-blue-primary: #0EA5E9;
            --aw-blue-light: #BAE6FD;
            --aw-blue-dark: #0369A1;
            --aw-blue-soft: #E0F2FE;
            --aw-text: #163247;
            --aw-muted: #648095;
            --aw-white: rgba(255, 255, 255, .72);
            --aw-border: rgba(14, 165, 233, .20);
        }

        /* =========================================================
           MAIN BACKGROUND
           ========================================================= */

        .stApp {
            background:
                radial-gradient(
                    circle at 85% 8%,
                    rgba(56, 189, 248, .22),
                    transparent 30%
                ),
                radial-gradient(
                    circle at 8% 88%,
                    rgba(14, 165, 233, .12),
                    transparent 28%
                ),
                #F5FBFF !important;
            color: var(--aw-text) !important;
        }

        .block-container {
            background: transparent !important;
        }

        /* =========================================================
           SIDEBAR
           ========================================================= */

        [data-testid="stSidebar"] {
            background:
                linear-gradient(
                    145deg,
                    rgba(224, 242, 254, .92),
                    rgba(255, 255, 255, .76)
                ) !important;
            border-right: 1px solid var(--aw-border) !important;
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            box-shadow: 8px 0 35px rgba(3, 105, 161, .06);
        }

        [data-testid="stSidebar"] .block-container {
            background: transparent !important;
        }

        .aw-brand {
            color: var(--aw-text) !important;
        }

        .aw-brand span {
            color: var(--aw-blue-primary) !important;
        }

        .aw-nav-label {
            color: var(--aw-blue-dark) !important;
            opacity: .62;
        }

        [data-testid="stSidebar"] .stButton > button {
            color: var(--aw-text) !important;
            background: transparent !important;
            border: 1px solid transparent !important;
            border-radius: 12px !important;
        }

        [data-testid="stSidebar"] .stButton > button:hover {
            color: var(--aw-blue-dark) !important;
            background: rgba(255, 255, 255, .65) !important;
            border-color: var(--aw-border) !important;
            box-shadow: 0 8px 25px rgba(3, 105, 161, .07);
        }

        /* =========================================================
           HERO
           ========================================================= */

        .aw-kicker {
            color: var(--aw-blue-primary) !important;
        }

        .aw-kicker span {
            color: var(--aw-blue-primary) !important;
        }

        .aw-title {
            color: var(--aw-text) !important;
        }

        .aw-gradient {
            color: var(--aw-blue-primary) !important;
            background: none !important;
            -webkit-text-fill-color: var(--aw-blue-primary) !important;
        }

        .aw-subtitle {
            color: var(--aw-muted) !important;
        }

        .aw-benefit {
            color: var(--aw-muted) !important;
        }

        .aw-check {
            color: var(--aw-blue-primary) !important;
        }

        /* =========================================================
           GLASS DOCUMENT
           ========================================================= */

        .aw-document-stage {
            background: transparent !important;
        }

        .aw-doc {
            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,.88),
                    rgba(240,249,255,.68)
                ) !important;
            border: 1px solid rgba(255,255,255,.92) !important;
            box-shadow:
                0 30px 70px rgba(3,105,161,.10),
                inset 0 1px 0 rgba(255,255,255,.98),
                0 0 45px rgba(56,189,248,.10) !important;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
        }

        .aw-doc-title {
            color: var(--aw-text) !important;
        }

        .aw-line {
            background: var(--aw-blue-light) !important;
            opacity: .65 !important;
        }

        .aw-insight {
            color: var(--aw-blue-dark) !important;
            background: rgba(255,255,255,.62) !important;
            border: 1px solid rgba(255,255,255,.94) !important;
            box-shadow:
                0 12px 30px rgba(3,105,161,.09),
                inset 0 1px 0 rgba(255,255,255,.98) !important;
            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);
        }

        .aw-insight:hover {
            background: rgba(255,255,255,.88) !important;
            border-color: rgba(14,165,233,.35) !important;
        }

        .aw-glow {
            background:
                radial-gradient(
                    circle,
                    rgba(56,189,248,.20),
                    rgba(125,211,252,.08),
                    transparent 70%
                ) !important;
        }

        /* =========================================================
           UPLOAD GLASS
           ========================================================= */

        .aw-upload {
            background: rgba(255,255,255,.58) !important;
            border: 1px dashed rgba(14,165,233,.38) !important;
            color: var(--aw-text) !important;
            box-shadow:
                0 18px 45px rgba(3,105,161,.06),
                inset 0 1px 0 rgba(255,255,255,.95);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
        }

        .aw-upload:hover {
            background: rgba(255,255,255,.82) !important;
            border-color: var(--aw-blue-primary) !important;
            box-shadow:
                0 20px 50px rgba(3,105,161,.10),
                0 0 30px rgba(56,189,248,.10) !important;
        }

        .aw-upload-icon,
        .aw-upload-title {
            color: var(--aw-blue-dark) !important;
        }

        .aw-upload-subtitle,
        .aw-upload-formats {
            color: var(--aw-muted) !important;
        }

        /* =========================================================
           FEATURE CARDS
           ========================================================= */

        .aw-section-title {
            color: var(--aw-text) !important;
        }

        .aw-section-title span {
            color: var(--aw-blue-primary) !important;
        }

        .aw-section-subtitle {
            color: var(--aw-muted) !important;
        }

        .aw-card {
            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,.78),
                    rgba(240,249,255,.58)
                ) !important;
            border: 1px solid rgba(255,255,255,.92) !important;
            color: var(--aw-text) !important;
            box-shadow:
                0 16px 40px rgba(3,105,161,.07),
                inset 0 1px 0 rgba(255,255,255,.96);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
        }

        .aw-card:hover {
            background: rgba(255,255,255,.90) !important;
            border-color: rgba(14,165,233,.30) !important;
            box-shadow:
                0 22px 50px rgba(3,105,161,.11),
                0 0 28px rgba(56,189,248,.08) !important;
        }

        .aw-card-icon {
            color: var(--aw-blue-primary) !important;
            background: rgba(224,242,254,.82) !important;
            border-color: rgba(14,165,233,.20) !important;
        }

        .aw-card-title {
            color: var(--aw-text) !important;
        }

        .aw-card-text {
            color: var(--aw-muted) !important;
        }

        /* =========================================================
           PRIVACY GLASS
           ========================================================= */

        .aw-privacy-card {
            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,.72),
                    rgba(224,242,254,.60)
                ) !important;
            border: 1px solid rgba(255,255,255,.94) !important;
            box-shadow:
                0 14px 35px rgba(3,105,161,.07),
                inset 0 1px 0 rgba(255,255,255,.98);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
        }

        .aw-privacy-icon {
            color: var(--aw-blue-primary) !important;
            background: rgba(224,242,254,.85) !important;
            border-color: rgba(14,165,233,.22) !important;
        }

        .aw-privacy-title {
            color: var(--aw-text) !important;
        }

        .aw-privacy-text {
            color: var(--aw-muted) !important;
        }

        /* =========================================================
           BUTTONS
           ========================================================= */

        .stButton > button {
            background:
                linear-gradient(
                    135deg,
                    #38BDF8,
                    #0EA5E9
                ) !important;
            color: #FFFFFF !important;
            border: 1px solid rgba(255,255,255,.55) !important;
            box-shadow:
                0 8px 24px rgba(3,105,161,.16),
                inset 0 1px 0 rgba(255,255,255,.28);
        }

        .stButton > button:hover {
            background:
                linear-gradient(
                    135deg,
                    #7DD3FC,
                    #38BDF8
                ) !important;
            color: #FFFFFF !important;
            box-shadow:
                0 12px 30px rgba(3,105,161,.20),
                0 0 24px rgba(56,189,248,.16);
        }

        /* =========================================================
           INPUTS
           ========================================================= */

        textarea,
        input,
        [data-baseweb="select"] > div {
            background: rgba(255,255,255,.72) !important;
            color: var(--aw-text) !important;
            border-color: rgba(14,165,233,.20) !important;
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
        }

        textarea:focus,
        input:focus {
            border-color: rgba(14,165,233,.55) !important;
            box-shadow: 0 0 0 3px rgba(56,189,248,.10) !important;
        }

        /* =========================================================
           AMBIENT SKY-BLUE LIGHT
           ========================================================= */

        .stApp::before {
            background:
                radial-gradient(
                    circle,
                    rgba(56,189,248,.18) 0%,
                    rgba(125,211,252,.07) 38%,
                    transparent 72%
                ) !important;
            animation: awAmbient 9s ease-in-out infinite alternate;
        }

        /* Scan beam */
        .aw-doc::after {
            background: linear-gradient(
                90deg,
                transparent,
                rgba(14,165,233,.85),
                transparent
            ) !important;
            box-shadow: 0 0 18px rgba(56,189,248,.30) !important;
        }

        ::selection {
            background: var(--aw-blue-primary) !important;
            color: #FFFFFF !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )
