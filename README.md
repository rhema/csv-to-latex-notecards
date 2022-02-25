# csv-to-latex-notecards
Script for generating latex notecards from qualitative interview transcripts that are in CSV format.

To run, use:

```
python3 csv-to-latex-card.py input.csv out.tex
```

This will generate an out.tex file that you can copy and paste into Overleaf or whatever LaTeX setup you gave to generate a PDF.

The CSV should have a format like below, with the minimum headers:
| id | context | text |
| --- | --- | --- |
| an id unique to the row for later reference (e.g. 1, 2, 3) | the participant identifier and possibly timestamps | The actual content of what was said. |

You can see an example in input.csv.

The preamble.txt and postamble.txt change what appears before and after the file. A variable called max_chars in the script changes the maximum amount of text to show per card, broken down per sentence.
