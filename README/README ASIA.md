\# \<h1 align="center"\>\*\*Arctic Sea Ice Age Analysis\*\*\</h1\> 

\<p align="justify"\>This project presents a Python-based analysis of Arctic Sea Ice Age and Sea Ice Concentration data. The study investigates the temporal variability of Arctic sea ice, including changes in ice age categories, daily sea ice concentration, and the distribution of different ice age classes.\</p\>

\<p align="justify"\>Developed as a scientific data analysis project, the study uses real Arctic sea ice data from the Copernicus Marine Service and applies a reproducible workflow involving data preparation, exploratory data analysis, statistical analysis, SQL querying, and data visualization.\</p\>

\*\*Development environment:\*\* Visual Studio Code (VS Code)

\*\*Project status:\*\* \_Completed\_ \- Python, SQL and Power BI analysis 

\#\# Objective

\<p align="justify"\>The objective of this project is to investigate the characteristics and temporal variability of Arctic sea ice using Sea Ice Age and Sea Ice Concentration data.\</p\>

The analysis addresses the following questions:

\<table align="center"\> \<tr\> \<th\>Question\</th\> \<th\>Approach\</th\> \</tr\> \<tr\> \<td\>How does Arctic sea ice concentration vary over time?\</td\> \<td\>Analysis of daily sea ice concentration observations\</td\> \</tr\> \<tr\> \<td\>How is sea ice distributed among different age categories?\</td\> \<td\>Comparison of sea ice age categories\</td\> \</tr\> \<tr\> \<td\>How do different sea ice age categories vary over time?\</td\> \<td\>Time-series analysis of age-category variables\</td\> \</tr\> \<tr\> \<td\>What are the daily sea ice concentration values for each ice age category?\</td\> \<td\>SQL queries applied to the \<code\>ice\_concentration\</code\> table\</td\> \</tr\> \<tr\> \<td\>What are the main characteristics of the Arctic sea ice dataset?\</td\> \<td\>Exploratory data analysis and descriptive statistics\</td\> \</tr\> \<tr\> \<td\>How can the analyzed data be explored interactively?\</td\> \<td\>Power BI dashboard and data visualizations\</td\> \</tr\> \</table\> 

\#\# Dataset

\<p align="justify"\>  
The dataset contains monthly Sea Surface Temperature anomaly observations from 1982 to 2024\. The data were obtained from the Copernicus Marine Service Ocean Climate Portal.  
\</p\>

