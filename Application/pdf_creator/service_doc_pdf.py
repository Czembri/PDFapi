import weasyprint


def html(**kwargs):
    html_txt= f"""
    <!doctype html>
        <html lang="pl">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
            </head>
            <body>
                <div class='container'>
                    <div class="row justify-content-center">
                        <div class="col justify-content-center d-flex">
                            <h4><i>Skrócony dokument serwisowy nr {kwargs["internaldocumentid"]["internaldocumentid"]}</i></h4>
                        </div>
                    </div>
                    <br>
                    <div class="row justify-content-end">
                        <div class="col d-flex justify-content-end">
                            <span>Data: {kwargs["documentdate"]["documentdate"]}</span>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col">
                            <p>Zgłaszający</p>
                            <p style="font-size:11px">Imię i nazwisko: {kwargs["clientname"]["clientname"]}</p>
                            <p style="font-size:11px">Adres: {kwargs["clientaddress"]["clientaddress"]}</p>
                        </div>
                        <div class="col">
                            <p>Przyjmujący zlecenie</p>
                            <p style="font-size:11px">Imię i nazwisko: {kwargs["employeename"]["employeename"]}</p>
                            <p style="font-size:11px">Nr pracownika: {kwargs["employeenumber"]["employeenumber"]}</p>
                        </div>
                    </div>
                    <hr style="width:100%;text-align:left;margin-left:0">
                    <div class="row justify-content-center">
                        <p style="font-size:11px">Rodzaj urządzenia: {kwargs["devicetype"]["devicetype"]}</p>
                        <p style="font-size:11px">Marka:  {kwargs["devicebrand"]["devicebrand"]}</p>
                        <p style="font-size:11px">Model: {kwargs["devicemodel"]["devicemodel"]}</p>
                    </div>
                    <hr style="width:100%;text-align:left;margin-left:0">
                    <div class="row">
                        <div class="col">
                            Opis usterki: 
                        </div>
                    </div>
                    <div class="row">
                        <div class="col">
                            {kwargs["descr"]["descr"]}
                        </div>
                    </div>
                    <br>
                    <br>
                    <br>
                    <br>
                    <div class="row">
                        <div class="col d-flex justify-content-start">
                            <span style="font-size:11px">Podpis zlecającego: </span>
                            <p>...................................</p>
                        </div>
                        <div class="col d-flex justify-content-end">
                            <span style="font-size:11px">Podpis wystawiającego: </span>
                            <p>...................................</p>
                        </div>
                    </div>
                </div>

                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
            </body>
        </html>
    """
    # html_file = open("G:\\Python\\projects\\PDFapi\\Application\\pdf_creator\\templates\\service_document_temp.html", "w")
    # html_file.write(html_txt)
    # html_file.close()

    return html_txt


def extract_information(**kwargs):
    html_tt = html(
        documentdate=kwargs['documentdate'], 
        clientname=kwargs['clientname'], 
        clientaddress=kwargs['clientaddress'],
        employeename=kwargs['employeename'],
        employeenumber=kwargs['employeenumber'],
        devicetype=kwargs['devicetype'],
        devicebrand=kwargs['devicebrand'],
        devicemodel=kwargs['devicemodel'],
        descr=kwargs['descr'],
        internaldocumentid=kwargs['internaldocumentid']
    )

    pdf = weasyprint.HTML(string=html_tt)
    return pdf.write_pdf()