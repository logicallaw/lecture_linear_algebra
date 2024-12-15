import PyPDF2


def rotatePDF(srcPDF, destPDF):
    with open(srcPDF, 'rb') as infile:
        reader = PyPDF2.PdfReader(infile)
        writer = PyPDF2.PdfWriter()

        # 반복문을 사용하여 모든 페이지를 90도 반시계 방향으로 회전시킨다.
        for page in reader.pages:
            rotated_page = page.rotate(90)
            writer.add_page(rotated_page)

        with open(destPDF, 'wb') as outfile:
            writer.write(outfile)
    print("Success!")


rotatePDF('./srcPDF.pdf', 'destPDF.pdf')
