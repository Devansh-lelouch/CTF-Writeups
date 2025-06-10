# Ancient Ahh Display 

![image](https://github.com/user-attachments/assets/2998de43-d364-4c80-aa0e-a276f2899af8)

# Solution 
Looking up Basys 3 Artix-7's display and getting to know its working online , basically its a 8 bit pixel which takes binary input and displays it . 

We got two files one display.txt and fgpa xlx file 

![image](https://github.com/user-attachments/assets/37b01c75-7c71-4bda-98f3-b963462f3b1c)

Taking these as the only required inputs and cross checking the xlx file and removing the clutter we get 

![image](https://github.com/user-attachments/assets/547e08be-49d7-4cea-9dbb-a76284964020)


now we need to map the code via verilog program to get binary digits which we can decode . 

![image](https://github.com/user-attachments/assets/4820166a-fff4-418c-8734-7f5b0911357e)

The first digit would be 00101 map it with the 

![image](https://github.com/user-attachments/assets/188efb59-5b8a-4e38-aa56-a83f6890ba6f)

00101 becomes 0010010

0010010 should be n since the flag has to start with a n but that isnt the case so we look what n should be in a 7bit 

![image](https://github.com/user-attachments/assets/db3d3b8b-1478-4bda-839e-888b9207117d)


looking again in the txt to find out our mistake 

![image](https://github.com/user-attachments/assets/1be0f62d-190f-49a7-907e-ddb54a7d3940)

meaning we have to map it from the other side instead of `00101` it should be `10100`

doing that and putting the results in the decoder we get 

![image](https://github.com/user-attachments/assets/a9323d74-2f21-435b-9652-2a8b6adad788)

putting it in a flag format we get 

>nite{tr0UbLe_bUbbLe_L0L}


