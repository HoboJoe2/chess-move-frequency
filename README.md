This is a python program to generate move frequency graphs from a pgn file.

After you run the program the graphs will be put in the images folder and the full dataset can be found in the data.txt file.

The images and data file that are in the repository by default were generated using the Lichess elite database (https://database.nikonoel.fr) from November 2020.

If you run the program with a different pgn file the images will be replaced automatically and a new data.txt file will be generated.

If the code didn't work correctly, make an issue on github and I will hopefully see it.

To use this program, follow these steps:

1. Download python from python.org
2. Download the files by clicking the green download button, then clicking download zip.
3. Extract the zip by right-clicking it and choosing 'extract'
4. Put your pgn file in the extracted folder
5. Double click on start.bat, if there is a windows defender popup click "show more" then press the run anyway button.

The batch script is "python -m venv .env && cd .env/Scripts && activate && cd.. && cd.. && pip install -r requirements.txt && python main.py", open command prompt, cd into the folder and run that if you trust windows defender more than me.
