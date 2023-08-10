# Customs Calculator

## INTRODUCTION:
Welcome to the **Customs Calculator**. Please read the instructions carefully to avoid any unnecessary errors
(**Do not skip them!**):
1. Only **numeric inputs** are **accepted**. **Negative numeric inputs** and **non-numeric inputs** are 
**automatically** considered as **errors** by the program.
2. Do not **leave anything blank** as the program will **not allow** it. If in any case, the amount to be computed is 
zero (0) then input the number zero (0).
3. Do not go **beyond the number of choices** as it will prompt you with an **INVALID INPUT** message.
4. You can **terminate** the program from inputting the **assigned number** if you want to quit the app.

## NOTES:
The **Customs Calculator** can help you calculate the following duties, taxes, and other charges (note that
some computations are still incomplete as they do not account for missing components and the backward computation):

### Total Landed Cost 
  - Formal Entry
    - Sea
    - Air
  - Informal Entry
    - Sea/Air


### Components of Landed Cost
  - **Dutiable Value** (DV)
    - Sea
    - Air
  - **Customs Duty** (CUD)
  - **Bank Charge** (BC)
  - **Brokerage Fee** (B/F)
    - Formal Entry
  - **Arrastre Charge** (A/C)
    - Outports
      - Shipside
      - Pierside
    - Port of Manila (POM) and Manila International Container Port (MICP)
      - Containerized Cargo (FCL)
        - Import
        - Export
        - Shut-out Export
      - Bulk or Break-bulk Cargo (LCL)
        - Import
        - Export
      - Containerized Dangerous Cargo
        - Class 1, 6, and 8
        - Class 2, 3, 4, and 7
        - Class 5 and 9
  - **Wharfage Due** (W/D)
    - Outports
      - Shipside
      - Pierside
    - Port of Manila (POM) and Manila International Container Port (MICP)
      - Containerized Cargo (FCL)
        - Import
        - Export
      - Bulk or Break-bulk Cargo (LCL)
        - Import
        - Export
      - Containerized Dangerous Cargo
        - 20 Footer Container
        - 40 Footer Container
  - **Import Processing Fee** (IPF)
  - **Customs Documentary Stamp** (CDS)
    - Formal Entry
    - Informal Entry

### Value-Added Tax (VAT)
  - Excise Tax Shipments
  - Non-Excise Tax Shipments

### Summary of Payments (SOP)
  - Covered by Letter of Credit (L/C)
  - Covered by Non-Letter of Credit
  - Covered by Informal Entry

### Container Security Fee (CSF)
  - 20 Footer Container
  - 40 Footer Container

### Pro-Rata
  - Individual Freight
  - Individual Insurance
  - Individual Dutiable Value
  - Individual Miscellaneous Expense

## INSTRUCTIONS:
To operate the Command-Line Interface of the Customs Tax Calculator, follow these steps:

1. Download the latest version of Python for your desktop. Here is the link for Windows (since my OS is Windows):
>https://www.python.org/downloads/windows/

>For other operating systems, you can look it up in this link:
>https://www.python.org/downloads/

>For a more comprehensive tutorial on how to download python click this link:
>https://www.youtube.com/watch?v=yivyNCtVVDk&ab_channel=GeekyScript

Note that in the YouTube video, the Python version is 3.11.1. However, the version should not significantly affect the
project, but make sure to download at least the latest one.

2. Next, download the files from my GitHub Repository using this link:
>https://github.com/iaaan05/customs-tax-calculator-py

3. Click the blue colored <> Code, then there should be a Download ZIP option. Click it, and choose to download it
to your desktop for convenience.

4. Locate the downloaded ZIP file and extract it using a tool like 7zip or WinRAR.

Note: After extracting it, open the extracted folder and move the content inside to your desktop, replacing the
existing one.

5. After replacing it, your folder structure should look similar to this, and you should be able to see where the menu
python file is located.

py-customs-dtoc-calculator
- csf
- landed_cost
- pro_rata
- sop
- utils
- vat
- .gitignore
- LICENSE
- run_app.py
- README.md

6. Search for the Command Prompt on your computer and run it as Administrator.

7. In the Command Prompt, enter `pip install customs_dtoc` to install the required package. This package is necessary for
the calculator to run.

8. After installing the required package, navigate back to the project folder and copy the path of the folder.

9. Go to the Command Prompt where you previously installed the package, or open another Command Prompt, and type
`cd 'the-copied-path-from-the-project-folder'`, paste (ctrl+v) the path of the project folder, and press enter to
navigate to the project folder.

11. In the Command Prompt, execute the app by typing py run_app.py.
