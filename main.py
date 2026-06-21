import pandas as pd
from excel_generator import generate_xlsx
from open_sap import remove_old_token, get_sap_token, open_sap, run_automation
from email_workorders import send_email
from pathlib import Path


downloads = Path(r"DOWNLOADS FILEPATH PLACEHOLDER")
workorders_file = Path(r"TARGET FOLDER PLACEHOLDER")
sap_token = downloads / "tx.sap"
script = Path(r"SAP SCRIPT PLACEHOLDER, should download a tab separated values file")

workers = {
    
}

def main():
    remove_old_token(sap_token)
    get_sap_token()
    open_sap(sap_token)
    run_automation(script)
    generate_xlsx()
    for worker in workers:
        email = workers.get(worker)
        send_email(email, workorders_file / f"Tech_{worker}.xlsx")



main()
