# DECISIONS.md

## Prototype Scope

I built a CSV-based ingestion prototype for SAP, utility electricity, and corporate travel data.

The goal is not to build a full carbon accounting engine. The goal is to demonstrate ingestion, normalization, review, traceability, and audit locking.

## SAP Decision

I chose SAP-style flat CSV exports for fuel/procurement data.

The sample uses SAP-like fields:

- WERKS for plant
- BUDAT for posting date
- MATNR for material
- MENGE for quantity
- MEINS for unit

I chose this because enterprise teams often begin ESG onboarding with manual SAP exports before API integrations are approved.

I did not implement IDoc, BAPI, or OData integration because those require client-specific SAP configuration and authentication.

## Utility Decision

I chose utility portal CSV exports for electricity data.

The sample includes:

- meter ID
- site code
- billing start date
- billing end date
- kWh
- tariff
- peak demand

I chose this because facilities teams commonly download billing data manually from utility portals.

I did not implement PDF bill extraction because OCR and bill layout parsing would be unreliable for a 4-day prototype.

## Travel Decision

I chose Concur-style travel export rows.

The sample supports:

- flights
- hotels
- ground transport

Flight rows may include airport codes without distance, so the system estimates distance for known airport pairs.

I did not implement live Concur/Navan OAuth integration.

## Analyst Review Decision

Rows are not automatically audit-ready. They are first marked pending or suspicious.

Analysts can approve rows and then lock them.

## Questions for PM

- Which clients need live integrations first?
- Which emissions factor database should be authoritative?
- Should analysts be able to edit records after approval?
- What exact evidence do auditors require?
- Should suspicious rows block audit locking?