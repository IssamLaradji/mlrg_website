# mlrg_website



1. You can update the mlrg website (http://www.cs.ubc.ca/labs/lci/mlrg/) by changing the contents of the folder `/cs/web/www.cs.ubc.ca/docs/labs/lci/mlrg/`:
    * For example, you can use your CS account to add `slides`, `schedules`, and `css` and `index.html` to that folder.



2. Here are the folder descriptions:
    * `schedules` contains the presentation tables for each term;
    * `slides` contains the pdf slides sent by the presenters; 
    * `css` contains the style sheet for `index.html`;
    * `index.html` is the main page of the MLRG website; and
    * `main.py` is a script used to generate `index.html` from `template.html`
    
3. **Adding a pdf file.**

Let's say you wish to add the slides `mirrorDescent.pdf` to the topic
`mirror descent`. You can then follow these steps:
   1. add `mirrorDescent.pdf` to the `slides` folder;
   2. open the corresponding csv file in `schedules`; and
   3. find the line `mirror descent` and change it to `mirror descent - mirrorDescent.pdf`. 
   
When you run `main.py`, this generates the pdf hyperlink in `index.html`.

4. **Adding a table**

Let's say you want to add `winter_2018_term_2.csv` to index.html,  modify the variable `table_names
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
then generate the new `index.html` by running `main.py`.
This adds the tables of the csv files specified in `table_names` to `index.html` in order.
