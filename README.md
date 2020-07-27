# Su-So
**Sudoku Solver**.

## Project in a nutshell 
While I got my hands dirty on the **Digit classification dataset problem** ,I wondered where could I possibly use it . One idea which hit my head was to solve a sudoku. I could just take a snap of the sudoku from the newspaper and the computer could solve it for me , I learnt that **backtracking** would work well to solve the sudoku but I had to inupt the numbers, which was not at all cool. I also found out that I could build a **Computer Vision** solution to it , which could possibly predict the digits and empty spaces. That's what it all took to start **#Su-So**. Besides that there has been many implementations with this project such as real time projections on the paper. It too didn't hit me interesting. At the end if I could predict the sudoku , I should be able to play with  it as well,
So I built a **GUI** model for it. All it has to do is create a interface for me to solve the sudoku , and when I quit(which is usually the case :) , I would ask the computer to solve it.

## Behind the scenes
This is the Sudoku snapshot taken.

<p align="center">
<img src="STAGES/STAGE_101.jpg" width="400" >
</p>

It's just been denoised using guassian blurring and turned into B&W .
<p align="center">
<img src="STAGES/STAGE_102.jpg" width="400" >
</p>

Later to find the exact boundaries , I used a ***flood fill algorithm*** which returns the largest connected blob in the snap , which usually the outer edge of the puzzle. This will later help us in determing the perspective transform (in simple words transforming the inclined pic into a neatly alligned pic) , Coz Computer Vision likes neatly alligned images.

<p align="center">
<img src="STAGES/STAGE_105.jpg" width="400" >
</p>



<p align="center">
<img src="STAGES/STAGE_107.jpg" width="400" >
</p>


![Alt Text](https://i.imgflip.com/3y4ue1.gif)

![Alt Text](https://imgflip.com/gif/49l1pa)
