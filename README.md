This is a python program to generate move frequency graphs from a pgn file.

After you run the program the graphs will be put in the images folder and the full dataset can be found in the data.txt file.

The images and data file that are in the repository by default were generated using the Lichess elite database (https://database.nikonoel.fr) from November 2020.

If you run the program with a different pgn file the images will be replaced automatically and a new data.txt file will be generated.

To use this program, follow these steps:

1. Download python from python.org
2. Download the files by clicking the green download button, then clicking download zip.
3. Open file explorer to where you just downloaded the zip
4. Extract the zip by right-clicking it and choosing 'extract'
5. Put your pgn file in the extracted folder and call it "pgn_file.pgn" (The name has to be that or the code won't work)
6. Copy the location of the folder by clicking the bar above the files and using Ctrl + C
(should be something similar to "C:/This PC/Documents/chess-move-frequency-master" depending on where you put the zip file)
7. Open command prompt and type "cd " then paste the location then press enter (Eg. "cd C:/This PC/Users/user/Documents/chess-move-frequency-master")
8. Type "pip install -r requirements.txt" then press enter and wait until it finishes
9. Close the command prompt
10. Run main.py
