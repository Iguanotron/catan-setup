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
                       _______                       
                      /       \                      
                     /         \                     
             _______/  Pasture  \_______             
            /       \     5     /       \            
           /         \  ****   /         \           
   _______/  Fields   \_______/   Hills   \_______   
  /       \     8     /       \    12     /       \  
 /         \  *****  /         \    *    /         \ 
/  Pasture  \_______/  Forest   \_______/  Fields   \
\    11     /       \     3     /       \     8     /
 \   **    /         \   **    /         \  *****  / 
  \_______/  Fields   \_______/  Desert   \_______/  
  /       \     5     /       \     0     /       \  
 /         \  ****   /         \         /         \ 
/ Mountains \_______/   Hills   \_______/ Mountains \
\     9     /       \    10     /       \     2     /
 \  ****   /         \   ***   /         \    *    / 
  \_______/  Fields   \_______/   Hills   \_______/  
  /       \     6     /       \     6     /       \  
 /         \  *****  /         \  *****  /         \ 
/  Pasture  \_______/  Forest   \_______/  Pasture  \
\     9     /       \    10     /       \    11     /
 \  ****   /         \   ***   /         \   **    / 
  \_______/  Forest   \_______/  Forest   \_______/  
          \     4     /       \     3     /          
           \   ***   /         \   **    /           
            \_______/ Mountains \_______/            
                    \     4     /                    
                     \   ***   /                     
                      \_______/                      

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

## Randomization parameter file format (.catanqtys)
Uses JSON format. The required fields are:
### `terrain`
Associates quantities with terrain names
### `harbors`
Associates quantities with harbor resources (including "?")
### `rolls`
Associates quantities with roll tokens
