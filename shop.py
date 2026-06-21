import streamlit as st
import requests 
BOT_TOKEN = "8640762406:AAF540rnfipL54HSUIRZqODSsBcQjM2uybo"
CHAT_ID = "7055252264"

def send_telegram_order(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}
    try:
        requests.post(url, data=payload)
    except:
        pass

st.set_page_config(page_title="متجر توفيق للرياضيات", page_icon="📖", layout="centered")
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🛒 متجر توفيق للرياضيات</h1>", unsafe_allow_html=True)

# تهيئة المتغيرات
سعر_الكتب = 0
shipping_cost = 0
shipping_method = ""

name = st.text_input("👤 الاسم الكامل:")
phone = st.text_input("📞 رقم الهاتف:")
wilaya = st.text_input("📍 الولاية/البلدية:")
address = st.text_area("🏠 العنوان بالتفصيل:")

st.write("### 📚 اختر الكتب:")
book1 = st.checkbox("كتاب الدوال (400 دج)")
book2 = st.checkbox("كتاب المتتاليات (400 دج)")
book3 = st.checkbox("كتاب الأعداد المركبة (400 دج)")
book4 = st.checkbox("كتاب الاحتمالات (400 دج)")

if book1: سعر_الكتب += 400
if book2: سعر_الكتب += 400
if book3: سعر_الكتب += 400
if book4: سعر_الكتب += 400

if wilaya:
    if "افلو" in wilaya.strip():
        aflo_option = st.radio("خيارات الاستلام في أفلو:", ("توصيل منزلي (100 دج)", "استلام شخصي (0 دج)"))
        shipping_cost = 100 if "توصيل" in aflo_option else 0
        shipping_method = aflo_option
    else:
        delivery_option = st.radio("نوع التوصيل عبر يالدين:", ("توصيل للمكتب (400 دج)", "توصيل للمنزل (700 دج)"))
        shipping_cost = 400 if "المكتب" in delivery_option else 700
        shipping_method = delivery_option

الإجمالي = سعر_الكتب + shipping_cost

if st.button("🚀 إرسال الطلب الآن"):
    if not name or not phone or سعر_الكتب == 0:
        st.error("❌ يرجى ملء الاسم، الهاتف واختيار كتاب واحد على الأقل.")
    else:
        selected_books = [b for b, val in [("الدوال", book1), ("المتتاليات", book2), ("الأعداد المركبة", book3), ("الاحتمالات", book4)] if val]
        books_text = ", ".join(selected_books)
        
        msg = (f"🔔 <b>طلب جديد في المتجر!</b>\n\n"
               f"👤 <b>الاسم:</b> {name}\n"
               f"📞 <b>الهاتف:</b> {phone}\n"
               f"📍 <b>الولاية:</b> {wilaya}\n"
               f"🏠 <b>العنوان:</b> {address}\n"
               f"📚 <b>الكتب:</b> {books_text}\n"
               f"🚚 <b>التوصيل:</b> {shipping_method}\n"
               f"💰 <b>الإجمالي:</b> {الإجمالي} دج")
        
        send_telegram_order(msg)
        st.success("✅ تم إرسال طلبك بنجاح!")
