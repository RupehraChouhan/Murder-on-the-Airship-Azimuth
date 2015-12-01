label intro:
    scene bg blackImage
    with fade
    python:
        Game.narrateADV("AIIEEEEEEE!")
        Game.narrateADV("A piercing shriek startles you awake.")
    
    scene bg cabinImage
    with fade
    python:
        Game.narrateADV("You take stock of your surroundings. You are aboard the skyship {i}Azimuth{/i}, owned and operated by Royaume & Sons Airshipping Lines and Manufactoria. You are in a small but luxuriously-appointed cabin. You turn up the galvanic lamp to consult your pocketwatch. It is forty-two minutes after nine in the evening.")
        Game.narrateADV("You recall the events of the previous afternoon. You embarked at the aerodrome in Aron at 5:35 this afternoon bound for Endsville. You were invited to dine with the other passengers shortly after departure. After a quick survey of them, you determined that none of them were at all interesting enough to bother spending precious minutes of your vacation with, so you declined supper, sequestered yourself in your cabin, and went immediately to sleep.")
        Game.narrateADV("That's the kind of idiosyncratic behaviour people expect from a famously-eccentric - but brilliant - amateur detective, after all.")
        
        Game.YOU.speakADV("And it seems - like every time I try to have an ordinary vacation - I am about to be presented with yet another opportunity to demonstrate my brilliant deductive talents.")
        
        Game.narrateADV("There is a polite knock on the door of your cabin.")
        Game.YOU.speakADV("There it is. Yes?")
        Game.narrateADV("Um, excuse me, but you're the famous detective, yes? The captain would like a word with you. If that's alright.")
        Game.YOU.speakADV("Of course. One moment.")
        Game.narrateADV("You pull on your clothes and step out into the hall. A nervous-looking uniformed airman escorts you to the cockpit.")
    
    scene bg cockPitImage
    show captain
    with fade
    python:
        captain = Game.npcs[Game.NPC_CAPTAIN]
        captain.speakADV("Good evening, Detective. I'm Captain Winfarthing. I'm sorry to trouble you, but I have need of your talents.")
        captain.speakADV("You see, there's been a murder aboard my ship.")
        Game.narrateADV("Thunder rumbles in the distance.")
        Game.YOU.speakADV("A murder? Who's been killed?")
        captain.speakADV("Henry Augustus Algernon Royaume.")
        Game.narrateADV("{i}Captain Winfarthing pauses to let that sink in.{/i}")
        
        Game.YOU.speakADV("I'm sorry, should that name mean something to me?")
        captain.speakADV("'Royaume' as in 'Royaume and Sons'. The airshipping line? They built this vessel, and they keep it flying. Mr. Royaume was its founder and chairman.")
        Game.YOU.speakADV("I see.")
        
        captain.speakADV("My steward, Miss Newport, found him dead in the baths. It might have been an accident, but it didn't look like one. I took the liberty of confining all the passengers to their berths. I've kept them separated.")
        Game.YOU.speakADV("Excellent.")
        captain.speakADV("Then, I sent for you. Forgive me for imposing, but your reputation does precede you. Your resolution of those ghastly murders in Huntingdon Court last year... and how you tracked down the Archduke of Cordovia's rubies? Very impressive. I've followed your career in the headlines with interest.")
        Game.YOU.speakADV("Not a career, my good captain, just a bit of a hobby.")
        captain.speakADV("Yes, of course. I've made a televox transmission to the Endsville Metropolitan Police. They'll be waiting for us when we land. We're due at 1:30 in the morning. I do hope you can find the killer by then, Detective - or before, if possible. What if the murderer strikes again?")
        Game.narrateADV("{i}Well, it won't come to that, you're sure. Not with a detetctive of your skills on the case!{/i}")
        captain.speakADV("And... I'm sure you know, having dealt with high society before, but they can be quite touchy about some subjects. If you pressure them too much on... delicate subjects, they might refuse to speak with you.")
        Game.narrateADV("{i}You have until 1:30 to catch the killer. Investigate rooms and interview suspects to find clues. Each room you search and suspect you interview will take ten minutes. If you want to try to solve the mystery early, select 'Solve the Case'.{/i}")
         
        Game.jump("start")
        