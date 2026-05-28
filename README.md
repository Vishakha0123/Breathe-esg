# Breathe ESG Ingestion Prototype

## Overview

This is a Django REST + React prototype for ingesting ESG activity data from three sources:

1. SAP fuel/procurement CSV
2. Utility electricity CSV
3. Corporate travel CSV

The system normalizes rows, flags suspicious records, and lets analysts approve and lock records for audit.

## Features

- CSV upload
- Source-specific parsers
- Raw source row storage
- Normalized activity records
- Scope 1, Scope 2, Scope 3 mapping
- Suspicious row flags
- Analyst approval
- Audit locking
- React review dashboard

## Backend Setup

```bash
cd backend
.\venv\Scripts\activate
python manage.py migrate
python manage.py seed
python manage.py runserver


## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

## Sample Data

Sample CSVs are available in:

```text
sample_data/
```

Files:

* sap_fuel.csv
* utility_electricity.csv
* travel_data.csv

---

## Deployment

### Frontend (Netlify)

Live URL:

```text
https://melodious-caramel-879d00.netlify.app
```

### Backend (Render)

API Base URL:

```text
https://breathe-esg-backend.onrender.com/api/activities/
```

---

## Architecture

### Backend

* Django REST Framework
* SQLite (local)
* PostgreSQL (production)
* CSV ingestion services
* Multi-tenant data model
* Audit trail support

### Frontend

* React + Vite
* Axios API integration
* Analyst review dashboard
* Upload workflow

---

## Analyst Workflow

1. Upload CSV source file
2. System parses and normalizes rows
3. Suspicious records are flagged
4. Analyst reviews records
5. Analyst approves rows
6. Approved rows can be locked for audit

---

## API Endpoints

### Upload CSV

```text
POST /api/upload/
```

### List Activities

```text
GET /api/activities/
```

### Approve Record

```text
POST /api/activities/<id>/approve/
```

### Lock Record

```text
POST /api/activities/<id>/lock/
```

---

## Production Notes

This prototype focuses on:

* realistic ingestion flows
* auditability
* normalization
* analyst review workflow

Not implemented:

* authentication
* async processing
* large-scale file handling
* real SAP/API integrations
* production-grade emissions factor engine
