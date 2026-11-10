---
theme: default
background: '#FFFDF9'
title: 'Mission: Save Pixel the Bear! | Conditionals'
info: |
  ## 5-Minute Demo Teaching for Timedoor Academy
  Topic: What If...? (Conditionals IF-ELSE)
  Target: Kids Ages 7-12
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# 🚀 What If...? The Secret Superpower of Coding!
### Mission: Awaken Pixel the Bear's Decision Brain!

<div class="grid grid-cols-2 gap-8 items-center mt-12 text-left">
  <div class="p-6 bg-white rounded-2xl border-4 border-gray-800 shadow-[6px_6px_0px_#2D3436] text-center">
    <img src="./assets/kenney/bear.png" class="w-32 h-32 mx-auto animate-bounce mb-4" />
    <h3 class="text-xl font-bold text-purple-600">Meet Pixel the Bear! 🐾</h3>
    <p class="text-sm text-gray-600 mt-2">"Hi super-coders! Today I need your brain superpower to make decisions!"</p>
  </div>
  
  <div class="p-6 bg-white rounded-2xl border-4 border-gray-800 shadow-[6px_6px_0px_#2D3436] flex flex-col gap-4">
    <span class="px-3 py-1 bg-amber-500 text-white font-bold rounded-lg w-max text-xs">🎮 QUICK WARM-UP GAME</span>
    <div class="p-3 bg-gray-50 border-2 border-gray-800 rounded-xl">
      <span class="font-bold text-blue-600">IF you wear BLUE today...</span>
      <p class="text-sm font-semibold">👉 Raise your hand up high! 🙋‍♂️</p>
    </div>
    <div class="p-3 bg-gray-50 border-2 border-gray-800 rounded-xl">
      <span class="font-bold text-purple-600">IF you love Minecraft / Roblox...</span>
      <p class="text-sm font-semibold">👉 Give me a big gamer smile! 😁</p>
    </div>
  </div>
</div>

<!--
Minute 00:00 - 01:00:
"Good afternoon, my awesome super-coders! How is everyone doing today? Awesome!
Before we start, let's play a super quick brain game!
IF you are wearing blue today... raise your hand up high!
Now... IF you love playing video games... give me a big smile!
Do you know what just happened? Your brain just executed a secret superpower called CONDITIONALS!"
-->

---
transition: slide-left
---

# 🌦️ Real-Life Logic: The Weather Dilemma
### Computers make choices just like you do every morning!

<div class="grid grid-cols-2 gap-8 items-center mt-8 text-left">
  <div class="p-6 bg-white rounded-2xl border-4 border-blue-500 shadow-[6px_6px_0px_#2D3436]">
    <div class="flex justify-between items-center mb-4">
      <span class="px-3 py-1 bg-blue-500 text-white font-bold rounded-lg text-xs">CONDITION: TRUE</span>
      <span class="text-3xl">🌧️</span>
    </div>
    <h3 class="text-lg font-bold text-blue-600">IF it is Raining outside...</h3>
    <div class="p-4 bg-gray-100 border-2 border-dashed border-gray-400 rounded-xl mt-4 flex items-center gap-4">
      <img src="./assets/kenney/panda.png" class="w-16 h-16" />
      <div>
        <h4 class="font-bold text-gray-800">THEN: Grab an Umbrella! ☂️</h4>
        <p class="text-xs text-gray-500">Stay 100% dry and safe!</p>
      </div>
    </div>
  </div>

  <div class="p-6 bg-white rounded-2xl border-4 border-amber-500 shadow-[6px_6px_0px_#2D3436]">
    <div class="flex justify-between items-center mb-4">
      <span class="px-3 py-1 bg-amber-500 text-white font-bold rounded-lg text-xs">CONDITION: FALSE</span>
      <span class="text-3xl">☀️</span>
    </div>
    <h3 class="text-lg font-bold text-amber-600">ELSE (It is Sunny)...</h3>
    <div class="p-4 bg-gray-100 border-2 border-dashed border-gray-400 rounded-xl mt-4 flex items-center gap-4">
      <img src="./assets/kenney/duck.png" class="w-16 h-16" />
      <div>
        <h4 class="font-bold text-gray-800">THEN: Wear Cool Sunglasses! 😎</h4>
        <p class="text-xs text-gray-500">Enjoy the warm golden sunshine!</p>
      </div>
    </div>
  </div>
</div>

<!--
Minute 01:00 - 02:00:
"Now, how do computers and robots make decisions? They do it just like us!
IF it's raining outside... what do you grab? That's right, an umbrella!
ELSE... if it's sunny outside... what do you wear? Cool sunglasses!
In coding, IF checks if something is TRUE. And ELSE is our superhero backup plan when it's FALSE!"
-->

---
transition: slide-left
---

# 🧩 Connecting to Scratch: The Super-C Block
### Let's give Pixel the Bear his walking and jumping code!

