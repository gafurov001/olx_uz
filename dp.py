import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_invoice(filename, invoice_data):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica", 25)
    c.drawString(30, height - 80, f"{invoice_data['first_name']} {invoice_data['last_name']}", charSpace=0)

    c.setFont("Helvetica", 14)
    c.drawString(30, height - 120, f"Telefon raqami")
    c.setFont("Helvetica", 15)
    c.drawImage("media/tel.png", 30, height - 148, width=17, height=17)
    c.drawString(55, height - 145, f"{invoice_data['phone_number']}")
    c.setFont("Helvetica", 14)
    c.drawString(220, height - 120, f"Elektron pochta")
    c.drawImage("media/sms.png", 218, height - 145, width=18, height=17)
    c.setFont("Helvetica", 15)
    c.drawString(244, height - 141, f"{invoice_data['email']}")
    c.setFont("Helvetica", 14)
    c.drawString(30, height - 190, f"Tug'ilgan yil")
    c.setFont("Helvetica", 16)
    c.drawImage("media/kalendar.png", 30, height - 213, width=18, height=17)
    c.drawString(55, height - 211, f"{invoice_data['year_of_birth']}")
    c.setFont("Helvetica", 14)
    c.drawString(30, height - 265, f"KASBIY TAJRIBA")
    c.setFont("Helvetica", 16)
    c.drawString(30, height - 305, f"{invoice_data['position_name']}")
    c.setFont("Helvetica", 13)
    c.drawString(30, height - 333, f"{invoice_data['employer']}")
    c.setFont("Helvetica", 13)
    c.drawString(30, height - 360,
                 f"{datetime.date.strftime(invoice_data['work_start_date'], '%B %Y')} - {'Hozir ham ishlayapti' if invoice_data['working_now'] else f'{datetime.date.strftime(invoice_data['work_end_date'], '%B %Y')} [{invoice_data['work_end_date'].month - invoice_data['work_start_date'].month} oylar]'}")
    c.setFont("Helvetica", 15)
    c.drawString(30, height - 420, f"TA'LIM")
    c.setFont("Helvetica", 13)
    c.drawString(30, height - 450, f"{invoice_data['name_of_educational']}")
    c.drawString(30, height - 475, f"{invoice_data['direction']}")
    c.drawString(30, height - 500,
                 f"{datetime.date.strftime(invoice_data['year_of_admission'], '%Y')} - {'hozir' if invoice_data['studying_now'] else datetime.date.strftime(invoice_data['graduation_year'], '%Y')}")
    c.drawImage("media/fon.png", 410, height - 790, width=700, height=900)
    c.setFont("Helvetica", 15)
    c.drawString(433, height - 80, f"KO'NIKMALAR")
    c.setFont("Helvetica", 13)
    c.drawString(433, height - 115, f"Tillarni bilishi")
    c.drawString(433, height - 145, f"{invoice_data['language']}")
    c.drawString(490, height - 145, f"{invoice_data['level_knowledge']}")
    c.setFont("Helvetica", 15)
    c.drawString(433, height - 190, f"XOBBI")
    c.setFont("Helvetica", 13)
    c.drawString(433, height - 220, f"{invoice_data['hobby']}")
    c.save()


invoice_data = {
    "first_name": "Faxriddin",
    "last_name": "Gafurov",
    "phone_number": "330073223",
    "email": "a@gmail.com",
    "year_of_birth": "2004",
    "position_name": "Developer",
    "employer": "EPAM",
    "work_start_date": datetime.date.today(),
    "work_end_date": datetime.date.today(),
    "year_of_admission": datetime.date.today(),
    "graduation_year": datetime.date.today(),
    "studying_now": False,
    "working_now": False,
    "name_of_educational": 'PDP',
    "direction": 'Python',
    "language": 'English',
    "level_knowledge": "O'rta",
    "hobby": "Kod yozish",
}

generate_invoice(f"{invoice_data['first_name'].lower()}_{invoice_data['last_name'].lower()}.pdf", invoice_data)


