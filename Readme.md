# Settlers of Catan Board Setup
### A command-line script that sets up a Catan board

## Disclaimer
I am not associated in any way with the board game Settlers of Catan, its
creators, or its publishers.

## Usage
Run `python3 catan.py`. Python 3 is required.

## Example output
```
> ./catan.py
Numbering Tiles....Done.
                                                                         
                                                                         
                                                                         
                         3:1     _______     2:1                         
                          ?     /       \   Brick                        
                      _________/         \_________                      
                      \_______/   Hills   \_______/                      
                      /       \     3     /       \                      
                     /         \   **    /         \                     
     3:1   /\_______/ Mountains \_______/  Pasture  \_______/\   2:1     
      ?   / /       \    12     /       \     3     /       \ \ Wool     
         / /         \    *    /         \   **    /         \ \         
        /_/  Fields   \_______/  Forest   \_______/  Fields   \_\        
          \     8     /       \    11     /       \     9     /          
           \  *****  /         \   **    /         \  ****   /           
            \_______/  Pasture  \_______/  Desert   \_______/            
            /       \    11     /       \     0     /       \            
           /         \   **    /         \         /         \           
        __/ Mountains \_______/  Forest   \_______/   Hills   \__        
        \ \     5     /       \     8     /       \    10     / /        
         \ \  ****   /         \  *****  /         \   ***   / /         
     2:1  \ \_______/  Fields   \_______/   Hills   \_______/ /  2:1     
    Grain  \/       \     4     /       \    10     /       \/ Lumber    
           /         \   ***   /         \   ***   /         \           
          / Mountains \_______/  Forest   \_______/  Fields   \          
          \     4     /       \     2     /       \     6     /          
           \   ***   /         \    *    /         \  *****  /           
            \_______/  Pasture  \_______/  Pasture  \_______/            
                  \ \     6     /       \     5     / /                  
                   \ \  *****  /         \  ****   / /                   
               2:1  \ \_______/  Forest   \_______/ /  3:1               
               Ore   \/       \     9     /       \/    ?                
                               \  ****   /                               
                                \_______/                                
                                /_______\                                
                                                                         
                                   3:1                                   
                                    ?                                    
                                                                         
                                                                         
```

## Board layout file format (.catanboard)
Tile positions on the hex grid are given in a checkerboard pattern.
For example, this is the default board:
```
  S S
   T
e T T w
 T T T
  T T
 T T T
E T T W
 T T T
  T T
 E T W

   N
```
Alternating tiles in a checkerboard pattern are ignored. Here are the
ignored tiles in the above board, marked with underscores):
```
 _S_S_ 
_ _T_ _
e_T_T_w
_T_T_T_
 _T_T_ 
_T_T_T_
E_T_T_W
_T_T_T_
 _T_T_ 
_E_T_W_
 _ _ _ 
_ _N_ _
```
Neighbors of a tile are found in the indicated relative positions to it:
```
 *
* *
 T
* *
 *
```
### Symbol meanings
|Symbol|Meaning          |
|------|-----------------|
|      |empty space      |
|T     |tile, random     |
|N     |harbor, north    |
|S     |harbor, south    |
|e     |harbor, southeast|
|E     |harbor, northeast|
|w     |harbor, southwest|
|W     |harbor, northwest|
|H     |tile, hills      |
|P     |tile, pasture    |
|F     |tile, forest     |
|f     |tile, fields     |
|M     |tile, mountains  |
|D     |tile, desert     |
|O     |tile, ocean      |

## Randomization parameter file format (.catanqtys)
Uses JSON format. The required fields are:
### `terrain`
Associates quantities with terrain names
### `harbors`
Associates quantities with harbor resources (including "?")
### `rolls`
Associates quantities with roll tokens
