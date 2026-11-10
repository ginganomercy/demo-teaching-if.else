"""
Timedoor Coding Academy - 5-Minute Demo Teaching PowerPoint Generator
Theme: Mission: Save Pixel the Bear! (Conditionals: IF - ELSE)
Aesthetics: Clean 2D Nintendo Pop / Kenney Game Assets
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Colors
    c_bg = RGBColor(255, 253, 249)        # #FFFDF9 Soft Cream
    c_dark = RGBColor(45, 52, 54)          # #2D3436 Dark Slate
    c_muted = RGBColor(99, 110, 114)       # #636E72
    c_purple = RGBColor(108, 92, 231)      # #6C5CE7
    c_blue = RGBColor(9, 132, 227)         # #0984E3
    c_yellow = RGBColor(253, 203, 110)     # #FDCB6E
    c_green = RGBColor(0, 184, 148)        # #00B894
    c_amber = RGBColor(225, 112, 85)       # #E17055
    c_white = RGBColor(255, 255, 255)
    c_card_border = RGBColor(45, 52, 54)

    kenney_dir = r"c:\Users\RAFLY A.R\Downloads\cv-ats\khusus-bikin-ppt\timedoor\assets\kenney"
    scratch_dir = r"c:\Users\RAFLY A.R\Downloads\cv-ats\khusus-bikin-ppt\timedoor\assets\scratch"

    def apply_canvas(slide, level_num, level_title):
        # 1. Background Fill
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = c_bg
        bg.line.fill.background()

        # 2. Top Header Bar
        top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.9))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = c_white
        top_bar.line.color.rgb = c_dark
        top_bar.line.width = Pt(3)

        # Level Badge
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.18), Inches(2.2), Inches(0.52))
        badge.fill.solid()
        badge.fill.fore_color.rgb = c_purple
        badge.line.color.rgb = c_dark
        badge.line.width = Pt(2)
        tf_b = badge.text_frame
        tf_b.word_wrap = True
        p_b = tf_b.paragraphs[0]
        p_b.text = f"LEVEL {level_num} / 5"
        p_b.font.size = Pt(14)
        p_b.font.bold = True
        p_b.font.color.rgb = c_white
        p_b.alignment = PP_ALIGN.CENTER

        # Mission Title in Header
        tx_box = slide.shapes.add_textbox(Inches(3.2), Inches(0.15), Inches(7.0), Inches(0.6))
        tf_h = tx_box.text_frame
        p_h = tf_h.paragraphs[0]
        p_h.text = f"Mission: {level_title}"
        p_h.font.size = Pt(18)
        p_h.font.bold = True
        p_h.font.color.rgb = c_dark

        # 3. Bottom Footer Bar
        bot_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(6.7), Inches(13.333), Inches(0.8))
        bot_bar.fill.solid()
        bot_bar.fill.fore_color.rgb = c_white
        bot_bar.line.color.rgb = c_dark
        bot_bar.line.width = Pt(2.5)

        tx_f = slide.shapes.add_textbox(Inches(0.8), Inches(6.8), Inches(9.0), Inches(0.5))
        p_f = tx_f.text_frame.paragraphs[0]
        p_f.text = "🐾 Part-Time Programming Teacher Demo | Timedoor Academy"
        p_f.font.size = Pt(13)
        p_f.font.color.rgb = c_muted

        tx_pg = slide.shapes.add_textbox(Inches(11.2), Inches(6.8), Inches(1.5), Inches(0.5))
        p_pg = tx_pg.text_frame.paragraphs[0]
        p_pg.text = f"Slide {level_num} of 5"
        p_pg.font.size = Pt(14)
        p_pg.font.bold = True
        p_pg.font.color.rgb = c_dark
        p_pg.alignment = PP_ALIGN.RIGHT

    # ==============================================================
    # SLIDE 1: WELCOME & THE BRAIN CODE GAME
    # ==============================================================
    s1 = prs.slides.add_slide(blank_layout)
    apply_canvas(s1, 1, "The Brain Code Game")

    # Main Title
    tb1 = s1.shapes.add_textbox(Inches(0.8), Inches(1.15), Inches(11.7), Inches(0.9))
    p1 = tb1.text_frame.paragraphs[0]
    p1.text = "What If...? The Secret Superpower of Coding! 🚀"
    p1.font.size = Pt(28)
    p1.font.bold = True
    p1.font.color.rgb = c_dark

    # Left Card: Mascot Pixel the Bear
    card_l = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.2), Inches(5.6), Inches(4.1))
    card_l.fill.solid()
    card_l.fill.fore_color.rgb = c_white
    card_l.line.color.rgb = c_dark
    card_l.line.width = Pt(3)

    bear_path = os.path.join(kenney_dir, "bear.png")
    if os.path.exists(bear_path):
        s1.shapes.add_picture(bear_path, Inches(2.7), Inches(2.5), width=Inches(1.8))

    tb_b = s1.shapes.add_textbox(Inches(1.0), Inches(4.5), Inches(5.2), Inches(1.5))
    tf_b = tb_b.text_frame
    p_b1 = tf_b.paragraphs[0]
    p_b1.text = "Meet Pixel the Bear! 🐾"
    p_b1.font.size = Pt(22)
    p_b1.font.bold = True
    p_b1.font.color.rgb = c_purple
    p_b1.alignment = PP_ALIGN.CENTER
    p_b2 = tf_b.add_paragraph()
    p_b2.text = "\"Hi super-coders! Today I need your brain superpower to make decisions!\""
    p_b2.font.size = Pt(15)
    p_b2.font.color.rgb = c_muted
    p_b2.alignment = PP_ALIGN.CENTER

    # Right Card: Brain Game Challenge
    card_r = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(2.2), Inches(5.6), Inches(4.1))
    card_r.fill.solid()
    card_r.fill.fore_color.rgb = c_white
    card_r.line.color.rgb = c_dark
    card_r.line.width = Pt(3)

    tb_r = s1.shapes.add_textbox(Inches(7.2), Inches(2.4), Inches(5.0), Inches(3.6))
    tf_r = tb_r.text_frame
    p_r0 = tf_r.paragraphs[0]
    p_r0.text = "🎮 QUICK WARM-UP GAME"
    p_r0.font.size = Pt(14)
    p_r0.font.bold = True
    p_r0.font.color.rgb = c_amber

    p_r1 = tf_r.add_paragraph()
    p_r1.text = "👕 IF you are wearing BLUE today..."
    p_r1.font.size = Pt(17)
    p_r1.font.bold = True
    p_r1.font.color.rgb = c_blue

    p_r2 = tf_r.add_paragraph()
    p_r2.text = "👉 Raise hand! (ELSE: Wave hands! 👋)"
    p_r2.font.size = Pt(14)
    p_r2.font.color.rgb = c_dark

    p_r3 = tf_r.add_paragraph()
    p_r3.text = "\n🎮 IF you love Minecraft or Roblox..."
    p_r3.font.size = Pt(17)
    p_r3.font.bold = True
    p_r3.font.color.rgb = c_purple

    p_r4 = tf_r.add_paragraph()
    p_r4.text = "👉 Give me your biggest gamer smile! 😁"
    p_r4.font.size = Pt(15)
    p_r4.font.color.rgb = c_dark

    s1.notes_slide.notes_text_frame.text = (
        "[Minute 00:00 - 01:00 | Energy: High & Warm]\n"
        "Good afternoon, my awesome super-coders! How is everyone doing today? Awesome!\n"
        "Today, we are on a secret gaming quest: Mission Save Pixel the Bear!\n"
        "Before we jump in, let's play a super quick brain game! Listen to my magical rules:\n"
        "IF you are wearing blue today... raise your hand up high!\n"
        "ELSE (if you're not wearing blue like me!)... give me a big friendly wave! 👋\n"
        "Now... IF you love playing Minecraft or Roblox... give me a big smile!\n"
        "Do you know what just happened? Your brain just executed a secret superpower called CONDITIONALS!"
    )

    # ==============================================================
    # SLIDE 2: REAL-LIFE LOGIC: THE WEATHER TRAP
    # ==============================================================
    s2 = prs.slides.add_slide(blank_layout)
    apply_canvas(s2, 2, "The Weather Dilemma")

    tb2 = s2.shapes.add_textbox(Inches(0.8), Inches(1.15), Inches(11.7), Inches(0.9))
    p2 = tb2.text_frame.paragraphs[0]
    p2.text = "Real-Life Logic: The Weather Dilemma 🌦️"
    p2.font.size = Pt(28)
    p2.font.bold = True
    p2.font.color.rgb = c_dark

    # IF Card (Rainy)
    card_if = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.2), Inches(5.6), Inches(4.1))
    card_if.fill.solid()
    card_if.fill.fore_color.rgb = c_white
    card_if.line.color.rgb = c_blue
    card_if.line.width = Pt(3.5)

    panda_path = os.path.join(kenney_dir, "panda.png")
    if os.path.exists(panda_path):
        s2.shapes.add_picture(panda_path, Inches(1.2), Inches(3.7), width=Inches(1.5))

    tb_if = s2.shapes.add_textbox(Inches(1.0), Inches(2.4), Inches(5.2), Inches(3.6))
    tf_if = tb_if.text_frame
    p_if0 = tf_if.paragraphs[0]
    p_if0.text = "🌧️ CONDITION: TRUE"
    p_if0.font.size = Pt(14)
    p_if0.font.bold = True
    p_if0.font.color.rgb = c_blue

    p_if1 = tf_if.add_paragraph()
    p_if1.text = "IF it is Raining outside..."
    p_if1.font.size = Pt(20)
    p_if1.font.bold = True
    p_if1.font.color.rgb = c_dark

    p_if2 = tf_if.add_paragraph()
    p_if2.text = "\n     👉 THEN: Grab an Umbrella! ☂️\n     Stay dry and safe from the storm!"
    p_if2.font.size = Pt(15)
    p_if2.font.color.rgb = c_muted

    # ELSE Card (Sunny)
    card_el = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(2.2), Inches(5.6), Inches(4.1))
    card_el.fill.solid()
    card_el.fill.fore_color.rgb = c_white
    card_el.line.color.rgb = c_amber
    card_el.line.width = Pt(3.5)

    duck_path = os.path.join(kenney_dir, "duck.png")
    if os.path.exists(duck_path):
        s2.shapes.add_picture(duck_path, Inches(7.3), Inches(3.7), width=Inches(1.5))

    tb_el = s2.shapes.add_textbox(Inches(7.1), Inches(2.4), Inches(5.2), Inches(3.6))
    tf_el = tb_el.text_frame
    p_el0 = tf_el.paragraphs[0]
    p_el0.text = "☀️ CONDITION: FALSE"
    p_el0.font.size = Pt(14)
    p_el0.font.bold = True
    p_el0.font.color.rgb = c_amber

    p_el1 = tf_el.add_paragraph()
    p_el1.text = "ELSE (It is Sunny)..."
    p_el1.font.size = Pt(20)
    p_el1.font.bold = True
    p_el1.font.color.rgb = c_dark

    p_el2 = tf_el.add_paragraph()
    p_el2.text = "\n     👉 THEN: Wear Sunglasses! 😎\n     Enjoy the warm golden sunshine!"
    p_el2.font.size = Pt(15)
    p_el2.font.color.rgb = c_muted

    s2.notes_slide.notes_text_frame.text = (
        "[Minute 01:00 - 02:00 | Energy: Interactive & Real-life]\n"
        "Now, how do computers and robots make decisions? They do it just like us!\n"
        "Imagine looking outside your bedroom window:\n"
        "IF it is raining outside... what do you grab? That's right, an umbrella! ☂️\n"
        "ELSE... if it's sunny outside... what do you wear? Cool sunglasses! 😎\n"
        "In coding, IF checks if something is TRUE. And ELSE is our superhero backup plan when it's FALSE!"
    )

    # ==============================================================
    # SLIDE 3: SCRATCH VISUAL LOGIC
    # ==============================================================
    s3 = prs.slides.add_slide(blank_layout)
    apply_canvas(s3, 3, "The Scratch Logic Bridge")

    tb3 = s3.shapes.add_textbox(Inches(0.8), Inches(1.15), Inches(11.7), Inches(0.9))
    p3 = tb3.text_frame.paragraphs[0]
    p3.text = "Connecting to Scratch: The Super-C Block 🧩"
    p3.font.size = Pt(28)
    p3.font.bold = True
    p3.font.color.rgb = c_dark

    # Left: Scratch Block Image
    scratch_img = os.path.join(scratch_dir, "scratch_if_else.png")
    if os.path.exists(scratch_img):
        s3.shapes.add_picture(scratch_img, Inches(0.8), Inches(2.2), width=Inches(6.4))

    # Right: Dilemma Box
    card_dil = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.5), Inches(2.2), Inches(5.0), Inches(4.1))
    card_dil.fill.solid()
    card_dil.fill.fore_color.rgb = RGBColor(232, 245, 233)
    card_dil.line.color.rgb = c_green
    card_dil.line.width = Pt(3)

    tb_dil = s3.shapes.add_textbox(Inches(7.8), Inches(2.4), Inches(4.4), Inches(3.6))
    tf_dil = tb_dil.text_frame
    p_d0 = tf_dil.paragraphs[0]
    p_d0.text = "⚠️ The River Dilemma!"
    p_d0.font.size = Pt(20)
    p_d0.font.bold = True
    p_d0.font.color.rgb = c_green

    p_d1 = tf_dil.add_paragraph()
    p_d1.text = "\nQuestion for Coders:"
    p_d1.font.size = Pt(16)
    p_d1.font.bold = True
    p_d1.font.color.rgb = c_dark

    p_d2 = tf_dil.add_paragraph()
    p_d2.text = "What happens if we FORGET the ELSE block when Pixel reaches the river?"
    p_d2.font.size = Pt(15)
    p_d2.font.color.rgb = c_muted

    p_d3 = tf_dil.add_paragraph()
    p_d3.text = "\n💡 The ELSE Hero:"
    p_d3.font.size = Pt(16)
    p_d3.font.bold = True
    p_d3.font.color.rgb = c_blue

    p_d4 = tf_dil.add_paragraph()
    p_d4.text = "Without ELSE, Pixel walks into the river (SPLASH!) With ELSE, Pixel leaps safely across! 🚀"
    p_d4.font.size = Pt(15)
    p_d4.font.color.rgb = c_dark

    s3.notes_slide.notes_text_frame.text = (
        "[Minute 02:00 - 03:15 | Energy: Curious & Instructive]\n"
        "In Scratch, this superpower looks like a giant hungry mouth — we call it the C-Block!\n"
        "Look at Pixel's code:\n"
        "IF path ahead, THEN walk 10 steps!\n"
        "ELSE... JUMP over the river! 🚀\n"
        "Coders, what would happen if we FORGOT the ELSE block when Pixel reaches the river?\n"
        "He would walk straight into the water! Splash!\n"
        "That's why ELSE is so important — it's the backup plan that saves our robot!"
    )

    # ==============================================================
    # SLIDE 4: INTERACTIVE CARD QUEST
    # ==============================================================
    s4 = prs.slides.add_slide(blank_layout)
    apply_canvas(s4, 4, "Mystery Card Quest")

    tb4 = s4.shapes.add_textbox(Inches(0.8), Inches(1.15), Inches(11.7), Inches(0.9))
    p4 = tb4.text_frame.paragraphs[0]
    p4.text = "Interactive Challenge: The Mystery Cards! 🃏"
    p4.font.size = Pt(28)
    p4.font.bold = True
    p4.font.color.rgb = c_dark

    # Instruction banner
    ban = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.1), Inches(11.7), Inches(0.7))
    ban.fill.solid()
    ban.fill.fore_color.rgb = RGBColor(237, 231, 246)
    ban.line.color.rgb = c_purple
    ban.line.width = Pt(2)
    tf_ban = ban.text_frame
    p_ban = tf_ban.paragraphs[0]
    p_ban.text = "👉 Code Rule: IF the card is RED ➔ Draw 2 Cards!  |  ELSE ➔ Jump 3 Times! 🦘"
    p_ban.font.size = Pt(16)
    p_ban.font.bold = True
    p_ban.font.color.rgb = c_purple
    p_ban.alignment = PP_ALIGN.CENTER

    # Card 1 Display
    card_h9 = os.path.join(kenney_dir, "card_hearts_9.png")
    if os.path.exists(card_h9):
        s4.shapes.add_picture(card_h9, Inches(2.8), Inches(3.1), width=Inches(2.2))

    lbl1 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.4), Inches(5.4), Inches(3.0), Inches(0.8))
    lbl1.fill.solid()
    lbl1.fill.fore_color.rgb = RGBColor(255, 235, 238)
    lbl1.line.color.rgb = RGBColor(229, 57, 53)
    lbl1.line.width = Pt(2)
    tf_l1 = lbl1.text_frame
    p_l1 = tf_l1.paragraphs[0]
    p_l1.text = "CARD A: RED! (TRUE)\nAction: Draw 2 Cards 🎴"
    p_l1.font.size = Pt(13)
    p_l1.font.bold = True
    p_l1.font.color.rgb = RGBColor(198, 40, 40)
    p_l1.alignment = PP_ALIGN.CENTER

    # Card 2 Display
    card_s7 = os.path.join(kenney_dir, "card_spades_7.png")
    if os.path.exists(card_s7):
        s4.shapes.add_picture(card_s7, Inches(8.3), Inches(3.1), width=Inches(2.2))

    lbl2 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.9), Inches(5.4), Inches(3.0), Inches(0.8))
    lbl2.fill.solid()
    lbl2.fill.fore_color.rgb = RGBColor(227, 242, 253)
    lbl2.line.color.rgb = c_blue
    lbl2.line.width = Pt(2)
    tf_l2 = lbl2.text_frame
    p_l2 = tf_l2.paragraphs[0]
    p_l2.text = "CARD B: BLUE! (FALSE)\nAction: Jump 3 Times! 🦘"
    p_l2.font.size = Pt(13)
    p_l2.font.bold = True
    p_l2.font.color.rgb = c_blue
    p_l2.alignment = PP_ALIGN.CENTER

    s4.notes_slide.notes_text_frame.text = (
        "[Minute 03:15 - 04:15 | Energy: Playful & Gamified]\n"
        "Time for our Mystery Card Challenge! Who wants to pick first?\n"
        "Here is our code rule:\n"
        "IF the card is RED... you draw 2 cards!\n"
        "ELSE (if it's not red)... you have to do 3 super jumps! 🦘\n"
        "Look at Card A... it's RED! Condition is TRUE!\n"
        "Now Card B... it's BLUE! Condition is FALSE, so we execute ELSE!"
    )

    # ==============================================================
    # SLIDE 5: MISSION ACCOMPLISHED & GOLD STARS
    # ==============================================================
    s5 = prs.slides.add_slide(blank_layout)
    apply_canvas(s5, 5, "Mission Accomplished!")

    tb5 = s5.shapes.add_textbox(Inches(0.8), Inches(1.15), Inches(11.7), Inches(0.9))
    p5 = tb5.text_frame.paragraphs[0]
    p5.text = "Mission Accomplished! You Are Master Coders! 🏆"
    p5.font.size = Pt(28)
    p5.font.bold = True
    p5.font.color.rgb = c_dark

    # Left: Star Badge Card
    card_vic = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.2), Inches(5.0), Inches(4.1))
    card_vic.fill.solid()
    card_vic.fill.fore_color.rgb = c_white
    card_vic.line.color.rgb = c_dark
    card_vic.line.width = Pt(3)

    star_path = os.path.join(kenney_dir, "star_gold.png")
    if os.path.exists(star_path):
        s5.shapes.add_picture(star_path, Inches(2.3), Inches(2.5), width=Inches(2.0))

    tb_v = s5.shapes.add_textbox(Inches(1.0), Inches(4.7), Inches(4.6), Inches(1.4))
    tf_v = tb_v.text_frame
    p_v1 = tf_v.paragraphs[0]
    p_v1.text = "LEVEL 5 UNLOCKED!"
    p_v1.font.size = Pt(22)
    p_v1.font.bold = True
    p_v1.font.color.rgb = c_purple
    p_v1.alignment = PP_ALIGN.CENTER
    p_v2 = tf_v.add_paragraph()
    p_v2.text = "Badge: Master of Decision Logic"
    p_v2.font.size = Pt(14)
    p_v2.font.color.rgb = c_muted
    p_v2.alignment = PP_ALIGN.CENTER

    # Right: Key Takeaways Card
    card_sum = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.3), Inches(2.2), Inches(6.2), Inches(4.1))
    card_sum.fill.solid()
    card_sum.fill.fore_color.rgb = c_white
    card_sum.line.color.rgb = c_dark
    card_sum.line.width = Pt(3)

    tb_sum = s5.shapes.add_textbox(Inches(6.6), Inches(2.4), Inches(5.6), Inches(3.6))
    tf_sum = tb_sum.text_frame
    p_s0 = tf_sum.paragraphs[0]
    p_s0.text = "✨ 2 GOLDEN CODING RULES"
    p_s0.font.size = Pt(15)
    p_s0.font.bold = True
    p_s0.font.color.rgb = c_amber

    p_s1 = tf_sum.add_paragraph()
    p_s1.text = "\n1️⃣ IF is the Question!"
    p_s1.font.size = Pt(18)
    p_s1.font.bold = True
    p_s1.font.color.rgb = c_purple

    p_s2 = tf_sum.add_paragraph()
    p_s2.text = "Checks whether something is TRUE or FALSE."
    p_s2.font.size = Pt(14)
    p_s2.font.color.rgb = c_muted

    p_s3 = tf_sum.add_paragraph()
    p_s3.text = "\n2️⃣ ELSE is the Hero Backup Plan!"
    p_s3.font.size = Pt(18)
    p_s3.font.bold = True
    p_s3.font.color.rgb = c_purple

    p_s4 = tf_sum.add_paragraph()
    p_s4.text = "Tells the computer what to do when it's NOT true."
    p_s4.font.size = Pt(14)
    p_s4.font.color.rgb = c_muted

    p_s5 = tf_sum.add_paragraph()
    p_s5.text = "\n✋ VIRTUAL HIGH-FIVE ON CAMERA! ✋"
    p_s5.font.size = Pt(16)
    p_s5.font.bold = True
    p_s5.font.color.rgb = c_green

    s5.notes_slide.notes_text_frame.text = (
        "[Minute 04:15 - 05:00 | Energy: Victorious & Celebratory]\n"
        "Look at that! We reached Level 5, and Pixel the Bear made it safely across!\n"
        "Let's lock in our 2 golden superpowers today:\n"
        "1. IF asks the question: Is this TRUE or FALSE?\n"
        "2. ELSE is the hero backup plan: What to do when it's NOT true!\n"
        "You all did an incredible job today! Can I get a virtual high-five on the camera? BAM!\n"
        "Thank you super-coders, see you on our next coding mission!"
    )

    out_file = r"c:\Users\RAFLY A.R\Downloads\cv-ats\khusus-bikin-ppt\timedoor\What_If_Conditionals_Timedoor_Demo.pptx"
    prs.save(out_file)
    print(f"Successfully created: {out_file} ({os.path.getsize(out_file)} bytes)")

if __name__ == "__main__":
    create_deck()
