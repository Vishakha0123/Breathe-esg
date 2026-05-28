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