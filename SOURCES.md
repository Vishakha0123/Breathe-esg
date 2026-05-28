# SOURCES.md

## SAP

I researched SAP-style exports for material and procurement activity.

What I learned:

SAP exports often use technical column names and can include plant codes, posting dates, material codes, quantities, and units.

Sample data includes:

- WERKS
- BUDAT
- MATNR
- MENGE
- MEINS
- KOSTL

Why sample looks this way:

The sample includes mixed date formats, plant codes, fuel materials, liters, gallons, and an unknown plant code.

What would break in production:

- custom SAP field names
- service procurement
- multi-line purchase orders
- IDoc hierarchy
- client-specific plant mappings

## Utility Electricity

I researched common utility portal exports and billing data.

What I learned:

Electricity data often includes meter IDs, billing periods, kWh, tariffs, and demand values. Billing periods may not align to calendar months.

Sample data includes:

- meter ID
- site code
- billing start
- billing end
- kWh
- tariff
- peak kW

Why sample looks this way:

The sample includes a long billing period, missing kWh, unknown site code, and realistic commercial/industrial tariff names.

What would break in production:

- PDF-only bills
- interval meter data
- estimated bills
- multiple meters per site
- utility-specific tariff formats

## Corporate Travel

I researched corporate travel platform exports such as Concur/Navan-style itinerary data.

What I learned:

Travel data may include flights, hotels, and ground transport. Flights may provide airport codes but not always distances.

Sample data includes:

- trip ID
- segment type
- origin airport
- destination airport
- distance km
- hotel nights
- amount

Why sample looks this way:

The sample includes missing flight distance, airport-code based estimation, hotel nights, ground transport distance, and an invalid airport code.

What would break in production:

- multi-leg flights
- cancellations/refunds
- missing airport metadata
- international emission factor differences
- class of travel adjustments