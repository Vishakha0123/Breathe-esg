from datetime import datetime

def parse_date(value):
    for fmt in("%d.%m.%Y","%Y-%m-%d"):
        try:
            return datetime.strptime(value, fmt).date()
        except Exception:
            pass
        return None
def normalize_unit(quantity,unit):
    unit=unit.upper().strip()
    if unit == "L":
        return quantity, "liters"
    
    if unit == "GAL":
        return quantity*3.78541, "liters"
    
    return quantity,unit

def parse(row):
    flags=[]
    quantity=float(row.get("MENGE") or 0)
    unit=row.get("MEINS") or ""
    normalized_quantity, normalized_unit=normalize_unit(quantity,unit)

    if quantity<0:
        flags.append("negative quantity")

    if unit.upper() not in ["L","GAL"]:
        flags.append("unrecognized unit")

    return{
        "site_code":row.get("WERKS"),
        "activity_type":"fuel",
        "scope":"scope_1",
        "activity_date":parse_date(row.get("BUDAT")),
        "quantity_original":quantity,
        "unit_original":unit,
        "quantity_normalized":normalized_quantity,
        "unit_normalized":normalized_unit,
        "emissions_kgco2e":normalized_quantity*2.68,
        "flags":flags,
    }