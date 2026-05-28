from datetime import datetime

def parse_date(value):
    try:
        return datetime.strptime(value,"%Y-%m-%d").date()
    except Exception:
        return None

def parse(row):
    flags=[]

    start=parse_date(row.get("billing_start"))
    end=parse_date(row.get("billing_end"))

    kwh_value=row.get("kwh")
    kwh=float(kwh_value) if kwh_value else None

    if not kwh:
        flags.append("missing kwh value")
    
    if start and end and (end-start).days>45:
        flags.append("billing period longer than 45 days")

    return{
        "site_code":row.get("site_code"),
        "activity_type":"electricity",
        "scope":"scope_2",
        "period_start":start,
        "period_end":end,
        "quantity_original":kwh,
        "unit_original":"kwh",
        "quantity_normalized":kwh,
        "unit_normalized":"kwh",
        "emissions_kgco2e":kwh*0.71 if kwh else None,
        "flags":flags,
    }
