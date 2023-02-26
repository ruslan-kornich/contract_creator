import docx
from django.conf import settings


def contract_create(data: dict) -> str:
    dictionary = data
    doc = docx.Document(settings.BLANK_PATH)
    style = doc.styles["Normal"]
    font = style.font
    font.name = "Times New Roman"
    font.size = docx.shared.Pt(11)
    for i in dictionary:
        for p in doc.paragraphs:
            if p.text.find(i) >= 0:
                p.text = p.text.replace(i, dictionary[i])
    for j in dictionary:
        for table in doc.tables:
            for col in table.columns:
                for cell in col.cells:
                    for paragraph in cell.paragraphs:
                        if paragraph.text.find(j) >= 0:
                            paragraph.text = paragraph.text.replace(j, dictionary[j])
    contract_path = settings.CONTRACT_PATH + f'{data.get("short_name")}.docx'
    doc.save(contract_path)
    return contract_path