<div class="grid grid-cols-2 gap-8 items-center mt-6 text-left">
  <div class="p-4 bg-white rounded-2xl border-4 border-gray-800 shadow-[6px_6px_0px_#2D3436] flex justify-center">
    <img src="./assets/scratch/scratch_if_else.svg" class="w-full max-w-md" />
  </div>

  <div class="p-6 bg-green-50 rounded-2xl border-4 border-green-600 shadow-[6px_6px_0px_#2D3436] flex flex-col gap-4">
    <div class="font-bold text-green-700 text-lg flex items-center gap-2">
      <span>⚠️</span> The River Dilemma!
    </div>
    <div class="p-3 bg-white border-2 border-gray-800 rounded-xl text-sm">
      <strong>Question for Coders:</strong><br/>
      What happens if we forget the <code>ELSE</code> block when Pixel reaches the river?
    </div>
    <div class="p-3 bg-blue-50 border-2 border-blue-400 rounded-xl text-sm">
      💡 <strong>The ELSE Hero:</strong><br/>
      Without <code>ELSE</code>, Pixel falls into the water! With <code>ELSE</code>, Pixel leaps over the river safely! 🚀
    </div>
  </div>
</div>

<!--
Minute 02:00 - 03:15:
"In Scratch, this superpower looks like a giant hungry mouth — we call it the C-Block!
Look at Pixel's code:
IF path ahead, THEN walk 10 steps!
ELSE... JUMP over the river!
Coders, what would happen if we FORGOT the ELSE block when Pixel reaches the river?
He would walk straight into the water! Splash!
That's why ELSE is so important — it's the backup plan that saves our robot!"
-->

---
transition: slide-left
---

# 🃏 Interactive Challenge: The Mystery Cards!
### Pick a card! Let's execute the code rule inside!

<p class="text-center font-bold text-purple-600 text-lg mt-2">
  👉 Rule: <strong>IF Red Card</strong> ➔ Draw 2 Cards! <strong>ELSE</strong> ➔ Jump 3 Times!
</p>

<div class="flex justify-center gap-16 mt-8">
  <div class="p-4 bg-white rounded-2xl border-4 border-gray-800 shadow-[6px_6px_0px_#2D3436] text-center w-52">
    <img src="./assets/kenney/card_hearts_9.png" class="w-32 mx-auto mb-2" />
    <span class="px-3 py-1 bg-red-500 text-white font-bold rounded-lg text-xs">CARD A: RED!</span>
    <p class="text-xs font-bold text-gray-700 mt-2">TRUE ➔ Draw 2 Cards! 🎴</p>
  </div>

  <div class="p-4 bg-white rounded-2xl border-4 border-gray-800 shadow-[6px_6px_0px_#2D3436] text-center w-52">
    <img src="./assets/kenney/card_spades_7.png" class="w-32 mx-auto mb-2" />
    <span class="px-3 py-1 bg-blue-500 text-white font-bold rounded-lg text-xs">CARD B: BLUE!</span>
    <p class="text-xs font-bold text-gray-700 mt-2">FALSE ➔ Jump 3 Times! 🦘</p>
  </div>
</div>

<!--
Minute 03:15 - 04:15:
"Time for our Mystery Card Challenge! Who wants to pick first?
Here is our code rule:
IF the card is RED... you draw 2 cards!
ELSE... you have to do 3 super jumps!
Look at Card A... it's RED! Condition is TRUE!
Now Card B... it's BLUE! Condition is FALSE, so we execute ELSE!"
-->

---
transition: slide-left
---

# 🏆 Mission Accomplished! You Are Master Coders!
### Pixel the Bear is safe at home thanks to your IF-ELSE superpowers!

<div class="grid grid-cols-2 gap-8 items-center mt-8 text-left">
  <div class="p-6 bg-white rounded-2xl border-4 border-gray-800 shadow-[6px_6px_0px_#2D3436] text-center">
    <img src="./assets/kenney/star_gold.png" class="w-32 h-32 mx-auto mb-4" />
    <h3 class="text-2xl font-black text-purple-600">LEVEL 5 UNLOCKED!</h3>
    <p class="text-sm text-gray-500 mt-1">Badge Awarded: Master of Decision Logic</p>
  </div>

  <div class="p-6 bg-white rounded-2xl border-4 border-gray-800 shadow-[6px_6px_0px_#2D3436] flex flex-col gap-4">
    <div class="p-3 bg-gray-50 border-2 border-gray-800 rounded-xl flex items-center gap-4">
      <span class="text-2xl">1️⃣</span>
      <div>
        <h4 class="font-bold text-purple-600">IF is the Question!</h4>
        <p class="text-xs text-gray-600">Checks whether something is TRUE or FALSE.</p>
      </div>
    </div>

    <div class="p-3 bg-gray-50 border-2 border-gray-800 rounded-xl flex items-center gap-4">
      <span class="text-2xl">2️⃣</span>
      <div>
        <h4 class="font-bold text-purple-600">ELSE is the Backup Plan!</h4>
        <p class="text-xs text-gray-600">Tells the computer what to do when it's NOT true.</p>
      </div>
    </div>

    <div class="p-3 bg-green-500 text-white font-black text-center rounded-xl text-lg shadow-[3px_3px_0px_#2D3436]">
      ✋ GIVE ME A VIRTUAL HIGH-FIVE! ✋
    </div>
  </div>
</div>

<!--
Minute 04:15 - 05:00:
"Look at that! We reached Level 5, and Pixel the Bear made it safely across the island!
Let's lock in our 2 golden superpowers today:
1. IF asks the question: Is this TRUE or FALSE?
2. ELSE is the hero backup plan: What to do when it's NOT true!
You all did an incredible job today! Can I get a virtual high-five on the camera? BAM!
Thank you super-coders, see you on our next mission!"
-->

