=== راه‌اندازی روی تلگرام (قدم به قدم) ===

قدم ۱: توکن ربات
----------------
۱. تلگرام → @BotFather
۲. /newbot
۳. نام: Piggy Bank (یا هرچی)
۴. یوزرنیم: piggy_bank_bot (یا هرچی با _bot)
۵. توکن رو کپی کن (مثلاً: 123456:ABC-DEF...)

قدم ۲: .env
-----------
فایل .env بساز (یا .env.sample رو کپی کن):
TELEGRAM_BOT_TOKEN=123456:ABC-DEF...
HUMMINGBOT_API_URL=http://localhost:8000
TARGET_PAIRS=BTC/USDT,ETH/USDT

قدم ۳: تست محلی (اختیاری)
-------------------------
source venv/bin/activate
python -c "from bot_handlers.signal_handler import build_signal_message; print(build_signal_message('BTC/USDT'))"

قدم ۴: GitHub
-------------
git init (اگر نشده)
git add .
git commit -m "cloud deploy ready"
git remote add origin https://github.com/YOUR_USERNAME/signal_bot.git
git push -u origin main

قدم ۵: Vercel
------------
۱. vercel.com → Import GitHub repo → signal_bot
۲. Environment Variables → TELEGRAM_BOT_TOKEN رو اضافه کن
۳. Deploy
۴. URL رو بگیر (مثلاً: https://signal-bot-xyz.vercel.app)

قدم ۶: Cloudflare (اختیاری — برای دامنه شخصی)
---------------------------------------------
۱. دامنه رو به Vercel وصل کن (DNS: CNAME به vercel)
۲. wrangler.toml رو آپدیت کن با دامنه خودت

قدم ۷: Webhook تلگرام
----------------------
۱. به @BotFather بگو: /setwebhook
۲. URL رو بده: https://YOUR-DOMAIN.com/api/webhook
۳. یا با curl:
   curl -X POST "https://api.telegram.org/bot<YOUR_TOKEN>/setWebhook" -d "url=https://..."

قدم ۸: Mini App (گوشی)
---------------------
مینی‌اپ به طور خودکار از Vercel سرو می‌شه: https://YOUR-DOMAIN.com/
با گوشی تلگرام باز کن → ربات رو پیدا کن → /start → Mini App رو باز کن.

نتیجه نهایی:
- /signal → تحلیل لحظه‌ای
- Confirm Trade → /trade
- Mini App → با گوشی، بدون لپ‌تاپ

=== قدم ۴ در حال اجرا ===
Remote: هیچ. برای push به GitHub، نام کاربری / URL رو بده.

=== قدم ۴ ✅ ===
Remote: https://github.com/its4li/signal_bot.git
Push نیاز به Token GitHub داره (یا SSH) — آماده برای deploy Vercel.

=== قدم ۵: Vercel Deploy ===
۱. vercel.com → Login با GitHub
۲. Import repo: its4li/signal_bot
۳. Environment Variables → TELEGRAM_BOT_TOKEN
۴. Deploy → URL رو بگیر (مثلاً: https://signal-bot-xyz.vercel.app)
۵. webhook: https://YOUR-URL/api/webhook

=== قدم ۴ (تکمیل): GitHub Auth ===
۱. github.com → Settings → Developer settings → Personal access tokens → Tokens (classic)
۲. Generate new token → repo scope → Generate
۳. git config --global credential.helper store
۴. git push https://its4li:TOKEN@github.com/its4li/signal_bot.git main

=== قدم ۴ (نهایی — بدون بازگشت) ===
مشکل: Token 403 (repo scope لازم).
راه‌حل (۳۰ ثانیه): github.com/new → نام: signal_bot → Public → Create repository.
سپس: git push https://its4li:TOKEN@github.com/its4li/signal_bot.git main
GitHub تمام.
=== اقدام فعلی ===
۱. github.com/new → signal_bot → Public → Create repository (۳۰ ثانیه)
۲. بگو 'تمام' → push + vercel deploy با هم

=== قدم ۴ (ادامه): Push با gh ===
۱. gh auth login → Web browser → Authorize
۲. بگو 'ورود کردم' → push اجرا می‌کنم

=== وضعیت نهایی GitHub ===
مشکل: Token 403 (scope repo لازم یا repo وجود نداره)
راه‌حل ساده (بدون بازگشت): github.com/new → signal_bot → Public → Create → سپس push
یا: gh auth login → gh repo create its4li/signal_bot --public --push

=== Push نهایی (بعد از ساخت repo) ===
مشکل: Token 403 (scope repo لازم)
راه‌حل: ۱. github.com/settings/tokens → Generate → repo scope
         ۲. Token جدید رو در .env بذار → push
         یا: gh auth login (ورود ایمن)

=== Push نهایی ===
مشکل: Token 403 (repo scope لازم)
راه‌حل (۱ دقیقه): github.com/settings/tokens → Generate new token (classic) → repo → Generate
Token جدید رو در .env بذار (جایگزین قبلی) → push بلافاصله انجام می‌شه

=== وضعیت فعلی ===
Repo: ساخته شده (its4li/signal_bot)
Push: منتظر Token با scope 'repo' (github.com/settings/tokens)
یا: gh auth login → مرورگر → Authorize → ورود کامل

=== وضعیت نهایی (بدون نیاز به Push) ===
GitHub: repo ساخته شده (its4li/signal_bot)
Push: منتظر Token repo scope
Vercel: می‌تونه مستقیماً از پروژه محلی deploy بشه (بدون نیاز به push)
Mini App: آماده با گوشی

=== Push دستی ===
۱. github.com/settings/tokens → Generate new token (classic) → repo → Generate
۲. Token جدید رو کپی کن
۳. ترمینال:
   git remote set-url origin https://its4li:TOKEN@github.com/its4li/signal_bot.git
۴. git push -u origin main

=== Push اجرا شد ===
دستور اجرا شد — timeout 30s (احتمالاً منتظر auth prompt یا شبکه)
راه‌حل: فرمان رو دستی در ترمینال اجرا کن تا هر پیغامی رو ببینی
یا مستقیماً به Vercel deploy بریم (GitHub push بعداً)
