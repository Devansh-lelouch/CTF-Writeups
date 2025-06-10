Since this was for hardware tp I just copied the writeup I did for the niteCTF for UART . I could have used the uart decorder and buad bitrate but i did it manually which took a lot of my time . 



# Qs 
1 . why do we not see any pcb designs with 90 degree traces?

A pcb board is basically printed circuit board and it has eletrical traces which are basically conductive paths or wires that connect components and everything else on the board. 
Now if we use electrical traces of 90 degrees there will be several promblems like : - 
* A 90 degree trace would  create a sudden change in the trace width at the corner leading to impedance discontinuities causing signal reflections which degrades the signals.
* high frequency signals are EMI ( electromagnetic interference ) now if theres a 90 degree turn it would act as antenna  radiation that RF energy in the surronding 
* Current flows smoothly along the traces but at 90 degree the current doesnt travel as smoothly as it should causing current density to be concentrated which might cause  heating in that area. 
* It also had lot of manafucturing promblems as well earlier . 
* So instead we use 45 degrees twice in this way : 

![image](https://github.com/user-attachments/assets/79ed4762-b8ad-4e77-9dbe-92ba53308a56)

one 45 then one 45 towards the up 

[Refrenced Video](https://youtu.be/466ZNCNC7OM?si=UGOk7ZYTH_toNO4g) 

2. why do we need an active low if we have an active high?

Active low - A signal is active low when its active at low voltage 
Active high - A signal is active high when its active at a high voltage . 

i mean we should have a active high and active low both in the circuit wont that make the device / circuit more compatible to various voltages also 
 active low signal can often be used as an inverted version of an active high signal which can be seen in  flip flops , logic gates and memory chips .
Sometimes there can be certain features like noise immunity which could be signal dependent and to tackle that its good to have active low and active highs 