\[Source: Copernicus Marine Service — Arctic Sea Ice Age Analysis\]([https://data.marine.copernicus.eu/product/SEAICE\_ARC\_PHY\_AUTO\_L4\_MY\_011\_025/description](https://data.marine.copernicus.eu/product/SEAICE_ARC_PHY_AUTO_L4_MY_011_025/description))

\<table align="center"\>  
  \<tr\>  
    \<th\>Variable\</th\>  
    \<th\>Description\</th\>  
  \</tr\>  
  \<tr\>  
    \<td\>\<code\>date\</code\>\</td\>  
    \<td\>Date of the observation\</td\>  
  \</tr\>  
  \<tr\>  
    \<td\>\<code\>sst\_anomaly\</code\>\</td\>  
    \<td\>Sea Surface Temperature anomaly (K)\</td\>  
  \</tr\>  
  \<tr\>  
    \<td\>\<code\>year\</code\>\</td\>  
    \<td\>Year extracted from the date\</td\>  
  \</tr\>  
  \<tr\>  
    \<td\>\<code\>month\</code\>\</td\>  
    \<td\>Month extracted from the date\</td\>  
  \</tr\>  
  \<tr\>  
    \<td\>\<code\>rolling\_12m\</code\>\</td\>  
    \<td\>12-month rolling mean\</td\>  
  \</tr\>  
  \<tr\>  
    \<td\>\<code\>period\</code\>\</td\>  
    \<td\>Predefined time period\</td\>  
  \</tr\>  
\</table\>

\#\# Methodology

\*\*Data Acquisition\*\*

\<p align="justify"\> The Arctic Sea Ice Age dataset was obtained in NetCDF format. Multiple daily files were downloaded and organized for processing. The files contain gridded observations covering the Arctic region.\</p\> 

\*\*Data Preparation\*\*

\<p align="justify"\> The NetCDF files were inspected and combined using Python and \<code\>xarray\</code\>. The dataset structure, dimensions, variables, coordinates, and metadata were examined before the analysis. \</p\>

\<p align="justify"\> The resulting data were prepared for analysis and exported into formats suitable for statistical analysis, SQL queries, and visualization. \</p\>

\*\*Exploratory Data Analysis\*\*

\<p align="justify"\> The dataset was explored to identify its dimensions, variables, temporal coverage, and the distribution of sea ice age and concentration values. Descriptive statistics and visualizations were used to investigate the main characteristics of the observations.\</p\> 

\*\*Sea Ice Age Analysis\*\*

\<p align="justify"\> Sea ice age categories were analyzed to investigate the distribution and temporal behavior of different ice age classes. The analysis focused on comparing younger and older sea ice categories and identifying differences in their concentration values.\</p\> 

\*\*Sea Ice Concentration Analysis\*\*

\<p align="justify"\> Daily sea ice concentration variables were analyzed for the different sea ice age categories. These observations were used to investigate how concentration varies across the available ice age classes.\</p\> 

\*\*SQL Analysis\*\*

\<p align="justify"\> A relational SQLite database was created from the processed sea ice data. SQL queries were developed to inspect the database, retrieve observations, examine the first records, and analyze daily sea ice concentration for different ice age categories.\</p\>

\<p align="justify"\> The SQL analysis provides an additional way of exploring the dataset and demonstrates the use of relational databases for scientific data analysis.\</p\>

\*\*Data Visualization\*\*

\<p align="justify"\> The analyzed data were visualized using Python and Power BI. Python visualizations were used during the exploratory analysis, while Power BI was used to create an interactive dashboard for presenting the main results.\</p\> 

\#\# Visualisations

\*\*Daily Sea Ice Age\*\*

\<p align="justify"\> Visualization of the daily mean Arctic sea ice age during the analyzed period. \</p\>

\<p align="center"\> \<img src="daily\_mean\_ice\_age.png" alt="Daily Mean Arctic Sea Ice Age" width="800"\> \</p\>

\*\*Power BI Dashboard\*\*

\<p align="justify"\> Interactive dashboard presenting the main Arctic sea ice age and concentration indicators and visualizations. \</p\>

\<p align="center"\> \<img src="power\_bi\_dashboard.png" alt="Arctic Sea Ice Power BI Dashboard" width="800"\> \</p\>

\#\# Results

\<p align="justify"\> The analysis provides an overview of Arctic sea ice age and sea ice concentration during the analyzed period. The results allow comparisons between different ice age categories and provide a structured view of daily Arctic sea ice conditions. \</p\>

\<p align="justify"\> The SQL queries provide a reproducible way of accessing and analyzing the processed data, while the Power BI dashboard presents the main results in an interactive format. \</p\>

\<p align="justify"\> The generated CSV files contain processed and summarized data that can be reused for further analysis and visualization. \</p\>

\#\# Output Files

\<table align="center"\> \<tr\> \<th align="center"\>File\</th\> \<th align="center"\>Description\</th\> \</tr\> \<tr\> \<td align="center"\>\<code\>analise\_gelo.py\</code\>\</td\> \<td align="center"\>Python analysis of the Arctic sea ice dataset\</td\> \</tr\> \<tr\> \<td align="center"\>\<code\>analise\_gelo.sql\</code\>\</td\> \<td align="center"\>SQL queries used to analyze the processed data\</td\> \</tr\> \<tr\> \<td align="center"\>\<code\>criar\_banco.py\</code\>\</td\> \<td align="center"\>Python script used to create the SQLite database\</td\> \</tr\> \<tr\> \<td align="center"\>\<code\>import\_os.py\</code\>\</td\> \<td align="center"\>Script used to locate and process the NetCDF files\</td\> \</tr\> \<tr\> \<td align="center"\>\<code\>gelo\_artico.db\</code\>\</td\> \<td align="center"\>SQLite database containing the processed sea ice data\</td\> \</tr\> \<tr\> \<td align="center"\>\<code\>dados\_gelo\_artico\_sql.csv\</code\>\</td\> \<td align="center"\>Processed data prepared for SQL analysis\</td\> \</tr\> \<tr\> \<td align="center"\>\<code\>Daily Mean Ice Age.png\</code\>\</td\> \<td align="center"\>Daily mean Arctic sea ice age visualization\</td\> \</tr\> \<tr\> \<td align="center"\>\<code\>Power BI.pbix\</code\>\</td\> \<td align="center"\>Power BI interactive dashboard\</td\> \</tr\> \</table\>

\#\# Scientific Context

\<p align="justify"\> Arctic sea ice is an important component of the climate system and plays a significant role in interactions between the atmosphere, ocean, and cryosphere. Sea ice age provides information about the history and persistence of ice within the Arctic system, while sea ice concentration describes the proportion of the ocean surface covered by sea ice. \</p\>

\<p align="justify"\> Analyzing sea ice age and concentration together allows different characteristics of the Arctic sea ice cover to be investigated. Younger and older ice categories can exhibit different temporal behaviors, making age information useful for understanding the structure and variability of the sea ice cover. \</p\>

\<p align="justify"\> This project focuses on describing patterns present in the dataset through data analysis and visualization. It does not attempt to establish the causes of the observed variations or directly quantify their environmental impacts. \</p\>

\#\# Technologies

\*\*Programming and Development\*\*  
\- Python  
\- Visual Studio Code (VS Code) 

\*\*Python Libraries\*\*  
\- Pandas  
\- Xarray  
\- Matplotlib   
\- NumPy

\*\*Database and Querying\*\*  
\- SQL   
\- SQLite

\*\*Data Visualization\*\*  
\- Power BI

\*\*Data Format\*\*  
\- NetCDF  
\- CSV

\#\# Skills Demonstrated

\<p align="center"\>\<i\>Python \- Pandas \- Xarray \- Data Cleaning \- Exploratory Data Analysis \- Time-Series Analysis \- Scientific Data Analysis \- SQL \- SQLite \- Data Visualisation \- Power BI \- Oceanographic Data \- Cryospheric Data\</i\>\</p\> 

\#\# Author

\#\#\# Mariana Gomes de Andrade Silva

Scientific data analysis project focused on Arctic sea ice age and concentration. 

\<p align="center"\>\<strong\>Interests: Oceanography \- Scientific Programming \- Data Analysis \- Environmental Data\</strong\>\</p\>