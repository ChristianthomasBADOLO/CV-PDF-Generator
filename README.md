# Professional CV Generator

This tool generates professional CVs in PDF format from JSON data. It parses a JSON file containing personal details, work experience, education, skills, etc., and converts it into a well-formatted PDF. The process involves generating an HTML CV template using AI-based enhancements, and then converting the HTML to a PDF using Google Chrome's print function.

## Features

- **HTML Template Generation**: Generates a minimalistic and professional HTML CV template filled with JSON data.
- **PDF Conversion**: Converts the HTML CV to PDF using Google Chrome's headless browser.


## Metodology

This image outlines the step-by-step process used to generate professional CVs from user-provided data, detailing each stage from data input to the final PDF output.


## Usage Guidelines

### JSON Input Format

Your JSON input can contain the following fields:

```json
{
  "personal_details": {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "123-456-7890",
    "address": "123 Main Street, Anytown, USA"
  },
  "work_experience": [
    {
      "position": "Software Engineer",
      "company": "ABC Corp",
      "start_date": "Jan 2020",
      "end_date": "Present",
      "responsibilities": [
        "Developed web applications",
        "Collaborated with cross-functional teams"
      ]
    }
  ],
  "education": [
    {
      "degree": "BSc in Computer Science",
      "institution": "University of XYZ",
      "start_date": "Sep 2015",
      "end_date": "Jun 2019"
    }
  ],
  "skills": [
    "Python", "JavaScript", "HTML", "CSS"
  ]
}
```

### Running the Tool

1. **Generate HTML Template**

    The JSON data is input into a Google Gemini prompt to generate the HTML template.

    ```python
    # Sample code for generating HTML using Google Gemini and your JSON data
    html_content = generate_html_from_json(json_data)
    ```

2. **Save HTML to File**

    ```python
    file_path = 'cv.html'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)
    ```

3. **Convert HTML to PDF**

This configuration is for Ubuntu and may vary for Windows. Please check and adapt the following code accordingly.


    ```python
    import os
    import time
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    import base64

    file_url = 'file://' + os.path.abspath('cv.html')
    chrome_driver_path = '/path/to/chromedriver'

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--kiosk-printing')

    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(file_url)
    time.sleep(3)

    params = {
        "landscape": False,
        "displayHeaderFooter": False,
        "printBackground": True,
        "preferCSSPageSize": True,
        "paperWidth": 8.27,
        "paperHeight": 11.69,
        "marginTop": 0,
        "marginBottom": 0,
        "marginLeft": 0,
        "marginRight": 0
    } # These parameters allow a good format downloading of the PDF

    result = driver.execute_cdp_cmd("Page.printToPDF", params)
    with open("cv.pdf", "wb") as file:
        file.write(base64.b64decode(result['data']))

    driver.quit()
    ```

### Example JSON Input

Refer to the sample JSON input format provided above. Customize it with your own data and follow the steps to generate your professional CV.

## Customizable Templates

You can customize the HTML template as per your requirements. Simply update the `generate_html_from_json` function to reflect your preferred design and layout.

## Contribution

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

