# Run the following by python3
pos = input("Position name: ")
add = input("Company location: ")
company = input("Company name: ")


from datetime import datetime
date = datetime.date(datetime.now())
d = date.strftime("%B %-dnd, %Y")

f = open("CoverLetter_temp")
st = f.read().replace("Company",company)
st = st.replace("POS",pos)
f.close()

from fpdf import FPDF
# page setting
pdf = FPDF("P","mm","A4")
pdf.add_page()
pdf.ln(20)
pdf.set_margins(25.4,25.4,25.4)

# Header
pdf.set_font("Times",size=34)
pdf.multi_cell(160,6,txt="     Yidi Chen\n\n")
pdf.set_font("Times",size=11)
pdf.set_text_color(0,102,102)
pdf.multi_cell(160,6,txt="2634 Marblevista Blvd | Columbus, OH, 43204  \n706-254-3412  \nyidi.chen.7@gmail.com \n\n")

# Company Info
pdf.set_text_color(0,0,0)
pdf.multi_cell(160,6,txt=d+"\n"+"Hiring Manager\n"+company+"\n"+add+"\n")
pdf.set_font("Times",size=11)

# Letter Content
pdf.multi_cell(160,6,txt = st)
pdf.output('../../Documents/job hunting/Coverletter/'+company+'_CoverLetter.pdf')
