# <h1 align="center">**Arctic Sea Ice Age Analysis**</h1>


<p align="justify">Third project in my oceanographic data series. After a single-variable time series and a full 3D ocean biogeochemistry model, this one moves into the cryosphere: Arctic sea ice age and sea ice concentration by age category, built from a raw NetCDF model file. The goal was to build a full workflow around this kind of polar data — inspecting and processing the NetCDF file, aggregating it into daily time series, loading it into SQLite, and connecting it to an interactive Power BI dashboard.</p>


**Development environment:** Visual Studio Code (VS Code)


**Project status:** _Completed_ — Python, SQL and Power BI


## Why This Dataset


<p align="justify">Arctic sea ice is one of the most direct, visible indicators of climate change, and I wanted a project that went beyond "how much ice is there" into "what kind of ice is there." Sea ice age does exactly that: instead of a single concentration number, the dataset breaks the ice pack down by how many years it has survived — from first-year ice up to six-year-plus ice — which is a much better proxy for how resilient the ice cover actually is than total concentration alone. It also gave me a smaller, more manageable NetCDF file to practice the inspect → aggregate → database → dashboard pipeline on before scaling up to the full 3D ocean model in the biogeochemistry project.</p>


Questions I tried to answer:


<table align="center">
  <tr>
    <th>Question</th>
    <th>Approach</th>
  </tr>
  <tr>
    <td>How does overall sea ice age change day to day?</td>
    <td>Daily spatial mean of sea ice age, plotted as a time series</td>
  </tr>
  <tr>
    <td>How is the ice pack distributed across age categories?</td>
    <td>Mean concentration per age category (1-year to 6-year ice)</td>
  </tr>
  <tr>
    <td>How does concentration for each age category change day to day?</td>
    <td>Daily spatial mean per category, aggregated into a time series</td>
  </tr>
  <tr>
    <td>Which age category was most and least present during the month?</td>
    <td>Min/max/average concentration per category in SQL</td>
  </tr>
  <tr>
    <td>On which days was 1-year-old ice concentration highest and lowest?</td>
    <td>Ranking queries (<code>ORDER BY ... LIMIT</code>) in SQL</td>
  </tr>
  <tr>
    <td>How can the daily concentration data be explored interactively?</td>
    <td>Power BI dashboard built on the SQLite export</td>
  </tr>
</table>


## Dataset


<p align="justify">
Daily Arctic sea ice fields for May 2026, in NetCDF-4 format, containing gridded sea ice age together with sea ice concentration split into six age categories (1-year through 6-year-plus ice).
</p>


