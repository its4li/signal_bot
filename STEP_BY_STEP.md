
=== قدم ۱: ساخت ربات تلگرام (Bot Token) ===
۱. تلگرام باز کن → @BotFather
۲. /newbot بفرست
۳. نام ربات رو وارد کن (مثلاً: PiggyTradeBot)
۴. یوزرنیم ربات رو وارد کن (مثلاً: piggy_trade_bot) — باید با _bot تموم بشه
۵. Bot Token رو کپی کن (مثال: 123456:ABC-DEF...)
۶. این توکن رو توی .env ذخیره کن:
   TELEGRAM_BOT_TOKEN=123456:ABC-DEF...

سپس ادامه بده.

=== قدم ۳ (Cloud) ✅ ===
- vercel.json: serverless endpoint (Python ta + webhook) + Mini App routing
- api/index.py: handler for Vercel Python runtime
- mini_app/index.html: رابط موبایل (بدون لپ‌تاپ)
- wrangler.toml: Cloudflare Workers reference
