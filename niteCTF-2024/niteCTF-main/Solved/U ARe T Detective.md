# U ARe The detective 
![image](https://github.com/user-attachments/assets/99eb59f0-1e4f-4aa3-a7fe-2650f38b8103)

The file given was a .sr extension. Googled to get to know that i can view it with pulseview . 

Opening in pulseview it looks like this 
![image](https://github.com/user-attachments/assets/988f2fb6-5932-4508-b984-f29ea59f513a)

there are lining on the D1 zooming in to view it more clearly 
![image](https://github.com/user-attachments/assets/a5335369-60fd-4aae-8050-1707a05e0323)

It looks like a sqaure waveform there should be a way to decode , the challenge name has UART in capital meaning its a hint working more on it to get to here : 
>https://tcm-sec.com/getting-started-with-iot-hardware-hacking-uart/#:~:text=Pulseview%20can%20decode%20the%20UART,show%20up%20on%20the%20bottom.

tried this to get 
![image](https://github.com/user-attachments/assets/0b010586-3ecb-4630-b415-1bda7585888f)

understood it is a binary data form but it makes no sense, couldnt understand what i should set in the UART decorder  so looking further came across this 
https://electronics.stackexchange.com/questions/425348/baud-rate-for-square-wave-data-signal-via-uart-if-frequency-is-given

Its basically in the form of 0 1 
decoding it on my own 

![image](https://github.com/user-attachments/assets/a9dcc910-7a50-4421-a244-e7624a6de928)


decoding it in binary convertor 

![image](https://github.com/user-attachments/assets/61aabd46-2a08-4c9b-a382-75f3b4e309e6)

but the first letter should be n as nite ctf 
using the reverse option on the tool it shows its n so the first binary is 01101110 
doing it further on all the square waveforms 
the first five would be nite{ only so no point in doing them  doing the rest one in similar style 

![image](https://github.com/user-attachments/assets/a51ef75c-3baa-4dfa-86a6-d719f0514103)

![image](https://github.com/user-attachments/assets/6166fba8-da81-4bf9-b630-7c3804fc0140)

the flag is : 
>nite{n0n_std_b4ud_r4t3s_ftw}




