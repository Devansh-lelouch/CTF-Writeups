# Challenge 
Author(s): Vikaran

Description:

You are trying to replicate the Shure ULXD8 X52 wireless mic at a cheaper price to beat the competition. At the final part, as you were measuring and noting down the output characteristics of its ADC, reckless mistakes cause you to short the supply and damage your only copy.

Given the output characteristics of the data, can you figure out what pins you need to set HIGH and LOW in your clone's firmware to get the same output chars(4 pins). You also want to modify the device to accept input only from a signal greater than or equal to 10Hz, what resistor value should you use in your design(round off to the nearest kilo ohm).

Output characteristics:

1)pin 10 and 11 act as outputs 2)A clock signal of around 32khz was supplied to pin 15 3)As soon as you receive the 24th bit from pin 12, pin 10 goes low

a,b,c,d - Mode and format pin numbers in ascending order.

Flag format: nite{a:(1/0),b:(1/0),c:(1/0),d:(1/0),(resistor value in kilo ohm)} - ignore brackets



# Solution 
My previous attempt during the niteCTF itself was [this](https://github.com/Devansh-lelouch/niteCTF/blob/main/Attempted%20but%20Failed/Attempts.md#mic-mimic) I did get the resistor value and the pin inputs right somehow but i got the pins completely wrong. 

Writing this writeup after seeing the official solutions, 
* Get the fcc id of the shure ULXD8 X52 , fcc id is basically american regulatory code given to electronic devices , using the fcc id we can find many important information. 
  - ![image](https://github.com/user-attachments/assets/1e8af773-0f43-4667-98f6-c897f2cdf5aa)
  - fcc id is DD4ULXD8X52
* Get adc id PCM1803A
* Get [this](https://www.ti.com/lit/ds/symlink/pcm1803a.pdf?ts=1735330938254&ref_url=https%253A%252F%252Fwww.google.com%252F) documentation.
* ![image](https://github.com/user-attachments/assets/82c738c5-8570-47d6-8c14-054a01c121a8)
  markes pins are those , whose info is given in the question.
   - ![image](https://github.com/user-attachments/assets/f601e59d-bbb6-495e-8a89-574a9b67fbae)

* Since its given pin 10,11 acts as output we know we are in master mode as - 

  - ![image](https://github.com/user-attachments/assets/d86ccb64-7ad0-42d3-af15-73f465afe75b)




* As soon we recieve the 24 bit from 12  pin (Dout )  , the pin 10  ( LRCK ) would get 0, observing the graphs and noticing to get the format  :
 
   - ![image](https://github.com/user-attachments/assets/83e03014-69b2-4cec-ac0a-433ee9570cee)

   - * ![image](https://github.com/user-attachments/assets/5f6c4373-60bf-4ffa-a795-62c346c43eaf)

So , 17:0 , 18:1 . 

* As sampling rates of only 16KHz to 96kHz are allowed 
 - ![image](https://github.com/user-attachments/assets/9dc4f16a-39c5-4140-b2ba-9709bf5b2b87)

 - with 35 khz only 512 fs in master mode would be allowed as it only gives the sampling rate in the allowed range 
 
  ![image](https://github.com/user-attachments/assets/5f5cde0c-2a68-4bf5-a737-50f518cb50c0) 

* ![image](https://github.com/user-attachments/assets/d20ff577-dd80-4bf1-bc3b-8e558e46b7b5)

so 19:1 and 20 : 0 

* the value of the resistor would be found using this formula : 

![image](https://github.com/user-attachments/assets/826113d5-4954-415a-9598-4a3eea96c176)

putting R = 10 and C as 10^-6 we would get R as 16 


### The flag would be : 
>nite{17:0,18:1,19:1,20:0,16}


