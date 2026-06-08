# MEPT Maritime English Test – Web App + Telegram Bot

Complete test system for seafarers preparing for Maritime English Proficiency Test.

## Files Included
- `index.html` – Main web interface
- `style.css` – Responsive styling
- `script.js` – All 100 grammar questions + reading + listening with answer keys
- `bot.py` – Telegram bot (grammar practice)
- `requirements.txt` – Python dependencies

## How to Use

### Web App
1. Open `index.html` in any browser (Chrome, Firefox, Edge).
2. Click tabs: Grammar, Reading, Writing, Listening, Speaking.
3. Select grammar set (1-5), answer 20 questions, submit to see score.
4. Reading: load set, choose True/False/Doesn't Say, submit.
5. Listening: based on transcripts, answer T/F/D.
6. Writing: type directly (self-evaluate).

### Telegram Bot
1. Install Python (3.7+).
2. Install library: `pip install -r requirements.txt`
3. Run bot: `python bot.py`
4. Open Telegram, search for `@MEPT_Exam_Bot` (or your bot's username after creation).
5. Start bot: `/start`
6. Practice grammar: `/grammar`

### Deploy to GitHub
1. Create new repository on GitHub.
2. Upload all 6 files.
3. Enable GitHub Pages (Settings → Pages → branch main) – web app will be live.

## Answer Keys
All grammar answers are pre-programmed (based on official MEPT keys). Reading and listening keys also included.

## Telegram Bot Token
The token is already inside `bot.py`. If you want a new bot:
- Talk to @BotFather on Telegram.
- Create new bot, copy token, replace in `bot.py`.

## Support
For any issues, check console (F12) or ask your IT officer.

Good luck with your exam! ⚓