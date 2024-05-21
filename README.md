# libTAS.SeedSearch
A simple python script to aid in searching for optimal initial RNG seeds.

# Prerequisites
- You will need python as well as [pyautogui](https://pyautogui.readthedocs.io/en/latest/install.html)
- You may need to retake the screenshots or adjust the mouse offsets, I have not tested this across multiple devices

# How to
1. Record a libTAS movie of the inputs you need to make to check the RNG event that you're looking to manipulate (entering the game from the menu, maybe walking a bit to the random event)
2. Under Movie enable "Don't enforce movie settings"
3. Drag-resize the libTAS window to the smallest it can be
4. Make sure to position the libTAS window in a spot where the game will not overlap it when it launches, the pause button must remain visible
5. Run the script. This is the most time consuming part, I find it best to just leave it on overnight or go do something else while it runs through the seeds.
6. When finished, either tab into the terminal and Ctrl+C or move your mouse cursor to the top left of the screen to interrupt it. Screenshots from the end of each movie will be available in the output folder.
