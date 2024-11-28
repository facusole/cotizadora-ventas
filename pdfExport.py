from fpdf import FPDF

def exportToPDF(data):
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # Set font
    pdf.set_font("Arial", size=12)

    # Add title
    pdf.cell(200, 10, txt="Cost Report", ln=True, align="C")

    # Add column headers
    pdf.ln(10)
    pdf.cell(40, 10, "Date", border=1, align="C")
    pdf.cell(40, 10, "Product Cost", border=1, align="C")
    pdf.cell(40, 10, "Technical Cost", border=1, align="C")
    pdf.cell(40, 10, "Logistics Cost", border=1, align="C")
    pdf.cell(40, 10, "Cost Before Taxes", border=1, align="C")
    pdf.cell(40, 10, "Price", border=1, align="C")
    pdf.cell(40, 10, "Price with IVA", border=1, align="C")

    # Line break
    pdf.ln()

    # Add data rows
    for entry in data:
        pdf.cell(40, 10, entry["date"], border=1)
        pdf.cell(40, 10, str(entry["productCost"]), border=1)
        pdf.cell(40, 10, str(entry["technicalCost"]), border=1)
        pdf.cell(40, 10, str(entry["logysticsCost"]), border=1)
        pdf.cell(40, 10, str(entry["costBeforeTaxes"]), border=1)
        pdf.cell(40, 10, str(entry["price"]), border=1)
        pdf.cell(40, 10, str(entry["priceWithIVA"]), border=1)
        pdf.ln()

    # Output the PDF
    pdf.output("archivos/cost_report.pdf")
