AIRPORTS={
    "BOM":"Mumbai",
    "DEL":"Delhi",
    "BLR":"Bangalore",
}

def estimate_distance(
    origin,destination):
    distances={
        ("BOM","DEL"):1140,
        ("DEL","BOM"):1140,
        ("BOM","BLR"):840,
    }

    return distances.get((origin,destination))

def parse(row):
    flags=[]
    segment_type=row.get("segment_type")
    origin=row.get("origin")
    destination=row.get("destination")

    if segment_type == "flight":
        if origin not in AIRPORTS or destination not in AIRPORTS:
            flags.append("unknown airport code")
        
        distance_value=row.get("distance_km")
        quantity=float(distance_value) if distance_value else estimate_distance(origin,destination)

        if not quantity:
            flags.append("Missing flight distance")

        return{
            "site_code":None,
            "activity_type":"flight",
            "scope":"scope_3",
            "quantity_original":quantity,
            "unit_original":"km",
            "quantity_normalized":quantity,
            "unit_normalized":"km",
            "emissions_kgco2e":quantity*0.115 if quantity else None,
            "flags":flags,
        }
    
    if segment_type == "hotel":
        nights=float(row.get("nights") or 0)

        if nights<=0:
            flags.append("invalid number of nights")
        
        return{
            "site_code":None,
            "activity_type":"hotel",
            "scope":"scope_3",
            "quantity_original":nights,
            "unit_original":"nights",
            "quantity_normalized":nights,
            "unit_normalized":"nights",
            "emissions_kgco2e":nights*30,
            "flags":flags,
        }
    
    distance=float(row.get("distance_km") or 0)

    if distance<=0:
        flags.append("Missing ground transport distance")

    return{
        "site_code":None,
        "activity_type":"ground_transport",
        "scope":"scope_3",
        "quantity_original":distance,
        "unit_original":"km",
        "quantity_normalized":distance,
        "unit_normalized":"km",
        "emissions_kgco2e":distance*0.18,
        "flags":flags,
    }
