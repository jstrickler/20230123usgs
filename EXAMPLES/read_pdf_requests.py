import sys
import os
from subprocess import run  # for running external PDF viewer
import requests

url = 'https://www.nasa.gov/pdf/739318main_ISS%20Utilization%20Brochure%202012%20Screenres%203-8-13.pdf'  # target URL
saved_pdf_file = 'nasa_iss.pdf'  # name of PDF file for saving

response = requests.get(url)  # open the URL
if response.status_code == requests.codes.OK:  # check status code
    if response.headers.get('content-type') == 'application/pdf':
        with open(saved_pdf_file, 'wb') as pdf_out:  # open local file
            pdf_out.write(response.content)  # write data to a local file in binary mode; response.content is data from URL

        if sys.platform == 'win32':  # select platform and choose the app to open the PDF file
            cmd = saved_pdf_file
        elif sys.platform == 'darwin':
            cmd = 'open ' + saved_pdf_file
        else:
            cmd = 'acroread ' + saved_pdf_file

        run(cmd.split())  # run requires command to be split into words
