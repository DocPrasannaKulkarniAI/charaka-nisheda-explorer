Niṣedha Explorer – Classical Prohibitions as per Charaka Samhita
Overview

Niṣedha Explorer is a web-based academic reference tool designed for the structured exploration of classical prohibitions (Niṣedha) as described in the Charaka Samhita.
The application enables users to systematically retrieve Niṣedha statements by combining textual context (Sthāna) with practical domain (Āhāra, Vihāra, Ācāra, Vicāra), thereby preserving the original yukti (rational logic) of Ayurveda.

This tool is intended for Ayurveda students, teachers, clinicians, and researchers.

Objectives

To digitize and structure classical Niṣedha references from Charaka Samhita

To prevent indiscriminate interpretation by enforcing contextual filtering

To support teaching, learning, and clinical reasoning grounded in classical texts

To provide a clean, extensible foundation for future AI-assisted (GPT-RAG) applications

Core Features

Dual mandatory filters

Sthāna-wise selection (textual context)

Domain-wise selection (Āhāra / Vihāra / Ācāra / Vicāra)

Devanāgarī-safe display of original ślokas

English meanings and structured interpretive remarks

Prevention of full-dataset dumping to maintain pedagogical clarity

Web-based, publicly accessible deployment

How to Use the App

Select one or more Sthāna (e.g., Sutrasthana, Vimanasthana).

Select one or more Niṣedha domains:

Āhāra (dietary)

Vihāra (lifestyle)

Ācāra (conduct/ethics)

Vicāra (clinical judgment)

View the filtered Niṣedha references, each displayed with:

Source (Sthāna / Chapter / Śloka)

Original Devanāgarī text

English meaning

Domain classification

Statement of prohibition / application

Note: Results are displayed only when both filters are selected, in keeping with Ayurvedic methodological rigor.

Data Source

Primary source: Charaka Samhita

Data manually curated and structured in Excel format

Columns include:

Sthāna

Chapter

Śloka

Śloka (Devanāgarī)

Meaning

Niṣedha domain

Interpretive remarks / current application

Technical Stack

Frontend / App framework: Streamlit

Data handling: Pandas

Data storage: Excel (.xlsx, Unicode-safe)

Deployment: Streamlit Community Cloud

Repository Structure
charaka-nisheda-explorer/
│
├── app.py
├── requirements.txt
└── data/
    └── Charaka_Nishedas.xlsx

Versioning

v1.0 – Initial public release

Dual mandatory filtering

Devanāgarī-safe display

Stable deployment

Intended Use

This tool is intended for:

Academic teaching and tutorials

Self-learning by students

Clinical reflection by practitioners

Research conceptualization and text analysis

It is not intended to replace classical study or clinical judgment.
