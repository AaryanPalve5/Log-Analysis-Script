# Log Analysis and Chatbot Integration

This project analyzes a server log file (`sample.log`) to extract valuable insights. It performs tasks like:

  - Counting IP request occurrences
  - Identifying the most frequently accessed endpoints
  - Detecting suspicious activity based on failed login attempts

Additionally, it integrates a chatbot powered by Google Gemini. This chatbot leverages the processed log data to answer user queries interactively, providing a convenient way to explore the analysis results.

## Features

* **Log File Parsing:** Extracts data from the server log file, focusing on IP addresses, endpoints, and status codes.
* **Data Analysis:** Analyzes the log data to reveal:
    * The most frequently accessed endpoints
    * Suspicious IPs based on failed login attempts (configurable threshold)
    * Request count per IP address
* **CSV Export:** Saves the analysis results to a CSV file (`log_analysis_results.csv`) for further analysis and visualization.
* **Chatbot Integration:** Uses Google Gemini's Retrieval-Augmented Generation (RAG) model to enable users to query the logs and results interactively.

## Files

* `chat_app.py`: Script implementing the chatbot that answers user queries using the processed log data.
* `log_analysis.py`: Script responsible for parsing the log file, performing analysis, and saving results.
* `log_analysis_results.csv`: CSV file storing the analysis results.
* `sample.log`: Sample log file containing server logs.
* `requirements.txt`: Text file listing the Python dependencies required for the project.
