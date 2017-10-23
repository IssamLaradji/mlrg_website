# mlrg_website



1. To update the website: http://www.cs.ubc.ca/labs/lci/mlrg/
    * user your CS account to add the folders `slides`, `schedules`, and `css` and the file `index.html` to:
`/cs/web/www.cs.ubc.ca/docs/labs/lci/mlrg/`



2. Here are the folder descriptions:
    * `schedules` contains the presentation tables for each term;
    * `slides` contains the pdf slides sent by the presenters; 
    * `css` contains the style sheet for `index.html`;
    * `index.html` is the main page of the MLRG website; and
    * `main.py` is a script used to generate `index.html` from `template.html`
    
3. To add the pdf file for a topic, for example, you wish to add the slides `mirrorDescent.pdf` to the topic
`mirror descent`. Put `mirrorDescent.pdf` in the `slides` folder and open the corresponding csv file in 
`schedules`. Find the topic `mirror descent` and change it to `mirror descent - mirrorDescent.pdf`. 
When you run `main.py`, this generates a pdf hyperlink in the corresponding table in `index.html`.

4. To add a table to index.html, for example `winter_2018_term_2.csv`,  modify the variable `table_names
in `main.py` from     

```python
table_names = ["winter_2017_term_1",
               "summer_2017",
               "winter_2017_term_2",
               "winter_2016_term_1",
               "summer_2016",
               "winter_2015_term_2",
               "winter_2015_term_1",
               "summer_2015_term_2"]
```
to
```python
    table_names = [
               "winter_2018_term_2",
               "winter_2017_term_1",
               "summer_2017",
               "winter_2017_term_2",
               "winter_2016_term_1",
               "summer_2016",
               "winter_2015_term_2",
               "winter_2015_term_1",
               "summer_2015_term_2"]
```
This adds the tables of the csv files specified in `table_names` to `index.html` in order.