# Phase2_Project_Group2 – Group 2: Movie Industry Analysis
## Team Members 
Njuki (Branch: `Njuki-README`) – README Author & Contributor to Data Cleaning/EDA
## Project Overview
This project analyzes movie industry data from multiple sources to provide insights for a new film studio looking to enter the market. The analysis focuses on:

    Genre performance (ratings and ROI)

    Director success metrics

    Content rating impact

    Language and popularity trends
    The goal is to understand how genres and ratings influence movie success and perception, from both critic and audience perspectives.

 ##   Objectives
Perform detailed data cleaning and preprocessing
Analyze trends in:
genre
popularity
votes
financial performance
Visualize relationships such as:
a.Budget vs. Revenue
b.Popularity vs. Success
c.Identify the most profitable and popular movies

# Data Sources
The analysis uses 7 key datasets:

    IMDB (SQLite database) - Movie metadata, directors, ratings

    TheMovieDB - Popularity metrics and language data

    Rotten Tomatoes Movies - Critic and audience ratings

    Rotten Tomatoes Critic Reviews - Detailed review data

    Box Office Mojo - Financial performance

    The Numbers - Budget and gross earnings

    im.db - Additional IMDb data in SQLite format
## Dataset Information
 Source- 
 Key Features- id, original_title, release_date, budget, revenue, runtime, popularity, vote_average and the move  genres
 Cleaning Steps inclueded;
 1.Removed missing and zero values 
 2.Dropped duplicates
 3.Converted date fields
 4.Genres broken down and interpreted
 
## Key  Business Questions
- Which movie genres  are most commonly produced?
- What kind of movies  generate the highest profits?
- How has movie production changed  over  time?
- Does a larger budget lead to higher revenue?
 Which directors and languages are associated with top-performing movies?
 ## Cleaning & Processing Summary
  Removed missing or zero-value entries (e.g. budgets, revenue)
 Dropped duplicates to ensure data integrity
 Processed and formatted the release_date fields
 Split multi-genre fields into normalized records using `.explode()`
 Standardized column names
 Extracted relevant columns (e.g., `movie_title`, `genres`, `audience_rating`, `tomatometer_rating`)
 Handled multi-genre entries using `.explode()` for genre-specific analysis
  Merged datasets as needed

 ## Tools and Libraries used 
 Python- the main programing language used
 pandas-Data manipulation 
 numpy-Numerical operations
 matplotlib- Plotting
 seaborn -Advanced visualizations
jupyter Notebook-Interactive data exploration
sqlite3 – Querying SQL database
  
  ##  Visuals
###  Top Genres
Bar chart showing the most common and profitable movie genres.
###  Movie Production Over the Years
Line graph showing the number of movies released annually.
###  Budget vs. Revenue
Scatter plot revealing correlations between production budgets and box office returns.
###  Correlation Matrix
Heatmap of key numerical features (budget, revenue, popularity, etc.).
### Movie Runtime Distribution
Histogram showing common durations of films in the dataset.
##  Getting Started

1. Clone the repository
2. Ensure all required datasets are in the `Data/` folder
3. Run `index.ipynb` in Jupyter Notebook
4. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn

## License
This project is intended for educational use only. No commercial license applied.

##  requirements.txt




 
