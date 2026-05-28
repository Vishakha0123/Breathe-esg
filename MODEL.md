# MODEL.md

## Core Design

The system separates raw input data from normalized ESG activity records.

RawRecord stores the exact source row received from SAP, utility exports, or travel exports. ActivityRecord stores the normalized version that analysts review.

This separation supports auditability because approved records can always be traced back to the original source row.

## Main Entities

### Tenant
Represents the enterprise client.

### Site
Represents a plant, warehouse, office, or facility.

### SourceSystem
Represents SAP, utility portal, or corporate travel platform.

### IngestionRun
Represents one file upload/import event.

### RawRecord
Stores the original row exactly as received.

### ActivityRecord
Stores normalized ESG activity data.

### ReviewDecision
Stores analyst review actions.

### AuditEvent
Stores important workflow events such as creation, approval, and locking.

## Scope Mapping

SAP fuel data is Scope 1.

Electricity consumption is Scope 2.

Business travel is Scope 3.

## Unit Normalization

The system stores both original and normalized values.

Example:

- Original: 120 GAL
- Normalized: 454.249 liters

This preserves source truth while giving analysts a common unit for review.

## Review Lifecycle

Records move through:

- pending
- suspicious
- approved
- locked

Suspicious records contain validation flags such as unknown plant codes, missing kWh, invalid airport codes, or negative quantities.

## Audit Trail

Approved and locked records create AuditEvent rows.

Locked records represent auditor-ready records and should not be edited in production.