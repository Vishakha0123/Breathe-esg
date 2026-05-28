# TRADEOFFS.md

## 1. No Live SAP Integration

I did not build direct SAP integration.

Reason:

SAP integrations require client-specific credentials, modules, field mappings, and security approval. A CSV upload is more realistic for a 4-day onboarding prototype.

## 2. No Utility PDF OCR

I did not build PDF bill extraction.

Reason:

Utility bills vary heavily by provider. OCR would take significant time and would likely be unreliable. CSV exports better demonstrate the ingestion and review workflow.

## 3. No Full Emissions Factor Engine

I used simplified emission factors.

Reason:

A production system should version emission factors by geography, year, activity type, and methodology. That is important, but outside this prototype’s main goal.

## 4. No Full Authentication System

I did not build role-based user login.

Reason:

The assignment focuses more on data model, ingestion, and review workflow. In production, analysts, admins, and auditors would need separate permissions.