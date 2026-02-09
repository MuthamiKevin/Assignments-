show search_path;
set search_path to retail;

CREATE TABLE IF NOT EXISTS retail_raw (
    InvoiceNo VARCHAR(20),
    StockCode VARCHAR(20),
    Description TEXT,
    Quantity INTEGER,
    InvoiceDate TIMESTAMP,
    UnitPrice NUMERIC(10,2),
    CustomerID NUMERIC,
    Country VARCHAR(50)
);

SELECT COUNT(*) 
FROM retail.retail_raw;

