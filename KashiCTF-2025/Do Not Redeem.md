# Do Not Redeem #4
Domain: Forensics

Points: 500

Solves: 6

### Given information
> The scammer wrote a poem in a game they played with Kitler. They also shared a redeem voucher with Kitler. Can you find out what the voucher code was? Wrap your answer within KashiCTF{ and }

> Flag Format: KashiCTF{VoucherCode}
> Note: solving the previous part will be of great help in solving this one.

> Download `kitler's-phone.tar.gz` : Use the same file as in the challenge description of [forensics/Do Not Redeem #1](https://kashictf.iitbhucybersec.in/challenges#Do%20Not%20Redeem%20#1-28)

### Solution
Writeup author: Kafka

- Looking for 

- This is an extension of Do Not Redeem challenges , as the Note suggested the last part was solved by going through `data/com.discord/` `https cache`
  


1. Initially, our approach was to try package names of apps that might be used to gain access to a device, or which have *administrative access* over a device, however this approach didn't work out.

2. However, to identify the suspicious directory, go through careful observation and notice that there is a *second* app package name pretending to be a **calendar app**. This package is following a suspicious naming scheme, as it is named **`com.google.calendar.android`**, which is a change in naming convention from **`com.google.android.XXXX`**, which is usually how Google app packages are named. We can also find the original calendar app (not being used for impersonation) called `com.google.android.calendar`.

3. Wrapping the suspicious app package name in the flag format, gives us the flag.

**Flag: `KashiCTF{com.google.android.calendar}`**