[Source: Copernicus Marine Service — Arctic Sea Ice Age Analysis](https://data.marine.copernicus.eu/product/SEAICE_ARC_PHY_AUTO_L4_MY_011_025/description)


<table align="center">
  <tr>
    <th>Property</th>
    <th>Value</th>
  </tr>
  <tr><td>Product ID</td><td><code>SEAICE_ARC_PHY_AUTO_L4_MY_011_025</code></td></tr>
  <tr><td>Source file</td><td><code>gelo_artico_maio_2026.nc</code></td></tr>
  <tr><td>Temporal resolution</td><td>Daily</td></tr>
  <tr><td>Period covered</td><td>May 2026 (31 daily records, 2026-05-01 to 2026-05-31)</td></tr>
  <tr><td>Spatial dimensions</td><td>Gridded, with <code>time</code>, <code>y</code> and <code>x</code> dimensions</td></tr>
  <tr><td>Format</td><td>NetCDF-4</td></tr>
</table>


### Variables


<table align="center">
  <tr>
    <th>Code</th>
    <th>Description</th>
  </tr>
  <tr><td><code>siage</code></td><td>Sea ice age (continuous variable, gridded)</td></tr>
  <tr><td><code>conc_1yi</code></td><td>Concentration of 1-year-old ice</td></tr>
  <tr><td><code>conc_2yi</code></td><td>Concentration of 2-year-old ice</td></tr>
  <tr><td><code>conc_3yi</code></td><td>Concentration of 3-year-old ice</td></tr>
  <tr><td><code>conc_4yi</code></td><td>Concentration of 4-year-old ice</td></tr>
  <tr><td><code>conc_5yi</code></td><td>Concentration of 5-year-old ice</td></tr>
  <tr><td><code>conc_6yi</code></td><td>Concentration of 6-year-plus ice</td></tr>
</table>


## What I Did


<table align="center">
  <tr><th align="center">Step</th><th align="center">Script</th><th align="center">Purpose</th></tr>
  <tr><td align="center">01</td><td><code>import_os.py</code></td><td align="justify">List the raw files available in <code>dados_brutos</code> before processing</td></tr>
  <tr><td align="center">02</td><td><code>analise_gelo.py</code></td><td align="justify">Inspect the NetCDF file, compute sea ice age statistics, aggregate daily means, and export the concentration data for SQL and Power BI</td></tr>
  <tr><td align="center">03</td><td><code>criar_banco.py</code></td><td align="justify">Load the processed concentration data into a SQLite database</td></tr>
  <tr><td align="center">04</td><td><code>analise_gelo.sql</code></td><td align="justify">Query the database — inspect records, compare age categories, rank days by concentration</td></tr>
</table>


**Inspecting the NetCDF file**


<p align="justify">
Before touching the numbers, I inspected <code>gelo_artico_maio_2026.nc</code> with <code>xarray</code>: its dimensions, data variables, coordinates, per-variable attributes, and missing-value counts for every variable. This step is what told me the file holds one continuous variable (<code>siage</code>) plus six concentration variables, one per ice age category.
</p>


**Sea ice age**


<p align="justify">
I calculated global minimum, maximum, mean and median for <code>siage</code>, then collapsed the spatial (<code>y</code>, <code>x</code>) dimensions into a daily mean, giving one sea ice age value per day for May 2026. That time series was plotted directly from Python and saved as a PNG — it wasn't pushed into the SQL/Power BI stage, since the database is built around the concentration-by-category variables instead.
</p>


**Sea ice concentration by age category**


<p align="justify">
For each of the six concentration variables, I computed the overall mean and then aggregated the spatial dimensions the same way as for <code>siage</code>, producing a daily concentration value per age category. That table is the core dataset used downstream, in both the SQL database and the Power BI dashboard.
</p>


**SQL analysis**


<p align="justify">
I loaded the daily concentration table into SQLite (<code>gelo_artico.db</code>) and wrote queries to inspect the table, pull the first records, compare category averages, find the highest and lowest concentration days for 1-year-old ice, rank the top and bottom five days, check the date range and record count, and compute the min/max/average for every age category at once.
</p>


**Data visualization**


<p align="justify">
Python produced the daily sea ice age plot during the exploratory stage. Power BI was used afterward to build an interactive dashboard on top of the exported concentration data, so the six age categories can be compared and filtered day by day.
</p>


## Database Structure


<table align="center">
  <tr><th align="center">Table</th><th align="center">Rows</th><th align="center">Columns</th><th align="center">What's in it</th></tr>
  <tr><td align="center"><code>ice_concentration</code></td><td align="center">31</td><td align="center">7</td><td align="justify">One row per day in May 2026, with the daily mean concentration for each of the six ice age categories</td></tr>
</table>


<p align="justify">Zero missing values in the exported table — every day in May 2026 has a value for all six categories.</p>


<p align="center"><strong>Mean daily concentration by age category (May 2026)</strong></p>


<table align="center">
  <tr><th>Category</th><th>Min</th><th>Mean</th><th>Max</th></tr>
  <tr><td>1-year ice (<code>conc_1yi</code>)</td><td>0.4753</td><td>0.5157</td><td>0.5453</td></tr>
  <tr><td>2-year ice (<code>conc_2yi</code>)</td><td>0.1076</td><td>0.1089</td><td>0.1099</td></tr>
  <tr><td>3-year ice (<code>conc_3yi</code>)</td><td>0.0543</td><td>0.0549</td><td>0.0556</td></tr>
  <tr><td>4-year ice (<code>conc_4yi</code>)</td><td>0.0107</td><td>0.0111</td><td>0.0116</td></tr>
  <tr><td>5-year ice (<code>conc_5yi</code>)</td><td>0.0075</td><td>0.0077</td><td>0.0079</td></tr>
  <tr><td>6-year-plus ice (<code>conc_6yi</code>)</td><td>0.0021</td><td>0.0022</td><td>0.0023</td></tr>
</table>


<p align="justify">The pattern is pretty stark: over half the ice pack sits in the youngest category, and concentration drops off sharply with age — by the 6-year-plus category, mean concentration is roughly 230x smaller than for 1-year ice. This lines up with what's expected physically: most Arctic ice melts before it gets old, so older categories represent a shrinking, more resilient minority of the total pack rather than the norm.</p>


## Visualisations


**Daily Sea Ice Age**


<p align="justify">
Daily mean Arctic sea ice age across May 2026, computed from the spatial average of <code>siage</code> for each day.
</p>


<p align="center">
  <img src="daily_mean_ice_age.png" alt="Daily Mean Arctic Sea Ice Age" width="800">
</p>


## Power BI Dashboard


<p align="justify">
The daily concentration-by-category table was loaded into Power BI to turn the SQL export into an interactive view of how the ice pack's age composition shifted over May 2026. The report lets you filter by date and compare the six age categories side by side, instead of reading them off a static table.
</p>


<p align="justify">
Power BI report file:
<p align="center">
  <code>arctic_sea_ice_power_bi_dashboard.pbix</code>
</p>


## Results


<p align="justify">
The 31-day series shows a sea ice pack heavily dominated by first-year ice, with concentration falling off sharply through each older category. The daily sea ice age plot gives a complementary, single-number view of how old the ice pack is on average day to day, while the category breakdown shows what that average is actually made of.
</p>


<p align="justify">
The SQL queries provide a reproducible way to re-slice the data (by day, by category, by ranking), and the Power BI dashboard presents the same daily concentration data interactively.
</p>


## Output Files


<table align="center">
  <tr><th align="center">File</th><th align="center">Description</th></tr>
  <tr><td align="center"><code>import_os.py</code></td><td align="center">Lists the raw files in <code>dados_brutos</code></td></tr>
  <tr><td align="center"><code>analise_gelo.py</code></td><td align="center">Main analysis: NetCDF inspection, sea ice age stats, daily aggregation, CSV export</td></tr>
  <tr><td align="center"><code>criar_banco.py</code></td><td align="center">Loads the processed CSV into the SQLite database</td></tr>
  <tr><td align="center"><code>analise_gelo.sql</code></td><td align="center">SQL queries used to explore the database</td></tr>
  <tr><td align="center"><code>gelo_artico_maio_2026.nc</code></td><td align="center">Raw NetCDF source file (May 2026)</td></tr>
  <tr><td align="center"><code>dados_gelo_artico_sql.csv</code></td><td align="center">Daily concentration by age category, prepared for SQL (31 rows)</td></tr>
  <tr><td align="center"><code>powerbi_gelo_artico.csv</code></td><td align="center">Same daily concentration data, exported for Power BI</td></tr>
  <tr><td align="center"><code>gelo_artico.db</code></td><td align="center">SQLite database containing the <code>ice_concentration</code> table</td></tr>
  <tr><td align="center"><code>daily_mean_ice_age.png</code></td><td align="center">Daily mean Arctic sea ice age visualization</td></tr>
  <tr><td align="center"><code>arctic_sea_ice_power_bi_dashboard.pbix</code></td><td align="center">Power BI interactive dashboard</td></tr>
</table>


## Notes


<p align="justify">
Arctic sea ice sits at the interface between ocean, atmosphere and cryosphere, and it's one of the more sensitive parts of the climate system — small changes there tend to ripple outward. Concentration alone says how much of the ocean surface is covered by ice on a given day, but it doesn't say much about how stable that ice cover actually is. Age fills that gap: it separates thin, fragile first-year ice from thicker, more resilient ice that has survived several melt seasons.
</p>


<p align="justify">
<strong>Why the age breakdown matters.</strong> In this May 2026 snapshot, first-year ice makes up by far the largest share of the pack, and each older category is smaller than the last by roughly an order of magnitude. That's consistent with a broader trend documented in Arctic research over the past few decades: multi-year ice, which used to make up a much larger share of the Arctic ice pack, has been shrinking as more ice melts out completely each summer instead of surviving into another year. A pack skewed this heavily toward young ice is structurally more vulnerable — first-year ice is thinner and melts out more easily than ice that has had years to thicken.
</p>


<p align="justify">
<strong>Albedo and Arctic amplification.</strong> Sea ice reflects far more sunlight than open ocean water. As older, thicker multi-year ice gets replaced by thinner first-year ice or by open water, the region absorbs more solar energy, which drives further warming and further ice loss — a feedback loop generally called Arctic amplification, and a major reason the Arctic is warming several times faster than the global average.
</p>


<p align="justify">
<strong>Why this matters beyond the Arctic.</strong> Shifts in the ice pack's age structure affect species that depend on stable, multi-year ice — polar bears and ice-associated seals among them — and affect indigenous communities whose travel and subsistence hunting rely on predictable ice conditions. They also open or close shipping routes as multi-year ice retreats or persists. Arctic sea ice loss has also been linked to changes in mid-latitude weather patterns, so the effects don't stay contained within the Arctic Circle.
</p>


<p align="justify">
That said, this project covers a single month (May 2026) from one processed NetCDF file — there's no seasonal or multi-year trend here, and it can't say whether the age distribution shown is typical for the season or represents a longer-term shift. It also describes the pattern present in the dataset rather than establishing what's driving it. A multi-month or multi-year version of this pipeline, comparing age composition across seasons, would be a natural next step.
</p>


## Tools


**Programming and Development**
- Python
- SQL
- Power BI
- Visual Studio Code (VS Code)


**Python Libraries**
- Xarray
- Pandas
- Matplotlib


**Database**
- SQLite


**Data Format**
- NetCDF
- CSV


## Skills Demonstrated


<p align="center"><i>Python - Pandas - Xarray - NetCDF Processing - Data Aggregation - Exploratory Data Analysis - Time-Series Analysis - SQL - SQLite - Database Design - Data Visualisation - Power BI - Scientific Data Analysis - Oceanographic Data</i></p>


## Bibliography


- [Copernicus Marine Service — Arctic Sea Ice Age Analysis, product description](https://data.marine.copernicus.eu/product/SEAICE_ARC_PHY_AUTO_L4_MY_011_025/description)
- [NSIDC — Sea Ice Age](https://nsidc.org/learn/parts-cryosphere/sea-ice/science-sea-ice)
- [NASA Climate — Arctic Sea Ice Age](https://climate.nasa.gov/vital-signs/arctic-sea-ice/)


## Author


### Mariana Gomes de Andrade Silva


<p align="justify">Second project in my oceanographic data series, focused on Arctic sea ice age and concentration by age category.</p>


<p align="center"><strong>Interests: Oceanography - Scientific Programming - Data Analysis - Environmental Data</strong></p>



