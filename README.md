# Breathe ESG Ingestion Prototype

## Overview

This project is a Django REST + React prototype for ingesting ESG activity data from multiple enterprise source systems.
The application supports ingestion, normalization, review, approval, and audit locking of ESG-related activity records.

Supported ingestion sources:

1. SAP fuel/procurement CSV
2. Utility electricity CSV
3. Corporate travel CSV

The system parses uploaded CSV files, stores raw rows for auditability, converts records into normalized activity records, flags suspicious data, and provides an analyst review workflow through a React dashboard.

---

# Features

* CSV upload workflow
* Source-specific ingestion parsers
* Raw source row preservation
* Normalized ESG activity records
* Scope 1 / Scope 2 / Scope 3 classification
* Suspicious record detection
* Analyst approval workflow
* Audit locking workflow
* Multi-source ingestion support
* React review dashboard
* REST API backend
* Deployment on Render + Netlify

---

# Tech Stack

## Backend

* Python
* Django
* Django REST Framework
* SQLite (local development)
* PostgreSQL (production)
* WhiteNoise
* Gunicorn

## Frontend

* React
* Vite
* Axios
* CSS

## Deployment

* Render (Backend)
* Netlify (Frontend)

# Backend Setup

## 1. Navigate to backend
```bash
cd backend
```
## 2. Create virtual environment
```bash
python -m venv venv
```
## 3. Activate virtual environment
### Windows
```bash
.\venv\Scripts\activate
```
## 4. Install dependencies
```bash
pip install -r requirements.txt
```
## 5. Run migrations
```bash
python manage.py migrate
```
## 6. Seed initial data
```bash
python manage.py seed
```
## 7. Start backend server
```bash
python manage.py runserver
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

# Frontend Setup

## 1. Navigate to frontend
```bash
cd frontend
```
## 2. Install dependencies
```bash
npm install
```
## 3. Start frontend server
```bash
npm run dev
```
Frontend runs on:

```text
http://localhost:5173
```

---

# Sample Data

Sample CSV files are located in:

```text
sample_data/
```

Files:

* sap_fuel.csv
* utility_electricity.csv
* travel.csv

---

# Deployment

## Frontend (Netlify)

Live Frontend URL:

```text
https://melodious-caramel-879d00.netlify.app
```

## Backend (Render)

Backend API URL:

```text
https://breathe-esg-1-h9ib.onrender.com/api
```

---

# Architecture

## Backend Architecture

The backend uses Django REST Framework for API development.

Core components:

* ingestion services
* source-specific parsers
* normalization pipeline
* suspicious flag generation
* audit tracking
* analyst workflow endpoints

### Main Models

* Tenant
* Site
* SourceSystem
* IngestionRun
* RawRecord
* ActivityRecord
* ReviewDecision
* AuditEvent

---

## Frontend Architecture

The frontend is built using React + Vite.

Features include:

* CSV upload interface
* activity review table
* suspicious flag visualization
* summary dashboard cards
* approve/lock actions
* API integration using Axios

---

# ESG Workflow

## Upload Workflow

1. Analyst uploads CSV file
2. Backend parser processes source-specific schema
3. Raw source rows stored in database
4. Records normalized into ActivityRecord objects
5. Suspicious rows flagged automatically
6. Analyst reviews records
7. Approved records can be locked for audit

---

# API Endpoints

## Upload CSV

```text
POST /api/upload/
```

Uploads and processes CSV source files.

---

## List Activities

```text
GET /api/activities/
```

Returns normalized activity records.

---

## Approve Record

```text
POST /api/activities/<id>/approve/
```

Approves an activity record.

---

## Lock Record

```text
POST /api/activities/<id>/lock/
```

Locks approved records for audit purposes.

---

# Suspicious Record Detection

The system flags suspicious rows for analyst review.

Examples:

* negative quantities
* missing values
* unknown site codes
* unusually large electricity usage
* abnormal travel distances
* long billing periods

Suspicious rows remain reviewable by analysts before approval.

# Deployment Notes

The backend is deployed on Render using:

* Gunicorn
* PostgreSQL
* WhiteNoise

The frontend is deployed on Netlify and communicates with the Render backend API.

---


